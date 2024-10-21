import base64
import json
import sys

# import paho.mqtt.client as mqtt
import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QFrame

from main1006 import Ui_MainWindow


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.start_x = None
        self.start_y = None
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框
        # 显示视频
        frame_layout = QVBoxLayout(self.frame_5)
        self.frame_web_view = QFrame(self)
        frame_layout.addWidget(self.frame_web_view)
        self.web_view = QWebEngineView(self.frame_web_view)
        frame_layout2 = QVBoxLayout(self.frame_web_view)
        frame_layout2.addWidget(self.web_view)
        # 加载视频页面
        self.web_view.load(QUrl('http://192.168.43.52:8080/?action=stream'))
        self.web_view.loadFinished.connect(self.on_load_finished)
        # 订阅主题，实时更新
        # self.mqtt_client = mqtt.Client()
        # self.mqtt_client.on_message = self.on_message
        # self.mqtt_client.connect("103.91.210.232", 42777, 60)  # 连接MQTT服务器参数
        # self.mqtt_client.subscribe("DHT11")
        # self.mqtt_client.subscribe("DC")
        # self.mqtt_client.subscribe("HX711")
        # self.mqtt_client.subscribe("BH1750")
        # self.mqtt_client.subscribe("SGP30")
        # 设置列表切换
        self.listWidget_2.itemSelectionChanged.connect(
            self.handleSelectionChange
        )
        self.listWidget_2.setCurrentRow(0)
        # 设置拍摄和检测按钮事件
        self.pushButton_5.clicked.connect(takePhoto)
        self.pushButton_6.clicked.connect(jiance)

    def on_message(self, client, userdata, message):
        try:
            topic = message.topic
            payload = message.payload.decode()
            if topic == "DHT11":  # 温湿度
                temp, humidity = payload.split(' ')
                self.label_16.setText(temp + "℃")
                self.label_18.setText(humidity + "%")
            elif topic == "DC":  # 电池
                self.label_14.setText(payload + "%")
            elif topic == "HX711":  # 种仓重量（g）
                self.label_2.setText(payload + "g")
            elif topic == "BH1750":  # 光照强度（lx）
                self.label_20.setText(payload + "lx")
            elif topic == "SGP30":  # co2和tvoc（ppm，ppb）
                co2, tvoc = payload.split(' ')
                self.label_29.setText(co2)  # co2
                self.label_27.setText(tvoc)  # tvoc
            elif topic == "土壤湿度":
                self.label_3.setText()
        except:
            pass

    def handleSelectionChange(self):
        text = self.listWidget_2.currentItem().text()
        if text == '主页':
            self.frame_2.show()
            self.frame_26.hide()
        elif text == '病虫害检测':
            self.frame_2.hide()
            self.frame_26.show()

    def on_load_finished(self):
        self.web_view.page().runJavaScript(
            '''document.getElementsByTagName("img")[0].setAttribute("style","border-radius:30px;")''')

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
        effect_shadow.setColor(QColor(162, 129, 247))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)

    def effect_shadow_style2(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 8)  # 偏移
        effect_shadow.setBlurRadius(48)  # 阴影半径
        effect_shadow.setColor(QColor(253, 139, 133))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)

    def effect_shadow_style3(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 8)  # 偏移
        effect_shadow.setBlurRadius(48)  # 阴影半径
        effect_shadow.setColor(QColor(243, 175, 189))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)

    def effect_shadow_style4(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 8)  # 偏移
        effect_shadow.setBlurRadius(48)  # 阴影半径
        effect_shadow.setColor(QColor(66, 226, 192))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)


def takePhoto():
    img_url = "http://192.168.43.52:8080/?action=snapshot"

    response = requests.get(img_url)

    if response.status_code == 200:
        filename = "snapshot.jpg"
        with open(filename, "wb") as f:
            f.write(response.content)
        myWin.label_12.setPixmap(QPixmap("snapshot.jpg"))
        myWin.label_12.setAlignment(Qt.AlignCenter)
        print(f"Successfully downloaded {filename}!")
    else:
        print(f"Request failed with code {response.status_code}!")


def jiance():
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
                myWin.label_25.setText(s)
            except KeyError:
                myWin.label_25.setText("检测API出现问题，请重新上传！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()


    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))


    # myWin.mqtt_client.on_connect = on_connect

    # myWin.mqtt_client.loop_start()
    sys.exit(app.exec_())
