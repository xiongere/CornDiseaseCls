# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 830)
        MainWindow.setMinimumSize(QtCore.QSize(1250, 830))
        MainWindow.setMaximumSize(QtCore.QSize(1250, 830))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UIProgram/ui_imgs/icons/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 100, 791, 711))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 0, 771, 481))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_show = QtWidgets.QLabel(self.frame_2)
        self.label_show.setGeometry(QtCore.QRect(0, 0, 770, 480))
        self.label_show.setMinimumSize(QtCore.QSize(770, 480))
        self.label_show.setMaximumSize(QtCore.QSize(770, 480))
        self.label_show.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_show.setText("")
        self.label_show.setObjectName("label_show")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 480, 771, 221))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 10, 771, 211))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 751, 181))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(810, 100, 431, 711))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 431, 221))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(230, 170, 191, 37))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.time_lb = QtWidgets.QLabel(self.layoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.time_lb.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.time_lb.setFont(font)
        self.time_lb.setText("")
        self.time_lb.setObjectName("time_lb")
        self.horizontalLayout_7.addWidget(self.time_lb)
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 170, 201, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.label_conf = QtWidgets.QLabel(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_conf.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_conf.setFont(font)
        self.label_conf.setText("")
        self.label_conf.setObjectName("label_conf")
        self.horizontalLayout_8.addWidget(self.label_conf)
        self.resLb = QtWidgets.QLabel(self.groupBox_2)
        self.resLb.setGeometry(QtCore.QRect(10, 60, 411, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resLb.sizePolicy().hasHeightForWidth())
        self.resLb.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.resLb.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(48)
        self.resLb.setFont(font)
        self.resLb.setAlignment(QtCore.Qt.AlignCenter)
        self.resLb.setObjectName("resLb")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 470, 431, 231))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.PicBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.PicBtn.setGeometry(QtCore.QRect(20, 40, 181, 71))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.PicBtn.setFont(font)
        self.PicBtn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UIProgram/ui_imgs/icons/img.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.PicBtn.setIcon(icon1)
        self.PicBtn.setIconSize(QtCore.QSize(40, 40))
        self.PicBtn.setObjectName("PicBtn")
        self.VideoBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.VideoBtn.setGeometry(QtCore.QRect(20, 140, 181, 71))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.VideoBtn.setFont(font)
        self.VideoBtn.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("UIProgram/ui_imgs/icons/video.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.VideoBtn.setIcon(icon2)
        self.VideoBtn.setIconSize(QtCore.QSize(40, 40))
        self.VideoBtn.setObjectName("VideoBtn")
        self.CapBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.CapBtn.setGeometry(QtCore.QRect(230, 140, 181, 71))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.CapBtn.setFont(font)
        self.CapBtn.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("UIProgram/ui_imgs/icons/camera.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.CapBtn.setIcon(icon3)
        self.CapBtn.setIconSize(QtCore.QSize(40, 40))
        self.CapBtn.setObjectName("CapBtn")
        self.FilesBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.FilesBtn.setGeometry(QtCore.QRect(230, 40, 181, 71))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.FilesBtn.setFont(font)
        self.FilesBtn.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/ui_imgs/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FilesBtn.setIcon(icon4)
        self.FilesBtn.setIconSize(QtCore.QSize(40, 40))
        self.FilesBtn.setObjectName("FilesBtn")
        self.groupBox = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox.setGeometry(QtCore.QRect(0, 230, 431, 231))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 30, 411, 191))
        self.textEdit_2.setObjectName("textEdit_2")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 1231, 91))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1231, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.frame_5)
        self.line.setGeometry(QtCore.QRect(10, 70, 1211, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(10, 45, 341, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(1100, 50, 121, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于yolov8的玉米病害智能诊断与防治系统"))
        self.groupBox_3.setTitle(_translate("MainWindow", "识别结果信息"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "文件路径"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "结果"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "置信度"))
        self.groupBox_2.setTitle(_translate("MainWindow", "识别结果"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">用时：</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">置信度：</span></p></body></html>"))
        self.resLb.setText(_translate("MainWindow", "暂无结果"))
        self.groupBox_4.setTitle(_translate("MainWindow", "操作"))
        self.PicBtn.setText(_translate("MainWindow", "打开图片"))
        self.VideoBtn.setText(_translate("MainWindow", "打开视频"))
        self.CapBtn.setText(_translate("MainWindow", "打开摄像头"))
        self.FilesBtn.setText(_translate("MainWindow", "打开文件夹"))
        self.groupBox.setTitle(_translate("MainWindow", "防治方法与建议"))
        self.label_3.setText(_translate("MainWindow", "基于yolov8的玉米病害智能诊断与防治系统"))
import ui_sources_rc
