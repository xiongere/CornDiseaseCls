#coding:utf-8
from ultralytics import YOLO
import matplotlib
matplotlib.use('TkAgg')

if __name__ == '__main__':
    # 训练模型配置文件路径
    yolo_yaml_path = 'ultralytics/cfg/models/v8/yolov8-cls.yaml'
    # 官方预训练模型路径
    pre_model_path = "yolov8n-cls.pt"
    # 加载预训练模型
    model = YOLO(yolo_yaml_path).load(pre_model_path)
    # 模型训练
    model.train(data='datasets/Data', epochs=150, batch=4)




