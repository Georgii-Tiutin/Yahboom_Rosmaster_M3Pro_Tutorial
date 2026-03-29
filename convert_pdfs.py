#!/usr/bin/env python3
"""
PDF → Markdown + Image Sidecar Pipeline

Converts PDF tutorials into AI-friendly format:
- One main Markdown file per PDF
- Extracted images in /images folder
- Per-image sidecar .md with metadata, OCR, and description

Usage:
    python convert_pdfs.py INPUT_DIR OUTPUT_DIR [options]

Examples:
    # Trial run on specific PDFs
    python convert_pdfs.py ROSMASTER-M3PRO ROSMASTER-M3PRO-DOCS-MD --only "1.AI Large Model Preparation/Preparation of AI large models.pdf"

    # Full batch with Claude descriptions
    python convert_pdfs.py ROSMASTER-M3PRO ROSMASTER-M3PRO-DOCS-MD --description-mode claude
"""

import argparse
import base64
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import traceback
from datetime import datetime
from pathlib import Path

from PIL import Image
from tqdm import tqdm

# ---------------------------------------------------------------------------
# Filename sanitization
# ---------------------------------------------------------------------------

def sanitize_name(filename: str) -> str:
    """Convert PDF filename to a safe directory/file name."""
    stem = Path(filename).stem
    name = stem.strip()
    name = name.replace("+", "_plus_")
    name = re.sub(r"[(){}[\]]", "", name)
    name = re.sub(r"\s+", "_", name)
    name = re.sub(r"_+", "_", name)
    name = name.strip("_")
    return name


# ---------------------------------------------------------------------------
# PDF discovery
# ---------------------------------------------------------------------------

def discover_pdfs(input_dir: str, only_patterns: list[str] | None = None) -> list[tuple[str, str]]:
    """
    Walk input_dir recursively. Return list of (absolute_pdf_path, relative_dir).
    If only_patterns is given, filter to PDFs whose relative path contains any pattern.
    Sorted by file size (smallest first).
    """
    results = []
    input_dir = os.path.abspath(input_dir)
    for root, dirs, files in os.walk(input_dir):
        dirs.sort()
        for f in sorted(files):
            if not f.lower().endswith(".pdf"):
                continue
            abs_path = os.path.join(root, f)
            rel_dir = os.path.relpath(root, input_dir)
            rel_path = os.path.join(rel_dir, f)

            if only_patterns:
                if not any(pat in rel_path for pat in only_patterns):
                    continue

            results.append((abs_path, rel_dir))

    # Sort by file size, smallest first
    results.sort(key=lambda x: os.path.getsize(x[0]))
    return results


# ---------------------------------------------------------------------------
# Marker Engine
# ---------------------------------------------------------------------------

class MarkerEngine:
    """Wraps Marker model loading and PDF conversion."""

    def __init__(self):
        print("Loading Marker models (this takes 30-60 seconds)...")
        from marker.converters.pdf import PdfConverter
        from marker.models import create_model_dict

        self.model_dict = create_model_dict()
        self.PdfConverter = PdfConverter
        print("Marker models loaded.")

    def convert(self, pdf_path: str):
        """Convert a PDF file. Returns MarkdownOutput with .markdown, .images, .metadata."""
        converter = self.PdfConverter(
            artifact_dict=self.model_dict,
        )
        return converter(pdf_path)


# ---------------------------------------------------------------------------
# Image processing helpers
# ---------------------------------------------------------------------------

def parse_marker_image_key(key: str) -> tuple[int, int]:
    """
    Parse a Marker image key like '_page_0_Picture_3' into (page_id, block_id).
    Falls back to (9999, 9999) if unparseable.
    """
    m = re.search(r"page[_-](\d+)", key, re.IGNORECASE)
    page_id = int(m.group(1)) if m else 9999
    # Try to find the trailing number as block_id
    m2 = re.search(r"(\d+)(?:\.\w+)?$", key)
    block_id = int(m2.group(1)) if m2 else 9999
    return (page_id, block_id)


def classify_image_heuristic(img: Image.Image, ocr_text: str) -> str:
    """Simple heuristic classification of image type."""
    w, h = img.size
    if w < 50 or h < 50:
        return "icon"

    # Check if mostly text (screenshot/code)
    ocr_density = len(ocr_text.strip()) / max(1, (w * h) / 10000)
    if ocr_density > 5:
        return "screenshot"

    # Check color diversity
    try:
        colors = img.convert("RGB").getcolors(maxcolors=1000)
        if colors is not None and len(colors) < 20:
            return "diagram"
    except Exception:
        pass

    # Check aspect ratio for charts
    aspect = w / max(h, 1)
    if 0.8 < aspect < 1.5 and w > 200:
        return "chart"

    return "photo"


def ocr_image(img: Image.Image) -> str:
    """Run Tesseract OCR on a PIL Image."""
    try:
        import pytesseract
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        return f"[OCR failed: {e}]"


def describe_image_claude(img: Image.Image, pdf_name: str, page_num: int, ocr_text: str) -> dict:
    """
    Use `claude -p` to generate caption, description, and type for an image.
    Returns dict with keys: caption, description, type.
    """
    # Save image to temp file
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        img.save(tmp, format="PNG")
        tmp_path = tmp.name

    try:
        prompt = f"""Read the image at {tmp_path} and analyze it. This image is from a robotics tutorial PDF called "{pdf_name}" (page {page_num}).

OCR text found in image: {ocr_text[:500] if ocr_text else "none"}

Respond with ONLY valid JSON (no markdown fences):
{{
  "caption": "1-2 sentence summary of what the image shows",
  "description": "Detailed multi-line description of the image content, layout, and purpose in the tutorial context",
  "type": "one of: diagram, screenshot, chart, photo, code, ui"
}}"""

        for attempt in range(3):
            try:
                result = subprocess.run(
                    ["claude", "-p", prompt, "--output-format", "text",
                     "--allowedTools", "Read"],
                    capture_output=True,
                    text=True,
                    timeout=90,
                )
                if result.returncode == 0 and result.stdout.strip():
                    output = result.stdout.strip()
                    # Try to extract JSON from response
                    # Remove markdown fences if present
                    output = re.sub(r"^```(?:json)?\s*", "", output)
                    output = re.sub(r"\s*```$", "", output)
                    data = json.loads(output)
                    return {
                        "caption": data.get("caption", ""),
                        "description": data.get("description", ""),
                        "type": data.get("type", "unknown"),
                    }
            except (subprocess.TimeoutExpired, json.JSONDecodeError) as e:
                if attempt < 2:
                    time.sleep(2 * (attempt + 1))
                    continue
            except Exception as e:
                if attempt < 2:
                    time.sleep(2 * (attempt + 1))
                    continue

        # Fallback
        return None
    finally:
        os.unlink(tmp_path)


def describe_image_heuristic(img: Image.Image, pdf_name: str, page_num: int, ocr_text: str, img_type: str) -> dict:
    """Generate a template-based description."""
    caption = f"Figure from page {page_num} of {pdf_name}"
    if ocr_text:
        first_line = ocr_text.split("\n")[0][:100]
        caption = f"Figure from page {page_num}: {first_line}"

    description = f"Image extracted from '{pdf_name}', page {page_num}. "
    description += f"Classified as: {img_type}. "
    if ocr_text:
        description += f"Contains text: {ocr_text[:200]}"

    return {"caption": caption, "description": description, "type": img_type}


# ---------------------------------------------------------------------------
# Sidecar generation
# ---------------------------------------------------------------------------

def generate_sidecar_md(
    img_name: str,
    pdf_name: str,
    page_num: int,
    img_type: str,
    caption: str,
    description: str,
    ocr_text: str,
) -> str:
    """Generate the sidecar markdown content for one image."""
    return f"""# {img_name}

## Metadata
- Source: {pdf_name}
- Page: {page_num}
- Type: {img_type}

## Caption
{caption}

## Description
{description}

## OCR Text
```
{ocr_text if ocr_text else "[No text detected]"}
```
"""


# ---------------------------------------------------------------------------
# PyMuPDF fallback image extraction
# ---------------------------------------------------------------------------

def extract_images_pymupdf(pdf_path: str, min_size: int = 50) -> dict:
    """
    Extract images from PDF using PyMuPDF as fallback when Marker misses them.
    Returns dict mapping 'pymupdf_page_{N}_img_{M}' -> PIL Image.
    """
    import fitz

    images = {}
    doc = fitz.open(pdf_path)
    for page_idx, page in enumerate(doc):
        img_list = page.get_images()
        for img_idx, img_info in enumerate(img_list):
            xref = img_info[0]
            try:
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                pil_img = Image.open(io.BytesIO(image_bytes))
                w, h = pil_img.size
                if w < min_size and h < min_size:
                    continue
                key = f"pymupdf_page_{page_idx}_img_{img_idx}"
                images[key] = pil_img
            except Exception:
                continue
    doc.close()
    return images


# ---------------------------------------------------------------------------
# Post-processing: Marker output → target structure
# ---------------------------------------------------------------------------

def post_process(
    markdown: str,
    images: dict,
    metadata: dict,
    output_dir: str,
    pdf_name: str,
    sanitized_name: str,
    description_mode: str,
) -> dict:
    """
    Transform Marker output into the target directory structure.
    Returns stats dict.
    """
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    if not images:
        # No images — just write the markdown
        md_path = os.path.join(output_dir, f"{sanitized_name}.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(markdown)
        return {"images": 0, "sidecars": 0}

    # Sort images by (page, block_id) for sequential naming
    sorted_keys = sorted(images.keys(), key=parse_marker_image_key)

    # Build mapping: original_key → (img_NNN, page_num, PIL Image)
    image_mapping = {}
    seq = 1
    for key in sorted_keys:
        img = images[key]
        if isinstance(img, Image.Image):
            w, h = img.size
            if w < 50 and h < 50:
                continue  # Skip tiny images
        page_num, _ = parse_marker_image_key(key)
        img_id = f"img_{seq:03d}"
        image_mapping[key] = (img_id, page_num, img)
        seq += 1

    # Save images as PNG and generate sidecars
    sidecar_count = 0
    for key, (img_id, page_num, img) in image_mapping.items():
        if not isinstance(img, Image.Image):
            continue

        # Save PNG
        png_path = os.path.join(images_dir, f"{img_id}.png")
        img.save(png_path, format="PNG")

        # OCR
        ocr_text = ocr_image(img)

        # Classification & description
        img_type = classify_image_heuristic(img, ocr_text)

        if description_mode == "claude":
            claude_result = describe_image_claude(img, pdf_name, page_num, ocr_text)
            if claude_result:
                caption = claude_result["caption"]
                description = claude_result["description"]
                img_type = claude_result.get("type", img_type)
            else:
                fallback = describe_image_heuristic(img, pdf_name, page_num, ocr_text, img_type)
                caption = fallback["caption"]
                description = fallback["description"]
        elif description_mode == "heuristic":
            result = describe_image_heuristic(img, pdf_name, page_num, ocr_text, img_type)
            caption = result["caption"]
            description = result["description"]
        else:  # none
            caption = ""
            description = ""

        # Write sidecar
        sidecar_content = generate_sidecar_md(
            img_id, pdf_name, page_num, img_type, caption, description, ocr_text
        )
        sidecar_path = os.path.join(images_dir, f"{img_id}.md")
        with open(sidecar_path, "w", encoding="utf-8") as f:
            f.write(sidecar_content)
        sidecar_count += 1

    # Rewrite markdown: replace Marker image refs with new paths
    updated_md = markdown
    unreferenced_images = []  # Images not found in markdown (e.g., PyMuPDF fallback)

    for key, (img_id, page_num, img) in image_mapping.items():
        if key.startswith("pymupdf_"):
            # PyMuPDF-extracted images have no references in markdown
            unreferenced_images.append((img_id, page_num))
            continue

        # Marker uses references like ![](key) or ![alt](key)
        key_stem = Path(key).stem
        key_variants = [key, key.lstrip("_"), key_stem, key_stem.lstrip("_")]

        matched = False
        for variant in key_variants:
            pattern = re.compile(
                r"(!\[[^\]]*\]\()(" + re.escape(variant) + r"[^\)]*?)(\))",
                re.IGNORECASE,
            )
            replacement = (
                f"![{img_id}](images/{img_id}.png)\n"
                f"[Image details](images/{img_id}.md)"
            )
            if pattern.search(updated_md):
                updated_md = pattern.sub(replacement, updated_md, count=1)
                matched = True
                break

        if not matched:
            unreferenced_images.append((img_id, page_num))

    # Append unreferenced images (from PyMuPDF fallback) at end of markdown,
    # grouped by page number
    if unreferenced_images:
        updated_md += "\n\n---\n\n## Extracted Images\n\n"
        current_page = -1
        for img_id, page_num in unreferenced_images:
            if page_num != current_page:
                updated_md += f"\n### Page {page_num + 1}\n\n"
                current_page = page_num
            updated_md += f"![{img_id}](images/{img_id}.png)\n"
            updated_md += f"[Image details](images/{img_id}.md)\n\n"

    # Write final markdown
    md_path = os.path.join(output_dir, f"{sanitized_name}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(updated_md)

    return {"images": len(image_mapping), "sidecars": sidecar_count}


# ---------------------------------------------------------------------------
# Progress tracker
# ---------------------------------------------------------------------------

class ProgressTracker:
    """Track conversion progress in a JSON file for resume capability."""

    def __init__(self, output_dir: str):
        self.path = os.path.join(output_dir, ".conversion_progress.json")
        self.data = self._load()

    def _load(self) -> dict:
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return json.load(f)
        return {"version": 1, "started": datetime.now().isoformat(), "completed": {}}

    def _save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)

    def is_completed(self, rel_path: str) -> bool:
        entry = self.data["completed"].get(rel_path, {})
        return entry.get("status") == "success"

    def is_failed(self, rel_path: str) -> bool:
        entry = self.data["completed"].get(rel_path, {})
        return entry.get("status") == "failed"

    def mark_success(self, rel_path: str, images: int, pages: int):
        self.data["completed"][rel_path] = {
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "images": images,
            "pages": pages,
        }
        self._save()

    def mark_failed(self, rel_path: str, error: str):
        self.data["completed"][rel_path] = {
            "status": "failed",
            "timestamp": datetime.now().isoformat(),
            "error": error[:500],
        }
        self._save()

    def summary(self) -> dict:
        completed = self.data["completed"]
        success = sum(1 for v in completed.values() if v["status"] == "success")
        failed = sum(1 for v in completed.values() if v["status"] == "failed")
        total_images = sum(v.get("images", 0) for v in completed.values() if v["status"] == "success")
        return {"success": success, "failed": failed, "total_images": total_images}


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_output(output_dir: str):
    """Verify the converted output for completeness."""
    issues = []
    stats = {"docs": 0, "images": 0, "sidecars": 0, "issues": 0}

    for root, dirs, files in os.walk(output_dir):
        md_files = [f for f in files if f.endswith(".md") and f != ".conversion_progress.json"]
        # Check if this is a document directory (has a main .md that's not a sidecar)
        if "images" in dirs or any(not f.startswith("img_") for f in md_files):
            main_mds = [f for f in md_files if not f.startswith("img_")]
            if not main_mds:
                continue

            stats["docs"] += 1
            for md in main_mds:
                md_path = os.path.join(root, md)
                if os.path.getsize(md_path) == 0:
                    issues.append(f"Empty markdown: {md_path}")

            images_dir = os.path.join(root, "images")
            if os.path.isdir(images_dir):
                pngs = [f for f in os.listdir(images_dir) if f.endswith(".png")]
                sidecars = [f for f in os.listdir(images_dir) if f.endswith(".md")]
                stats["images"] += len(pngs)
                stats["sidecars"] += len(sidecars)

                if len(pngs) != len(sidecars):
                    issues.append(
                        f"Mismatch in {images_dir}: {len(pngs)} PNGs vs {len(sidecars)} sidecars"
                    )

    stats["issues"] = len(issues)
    print(f"\n=== Verification Results ===")
    print(f"Documents: {stats['docs']}")
    print(f"Images: {stats['images']}")
    print(f"Sidecars: {stats['sidecars']}")
    print(f"Issues: {stats['issues']}")
    for issue in issues:
        print(f"  ! {issue}")
    return stats


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def convert_single_pdf(
    engine: MarkerEngine,
    pdf_path: str,
    rel_dir: str,
    output_base: str,
    pdf_filename: str,
    description_mode: str,
) -> dict:
    """Convert a single PDF through the full pipeline. Returns stats dict."""
    san_name = sanitize_name(pdf_filename)
    output_dir = os.path.join(output_base, rel_dir, san_name)
    os.makedirs(output_dir, exist_ok=True)

    # Run Marker (with PyMuPDF fallback if Marker crashes)
    try:
        result = engine.convert(pdf_path)
        markdown = result.markdown
        images = result.images
        md_metadata = result.metadata
    except Exception as marker_err:
        # Fallback: extract text with PyMuPDF
        import fitz
        tqdm.write(f"    ⚠ Marker failed ({marker_err}), falling back to PyMuPDF")
        doc = fitz.open(pdf_path)
        markdown = ""
        for page in doc:
            markdown += page.get_text("text") + "\n\n"
        doc.close()
        images = {}
        md_metadata = {}

    # Fallback: if Marker found no images, try PyMuPDF
    if not images:
        pymupdf_images = extract_images_pymupdf(pdf_path)
        if pymupdf_images:
            images = pymupdf_images
            # Inject image references at page boundaries in markdown
            # Group by page and append references at end of markdown
            from collections import defaultdict
            pages = defaultdict(list)
            for key in sorted(pymupdf_images.keys()):
                m = re.search(r"page_(\d+)", key)
                page_num = int(m.group(1)) if m else 0
                pages[page_num].append(key)

    # Post-process
    stats = post_process(
        markdown=markdown,
        images=images,
        metadata=md_metadata,
        output_dir=output_dir,
        pdf_name=pdf_filename,
        sanitized_name=san_name,
        description_mode=description_mode,
    )

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF tutorials to Markdown + Image Sidecars"
    )
    parser.add_argument("input_dir", help="Source directory with PDFs")
    parser.add_argument("output_dir", help="Target directory for converted output")
    parser.add_argument(
        "--description-mode",
        choices=["none", "heuristic", "claude"],
        default="heuristic",
        help="Image description strategy (default: heuristic)",
    )
    parser.add_argument("--force", action="store_true", help="Re-convert all PDFs")
    parser.add_argument("--skip-failed", action="store_true", help="Skip previously failed PDFs")
    parser.add_argument("--dry-run", action="store_true", help="List PDFs without converting")
    parser.add_argument("--verify", action="store_true", help="Verify output completeness")
    parser.add_argument(
        "--only",
        action="append",
        help="Only convert PDFs matching this pattern (can be used multiple times)",
    )

    args = parser.parse_args()

    if args.verify:
        verify_output(args.output_dir)
        return

    # Discover PDFs
    pdfs = discover_pdfs(args.input_dir, args.only)
    print(f"Found {len(pdfs)} PDFs to process.")

    if args.dry_run:
        for pdf_path, rel_dir in pdfs:
            filename = os.path.basename(pdf_path)
            size_kb = os.path.getsize(pdf_path) / 1024
            print(f"  [{size_kb:7.1f} KB] {rel_dir}/{filename}")
        return

    # Progress tracking
    os.makedirs(args.output_dir, exist_ok=True)
    tracker = ProgressTracker(args.output_dir)

    # Load Marker models once
    engine = MarkerEngine()

    # Process each PDF
    total_images = 0
    success_count = 0
    fail_count = 0

    for pdf_path, rel_dir in tqdm(pdfs, desc="Converting PDFs"):
        filename = os.path.basename(pdf_path)
        rel_path = os.path.join(rel_dir, filename)

        # Check progress
        if not args.force and tracker.is_completed(rel_path):
            tqdm.write(f"  SKIP (done): {rel_path}")
            continue
        if args.skip_failed and tracker.is_failed(rel_path):
            tqdm.write(f"  SKIP (failed): {rel_path}")
            continue

        tqdm.write(f"  Converting: {rel_path}")
        try:
            stats = convert_single_pdf(
                engine=engine,
                pdf_path=pdf_path,
                rel_dir=rel_dir,
                output_base=args.output_dir,
                pdf_filename=filename,
                description_mode=args.description_mode,
            )
            tracker.mark_success(rel_path, stats["images"], 0)
            total_images += stats["images"]
            success_count += 1
            tqdm.write(f"    ✓ {stats['images']} images extracted")
        except Exception as e:
            tracker.mark_failed(rel_path, str(e))
            fail_count += 1
            tqdm.write(f"    ✗ Error: {e}")
            traceback.print_exc()

    # Summary
    print(f"\n=== Conversion Complete ===")
    print(f"Success: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"Total images: {total_images}")

    overall = tracker.summary()
    print(f"\nOverall progress: {overall['success']} completed, {overall['failed']} failed, {overall['total_images']} images")


if __name__ == "__main__":
    main()
