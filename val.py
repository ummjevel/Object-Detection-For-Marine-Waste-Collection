#!/usr/bin/env python3

import torch
from ultralytics import YOLO

model = YOLO("runs/detect/yolov8n_underwater2/weights/best.pt")
model.val()
