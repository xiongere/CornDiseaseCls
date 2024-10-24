import base64
import json
import sys
import requests
import cv2  # 添加OpenCV库
import random  # 用于生成随机数据
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QFrame, QLabel
from main1006 import Ui_MainWindow


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.start_x = None
        self.start_y = None
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框

        # 摄像头显示
        self.video_label = QLabel(self.frame_5)
        self.video_label.setScaledContents(True)  # 允许缩放内容
        self.video_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)  # 设置大小策略
        layout = QVBoxLayout(self.frame_5)
        layout.addWidget(self.video_label)

        self.capture = cv2.VideoCapture(0)  # 0 为默认摄像头
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # 每30ms更新一次

        # 初始化电池和种仓容量
        self.battery = 100  # 电池从100%开始
        self.weight = 5000  # 种仓容量从5000g开始

        # 其他初始化代码...
        self.listWidget_2.itemSelectionChanged.connect(self.handleSelectionChange)
        self.listWidget_2.setCurrentRow(0)
        self.pushButton_5.clicked.connect(self.takePhoto)
        self.pushButton_6.clicked.connect(self.jiance)

        # 启动定时器，每10秒生成随机数据，并减少电池电量和种仓重量
        self.data_timer = QtCore.QTimer(self)
        self.data_timer.timeout.connect(self.generate_random_data)
        self.data_timer.start(10000)  # 每10秒生成一次数据

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 转换颜色格式
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            q_pixmap = QPixmap.fromImage(q_img)

            # 调整 QPixmap 尺寸以填充 QLabel
            self.video_label.setPixmap(
                q_pixmap.scaled(self.video_label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))

    def closeEvent(self, event):
        self.capture.release()  # 释放摄像头资源
        event.accept()

    # 随机数据生成函数，电池和种仓容量递减
    def generate_random_data(self):
        try:
            # 模拟随机传感器数据
            temp = round(random.uniform(15, 35), 1)  # 模拟温度
            humidity = round(random.uniform(20, 80), 1)  # 模拟湿度
            light_intensity = random.randint(100, 10000)  # 模拟光照强度
            co2 = random.randint(400, 5000)  # 模拟二氧化碳浓度
            tvoc = random.randint(50, 500)  # 模拟TVOC浓度

            # 电池和种仓减少
            if self.battery > 0:
                self.battery -= 1  # 每次减少1%
            if self.weight > 0:
                self.weight -= random.randint(1, 100)  # 每次减少1-100g

            # 更新界面上的数据显示
            self.label_16.setText(f"{temp}℃")
            self.label_18.setText(f"{humidity}%")
            self.label_14.setText(f"{self.battery}%")
            self.label_2.setText(f"{self.weight}g")
            self.label_20.setText(f"{light_intensity}lx")
            self.label_29.setText(f"{co2}ppm")
            self.label_27.setText(f"{tvoc}ppb")

            # 生成建议
            suggestions = []
            if temp > 30:
                suggestions.append("温度过高，建议降温。")
            if humidity < 30:
                suggestions.append("湿度较低，建议增加湿度。")
            if self.battery < 20:
                suggestions.append("电池电量低，建议充电。")
            if light_intensity < 300:
                suggestions.append("光照不足，建议增加光照。")
            if co2 > 1000:
                suggestions.append("二氧化碳浓度过高，建议通风。")
            if tvoc > 200:
                suggestions.append("TVOC浓度较高，建议检查空气质量。")

            # 显示建议在所有参数上方
            if suggestions:
                self.label_25.setText("\n".join(suggestions))
            else:
                self.label_25.setText("所有参数正常。")

        except Exception as e:
            print(e)

    def handleSelectionChange(self):
        text = self.listWidget_2.currentItem().text()
        if text == '主页':
            self.frame_2.show()
            self.frame_26.hide()
        elif text == '病虫害检测':
            self.frame_2.hide()
            self.frame_26.show()

    def takePhoto(self):
        img_url = "http://192.168.43.52:8080/?action=snapshot"

        response = requests.get(img_url)

        if response.status_code == 200:
            filename = "snapshot.jpg"
            with open(filename, "wb") as f:
                f.write(response.content)
            self.label_12.setPixmap(QPixmap("snapshot.jpg"))
            self.label_12.setAlignment(Qt.AlignCenter)
            print(f"Successfully downloaded {filename}!")
        else:
            print(f"Request failed with code {response.status_code}!")

    def jiance(self):
        url = 'https://yumi.market.alicloudapi.com/ai_image_single_classification/ai_yumi/yumi/v1'
        headers = {
            'Authorization': 'APPCODE d2de5be83d364550881b30cb64fb5d26',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        with open('./snapshot.jpg', 'rb') as f:
            image_base64 = base64.b64encode(f.read()).decode()
            image_base64 = "data:image/jpeg;base64,{}".format(image_base64)

            data = {
                'IMAGE': image_base64
            }
            response = requests.post(url, headers=headers, data=data, verify=True)
            content = json.loads(response.text)
            if content:
                try:
                    s = "分类名称: {}, 分类置信度: {}".format(content["图像分类实体信息"][0]['分类名称'],
                                                     content["图像分类实体信息"][0]['分类置信度'])
                    self.label_25.setText(s)
                except KeyError:
                    self.label_25.setText("检测API出现问题，请重新上传！")

    def mousePressEvent(self, event):
        super(MyMainForm, self).mousePressEvent(event)
        self.start_x = event.x()
        self.start_y = event.y()

    def mouseReleaseEvent(self, event):
        self.origin_x = None
        self.origin_y = None
        self.start_x = None
        self.start_y = None

    def mouseMoveEvent(self, event):
        try:
            super(MyMainForm, self).mouseMoveEvent(event)
            dis_x = event.x() - self.start_x
            dis_y = event.y() - self.start_y
            self.move(self.x() + dis_x, self.y() + dis_y)
        except BaseException as f:
            pass

    def effect_shadow_style(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 8)  # 偏移
        effect_shadow.setBlurRadius(48)  # 阴影半径
        effect_shadow.setColor(QColor(0, 0, 0, 30))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
