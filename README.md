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
### Running the Application
```bash
python app.py --weights <model_weights> --source <input_source> --device <cpu/gpu>
```
Example:
```bash
python app.py --weights yolov8s.pt --source data/images --device cpu
```
### Command Line Arguments
- `--weights`: Path to the YOLOv8 model weights file (default is `yolov8s.pt`).
- `--source`: Directory path for input images or videos.
- `--device`: Specify the device to run the model on (`cpu` or `gpu`).

## 🖥️ User Interface
The project provides a user-friendly interface through HTML templates for interacting with the application and selecting different input sources and tasks.


## 📊 Model Usage
- For object detection: `python app.py --weights yolov8s.pt`
- For instance segmentation: `python app.py --weights yolov8s-seg.pt`
- For image classification: `python app.py --weights yolov8s-cls.pt`
- For human pose estimation: `python app.py --weights yolov8s-pose.pt`

## 🚀 Deployment
Run the `app.py` script with the desired model and input source to start the Flask application on the specified port (default is 5000).

## 💻 Source Code
Refer to `app.py` for the main application logic, including prediction functions and Flask routes.

## ✅ Conclusion
This project showcases the YOLOv8 model's capabilities for various image processing tasks, providing accurate results for image classification, object detection, and human pose estimation.

## 🌟 Future Enhancements
Potential future enhancements include real-time processing, expanded training datasets, multi-camera support, advanced tracking algorithms, and complex interaction recognition.
