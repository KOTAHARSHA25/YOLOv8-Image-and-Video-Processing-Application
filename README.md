# NexVision AI: YOLOv8 Image and Video Processing

<div align="center">
  <h3><strong><a href="https://yolov8-image-and-video-processing.onrender.com/">🚀 Live Demo (Render)</a></strong></h3>
</div>

## 🚀 Introduction
NexVision AI is an advanced Computer Vision Engine powered by **PyTorch & Ultralytics YOLOv8**. It accurately identifies and classifies objects, detects various instance segments, and estimates human poses across static images, YouTube streams, local webcams, and RTSP IP cameras. The application utilizes a customized **Cyber Glassmorphism UI** with full AJAX single-page capabilities.

## 🗂️ Features
- **Local Media**: Upload images and videos for detection, segmentation, and pose estimation.
- **YouTube Streams**: Pipe live YouTube videos directly into the inference engine.
- **RTSP Streams**: Connect to IP security cameras.
- **Live Webcam**: Stream dynamically from your local system.

## 📥 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/KOTAHARSHA25/YOLOv8-Image-and-Video-Processing-Application.git
   cd YOLOv8-Image-and-Video-Processing-Application
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage
### Running the Application Local
To run the web app on your local machine, simply run:
```bash
python app.py
```
Then, open your web browser and go to `http://127.0.0.1:7860`.

### Selecting a Model
The application supports **dynamic model selection directly from the Web UI**.
1. Choose an input source (Local Media, YouTube, RTSP, or Webcam).
2. Select your desired model (Detection, Segmentation, Pose Estimation) from the drop-down menu.
3. Live inference stream will play natively within your browser window using pure Javascript, allowing you to seamlessly start and stop feeds without reloading the page.

## 🚀 Deployment
This application has been engineered to run within the memory constraints of Render.com's infrastructure using lazy-loading PyTorch model orchestration to prevent Out-Of-Memory (OOM) 502 limits.

🚀 **Live Deployment URL:** [https://yolov8-image-and-video-processing.onrender.com/](https://yolov8-image-and-video-processing.onrender.com/)

## 💻 Tech Stack
- **Backend**: Flask / Python
- **ML Architecture**: OpenCV, PyTorch, Ultralytics YOLOv8
- **Frontend**: Custom Glassmorphism Theme (HTML/CSS/JS/AJAX API)

## ✅ Conclusion
This project demonstrates robust streaming, single-page application (SPA) paradigms, and highly decoupled REST backend handling suitable for a production Computer Vision engineering portfolio.
