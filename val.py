#!/usr/bin/env python3

import torch
from ultralytics import YOLO

model = YOLO("model.pt")
model.val()
model.val(data='underwater_cuda.yaml')