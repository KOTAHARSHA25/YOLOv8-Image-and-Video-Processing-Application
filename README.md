---
title: YOLOv8 Image & Video Processing
emoji: 🎥
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
short_description: YOLOv8 Object Detection, Segmentation & Pose Estimation
---

# YOLOv8-Image-and-Video-Processing-Application

## 🚀 Introduction
This project demonstrates the capabilities of the YOLOv8 model for image classification, object detection, and human pose estimation. It accurately identifies and classifies objects, detects various segments, and estimates human poses in both images and videos.

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
Then, open your web browser and go to `http://localhost:7860`.

### Selecting a Model
The application now supports **dynamic model selection directly from the Web UI**. You no longer need to pass command line arguments for models.
1. Upload your image or video on the web page.
2. Select your desired model (Detection, Segmentation, Pose) from the drop-down menu.
3. The application will automatically download the required YOLOv8 weights (if not already downloaded) and process your image/video!

## 🖥️ User Interface
The project provides a user-friendly interface through HTML templates. You can interact with the application, upload media, and choose your preferred computer vision task (Detection, Segmentation, Pose) natively in the browser without touching the command line.

## 🚀 Deployment
This application is fully Dockerized and deployed continuously on Hugging Face Spaces for free.

🚀 **Live Demo on Hugging Face Spaces:** [https://huggingface.co/spaces/HARSHAKOTA25/YOLOv8-Image-and-Video-Processing-Application](https://huggingface.co/spaces/HARSHAKOTA25/YOLOv8-Image-and-Video-Processing-Application)

## 💻 Source Code
Refer to `app.py` for the main application logic, including prediction functions and Flask routes.

## ✅ Conclusion
This project showcases the YOLOv8 model's capabilities for various image processing tasks, providing accurate results for image classification, object detection, and human pose estimation.

## 🌟 Future Enhancements
Potential future enhancements include real-time processing, expanded training datasets, multi-camera support, advanced tracking algorithms, and complex interaction recognition.
