# 해양 쓰레기 수거 자동화를 위한 객체 인식 모델 개발

## 개요

- 해양 쓰레기 종류는 해안, 부유, 침적 쓰레기로 나뉨.
- 해양 침적 쓰레기는 5만 톤이 유입되지만 3만 톤만 수거되고 있는 상황.
- 해양 침적 쓰레기 수거의 경우 정보 지원 및 전문인력과 시간이 소요됨.
- 해양 침적 쓰레기 객체 인식을 위한 모델을 개발한다면,
    - 해양 침적 쓰레기 수거 시 실시하는 설계조사에 도움이 되며, 수중 조사 솔루션 개발로 확장 가능
    - 활용방안으로는 정책 수행, 폐기물로 업사이클링, 미세플라스틱 생성 억제에 도움

## 기간
- 2022.01.03 ~ 2022.02.17 (1차, 팀), repository에 있는 pdf 참고. yolov4 사용
- 2023.04.10 ~ 2023.04.29 (2차, 개인), yolov8 사용, 현재 readme 내용

## 데이터
### 출처
[AI-HUB 해양 침적 쓰레기 이미지](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=236)
### 규모
- 수중 촬영 이미지만 사용
- 총 5개의 라벨(tire, trap, net, wood, ropes)
- 9008개의 이미지
- 1920x1080

## 전처리
1. xml to text
2. split train data and validation data from train dataset
3. resize(640x640) and padding
4. make yaml file
5. (개선) augmentation

## 학습
- model : yolov8(yolov8n, yolov8m)
- gpu : NVIDIA GeForce RTX 2080
- version: Python-3.8.16 torch-1.12.1 CUDA:0

### nano(1, 2) -> medium(3, 4, 5)

#### version 1
- patience = 5
- model = yolov8n.pt
- batch = 16
- 20 epochs completed in 0.299 hours.
- ![image](https://github.com/ummjevel/Object-Detection-For-Marine-Waste-Collection/assets/49097057/245977c6-f46e-44bf-9cf2-70c4cd919502)

#### version 2
- patience = 30
- model = runs/detect/yolov8n_underwater/weights/best.pt
- batch = 32
- 100 epochs completed in 1.395 hours.
- ![image](https://github.com/ummjevel/Object-Detection-For-Marine-Waste-Collection/assets/49097057/44dc9bb0-54f6-4455-9c79-5c45c73bb50d)


### version 3
- patience = 30
- model = yolov8m.pt
- batch = 16
- 100 epochs completed in 4.516 hours.
- ![image](https://github.com/ummjevel/Object-Detection-For-Marine-Waste-Collection/assets/49097057/d363af71-a7a3-4b07-bc50-6a23eeb9e191)

### version 4
- patience = 30
- model = runs/detect/yolov8m_underwater/weights/best.pt
- batch = 16
- 100 epochs completed in 4.499 hours.
- ![image](https://github.com/ummjevel/Object-Detection-For-Marine-Waste-Collection/assets/49097057/78124db1-6d8f-4642-a962-acb557193add)

### version 5
- patience = 50
- model = runs/detect/yolov8m_underwater2/weights/best.pt
- batch = 16
- 295 epochs completed in 13.293 hours. (Best results observed at epoch 245)
- ![image](https://github.com/ummjevel/Object-Detection-For-Marine-Waste-Collection/assets/49097057/ba5645a9-4756-48e1-9208-a66daec40255)

## 개선
- method: augmentation (albumentations)
```
transform = A.Compose([
    A.OneOf([
        A.HorizontalFlip(p=1),
        A.RandomRotate90(p=1),
        A.VerticalFlip(p=1),
        A.GaussNoise(p=1),
        A.HueSaturationValue(50, 50, 20,  p=1.0),
        A.RGBShift(50, 50, 50,  p=1.0),
        A.RandomBrightnessContrast(0.5, 0.2, True,  p=1.0),
        A.RandomFog(0.3, 0.5, 0.08,  p=1.0),
        A.RandomGamma((80, 200),  p=1.0),
        A.CLAHE(6.0, (10, 10), p=1.0)
    ], p=1),
], bbox_params=A.BboxParams(format='yolo'))
```
- tire : 0, trap : 1, net : 2, wood : 3, ropes : 4
- {'0': 1949, '3': 1526, '4': 2201, '1': 2811, '2': 595} -> {'0': 2860, '3': 2827, '4': 3059, '1': 2937, '2': 2801}
- 9008 -> 11368
- 하나의 이미지에 여러 라벨의 객체가 있습니다.
- 라벨 별 개수를 비슷하게 맞추려 노력하였습니다.

### version 6
- patience = 50
- model = runs/detect/yolov8m_underwater5/weights/best.pt
- batch = 16
-  136 epochs completed in 9.129 hours.(Best results observed at epoch 86)
- ![image](https://github.com/ummjevel/Object-Detection-For-Marine-Waste-Collection/assets/49097057/5d9a1179-7aee-49fc-a50e-83579ac9c8ba)


- PR curve 
<img src="https://github.com/ummjevel/Object-Detection-For-Marine-Waste-Collection/assets/49097057/4b3cd6de-b9eb-459a-b1f0-da90d9af2256)" width=50% height=50%>

- F1 curve 
<img src="https://github.com/ummjevel/Object-Detection-For-Marine-Waste-Collection/assets/49097057/1d505b46-c426-475b-95fa-9e97fc487784)" width=50% height=50%>



