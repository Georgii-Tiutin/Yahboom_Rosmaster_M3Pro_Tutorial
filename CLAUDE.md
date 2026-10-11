# CLAUDE.md

## Repository Purpose

AI-friendly documentation repository for the **Yahboom ROSMASTER M3 Pro** ROS2 robot platform. Contains 237 tutorials converted from PDF to Markdown with extracted images and per-image description sidecars.

## Agents

- `agents/generic-rosmaster-m3pro.md` — Load this agent for any ROSMASTER M3 Pro development work. Contains platform overview, hardware/software specs, and a documentation map with references to all course folders.

## How to Find Documentation

Use Grep/Glob to search through `ROSMASTER-M3PRO-DOCS-MD/`. Course directories are numbered 0–17.

> **Caveat (2026-08-26): these numbers are a stale snapshot.** This tree was converted
> *before* an upstream Yahboom repository update in which some courses changed position, so
> the local folder numbers do not reliably match the current official numbering. **Refer to
> courses by name, not by number** — a given number here may point at a different course
> than the same number upstream. The table below describes *this local tree* and remains
> correct for searching it. (A likely symptom of the same reshuffle: course `0.` skips from
> `4.` to `6.` with no section 5.)


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

## PDF Conversion Pipeline

```bash
python3 convert_pdfs.py ROSMASTER-M3PRO ROSMASTER-M3PRO-DOCS-MD --description-mode claude
```

Supports `--force`, `--skip-failed`, `--verify`, `--only PATTERN`. Auto-resumes via `.conversion_progress.json`.
