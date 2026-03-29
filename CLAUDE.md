# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

AI-friendly documentation repository for the **Yahboom ROSMASTER M3 Pro** ROS2 robot platform. Contains 237 tutorials converted from PDF to Markdown with extracted images and per-image description sidecars.

## Structure

- `ROSMASTER-M3PRO-DOCS-MD/` — Converted documentation: Markdown files + `images/` folders with PNGs and `.md` sidecar descriptions. Organized in numbered course directories (0–17) mirroring the original PDF structure.
- `agents/` — Claude Code agent files for robot development contexts.
  - `generic-rosmaster-m3pro.md` — Load this agent for any ROSMASTER M3 Pro development work. Contains platform overview, hardware/software specs, and a documentation map with references to all course folders.
- `convert_pdfs.py` — Pipeline script that converts PDFs to Markdown + image sidecars (Marker + PyMuPDF + Tesseract OCR + Claude descriptions).
- `ROSMASTER-M3PRO.Download.link` — Git origin for the original PDF repository (gitignored).
- `ROSMASTER-M3PRO/` — Original PDF documentation (gitignored, clone from link above).
- `incoming/` — Staging area (gitignored).

## How to Find Documentation

Use Grep/Glob to search through `ROSMASTER-M3PRO-DOCS-MD/`. Course directories are numbered 0–17:

| # | Topic |
|---|-------|
| 0 | Configuration & operation quickstart |
| 1–4 | AI large model (preparation, basics, text version, voice version) |
| 5 | Chassis control (Mecanum wheels, velocity calibration, line patrol) |
| 6 | LiDAR (SLAM mapping, Navigation2, obstacle avoidance, tracking) |
| 7 | Depth camera (distance/volume measurement, YOLOv8, tracking) |
| 8 | Mediapipe (hand/face/posture detection, gesture control) |
| 9 | Robotic arm & 3D gripping (sorting, tracking, KCF) |
| 10 | MoveIt2 simulation (kinematics, trajectory planning, collision) |
| 11 | Multi-vehicle (formation, coordinated navigation) |
| 12 | STM32 control board (dev environment, basic routines, micro-ROS) |
| 13 | Main controller setup (Jetson Nano, Orin, Raspberry Pi 5) |
| 14 | Linux system basics |
| 15 | ROS2 basics (full curriculum: nodes, topics, services, TF2, Gazebo) |
| 16 | Docker |
| 17 | Image processing (OpenCV fundamentals) |

## Document Format

Each tutorial is a folder containing:
- `<name>.md` — Main markdown with text, code blocks, tables, and image references
- `images/img_NNN.png` — Extracted screenshots and diagrams
- `images/img_NNN.md` — Sidecar with metadata (source page, type), caption, detailed description, and OCR text

## PDF Conversion Pipeline

```bash
python3 convert_pdfs.py ROSMASTER-M3PRO ROSMASTER-M3PRO-DOCS-MD --description-mode claude
```

Supports `--force`, `--skip-failed`, `--verify`, `--only PATTERN`. Auto-resumes via `.conversion_progress.json`.
