# -*- coding: utf-8 -*-
import time
from PyQt5.QtWidgets import QApplication , QMainWindow, QFileDialog, \
    QMessageBox,QWidget,QHeaderView,QTableWidgetItem, QAbstractItemView
import sys
import os
from ultralytics import YOLO
sys.path.append('UIProgram')
from UIProgram.UiMain import Ui_MainWindow
import sys
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal,QCoreApplication
import detect_tools as tools
import cv2
import Config
from UIProgram.QssLoader import QSSLoader
import numpy as np
import torch
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initMain()
        self.signalconnect()

        # 加载css渲染效果
        style_file = 'UIProgram/style.css'
        qssStyleSheet = QSSLoader.read_qss_file(style_file)
        self.setStyleSheet(qssStyleSheet)

        self.conf = 0.5
        self.unkonwn_text = '无法识别'

        # 视频与摄像头检测频率，每5帧检测一次
        self.detection_frequency = 5

    def signalconnect(self):
        self.ui.PicBtn.clicked.connect(self.open_img)
        self.ui.VideoBtn.clicked.connect(self.vedio_show)
        self.ui.CapBtn.clicked.connect(self.camera_show)
        self.ui.FilesBtn.clicked.connect(self.detact_batch_imgs)
        self.ui.tableWidget.cellClicked.connect(self.on_cell_clicked)

    def initMain(self):
        self.show_width = 770
        self.show_height = 480

        self.org_path = None

        self.is_camera_open = False
        self.cap = None

        self.device = 0 if torch.cuda.is_available() else 'cpu'

        # 加载检测模型
        self.model = YOLO(Config.model_path, task='classify')
        self.model(np.zeros((48, 48, 3)).astype(np.uint8), device=self.device)  #预先加载推理模型

        # 更新视频图像
        self.timer_camera = QTimer()

        # 更新检测信息表格
        # self.timer_info = QTimer()

        # 表格
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.ui.tableWidget.setColumnWidth(0, 100)  # 设置列宽
        self.ui.tableWidget.setColumnWidth(1, 300)
        self.ui.tableWidget.setColumnWidth(2, 210)
        self.ui.tableWidget.setColumnWidth(3, 140)
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 表格铺满
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        # self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置表格不可编辑
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置表格整行选中
        self.ui.tableWidget.verticalHeader().setVisible(False)  # 隐藏列标题
        self.ui.tableWidget.setAlternatingRowColors(True)  # 表格背景交替


    def open_img(self):
        if self.cap:
            # 打开图片前关闭摄像头
            self.video_stop()
            self.is_camera_open = False
            self.ui.CapBtn.setText('打开摄像头')
            self.cap = None

        # 弹出的窗口名称：'打开图片'
        # 默认打开的目录：'./'
        file_path, _ = QFileDialog.getOpenFileName(None, '打开图片', './', "Image files (*.jpg *.jpeg *.png *.bmp)")
        if not file_path:
            return

        self.org_path = file_path
        self.org_img = tools.img_cvread(self.org_path)

        # 目标检测
        t1 = time.time()
        self.results = self.model(self.org_path, conf=self.conf)[0]
        print(self.results)
        self.conf_list = self.results.probs.data.tolist()

        cls_index = self.results.probs.top1
        conf = self.conf_list[cls_index]
        if conf > self.conf:
            show_conf = '{:.2f}%'.format(conf*100)
            res_name = Config.CH_names[cls_index]
            self.ui.textEdit_2.setText(Config.method_infos[res_name])
        else:
            show_conf = '100%'
            res_name = self.unkonwn_text
            self.ui.textEdit_2.setText('')

        self.ui.label_conf.setText(show_conf)
        self.ui.resLb.setText(res_name)

        t2 = time.time()
        take_time_str = '{:.3f} s'.format(t2 - t1)
        self.ui.time_lb.setText(take_time_str)

        now_img = self.org_img.copy()

        # 获取缩放后的图片尺寸
        self.img_width, self.img_height = self.get_resize_size(now_img)
        resize_cvimg = cv2.resize(now_img,(self.img_width, self.img_height))
        pix_img = tools.cvimg_to_qpiximg(resize_cvimg)
        self.ui.label_show.setPixmap(pix_img)
        self.ui.label_show.setAlignment(Qt.AlignCenter)

        # # 删除表格所有行
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.clearContents()
        self.tabel_info_show(res_name, show_conf, path=self.org_path)


    def detact_batch_imgs(self):
        # 批量检测图片
        if self.cap:
            # 打开图片前关闭摄像头
            self.video_stop()
            self.is_camera_open = False
            self.ui.CapBtn.setText('打开摄像头')
            self.cap = None
        directory = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
        if not  directory:
            return
        # # 删除表格所有行
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.clearContents()
        self.org_path = directory
        img_suffix = ['jpg','png','jpeg','bmp']
        for file_name in os.listdir(directory):
            full_path = os.path.join(directory,file_name)
            if os.path.isfile(full_path) and file_name.split('.')[-1].lower() in img_suffix:
                img_path = full_path
                self.org_img = tools.img_cvread(img_path)
                # 目标检测
                t1 = time.time()
                self.results = self.model(self.org_img, conf=self.conf)[0]
                self.conf_list = self.results.probs.data.tolist()

                cls_index = self.results.probs.top1
                conf = self.conf_list[cls_index]
                if conf > self.conf:
                    show_conf = '{:.2f}%'.format(conf * 100)
                    res_name = Config.CH_names[cls_index]
                    self.ui.textEdit_2.setText(Config.method_infos[res_name])
                else:
                    show_conf = '100%'
                    res_name = self.unkonwn_text
                    self.ui.textEdit_2.setText('')

                self.ui.label_conf.setText(show_conf)
                self.ui.resLb.setText(res_name)

                t2 = time.time()
                take_time_str = '{:.3f} s'.format(t2 - t1)
                self.ui.time_lb.setText(take_time_str)

                now_img = self.org_img.copy()

                # 获取缩放后的图片尺寸
                self.img_width, self.img_height = self.get_resize_size(now_img)
                resize_cvimg = cv2.resize(now_img, (self.img_width, self.img_height))
                pix_img = tools.cvimg_to_qpiximg(resize_cvimg)
                self.ui.label_show.setPixmap(pix_img)
                self.ui.label_show.setAlignment(Qt.AlignCenter)

                # # 删除表格所有行
                # self.ui.tableWidget.setRowCount(0)
                # self.ui.tableWidget.clearContents()
                self.tabel_info_show(res_name, show_conf, path=img_path)
                self.ui.tableWidget.scrollToBottom()
                QApplication.processEvents()  #刷新页面


    def get_video_path(self):
        file_path, _ = QFileDialog.getOpenFileName(None, '打开视频', './', "Image files (*.avi *.mp4 *.wmv *.mkv)")
        if not file_path:
            return None
        self.org_path = file_path
        return file_path

    def video_start(self):
        self.video_index = 0
        # 删除表格所有行
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.clearContents()

        # 定时器开启，每隔一段时间，读取一帧
        self.timer_camera.start(1)
        self.timer_camera.timeout.connect(self.open_frame)

    def tabel_info_show(self, cls, conf, path=None):
        row_count = self.ui.tableWidget.rowCount()  # 返回当前行数(尾部)
        self.ui.tableWidget.insertRow(row_count)  # 尾部插入一行
        item_id = QTableWidgetItem(str(row_count+1))  # 序号
        item_id.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置文本居中
        item_path = QTableWidgetItem(str(path))  # 路径
        # item_path.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        item_cls = QTableWidgetItem(str(cls))
        item_cls.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置文本居中

        item_conf = QTableWidgetItem(str(conf))
        item_conf.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置文本居中

        self.ui.tableWidget.setItem(row_count, 0, item_id)
        self.ui.tableWidget.setItem(row_count, 1, item_path)
        self.ui.tableWidget.setItem(row_count, 2, item_cls)
        self.ui.tableWidget.setItem(row_count, 3, item_conf)
        self.ui.tableWidget.scrollToBottom()

    def video_stop(self):
        self.cap.release()
        self.timer_camera.stop()
        # self.timer_info.stop()

    def open_frame(self):
        ret, now_img = self.cap.read()
        if ret:
            self.video_index += 1
            if self.video_index % self.detection_frequency == 0:
                # 检测频率self.detection_frequency
                # 目标检测
                t1 = time.time()
                self.results = self.model(now_img, conf=self.conf)[0]
                self.conf_list = self.results.probs.data.tolist()

                cls_index = self.results.probs.top1
                conf = self.conf_list[cls_index]
                if conf > self.conf:
                    show_conf = '{:.2f}%'.format(conf * 100)
                    res_name = Config.CH_names[cls_index]
                    self.ui.textEdit_2.setText(Config.method_infos[res_name])

                else:
                    show_conf = '100%'
                    res_name = self.unkonwn_text
                    self.ui.textEdit_2.setText('')

                self.ui.label_conf.setText(show_conf)
                self.ui.resLb.setText(res_name)

                t2 = time.time()
                take_time_str = '{:.3f} s'.format(t2 - t1)
                self.ui.time_lb.setText(take_time_str)

                # 删除表格所有行
                # self.ui.tableWidget.setRowCount(0)
                # self.ui.tableWidget.clearContents()
                if self.is_camera_open is True:
                    path = 'Camera'
                else:
                    path = self.org_path
                self.tabel_info_show(res_name, show_conf, path=path)

            # 获取缩放后的图片尺寸
            self.img_width, self.img_height = self.get_resize_size(now_img)
            resize_cvimg = cv2.resize(now_img, (self.img_width, self.img_height))
            pix_img = tools.cvimg_to_qpiximg(resize_cvimg)
            self.ui.label_show.setPixmap(pix_img)
            self.ui.label_show.setAlignment(Qt.AlignCenter)
        else:
            self.cap.release()
            self.timer_camera.stop()

    def vedio_show(self):
        if self.is_camera_open:
            self.is_camera_open = False
            self.ui.CapBtn.setText('打开摄像头')

        video_path = self.get_video_path()
        if not video_path:
            return None
        self.cap = cv2.VideoCapture(video_path)
        self.video_start()

    def camera_show(self):
        self.is_camera_open = not self.is_camera_open
        if self.is_camera_open:
            self.ui.CapBtn.setText('关闭摄像头')
            self.cap = cv2.VideoCapture(0)
            self.video_start()
        else:
            self.ui.CapBtn.setText('打开摄像头')
            self.ui.label_show.setText('')
            if self.cap:
                self.cap.release()
                cv2.destroyAllWindows()
            self.ui.label_show.clear()

    def get_resize_size(self, img):
        _img = img.copy()
        img_height, img_width , depth= _img.shape
        ratio = img_width / img_height
        if ratio >= self.show_width / self.show_height:
            self.img_width = self.show_width
            self.img_height = int(self.img_width / ratio)
        else:
            self.img_height = self.show_height
            self.img_width = int(self.img_height * ratio)
        return self.img_width, self.img_height


    def on_cell_clicked(self,row,column):
        """
        鼠标点击表格触发，界面显示当前行内容
        """
        if self.cap:
            # 视频不支持表格选择
            return
        img_path = self.ui.tableWidget.item(row, 1).text()
        cls = self.ui.tableWidget.item(row, 2).text()
        conf = self.ui.tableWidget.item(row, 3).text()

        now_img = tools.img_cvread(img_path)
        # 显示行信息
        self.ui.resLb.setText(cls)
        self.ui.label_conf.setText(conf)
        self.ui.textEdit_2.setText(Config.method_infos[cls])

        # 获取缩放后的图片尺寸
        self.img_width, self.img_height = self.get_resize_size(now_img)
        resize_cvimg = cv2.resize(now_img, (self.img_width, self.img_height))
        pix_img = tools.cvimg_to_qpiximg(resize_cvimg)
        self.ui.label_show.setPixmap(pix_img)
        self.ui.label_show.setAlignment(Qt.AlignCenter)



if __name__ == "__main__":
    # 对于按钮文字显示不全的，完成高清屏幕自适应设置
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
