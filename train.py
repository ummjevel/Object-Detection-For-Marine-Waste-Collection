#!/usr/bin/env python3

import torch
import gc
from ultralytics import YOLO


def main():

    gc.collect()
    torch.cuda.empty_cache()
    model = YOLO('runs/detect/yolov8m_underwater2/weights/best.pt') # YOLO('yolov8m.pt')  # YOLO('runs/detect/yolov8n_underwater/weights/best.pt') # YOLO('yolov8n.pt')
    model.to('cuda')
    
    results = model.train(
        data='underwater_cuda.yaml',
        imgsz=640,
        epochs=300,
        patience=50,
        batch=16,
        name='yolov8m_underwater',
        device=0,
        optimizer='Adam'
    )


if __name__== "__main__":
    main()
