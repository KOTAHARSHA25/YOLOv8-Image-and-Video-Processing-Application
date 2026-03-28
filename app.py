from flask import Flask, render_template, Response, request, jsonify
import json
import argparse
import os
import sys
from pathlib import Path
from ultralytics import YOLO
from ultralytics.utils.checks import cv2, print_args
from utils.general import update_options

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))

app = Flask(__name__)

# Initialize default options so it doesn't crash under Gunicorn/WSGI
class DefaultOpt:
    source = '0'
    save_txt = False
    conf = 0.25
    iou = 0.7
    imgsz = [640]
    half = False
    device = ''
    show = False
    save = False
    save_conf = False
    save_crop = False
    show_labels = True
    show_conf = True
    max_det = 300
    vid_stride = 1
    stream_buffer = False
    line_width = None
    visualize = False
    augment = False
    agnostic_nms = False
    retina_masks = False
    classes = None
    show_boxes = True
    exist_ok = False
    project = ROOT / 'runs/detect'
    name = 'exp'
    dnn = False
    raw_data = ROOT / 'data/raw'

opt = DefaultOpt()

import gc

# Memory-safe model lazy loader
models_cache = {}
def get_model(model_type):
    global models_cache
    if model_type not in models_cache:
        # Clear out other models to prevent Render Free Tier OOM (512MB RAM Limit)
        models_cache.clear()
        gc.collect()
        if model_type == 'Segmentation':
            models_cache[model_type] = YOLO('yolov8s-seg.pt')
        elif model_type == 'Pose Estimation':
            models_cache[model_type] = YOLO('yolov8s-pose.pt')
        else:
            models_cache[model_type] = YOLO('yolov8s.pt')
    return models_cache[model_type]

def predict(opt, model_type="Detection"):
    current_model = get_model(model_type)
    results = current_model(**vars(opt), stream=True)

    for result in results:
        if opt.save_txt:
            result_json = json.loads(result.tojson())
            yield json.dumps({'results': result_json})
        else:
            im0 = cv2.imencode('.jpg', result.plot())[1].tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + im0 + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/local')
def locals():
    return render_template('local.html')

@app.route('/yt')
def yt():
    return render_template('yt.html')

@app.route('/rtsp')
def rtsp():
    return render_template('rtsp.html')

@app.route('/webcam')
def cams():
    return render_template('cams.html')

@app.route('/upload', methods=['POST'])
def handle_upload():
    # New route for AJAX uploads to prevent DOM breaking
    if 'myfile' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    uploaded_file = request.files['myfile']
    if uploaded_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    from werkzeug.utils import secure_filename
    filename = secure_filename(uploaded_file.filename)
    
    # Save the file securely
    raw_data_dir = Path(__file__).parent / 'data' / 'raw'
    raw_data_dir.mkdir(parents=True, exist_ok=True)
    source_path = raw_data_dir / filename
    uploaded_file.save(str(source_path))

    return jsonify({
        'success': True, 
        'source': str(source_path.resolve())
    })

@app.route('/predict', methods=['GET'])
def video_feed():
    import copy
    req_opt = copy.copy(opt)
    
    source_query = request.args.get('source')
    save_txt_query = request.args.get('save_txt')

    if source_query:
        req_opt.source = source_query
    if save_txt_query == 'T':
        req_opt.save_txt = True
    else:
        req_opt.save_txt = False
        
    model_type = request.args.get('model_type', 'Detection')
    
    return Response(predict(req_opt, model_type), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model','--weights', type=str, default=ROOT / 'yolov8s.pt', help='model path or triton URL')
    parser.add_argument('--source', type=str, default=ROOT / 'data/images', help='source directory for images or videos')
    parser.add_argument('--conf','--conf-thres', type=float, default=0.25, help='object confidence threshold for detection')
    parser.add_argument('--iou', '--iou-thres', type=float, default=0.7, help='intersection over union (IoU) threshold for NMS')
    parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[640], help='image size as scalar or (h, w) list, i.e. (640, 480)')
    parser.add_argument('--half', action='store_true', help='use half precision (FP16)')
    parser.add_argument('--device', default='', help='device to run on, i.e. cuda device=0/1/2/3 or device=cpu')
    parser.add_argument('--show','--view-img', default=False, action='store_true', help='show results if possible')
    parser.add_argument('--save', action='store_true', help='save images with results')
    parser.add_argument('--save_txt','--save-txt', action='store_true', help='save results as .txt file')
    parser.add_argument('--save_conf', '--save-conf', action='store_true', help='save results with confidence scores')
    parser.add_argument('--save_crop', '--save-crop', action='store_true', help='save cropped images with results')
    parser.add_argument('--show_labels','--show-labels', default=True, action='store_true', help='show labels')
    parser.add_argument('--show_conf', '--show-conf', default=True, action='store_true', help='show confidence scores')
    parser.add_argument('--max_det','--max-det', type=int, default=300, help='maximum number of detections per image')
    parser.add_argument('--vid_stride', '--vid-stride', type=int, default=1, help='video frame-rate stride')
    parser.add_argument('--stream_buffer', '--stream-buffer', default=False, action='store_true', help='buffer all streaming frames (True) or return the most recent frame (False)')
    parser.add_argument('--line_width', '--line-thickness', default=None, type=int, help='The line width of the bounding boxes. If None, it is scaled to the image size.')
    parser.add_argument('--visualize', default=False, action='store_true', help='visualize model features')
    parser.add_argument('--augment', default=False, action='store_true', help='apply image augmentation to prediction sources')
    parser.add_argument('--agnostic_nms', '--agnostic-nms', default=False, action='store_true', help='class-agnostic NMS')
    parser.add_argument('--retina_masks', '--retina-masks', default=False, action='store_true', help='whether to plot masks in native resolution')
    parser.add_argument('--classes', type=list, help='filter results by class, i.e. classes=0, or classes=[0,2,3]') # 'filter by class: --classes 0, or --classes 0 2 3')
    parser.add_argument('--show_boxes', default=True, action='store_false', help='Show boxes in segmentation predictions')
    parser.add_argument('--exist_ok', '--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--project', default=ROOT / 'runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--dnn', action='store_true', help='use OpenCV DNN for ONNX inference')
    parser.add_argument('--raw_data', '--raw-data', default=ROOT / 'data/raw', help='save raw images to data/raw')
    parser.add_argument('--port', default=7860, type=int, help='port deployment')
    opt, unknown = parser.parse_known_args()
    print_args(vars(opt))
    port = opt.port
    delattr(opt, 'port')
    raw_data = Path(opt.raw_data)
    raw_data.mkdir(parents=True, exist_ok=True)
    delattr(opt, 'raw_data')
    # model = YOLO(str(opt.model)) # Moved to global dictionary cache
    app.run(host='0.0.0.0', port=port, debug=False)