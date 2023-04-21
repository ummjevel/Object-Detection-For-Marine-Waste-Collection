import torch
from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.pt', device='gpu')
    model.to('cuda')
    
    results = model.train(
        data='underwater.yaml',
        imgsz=640,
        epochs=100,
        patience=5,
        batch=16,
        name='yolov8n_underwater',
        device=0,
        optimizer='Adam'
    )


if __name__=="__main__":
    main()
