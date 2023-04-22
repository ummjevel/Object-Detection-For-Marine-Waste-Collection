#!/usr/bin/env python3

import torch
from ultralytics import YOLO


def main():
    model = YOLO('runs/detect/yolov8m_underwater/weights/best.pt') # YOLO('yolov8m.pt')  # YOLO('runs/detect/yolov8n_underwater/weights/best.pt') # YOLO('yolov8n.pt')
    model.to('cuda')
    
    results = model.train(
        data='underwater_cuda.yaml',
        imgsz=640,
        epochs=100,
        patience=30,
        batch=16,
        name='yolov8m_underwater',
        device=0,
        optimizer='Adam'
    )


if __name__== "__main__":
    main()
