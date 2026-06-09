# 🐳 Edge AI Deployment: YOLOv11 on Raspberry Pi 5 via Hailo AI HAT+

<div align="left">
  <img src="https://img.shields.io/badge/Raspberry%20Pi-5-C51A4A?style=for-the-badge&logo=Raspberry-Pi&logoColor=white" alt="RPi5">
  <img src="https://img.shields.io/badge/Hailo-8L%20%7C%2010-00E676?style=for-the-badge" alt="Hailo">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/YOLOv11-⚡-orange?style=for-the-badge" alt="YOLOv11">
</div>

<br>

## 🌟 Overview
This repository contains a production-ready, fully containerized deployment pipeline for running **YOLOv11** object detection models on the **Raspberry Pi 5** accelerated by the **Hailo AI HAT+ (Hailo-8L/10)**. 

Designed specifically for real-time edge processing in autonomous systems and ADAS applications, this architecture guarantees consistent frame rates (FPS) and sub-millisecond inference latencies while protecting the edge OS from dependency corruption.

---

## 🚀 Why Docker for Edge AI Systems?
Deploying deep learning models on embedded hardware often results in broken operating systems due to tight version coupling between AI runtimes (Hailo-RT), framework bindings (OpenCV), and system libraries. This project uses Docker to apply the **Immutable Infrastructure** philosophy:

* **Complete Environment Isolation:** All heavy dependencies (`hailo-platform`, `opencv-python-headless`, `numpy`) are isolated inside an ARM64 container. The host OS remains completely pristine.
* **Deterministic Hardware Passthrough:** Safely maps the host's PCIe accelerator device (`/dev/hailo0`) straight into the container without loss of performance.
* **Instant Scalability:** Simplifies fleet deployment. Running this advanced ADAS vision pipeline on 1 or 100 Raspberry Pi 5 units requires the exact same single command.

---

## 🏗️ System Mimarisi & Data Pipeline

```mermaid
graph LR
    A[🎥 Live Camera Input] -->|Raw Frames| B[🐳 Docker Container]
    B -->|Pre-processing| C[⚙️ Hailo-RT Engine]
    C -->|PCIe Passthrough /dev/hailo0| D[🚀 Hailo AI HAT+ Hardware]
    D -->|INT8 Accelerated Inference| C
    C -->|Tensor Output| E[🛠️ Post-Processing & NMS]
    E -->|Calculated Bounding Boxes| F[🖥️ Visual Output / Actuator Control]
