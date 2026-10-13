# CLAUDE.md

## Repository Purpose

AI-friendly documentation repository for the **Yahboom ROSMASTER M3 Pro** ROS2 robot platform. Contains 288 tutorials (courses 00–23, Yahboom upstream commit `015d065`, Aug 2026) converted from PDF to Markdown with extracted images and per-image description sidecars.

## Agents

- `agents/generic-rosmaster-m3pro.md` — Load this agent for any ROSMASTER M3 Pro development work. Contains platform overview, hardware/software specs, and a documentation map with references to all course folders.

## How to Find Documentation

Use Grep/Glob to search through `ROSMASTER-M3PRO-DOCS-MD/`. Course folders are numbered `00`–`23` and match Yahboom's current upstream numbering.

| # | Course |
|---|--------|
| 00 | Configuration and operation guide (quick start, login, Docker entry, firmware parameters) |
| 01 | Chassis control (mecanum wheels, velocity calibration) |
| 02 | LiDAR (SLAM mapping, Navigation2, obstacle avoidance) |
| 03 | Depth camera (DaBai DCW2, distance/volume measurement, YOLO) |
| 04 | Robotic arm and 3D space gripping |
| 05 | Road network planning and navigation |
| 06–10 | OpenClaw (basics, interaction methods, development, embodied applications, scenario sandbox) |
| 11–14 | AI large models (basics, development, voice version, text version) |
| 15 | Mediapipe vision |
| 16 | MoveIt2 simulation |
| 17 | Multi-vehicle |
| 18 | STM32 control board (dev environment, firmware flashing, basic routines, micro-ROS) |
| 19 | Docker |
| 20 | Image processing basics (OpenCV) |
| 21 | Main controller setup (Jetson Nano, Orin, Raspberry Pi 5) |
| 22 | Linux system basics |
| 23 | ROS 2 basics |

`HARDWARE.md` and `keep_in_mind.md` in `ROSMASTER-M3PRO-DOCS-MD/` are the owner's notes on one specific unit, not Yahboom content. Their "course 0" references mean `00.Configuration and Operation Guide`.

## PDF Conversion Pipeline

```bash
python3 convert_pdfs.py ROSMASTER-M3PRO ROSMASTER-M3PRO-DOCS-MD --description-mode claude
```

Supports `--force`, `--skip-failed`, `--verify`, `--only PATTERN`. Auto-resumes via `.conversion_progress.json`.
