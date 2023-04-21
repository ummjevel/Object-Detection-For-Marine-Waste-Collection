#!/usr/bin/env python3

import torch
from ultralytics import YOLO


def main():
    model = YOLO('runs/detect/yolov8n_underwater/weights/best.pt') # YOLO('yolov8n.pt')
    model.to('cuda')
    
    results = model.train(
        data='underwater_cuda.yaml',
        imgsz=640,
        epochs=100,
        patience=30,
        batch=32,
        name='yolov8n_underwater',
        device=0,
        optimizer='Adam'
    )


if __name__== "__main__":
    main()
