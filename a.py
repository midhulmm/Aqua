data_path = './data/file.csv'
%cd /content/drive/MyDrive/yolo2
pip install ultralytics
from ultralytics import YOLO
model=YOLO("/content/drive/MyDrive/yolo2/runs/detect/train/weights/best.pt")
data=model("/content/drive/MyDrive/yolo2/train/images/002_jpg.rf.130be8cea6916f0b23e66d22daca3d3a.jpg")
data[0].show()