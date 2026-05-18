from ultralytics import YOLO

#LOAD BASE MODEL
model = YOLO('yolov8n.pt')

#TRAIN THE MODEL
model.train(
    data='data.yaml',
    epochs=100, 
    imgsz=640, 
    batch=4
)