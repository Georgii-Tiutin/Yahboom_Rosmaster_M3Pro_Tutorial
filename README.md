# Yahboom ROSMASTER M3 Pro Tutorials — AI-Friendly Version

The official [Yahboom ROSMASTER M3 Pro tutorials](https://github.com/YahboomTechnology/ROSMASTER-M3PRO), converted from PDF to **Markdown + extracted images with text descriptions**, so that AI coding assistants (Claude Code, Cursor, Copilot…) and search tools can read them directly.

Converted by **Georgii Tiutin**.

> **Unofficial conversion.** This is not affiliated with or endorsed by Yahboom. All tutorial
> content, images and code belong to **Yahboom Technology**; the original PDFs are at
> [YahboomTechnology/ROSMASTER-M3PRO](https://github.com/YahboomTechnology/ROSMASTER-M3PRO).
> It is shared non-commercially to help other M3 Pro owners. If Yahboom would prefer it not
> to be published, please open an issue here and it will be taken down.

## Why

The PDFs are easy for people to read but hard for AI tools: they can't search across 237 PDFs, and they can't see the screenshots that many steps depend on. Here every tutorial is plain Markdown, and every image has a text description and its OCR'd text, so an assistant can find the right tutorial with a text search and understand the screenshots too.

## What's inside

- **`ROSMASTER-M3PRO-DOCS-MD/`**: the 237 tutorials as Markdown, in 18 course folders:
  - robot configuration, chassis control, LiDAR SLAM / navigation
  - depth camera, Mediapipe vision, robotic arm and 3D gripping
  - MoveIt2 simulation, multi-vehicle coordination
  - AI large model integration (text and voice)
  - STM32 control board, ROS 2 basics, Docker, Linux, OpenCV
- **`ROSMASTER-M3PRO-DOCS-MD/Annex Download Files/`**: only the `Download.link.txt` files. Yahboom's code, 3D model and firmware downloads (~6.5 GB) are **not** included; follow the links to get them.
- **`agents/generic-rosmaster-m3pro.md`**: a Claude Code agent with the platform specs and a map of the documentation.
- **`convert_pdfs.py`**: the conversion script, so the docs can be rebuilt when Yahboom updates the PDFs.
- **Owner's notes (not from Yahboom):**
  - `ROSMASTER-M3PRO-DOCS-MD/HARDWARE.md`: hardware facts checked on one specific unit (Jetson Orin NX 8GB). Yours may differ.
  - `ROSMASTER-M3PRO-DOCS-MD/keep_in_mind.md`: reusable patterns and pitfalls collected while working through the courses.

## Version

The current docs were converted from Yahboom's repository as of **18 Nov 2025** (commit `617590d`). Yahboom has since added and renumbered some courses, so **folder numbers here may not match the latest upstream numbering**; refer to courses by name. An update to the latest version is in progress.

## Document format

Each tutorial is a folder:

```
<tutorial_name>/
  <tutorial_name>.md        # main content: headings, code blocks, tables, image references
  images/
    img_001.png             # extracted screenshot or diagram
    img_001.md              # sidecar: source page, image type, caption, description, OCR text
    img_002.png
    img_002.md
```

Image sidecar files contain:
- source PDF name and page number
- image type (screenshot, diagram, chart, photo, code, ui)
- an AI-generated caption and detailed description
- the text found in the image (OCR)

## Using it with Claude Code

1. Clone this repository somewhere on your computer:
   ```bash
   git clone https://github.com/Georgii-Tiutin/Yahboom_Rosmaster_M3Pro_Tutorial.git
   ```
2. Link the docs into your robot project:
   ```bash
   ln -s /path/to/Yahboom_Rosmaster_M3Pro_Tutorial/ROSMASTER-M3PRO-DOCS-MD ./ROSMASTER-M3PRO-DOCS-MD
   ```
3. Copy the agent file:
   ```bash
   mkdir -p .claude/agents
   cp /path/to/Yahboom_Rosmaster_M3Pro_Tutorial/agents/generic-rosmaster-m3pro.md .claude/agents/
   ```
4. Claude Code searches the documentation on demand with Grep/Glob/Read; nothing needs loading up front.

Other AI tools work the same way: point them at `ROSMASTER-M3PRO-DOCS-MD/`.

## Rebuilding from the PDFs

Requirements: `brew install tesseract`, `pip3 install marker-pdf pillow tqdm`, and the [Claude Code CLI](https://claude.com/claude-code) if you want AI image descriptions.

```bash
# Get the original PDFs
git clone https://github.com/YahboomTechnology/ROSMASTER-M3PRO.git

# Convert everything (resumes automatically if interrupted)
python3 convert_pdfs.py ROSMASTER-M3PRO ROSMASTER-M3PRO-DOCS-MD --description-mode claude

# Check the output is complete
python3 convert_pdfs.py ROSMASTER-M3PRO ROSMASTER-M3PRO-DOCS-MD --verify
```

`--description-mode` can be `claude` (AI descriptions), `heuristic` (basic descriptions, no AI) or `none`. Other options: `--force`, `--skip-failed`, `--dry-run`, `--only PATTERN`.

## Robot platform

| Component | Details |
|-----------|---------|
| Chassis | Mecanum wheels, pendulum suspension, omnidirectional |
| Arm | 6-DOF robotic arm on serial bus servos |
| Camera | Binocular structured-light depth camera (Orbbec DaBai DCW2) |
| LiDAR | Dual TOF (front-left + rear-right), 360° scanning |
| Main controllers | Raspberry Pi 5, Jetson Nano B01, Jetson Orin Nano / NX Super |
| ROS | ROS 2 Humble |
| AI | Speech recognition, NLU, multimodal interaction, RAG |

## Licence

- **The tutorials** (everything converted from Yahboom's PDFs, including the extracted images and their description files) belong to Yahboom Technology. No licence is granted for them here.
- **The conversion script, agent file, owner's notes and this README** are © 2026 Georgii Tiutin, released under the [MIT License](LICENSE). The exact list of files is at the top of `LICENSE`.

## Contact

- Questions about the robot or the tutorials themselves: Yahboom technical support, support@yahboom.com
- Problems with the conversion (missing pages, broken tables, wrong descriptions): open an issue in this repository
