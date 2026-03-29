# ROSMASTER M3 Pro — AI-Friendly Documentation

Converted documentation for the [Yahboom ROSMASTER M3 Pro](https://category.yahboom.net/products/rosmaster-m3-pro) ROS2 robot platform.

237 PDF tutorials converted to **Markdown + extracted images with AI-generated descriptions**, optimized for use with LLMs and RAG systems.

## What's Inside

- **`ROSMASTER-M3PRO-DOCS-MD/`** — 237 tutorials as Markdown, organized in 18 course directories covering:
  - Robot configuration, chassis control, LiDAR SLAM/navigation
  - Depth camera, Mediapipe vision, robotic arm gripping
  - MoveIt2 simulation, multi-vehicle coordination
  - AI large model integration (text and voice)
  - STM32 control board, ROS2 basics, Docker, Linux, OpenCV

- **`agents/generic-rosmaster-m3pro.md`** — Claude Code agent file with platform specs and documentation map. Symlink `ROSMASTER-M3PRO-DOCS-MD/` into your project and load this agent for development assistance.

- **`convert_pdfs.py`** — Conversion pipeline (Marker + PyMuPDF + Tesseract + Claude Code CLI for image descriptions).

## Document Format

Each tutorial is a folder:

```
<tutorial_name>/
  <tutorial_name>.md        # Main content with headings, code blocks, tables, image refs
  images/
    img_001.png             # Extracted screenshot/diagram
    img_001.md              # Sidecar: metadata, caption, description, OCR text
    img_002.png
    img_002.md
```

Image sidecar files contain:
- Source PDF name and page number
- Image type classification (screenshot, diagram, chart, photo, code, ui)
- AI-generated caption and detailed description
- OCR-extracted text

## Using with Claude Code

1. Symlink the docs into your robot project:
   ```bash
   ln -s /path/to/robotdoc/ROSMASTER-M3PRO-DOCS-MD ./ROSMASTER-M3PRO-DOCS-MD
   ```

2. Copy the agent file:
   ```bash
   cp /path/to/robotdoc/agents/generic-rosmaster-m3pro.md .claude/agents/
   ```

3. Claude Code will search through documentation on demand using Grep/Glob/Read.

## Rebuilding from PDFs

Requires: `brew install tesseract`, `pip3 install marker-pdf`

```bash
# Clone original PDFs
git clone git@github.com:YahboomTechnology/ROSMASTER-M3PRO.git

# Convert all (auto-resumes if interrupted)
python3 convert_pdfs.py ROSMASTER-M3PRO ROSMASTER-M3PRO-DOCS-MD --description-mode claude

# Verify output
python3 convert_pdfs.py ROSMASTER-M3PRO ROSMASTER-M3PRO-DOCS-MD --verify
```

## Robot Platform

| Component | Details |
|-----------|---------|
| Chassis | Mecanum wheels, pendulum suspension, omnidirectional |
| Arm | 6-DOF servo-driven robotic arm |
| Camera | Binocular structured light depth camera (Dabai DCW2) |
| LiDAR | Dual TOF (front-left + rear-right), 360-degree scanning |
| Controllers | Raspberry Pi 5, Jetson Nano B01, Jetson Orin Nano/NX Super |
| ROS | ROS2 Humble |
| AI | Speech recognition, NLU, multimodal interaction, RAG |

## Contact

Yahboom technical support: support@yahboom.com
