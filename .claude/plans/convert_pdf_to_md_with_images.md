# Plan: PDF → Markdown + Image Sidecar Pipeline

## Context
The ROSMASTER-M3PRO directory contains 237 PDF tutorials (496MB total, 1457 pages, ~1473 embedded images) for a Yahboom robotics platform. These need to be converted to an AI-friendly format: Markdown files with extracted images and per-image sidecar `.md` files containing descriptions, OCR text, and metadata. The output goes to `ROSMASTER-M3PRO-DOCS-MD/` mirroring the source directory structure.

User's spec: `./incoming/pdf_to_markdown_pipeline_task.md`

## Decisions Made

### Parser: Marker (marker-pdf) ✅
- Marker handles native-text PDFs well — preserves headings, lists, code blocks, tables
- PyMuPDF fallback added for: (a) image extraction when Marker misses images, (b) text extraction when Marker crashes on edge-case PDFs (e.g., single-page trivial docs)

### PaddleOCR-VL-1.5 ❌ Tested and rejected
- Investigated https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.5 (0.9B VLM, ~3-4GB download)
- Installed `paddlepaddle` and `paddleocr[doc-parser]`, tested on `1.ROS control.pdf` (9 pages, 8 images)
- **Decision: reject** — Marker + Claude pipeline is superior for this use case. See comparison below.

#### Comparison: PaddleOCR-VL vs Marker + Claude (tested on `1.ROS control.pdf`)

| Aspect | PaddleOCR-VL | Marker + Claude |
|--------|-------------|-----------------|
| **Code blocks** | Not fenced — commands as plain text | Fenced in triple backticks ✅ |
| **Tables** | Verbose HTML `<table>` with inline styles | Clean markdown pipe tables ✅ |
| **Technical accuracy** | Typos: `geometry_msg` instead of `geometry_msgs`, `std_msg` instead of `std_msgs` | Correct ROS message types ✅ |
| **Output format** | 9 separate files (one per page) — needs stitching | Single unified document ✅ |
| **Images extracted** | 5 | 8 (PyMuPDF fallback) ✅ |
| **Image placement** | Inline at correct position | Appended by page (fallback) — Marker inline when it extracts them |
| **Image descriptions** | None — raw `<img>` tags only | Rich Claude descriptions + OCR + metadata sidecars ✅ |
| **Heading quality** | Cleaner (less HTML noise) ✅ | More verbose (bold + span anchors) |
| **Processing time** | Order of magnitude slower | ~2 min for this PDF ✅ |

**Key reasons for rejection:**
1. **No image descriptions** — the whole point of the sidecar format is rich AI-generated descriptions; PaddleOCR-VL doesn't produce any
2. **Command typos** in ROS message types would mislead downstream AI consumers
3. **No code fencing** — critical for a robotics tutorial full of terminal commands
4. **Much slower processing** — significantly longer per PDF despite producing lower-quality output
5. **These PDFs have native digital text** — PaddleOCR-VL's strength (pixel-level OCR for scanned documents) is unnecessary here

PaddleOCR-VL test output saved at: `./incoming/paddleocr_test/`

### Image Descriptions: `claude -p` via Claude Code CLI ✅
- Uses `claude -p` with `--allowedTools Read` to have Claude read and describe each image
- Runs through user's subscription — no API charges
- ~12s per image, produces high-quality contextual descriptions
- Falls back to heuristic (template from PDF title + page + OCR) on failure
- **Important**: `--bare` flag breaks auth — must NOT be used

## Dependencies

```bash
brew install tesseract
pip3 install marker-pdf   # pulls surya-ocr, torch, etc.
```

Already installed: `Pillow`, `PyMuPDF`, `pytesseract`, `tqdm`

## Output Structure

The converted directory mirrors the exact same folder/chapter structure as the source:

```
ROSMASTER-M3PRO-DOCS-MD/
  0.Configuration and Operation Guide/
    1._Quick_start_handle_to_control_the_car/
      1._Quick_start_handle_to_control_the_car.md
      images/
        img_001.png
        img_001.md
  12.Control Board Course/
    1.Development environment setup/        ← subdirectory preserved
      1._Introduction_to_the_Control_Board/
        ...
  ...
```

## Script: `convert_pdfs.py`

**Status: implemented and tested.** Single CLI script at repo root, ~450 lines.

```bash
python3 convert_pdfs.py ROSMASTER-M3PRO ROSMASTER-M3PRO-DOCS-MD \
  --description-mode claude [--force] [--skip-failed] [--dry-run] [--verify] [--only PATTERN]
```

### Key implementation details
- `MarkerEngine` loads ML models once, reuses across all PDFs
- PyMuPDF fallback for image extraction (when Marker returns 0 images) and text extraction (when Marker crashes)
- `ProgressTracker` saves to `.conversion_progress.json` — supports resume, skip-failed, force
- Images < 50×50px filtered as icons/separators
- Unreferenced images (from PyMuPDF fallback) appended at end of markdown grouped by page

## Trial Results (Phase B+C complete ✅)

| PDF | Marker images | PyMuPDF fallback | Claude descriptions | Time |
|-----|--------------|------------------|--------------------| -----|
| Preparation of AI large models (1pg, 21KB) | ❌ Marker crashed | 0 (no images) | N/A | 4s |
| 1.ROS control (9pg, 8 images) | 0 | 8 ✅ | 8 ✅ | 2:15 |
| 9.Navigation2 (26pg, 20 images) | 20 ✅ | N/A | 20 ✅ | 5:34 |

All 3 pass verification: 28 images, 28 sidecars, 0 issues.

## Full Batch Estimate (Phase D)

| Component | Count | Rate | Time |
|-----------|-------|------|------|
| Marker PDF conversion | 237 PDFs | ~25s/PDF | ~99 min |
| Claude image descriptions | 1,473 images | ~12s/image | ~295 min |
| **Total** | | | **~6.5 hours** |

### Command to run full batch:

```bash
python3 convert_pdfs.py ROSMASTER-M3PRO ROSMASTER-M3PRO-DOCS-MD --description-mode claude
```

The script auto-resumes — if interrupted, just re-run the same command and it skips completed PDFs.

After completion, verify:
```bash
python3 convert_pdfs.py ROSMASTER-M3PRO ROSMASTER-M3PRO-DOCS-MD --verify
```

## Files
- **Script**: `./convert_pdfs.py`
- **Task spec**: `./incoming/pdf_to_markdown_pipeline_task.md`
