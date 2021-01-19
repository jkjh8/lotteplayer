# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(689, 866)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.lbl_Main_Lable = QLabel(self.centralwidget)
        self.lbl_Main_Lable.setObjectName(u"lbl_Main_Lable")
        font = QFont()
        font.setFamily(u"NanumBarunGothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50);
        self.lbl_Main_Lable.setFont(font)

        self.horizontalLayout.addWidget(self.lbl_Main_Lable)

        self.lbl_Iind_Player_1 = QLabel(self.centralwidget)
        self.lbl_Iind_Player_1.setObjectName(u"lbl_Iind_Player_1")
        self.lbl_Iind_Player_1.setMaximumSize(QSize(30, 16777215))
        self.lbl_Iind_Player_1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lbl_Iind_Player_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_Iind_Player_1)

        self.lbl_Iind_Player_2 = QLabel(self.centralwidget)
        self.lbl_Iind_Player_2.setObjectName(u"lbl_Iind_Player_2")
        self.lbl_Iind_Player_2.setMaximumSize(QSize(30, 16777215))
        self.lbl_Iind_Player_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lbl_Iind_Player_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_Iind_Player_2)

        self.lbl_Iind_Player_3 = QLabel(self.centralwidget)
        self.lbl_Iind_Player_3.setObjectName(u"lbl_Iind_Player_3")
        self.lbl_Iind_Player_3.setMaximumSize(QSize(30, 16777215))
        self.lbl_Iind_Player_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lbl_Iind_Player_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_Iind_Player_3)

        self.lbl_Iind_Player_4 = QLabel(self.centralwidget)
        self.lbl_Iind_Player_4.setObjectName(u"lbl_Iind_Player_4")
        self.lbl_Iind_Player_4.setMaximumSize(QSize(30, 16777215))
        self.lbl_Iind_Player_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lbl_Iind_Player_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_Iind_Player_4)

        self.lbl_Iind_Player_5 = QLabel(self.centralwidget)
        self.lbl_Iind_Player_5.setObjectName(u"lbl_Iind_Player_5")
        self.lbl_Iind_Player_5.setMaximumSize(QSize(30, 16777215))
        self.lbl_Iind_Player_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lbl_Iind_Player_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_Iind_Player_5)

        self.lbl_Iind_Player_6 = QLabel(self.centralwidget)
        self.lbl_Iind_Player_6.setObjectName(u"lbl_Iind_Player_6")
        self.lbl_Iind_Player_6.setMaximumSize(QSize(30, 16777215))
        self.lbl_Iind_Player_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lbl_Iind_Player_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_Iind_Player_6)

        self.lbl_Iind_Player_7 = QLabel(self.centralwidget)
        self.lbl_Iind_Player_7.setObjectName(u"lbl_Iind_Player_7")
        self.lbl_Iind_Player_7.setMaximumSize(QSize(30, 16777215))
        self.lbl_Iind_Player_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lbl_Iind_Player_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_Iind_Player_7)

        self.lbl_Iind_Player_8 = QLabel(self.centralwidget)
        self.lbl_Iind_Player_8.setObjectName(u"lbl_Iind_Player_8")
        self.lbl_Iind_Player_8.setMaximumSize(QSize(30, 16777215))
        self.lbl_Iind_Player_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lbl_Iind_Player_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_Iind_Player_8)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbl_Player_1_Status = QLabel(self.centralwidget)
        self.lbl_Player_1_Status.setObjectName(u"lbl_Player_1_Status")

        self.verticalLayout.addWidget(self.lbl_Player_1_Status)

        self.main_scrollArea = QScrollArea(self.centralwidget)
        self.main_scrollArea.setObjectName(u"main_scrollArea")
        self.main_scrollArea.setWidgetResizable(True)
        self.main_ScrollAreaWidgetContents = QWidget()
        self.main_ScrollAreaWidgetContents.setObjectName(u"main_ScrollAreaWidgetContents")
        self.main_ScrollAreaWidgetContents.setGeometry(QRect(0, 0, 652, 1331))
        self.verticalLayout_2 = QVBoxLayout(self.main_ScrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.vlo_Player_1 = QVBoxLayout()
        self.vlo_Player_1.setObjectName(u"vlo_Player_1")
        self.vlo_Player_1.setContentsMargins(6, 0, 6, 0)
        self.lbl_Player_Name_1 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Name_1.setObjectName(u"lbl_Player_Name_1")
        self.lbl_Player_Name_1.setFont(font)
        self.lbl_Player_Name_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.vlo_Player_1.addWidget(self.lbl_Player_Name_1)

        self.hbox_Player_File_1 = QHBoxLayout()
        self.hbox_Player_File_1.setObjectName(u"hbox_Player_File_1")
        self.lbl_Player_FileName_1 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_FileName_1.setObjectName(u"lbl_Player_FileName_1")
        self.lbl_Player_FileName_1.setMinimumSize(QSize(50, 20))
        font1 = QFont()
        font1.setFamily(u"NanumBarunGothic")
        font1.setPointSize(10)
        self.lbl_Player_FileName_1.setFont(font1)
        self.lbl_Player_FileName_1.setAlignment(Qt.AlignCenter)

        self.hbox_Player_File_1.addWidget(self.lbl_Player_FileName_1)

        self.let_Player_FileName_1 = QLineEdit(self.main_ScrollAreaWidgetContents)
        self.let_Player_FileName_1.setObjectName(u"let_Player_FileName_1")
        self.let_Player_FileName_1.setFrame(False)

        self.hbox_Player_File_1.addWidget(self.let_Player_FileName_1)

        self.btn_Player_FileOpen_1 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_FileOpen_1.setObjectName(u"btn_Player_FileOpen_1")
        self.btn_Player_FileOpen_1.setMinimumSize(QSize(50, 30))
        icon = QIcon()
        icon.addFile(u":/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Player_FileOpen_1.setIcon(icon)
        self.btn_Player_FileOpen_1.setIconSize(QSize(25, 25))
        self.btn_Player_FileOpen_1.setFlat(True)

        self.hbox_Player_File_1.addWidget(self.btn_Player_FileOpen_1)


        self.vlo_Player_1.addLayout(self.hbox_Player_File_1)

        self.hbox_Player_Devices_1 = QHBoxLayout()
        self.hbox_Player_Devices_1.setObjectName(u"hbox_Player_Devices_1")
        self.lbl_Player_1_Device = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_1_Device.setObjectName(u"lbl_Player_1_Device")
        self.lbl_Player_1_Device.setMaximumSize(QSize(50, 16777215))
        self.lbl_Player_1_Device.setFont(font1)
        self.lbl_Player_1_Device.setAlignment(Qt.AlignCenter)

        self.hbox_Player_Devices_1.addWidget(self.lbl_Player_1_Device)

        self.cbb_Player_Device_Sel_1 = QComboBox(self.main_ScrollAreaWidgetContents)
        self.cbb_Player_Device_Sel_1.setObjectName(u"cbb_Player_Device_Sel_1")
        self.cbb_Player_Device_Sel_1.setMinimumSize(QSize(350, 20))

        self.hbox_Player_Devices_1.addWidget(self.cbb_Player_Device_Sel_1)

        self.btn_Player_Play_1 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Play_1.setObjectName(u"btn_Player_Play_1")
        self.btn_Player_Play_1.setMinimumSize(QSize(0, 30))
        self.btn_Player_Play_1.setMaximumSize(QSize(80, 80))
        self.btn_Player_Play_1.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#ffffff}\n"
"QPushButton:hover{background-color:#22BCDD}\n"
"QPushButton:pressed{color:white;background-color:#485152}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/pause.png", QSize(), QIcon.Disabled, QIcon.On)
        self.btn_Player_Play_1.setIcon(icon1)
        self.btn_Player_Play_1.setIconSize(QSize(20, 20))
        self.btn_Player_Play_1.setCheckable(True)
        self.btn_Player_Play_1.setFlat(True)

        self.hbox_Player_Devices_1.addWidget(self.btn_Player_Play_1)

        self.btn_Player_Stop_1 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Stop_1.setObjectName(u"btn_Player_Stop_1")
        self.btn_Player_Stop_1.setMinimumSize(QSize(0, 30))
        self.btn_Player_Stop_1.setMaximumSize(QSize(80, 80))
        self.btn_Player_Stop_1.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#FFFFFF}QPushButton:hover{background-color:#CD6155}\n"
"QPushButton:pressed{color:white;background-color:#CC0033}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Player_Stop_1.setIcon(icon2)
        self.btn_Player_Stop_1.setIconSize(QSize(15, 15))
        self.btn_Player_Stop_1.setFlat(True)

        self.hbox_Player_Devices_1.addWidget(self.btn_Player_Stop_1)


        self.vlo_Player_1.addLayout(self.hbox_Player_Devices_1)

        self.hbox_Player_PlayTime_1 = QHBoxLayout()
        self.hbox_Player_PlayTime_1.setObjectName(u"hbox_Player_PlayTime_1")
        self.lbl_Player_RunTime_1 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_RunTime_1.setObjectName(u"lbl_Player_RunTime_1")
        self.lbl_Player_RunTime_1.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_1.addWidget(self.lbl_Player_RunTime_1)

        self.psb_Player_PlayTime_1 = QProgressBar(self.main_ScrollAreaWidgetContents)
        self.psb_Player_PlayTime_1.setObjectName(u"psb_Player_PlayTime_1")
        self.psb_Player_PlayTime_1.setMaximumSize(QSize(16777215, 10))
        self.psb_Player_PlayTime_1.setStyleSheet(u"QProgressBar {background-color:#D5D8DC; border:1px solid grey; border-radius:5px;}\n"
"QProgressBar::chunk {background-color: #05B8CC; width: 20px;}")
        self.psb_Player_PlayTime_1.setValue(24)
        self.psb_Player_PlayTime_1.setFormat(u"")

        self.hbox_Player_PlayTime_1.addWidget(self.psb_Player_PlayTime_1)

        self.lbl_Player_EndTime_1 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_EndTime_1.setObjectName(u"lbl_Player_EndTime_1")
        self.lbl_Player_EndTime_1.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_1.addWidget(self.lbl_Player_EndTime_1)


        self.vlo_Player_1.addLayout(self.hbox_Player_PlayTime_1)

        self.lbl_Player_Status_1 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Status_1.setObjectName(u"lbl_Player_Status_1")
        self.lbl_Player_Status_1.setMinimumSize(QSize(0, 20))

        self.vlo_Player_1.addWidget(self.lbl_Player_Status_1)


        self.verticalLayout_2.addLayout(self.vlo_Player_1)

        self.line_1 = QFrame(self.main_ScrollAreaWidgetContents)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_1)

        self.vlo_Player_2 = QVBoxLayout()
        self.vlo_Player_2.setObjectName(u"vlo_Player_2")
        self.vlo_Player_2.setContentsMargins(6, 0, 6, 0)
        self.lbl_Player_Name_2 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Name_2.setObjectName(u"lbl_Player_Name_2")
        self.lbl_Player_Name_2.setFont(font)
        self.lbl_Player_Name_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.vlo_Player_2.addWidget(self.lbl_Player_Name_2)

        self.hbox_Player_File_2 = QHBoxLayout()
        self.hbox_Player_File_2.setObjectName(u"hbox_Player_File_2")
        self.lbl_Player_FileName_2 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_FileName_2.setObjectName(u"lbl_Player_FileName_2")
        self.lbl_Player_FileName_2.setMinimumSize(QSize(50, 20))
        self.lbl_Player_FileName_2.setFont(font1)
        self.lbl_Player_FileName_2.setAlignment(Qt.AlignCenter)

        self.hbox_Player_File_2.addWidget(self.lbl_Player_FileName_2)

        self.let_Player_FileName_2 = QLineEdit(self.main_ScrollAreaWidgetContents)
        self.let_Player_FileName_2.setObjectName(u"let_Player_FileName_2")
        self.let_Player_FileName_2.setFrame(False)

        self.hbox_Player_File_2.addWidget(self.let_Player_FileName_2)

        self.btn_Player_FileOpen_2 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_FileOpen_2.setObjectName(u"btn_Player_FileOpen_2")
        self.btn_Player_FileOpen_2.setMinimumSize(QSize(50, 30))
        self.btn_Player_FileOpen_2.setIcon(icon)
        self.btn_Player_FileOpen_2.setIconSize(QSize(25, 25))
        self.btn_Player_FileOpen_2.setFlat(True)

        self.hbox_Player_File_2.addWidget(self.btn_Player_FileOpen_2)


        self.vlo_Player_2.addLayout(self.hbox_Player_File_2)

        self.hbox_Player_Devices_2 = QHBoxLayout()
        self.hbox_Player_Devices_2.setObjectName(u"hbox_Player_Devices_2")
        self.lbl_Player_Device_2 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Device_2.setObjectName(u"lbl_Player_Device_2")
        self.lbl_Player_Device_2.setMaximumSize(QSize(50, 16777215))
        self.lbl_Player_Device_2.setFont(font1)
        self.lbl_Player_Device_2.setAlignment(Qt.AlignCenter)

        self.hbox_Player_Devices_2.addWidget(self.lbl_Player_Device_2)

        self.cbb_Player_Device_Sel_2 = QComboBox(self.main_ScrollAreaWidgetContents)
        self.cbb_Player_Device_Sel_2.setObjectName(u"cbb_Player_Device_Sel_2")
        self.cbb_Player_Device_Sel_2.setMinimumSize(QSize(350, 20))

        self.hbox_Player_Devices_2.addWidget(self.cbb_Player_Device_Sel_2)

        self.btn_Player_Play_2 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Play_2.setObjectName(u"btn_Player_Play_2")
        self.btn_Player_Play_2.setMinimumSize(QSize(0, 30))
        self.btn_Player_Play_2.setMaximumSize(QSize(80, 80))
        self.btn_Player_Play_2.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#ffffff}\n"
"QPushButton:hover{background-color:#22BCDD}\n"
"QPushButton:pressed{color:white;background-color:#485152}")
        self.btn_Player_Play_2.setIcon(icon1)
        self.btn_Player_Play_2.setIconSize(QSize(20, 19))
        self.btn_Player_Play_2.setCheckable(True)
        self.btn_Player_Play_2.setFlat(True)

        self.hbox_Player_Devices_2.addWidget(self.btn_Player_Play_2)

        self.btn_Player_Stop_2 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Stop_2.setObjectName(u"btn_Player_Stop_2")
        self.btn_Player_Stop_2.setMinimumSize(QSize(0, 30))
        self.btn_Player_Stop_2.setMaximumSize(QSize(80, 80))
        self.btn_Player_Stop_2.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#FFFFFF}QPushButton:hover{background-color:#CD6155}\n"
"QPushButton:pressed{color:white;background-color:#CC0033}")
        self.btn_Player_Stop_2.setIcon(icon2)
        self.btn_Player_Stop_2.setIconSize(QSize(15, 15))
        self.btn_Player_Stop_2.setFlat(True)

        self.hbox_Player_Devices_2.addWidget(self.btn_Player_Stop_2)


        self.vlo_Player_2.addLayout(self.hbox_Player_Devices_2)

        self.hbox_Player_PlayTime_2 = QHBoxLayout()
        self.hbox_Player_PlayTime_2.setObjectName(u"hbox_Player_PlayTime_2")
        self.lbl_Player_RunTime_2 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_RunTime_2.setObjectName(u"lbl_Player_RunTime_2")
        self.lbl_Player_RunTime_2.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_2.addWidget(self.lbl_Player_RunTime_2)

        self.psb_Player_1_PlayTime_2 = QProgressBar(self.main_ScrollAreaWidgetContents)
        self.psb_Player_1_PlayTime_2.setObjectName(u"psb_Player_1_PlayTime_2")
        self.psb_Player_1_PlayTime_2.setMaximumSize(QSize(16777215, 10))
        self.psb_Player_1_PlayTime_2.setStyleSheet(u"QProgressBar {background-color:#D5D8DC; border:1px solid grey; border-radius:5px;}\n"
"QProgressBar::chunk {background-color: #05B8CC; width: 20px;}")
        self.psb_Player_1_PlayTime_2.setValue(24)
        self.psb_Player_1_PlayTime_2.setFormat(u"")

        self.hbox_Player_PlayTime_2.addWidget(self.psb_Player_1_PlayTime_2)

        self.lbl_Player_EndTime_2 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_EndTime_2.setObjectName(u"lbl_Player_EndTime_2")
        self.lbl_Player_EndTime_2.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_2.addWidget(self.lbl_Player_EndTime_2)


        self.vlo_Player_2.addLayout(self.hbox_Player_PlayTime_2)

        self.lbl_Player_Status_2 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Status_2.setObjectName(u"lbl_Player_Status_2")
        self.lbl_Player_Status_2.setMinimumSize(QSize(0, 20))

        self.vlo_Player_2.addWidget(self.lbl_Player_Status_2)


        self.verticalLayout_2.addLayout(self.vlo_Player_2)

        self.line_2 = QFrame(self.main_ScrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.vlo_Player_3 = QVBoxLayout()
        self.vlo_Player_3.setObjectName(u"vlo_Player_3")
        self.vlo_Player_3.setContentsMargins(6, 0, 6, 0)
        self.lbl_Player_Name_3 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Name_3.setObjectName(u"lbl_Player_Name_3")
        self.lbl_Player_Name_3.setFont(font)
        self.lbl_Player_Name_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.vlo_Player_3.addWidget(self.lbl_Player_Name_3)

        self.hbox_Player_File_7 = QHBoxLayout()
        self.hbox_Player_File_7.setObjectName(u"hbox_Player_File_7")
        self.lbl_Player_FileName_7 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_FileName_7.setObjectName(u"lbl_Player_FileName_7")
        self.lbl_Player_FileName_7.setMinimumSize(QSize(50, 20))
        self.lbl_Player_FileName_7.setFont(font1)
        self.lbl_Player_FileName_7.setAlignment(Qt.AlignCenter)

        self.hbox_Player_File_7.addWidget(self.lbl_Player_FileName_7)

        self.let_Player_FileName_7 = QLineEdit(self.main_ScrollAreaWidgetContents)
        self.let_Player_FileName_7.setObjectName(u"let_Player_FileName_7")
        self.let_Player_FileName_7.setFrame(False)

        self.hbox_Player_File_7.addWidget(self.let_Player_FileName_7)

        self.btn_Player_FileOpen_7 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_FileOpen_7.setObjectName(u"btn_Player_FileOpen_7")
        self.btn_Player_FileOpen_7.setMinimumSize(QSize(50, 30))
        self.btn_Player_FileOpen_7.setIcon(icon)
        self.btn_Player_FileOpen_7.setIconSize(QSize(25, 25))
        self.btn_Player_FileOpen_7.setFlat(True)

        self.hbox_Player_File_7.addWidget(self.btn_Player_FileOpen_7)


        self.vlo_Player_3.addLayout(self.hbox_Player_File_7)

        self.hbox_Player_Devices_7 = QHBoxLayout()
        self.hbox_Player_Devices_7.setObjectName(u"hbox_Player_Devices_7")
        self.lbl_Player_Device_5 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Device_5.setObjectName(u"lbl_Player_Device_5")
        self.lbl_Player_Device_5.setMaximumSize(QSize(50, 16777215))
        self.lbl_Player_Device_5.setFont(font1)
        self.lbl_Player_Device_5.setAlignment(Qt.AlignCenter)

        self.hbox_Player_Devices_7.addWidget(self.lbl_Player_Device_5)

        self.cbb_Player_Device_Sel_7 = QComboBox(self.main_ScrollAreaWidgetContents)
        self.cbb_Player_Device_Sel_7.setObjectName(u"cbb_Player_Device_Sel_7")
        self.cbb_Player_Device_Sel_7.setMinimumSize(QSize(350, 20))

        self.hbox_Player_Devices_7.addWidget(self.cbb_Player_Device_Sel_7)

        self.btn_Player_Play_7 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Play_7.setObjectName(u"btn_Player_Play_7")
        self.btn_Player_Play_7.setMinimumSize(QSize(0, 30))
        self.btn_Player_Play_7.setMaximumSize(QSize(80, 80))
        self.btn_Player_Play_7.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#ffffff}\n"
"QPushButton:hover{background-color:#22BCDD}\n"
"QPushButton:pressed{color:white;background-color:#485152}")
        self.btn_Player_Play_7.setIcon(icon1)
        self.btn_Player_Play_7.setIconSize(QSize(20, 20))
        self.btn_Player_Play_7.setCheckable(True)
        self.btn_Player_Play_7.setFlat(True)

        self.hbox_Player_Devices_7.addWidget(self.btn_Player_Play_7)

        self.btn_Player_Stop_7 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Stop_7.setObjectName(u"btn_Player_Stop_7")
        self.btn_Player_Stop_7.setMinimumSize(QSize(0, 30))
        self.btn_Player_Stop_7.setMaximumSize(QSize(80, 80))
        self.btn_Player_Stop_7.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#FFFFFF}QPushButton:hover{background-color:#CD6155}\n"
"QPushButton:pressed{color:white;background-color:#CC0033}")
        self.btn_Player_Stop_7.setIcon(icon2)
        self.btn_Player_Stop_7.setIconSize(QSize(15, 15))
        self.btn_Player_Stop_7.setFlat(True)

        self.hbox_Player_Devices_7.addWidget(self.btn_Player_Stop_7)


        self.vlo_Player_3.addLayout(self.hbox_Player_Devices_7)

        self.hbox_Player_PlayTime_7 = QHBoxLayout()
        self.hbox_Player_PlayTime_7.setObjectName(u"hbox_Player_PlayTime_7")
        self.lbl_Player_RunTime_7 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_RunTime_7.setObjectName(u"lbl_Player_RunTime_7")
        self.lbl_Player_RunTime_7.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_7.addWidget(self.lbl_Player_RunTime_7)

        self.psb_Player_1_PlayTime_5 = QProgressBar(self.main_ScrollAreaWidgetContents)
        self.psb_Player_1_PlayTime_5.setObjectName(u"psb_Player_1_PlayTime_5")
        self.psb_Player_1_PlayTime_5.setMaximumSize(QSize(16777215, 10))
        self.psb_Player_1_PlayTime_5.setStyleSheet(u"QProgressBar {background-color:#D5D8DC; border:1px solid grey; border-radius:5px;}\n"
"QProgressBar::chunk {background-color: #05B8CC; width: 20px;}")
        self.psb_Player_1_PlayTime_5.setValue(24)
        self.psb_Player_1_PlayTime_5.setFormat(u"")

        self.hbox_Player_PlayTime_7.addWidget(self.psb_Player_1_PlayTime_5)

        self.lbl_Player_EndTime_7 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_EndTime_7.setObjectName(u"lbl_Player_EndTime_7")
        self.lbl_Player_EndTime_7.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_7.addWidget(self.lbl_Player_EndTime_7)


        self.vlo_Player_3.addLayout(self.hbox_Player_PlayTime_7)

        self.lbl_Player_Status_7 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Status_7.setObjectName(u"lbl_Player_Status_7")
        self.lbl_Player_Status_7.setMinimumSize(QSize(0, 20))

        self.vlo_Player_3.addWidget(self.lbl_Player_Status_7)


        self.verticalLayout_2.addLayout(self.vlo_Player_3)

        self.line_3 = QFrame(self.main_ScrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.vlo_Player_8 = QVBoxLayout()
        self.vlo_Player_8.setObjectName(u"vlo_Player_8")
        self.vlo_Player_8.setContentsMargins(6, 0, 6, 0)
        self.lbl_Player_Name_8 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Name_8.setObjectName(u"lbl_Player_Name_8")
        self.lbl_Player_Name_8.setFont(font)
        self.lbl_Player_Name_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.vlo_Player_8.addWidget(self.lbl_Player_Name_8)

        self.hbox_Player_File_8 = QHBoxLayout()
        self.hbox_Player_File_8.setObjectName(u"hbox_Player_File_8")
        self.lbl_Player_FileName_8 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_FileName_8.setObjectName(u"lbl_Player_FileName_8")
        self.lbl_Player_FileName_8.setMinimumSize(QSize(50, 20))
        self.lbl_Player_FileName_8.setFont(font1)
        self.lbl_Player_FileName_8.setAlignment(Qt.AlignCenter)

        self.hbox_Player_File_8.addWidget(self.lbl_Player_FileName_8)

        self.let_Player_FileName_8 = QLineEdit(self.main_ScrollAreaWidgetContents)
        self.let_Player_FileName_8.setObjectName(u"let_Player_FileName_8")
        self.let_Player_FileName_8.setFrame(False)

        self.hbox_Player_File_8.addWidget(self.let_Player_FileName_8)

        self.btn_Player_FileOpen_8 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_FileOpen_8.setObjectName(u"btn_Player_FileOpen_8")
        self.btn_Player_FileOpen_8.setMinimumSize(QSize(50, 30))
        self.btn_Player_FileOpen_8.setIcon(icon)
        self.btn_Player_FileOpen_8.setIconSize(QSize(25, 25))
        self.btn_Player_FileOpen_8.setFlat(True)

        self.hbox_Player_File_8.addWidget(self.btn_Player_FileOpen_8)


        self.vlo_Player_8.addLayout(self.hbox_Player_File_8)

        self.hbox_Player_Devices_8 = QHBoxLayout()
        self.hbox_Player_Devices_8.setObjectName(u"hbox_Player_Devices_8")
        self.lbl_Player_Device_6 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Device_6.setObjectName(u"lbl_Player_Device_6")
        self.lbl_Player_Device_6.setMaximumSize(QSize(50, 16777215))
        self.lbl_Player_Device_6.setFont(font1)
        self.lbl_Player_Device_6.setAlignment(Qt.AlignCenter)

        self.hbox_Player_Devices_8.addWidget(self.lbl_Player_Device_6)

        self.cbb_Player_Device_Sel_8 = QComboBox(self.main_ScrollAreaWidgetContents)
        self.cbb_Player_Device_Sel_8.setObjectName(u"cbb_Player_Device_Sel_8")
        self.cbb_Player_Device_Sel_8.setMinimumSize(QSize(350, 20))

        self.hbox_Player_Devices_8.addWidget(self.cbb_Player_Device_Sel_8)

        self.btn_Player_Play_8 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Play_8.setObjectName(u"btn_Player_Play_8")
        self.btn_Player_Play_8.setMinimumSize(QSize(0, 30))
        self.btn_Player_Play_8.setMaximumSize(QSize(80, 80))
        self.btn_Player_Play_8.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#ffffff}\n"
"QPushButton:hover{background-color:#22BCDD}\n"
"QPushButton:pressed{color:white;background-color:#485152}")
        self.btn_Player_Play_8.setIcon(icon1)
        self.btn_Player_Play_8.setIconSize(QSize(20, 20))
        self.btn_Player_Play_8.setCheckable(True)
        self.btn_Player_Play_8.setFlat(True)

        self.hbox_Player_Devices_8.addWidget(self.btn_Player_Play_8)

        self.btn_Player_Stop_8 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Stop_8.setObjectName(u"btn_Player_Stop_8")
        self.btn_Player_Stop_8.setMinimumSize(QSize(0, 30))
        self.btn_Player_Stop_8.setMaximumSize(QSize(80, 80))
        self.btn_Player_Stop_8.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#FFFFFF}QPushButton:hover{background-color:#CD6155}\n"
"QPushButton:pressed{color:white;background-color:#CC0033}")
        self.btn_Player_Stop_8.setIcon(icon2)
        self.btn_Player_Stop_8.setIconSize(QSize(15, 15))
        self.btn_Player_Stop_8.setFlat(True)

        self.hbox_Player_Devices_8.addWidget(self.btn_Player_Stop_8)


        self.vlo_Player_8.addLayout(self.hbox_Player_Devices_8)

        self.hbox_Player_PlayTime_8 = QHBoxLayout()
        self.hbox_Player_PlayTime_8.setObjectName(u"hbox_Player_PlayTime_8")
        self.lbl_Player_RunTime_8 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_RunTime_8.setObjectName(u"lbl_Player_RunTime_8")
        self.lbl_Player_RunTime_8.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_8.addWidget(self.lbl_Player_RunTime_8)

        self.psb_Player_1_PlayTime_6 = QProgressBar(self.main_ScrollAreaWidgetContents)
        self.psb_Player_1_PlayTime_6.setObjectName(u"psb_Player_1_PlayTime_6")
        self.psb_Player_1_PlayTime_6.setMaximumSize(QSize(16777215, 10))
        self.psb_Player_1_PlayTime_6.setStyleSheet(u"QProgressBar {background-color:#D5D8DC; border:1px solid grey; border-radius:5px;}\n"
"QProgressBar::chunk {background-color: #05B8CC; width: 20px;}")
        self.psb_Player_1_PlayTime_6.setValue(24)
        self.psb_Player_1_PlayTime_6.setFormat(u"")

        self.hbox_Player_PlayTime_8.addWidget(self.psb_Player_1_PlayTime_6)

        self.lbl_Player_EndTime_8 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_EndTime_8.setObjectName(u"lbl_Player_EndTime_8")
        self.lbl_Player_EndTime_8.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_8.addWidget(self.lbl_Player_EndTime_8)


        self.vlo_Player_8.addLayout(self.hbox_Player_PlayTime_8)

        self.lbl_Player_Status_8 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Status_8.setObjectName(u"lbl_Player_Status_8")
        self.lbl_Player_Status_8.setMinimumSize(QSize(0, 20))

        self.vlo_Player_8.addWidget(self.lbl_Player_Status_8)


        self.verticalLayout_2.addLayout(self.vlo_Player_8)

        self.line_7 = QFrame(self.main_ScrollAreaWidgetContents)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_7)

        self.vlo_Player_9 = QVBoxLayout()
        self.vlo_Player_9.setObjectName(u"vlo_Player_9")
        self.vlo_Player_9.setContentsMargins(6, 0, 6, 0)
        self.lbl_Player_Name_9 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Name_9.setObjectName(u"lbl_Player_Name_9")
        self.lbl_Player_Name_9.setFont(font)
        self.lbl_Player_Name_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.vlo_Player_9.addWidget(self.lbl_Player_Name_9)

        self.hbox_Player_File_9 = QHBoxLayout()
        self.hbox_Player_File_9.setObjectName(u"hbox_Player_File_9")
        self.lbl_Player_FileName_9 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_FileName_9.setObjectName(u"lbl_Player_FileName_9")
        self.lbl_Player_FileName_9.setMinimumSize(QSize(50, 20))
        self.lbl_Player_FileName_9.setFont(font1)
        self.lbl_Player_FileName_9.setAlignment(Qt.AlignCenter)

        self.hbox_Player_File_9.addWidget(self.lbl_Player_FileName_9)

        self.let_Player_FileName_9 = QLineEdit(self.main_ScrollAreaWidgetContents)
        self.let_Player_FileName_9.setObjectName(u"let_Player_FileName_9")
        self.let_Player_FileName_9.setFrame(False)

        self.hbox_Player_File_9.addWidget(self.let_Player_FileName_9)

        self.btn_Player_FileOpen_9 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_FileOpen_9.setObjectName(u"btn_Player_FileOpen_9")
        self.btn_Player_FileOpen_9.setMinimumSize(QSize(50, 30))
        self.btn_Player_FileOpen_9.setIcon(icon)
        self.btn_Player_FileOpen_9.setIconSize(QSize(25, 25))
        self.btn_Player_FileOpen_9.setFlat(True)

        self.hbox_Player_File_9.addWidget(self.btn_Player_FileOpen_9)


        self.vlo_Player_9.addLayout(self.hbox_Player_File_9)

        self.hbox_Player_Devices_9 = QHBoxLayout()
        self.hbox_Player_Devices_9.setObjectName(u"hbox_Player_Devices_9")
        self.lbl_Player_Device_7 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Device_7.setObjectName(u"lbl_Player_Device_7")
        self.lbl_Player_Device_7.setMaximumSize(QSize(50, 16777215))
        self.lbl_Player_Device_7.setFont(font1)
        self.lbl_Player_Device_7.setAlignment(Qt.AlignCenter)

        self.hbox_Player_Devices_9.addWidget(self.lbl_Player_Device_7)

        self.cbb_Player_Device_Sel_9 = QComboBox(self.main_ScrollAreaWidgetContents)
        self.cbb_Player_Device_Sel_9.setObjectName(u"cbb_Player_Device_Sel_9")
        self.cbb_Player_Device_Sel_9.setMinimumSize(QSize(350, 20))

        self.hbox_Player_Devices_9.addWidget(self.cbb_Player_Device_Sel_9)

        self.btn_Player_Play_9 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Play_9.setObjectName(u"btn_Player_Play_9")
        self.btn_Player_Play_9.setMinimumSize(QSize(0, 30))
        self.btn_Player_Play_9.setMaximumSize(QSize(80, 80))
        self.btn_Player_Play_9.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#ffffff}\n"
"QPushButton:hover{background-color:#22BCDD}\n"
"QPushButton:pressed{color:white;background-color:#485152}")
        self.btn_Player_Play_9.setIcon(icon1)
        self.btn_Player_Play_9.setIconSize(QSize(20, 20))
        self.btn_Player_Play_9.setCheckable(True)
        self.btn_Player_Play_9.setFlat(True)

        self.hbox_Player_Devices_9.addWidget(self.btn_Player_Play_9)

        self.btn_Player_Stop_9 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Stop_9.setObjectName(u"btn_Player_Stop_9")
        self.btn_Player_Stop_9.setMinimumSize(QSize(0, 30))
        self.btn_Player_Stop_9.setMaximumSize(QSize(80, 80))
        self.btn_Player_Stop_9.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#FFFFFF}QPushButton:hover{background-color:#CD6155}\n"
"QPushButton:pressed{color:white;background-color:#CC0033}")
        self.btn_Player_Stop_9.setIcon(icon2)
        self.btn_Player_Stop_9.setIconSize(QSize(15, 15))
        self.btn_Player_Stop_9.setFlat(True)

        self.hbox_Player_Devices_9.addWidget(self.btn_Player_Stop_9)


        self.vlo_Player_9.addLayout(self.hbox_Player_Devices_9)

        self.hbox_Player_PlayTime_9 = QHBoxLayout()
        self.hbox_Player_PlayTime_9.setObjectName(u"hbox_Player_PlayTime_9")
        self.lbl_Player_RunTime_9 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_RunTime_9.setObjectName(u"lbl_Player_RunTime_9")
        self.lbl_Player_RunTime_9.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_9.addWidget(self.lbl_Player_RunTime_9)

        self.psb_Player_1_PlayTime_7 = QProgressBar(self.main_ScrollAreaWidgetContents)
        self.psb_Player_1_PlayTime_7.setObjectName(u"psb_Player_1_PlayTime_7")
        self.psb_Player_1_PlayTime_7.setMaximumSize(QSize(16777215, 10))
        self.psb_Player_1_PlayTime_7.setStyleSheet(u"QProgressBar {background-color:#D5D8DC; border:1px solid grey; border-radius:5px;}\n"
"QProgressBar::chunk {background-color: #05B8CC; width: 20px;}")
        self.psb_Player_1_PlayTime_7.setValue(24)
        self.psb_Player_1_PlayTime_7.setFormat(u"")

        self.hbox_Player_PlayTime_9.addWidget(self.psb_Player_1_PlayTime_7)

        self.lbl_Player_EndTime_9 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_EndTime_9.setObjectName(u"lbl_Player_EndTime_9")
        self.lbl_Player_EndTime_9.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_9.addWidget(self.lbl_Player_EndTime_9)


        self.vlo_Player_9.addLayout(self.hbox_Player_PlayTime_9)

        self.lbl_Player_Status_9 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Status_9.setObjectName(u"lbl_Player_Status_9")
        self.lbl_Player_Status_9.setMinimumSize(QSize(0, 20))

        self.vlo_Player_9.addWidget(self.lbl_Player_Status_9)


        self.verticalLayout_2.addLayout(self.vlo_Player_9)

        self.line_6 = QFrame(self.main_ScrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_6)

        self.vlo_Player_10 = QVBoxLayout()
        self.vlo_Player_10.setObjectName(u"vlo_Player_10")
        self.vlo_Player_10.setContentsMargins(6, 0, 6, 0)
        self.lbl_Player_Name_10 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Name_10.setObjectName(u"lbl_Player_Name_10")
        self.lbl_Player_Name_10.setFont(font)
        self.lbl_Player_Name_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.vlo_Player_10.addWidget(self.lbl_Player_Name_10)

        self.hbox_Player_File_10 = QHBoxLayout()
        self.hbox_Player_File_10.setObjectName(u"hbox_Player_File_10")
        self.lbl_Player_FileName_10 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_FileName_10.setObjectName(u"lbl_Player_FileName_10")
        self.lbl_Player_FileName_10.setMinimumSize(QSize(50, 20))
        self.lbl_Player_FileName_10.setFont(font1)
        self.lbl_Player_FileName_10.setAlignment(Qt.AlignCenter)

        self.hbox_Player_File_10.addWidget(self.lbl_Player_FileName_10)

        self.let_Player_FileName_10 = QLineEdit(self.main_ScrollAreaWidgetContents)
        self.let_Player_FileName_10.setObjectName(u"let_Player_FileName_10")
        self.let_Player_FileName_10.setFrame(False)

        self.hbox_Player_File_10.addWidget(self.let_Player_FileName_10)

        self.btn_Player_FileOpen_10 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_FileOpen_10.setObjectName(u"btn_Player_FileOpen_10")
        self.btn_Player_FileOpen_10.setMinimumSize(QSize(50, 30))
        self.btn_Player_FileOpen_10.setIcon(icon)
        self.btn_Player_FileOpen_10.setIconSize(QSize(25, 25))
        self.btn_Player_FileOpen_10.setFlat(True)

        self.hbox_Player_File_10.addWidget(self.btn_Player_FileOpen_10)


        self.vlo_Player_10.addLayout(self.hbox_Player_File_10)

        self.hbox_Player_Devices_10 = QHBoxLayout()
        self.hbox_Player_Devices_10.setObjectName(u"hbox_Player_Devices_10")
        self.lbl_Player_Device_8 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Device_8.setObjectName(u"lbl_Player_Device_8")
        self.lbl_Player_Device_8.setMaximumSize(QSize(50, 16777215))
        self.lbl_Player_Device_8.setFont(font1)
        self.lbl_Player_Device_8.setAlignment(Qt.AlignCenter)

        self.hbox_Player_Devices_10.addWidget(self.lbl_Player_Device_8)

        self.cbb_Player_Device_Sel_10 = QComboBox(self.main_ScrollAreaWidgetContents)
        self.cbb_Player_Device_Sel_10.setObjectName(u"cbb_Player_Device_Sel_10")
        self.cbb_Player_Device_Sel_10.setMinimumSize(QSize(350, 20))

        self.hbox_Player_Devices_10.addWidget(self.cbb_Player_Device_Sel_10)

        self.btn_Player_Play_10 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Play_10.setObjectName(u"btn_Player_Play_10")
        self.btn_Player_Play_10.setMinimumSize(QSize(0, 30))
        self.btn_Player_Play_10.setMaximumSize(QSize(80, 80))
        self.btn_Player_Play_10.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#ffffff}\n"
"QPushButton:hover{background-color:#22BCDD}\n"
"QPushButton:pressed{color:white;background-color:#485152}")
        self.btn_Player_Play_10.setIcon(icon1)
        self.btn_Player_Play_10.setIconSize(QSize(20, 20))
        self.btn_Player_Play_10.setCheckable(True)
        self.btn_Player_Play_10.setFlat(True)

        self.hbox_Player_Devices_10.addWidget(self.btn_Player_Play_10)

        self.btn_Player_Stop_10 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Stop_10.setObjectName(u"btn_Player_Stop_10")
        self.btn_Player_Stop_10.setMinimumSize(QSize(0, 30))
        self.btn_Player_Stop_10.setMaximumSize(QSize(80, 80))
        self.btn_Player_Stop_10.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#FFFFFF}QPushButton:hover{background-color:#CD6155}\n"
"QPushButton:pressed{color:white;background-color:#CC0033}")
        self.btn_Player_Stop_10.setIcon(icon2)
        self.btn_Player_Stop_10.setIconSize(QSize(15, 15))
        self.btn_Player_Stop_10.setFlat(True)

        self.hbox_Player_Devices_10.addWidget(self.btn_Player_Stop_10)


        self.vlo_Player_10.addLayout(self.hbox_Player_Devices_10)

        self.hbox_Player_PlayTime_10 = QHBoxLayout()
        self.hbox_Player_PlayTime_10.setObjectName(u"hbox_Player_PlayTime_10")
        self.lbl_Player_RunTime_10 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_RunTime_10.setObjectName(u"lbl_Player_RunTime_10")
        self.lbl_Player_RunTime_10.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_10.addWidget(self.lbl_Player_RunTime_10)

        self.psb_Player_1_PlayTime_8 = QProgressBar(self.main_ScrollAreaWidgetContents)
        self.psb_Player_1_PlayTime_8.setObjectName(u"psb_Player_1_PlayTime_8")
        self.psb_Player_1_PlayTime_8.setMaximumSize(QSize(16777215, 10))
        self.psb_Player_1_PlayTime_8.setStyleSheet(u"QProgressBar {background-color:#D5D8DC; border:1px solid grey; border-radius:5px;}\n"
"QProgressBar::chunk {background-color: #05B8CC; width: 20px;}")
        self.psb_Player_1_PlayTime_8.setValue(24)
        self.psb_Player_1_PlayTime_8.setFormat(u"")

        self.hbox_Player_PlayTime_10.addWidget(self.psb_Player_1_PlayTime_8)

        self.lbl_Player_EndTime_10 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_EndTime_10.setObjectName(u"lbl_Player_EndTime_10")
        self.lbl_Player_EndTime_10.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_10.addWidget(self.lbl_Player_EndTime_10)


        self.vlo_Player_10.addLayout(self.hbox_Player_PlayTime_10)

        self.lbl_Player_Status_10 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Status_10.setObjectName(u"lbl_Player_Status_10")
        self.lbl_Player_Status_10.setMinimumSize(QSize(0, 20))

        self.vlo_Player_10.addWidget(self.lbl_Player_Status_10)


        self.verticalLayout_2.addLayout(self.vlo_Player_10)

        self.line_5 = QFrame(self.main_ScrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.vlo_Player_11 = QVBoxLayout()
        self.vlo_Player_11.setObjectName(u"vlo_Player_11")
        self.vlo_Player_11.setContentsMargins(6, 0, 6, 0)
        self.lbl_Player_Name_11 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Name_11.setObjectName(u"lbl_Player_Name_11")
        self.lbl_Player_Name_11.setFont(font)
        self.lbl_Player_Name_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.vlo_Player_11.addWidget(self.lbl_Player_Name_11)

        self.hbox_Player_File_11 = QHBoxLayout()
        self.hbox_Player_File_11.setObjectName(u"hbox_Player_File_11")
        self.lbl_Player_FileName_11 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_FileName_11.setObjectName(u"lbl_Player_FileName_11")
        self.lbl_Player_FileName_11.setMinimumSize(QSize(50, 20))
        self.lbl_Player_FileName_11.setFont(font1)
        self.lbl_Player_FileName_11.setAlignment(Qt.AlignCenter)

        self.hbox_Player_File_11.addWidget(self.lbl_Player_FileName_11)

        self.let_Player_FileName_11 = QLineEdit(self.main_ScrollAreaWidgetContents)
        self.let_Player_FileName_11.setObjectName(u"let_Player_FileName_11")
        self.let_Player_FileName_11.setFrame(False)

        self.hbox_Player_File_11.addWidget(self.let_Player_FileName_11)

        self.btn_Player_FileOpen_11 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_FileOpen_11.setObjectName(u"btn_Player_FileOpen_11")
        self.btn_Player_FileOpen_11.setMinimumSize(QSize(50, 30))
        self.btn_Player_FileOpen_11.setIcon(icon)
        self.btn_Player_FileOpen_11.setIconSize(QSize(25, 25))
        self.btn_Player_FileOpen_11.setFlat(True)

        self.hbox_Player_File_11.addWidget(self.btn_Player_FileOpen_11)


        self.vlo_Player_11.addLayout(self.hbox_Player_File_11)

        self.hbox_Player_Devices_11 = QHBoxLayout()
        self.hbox_Player_Devices_11.setObjectName(u"hbox_Player_Devices_11")
        self.lbl_Player_Device_9 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Device_9.setObjectName(u"lbl_Player_Device_9")
        self.lbl_Player_Device_9.setMaximumSize(QSize(50, 16777215))
        self.lbl_Player_Device_9.setFont(font1)
        self.lbl_Player_Device_9.setAlignment(Qt.AlignCenter)

        self.hbox_Player_Devices_11.addWidget(self.lbl_Player_Device_9)

        self.cbb_Player_Device_Sel_11 = QComboBox(self.main_ScrollAreaWidgetContents)
        self.cbb_Player_Device_Sel_11.setObjectName(u"cbb_Player_Device_Sel_11")
        self.cbb_Player_Device_Sel_11.setMinimumSize(QSize(350, 20))

        self.hbox_Player_Devices_11.addWidget(self.cbb_Player_Device_Sel_11)

        self.btn_Player_Play_11 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Play_11.setObjectName(u"btn_Player_Play_11")
        self.btn_Player_Play_11.setMinimumSize(QSize(0, 30))
        self.btn_Player_Play_11.setMaximumSize(QSize(80, 80))
        self.btn_Player_Play_11.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#ffffff}\n"
"QPushButton:hover{background-color:#22BCDD}\n"
"QPushButton:pressed{color:white;background-color:#485152}")
        self.btn_Player_Play_11.setIcon(icon1)
        self.btn_Player_Play_11.setIconSize(QSize(20, 20))
        self.btn_Player_Play_11.setCheckable(True)
        self.btn_Player_Play_11.setFlat(True)

        self.hbox_Player_Devices_11.addWidget(self.btn_Player_Play_11)

        self.btn_Player_Stop_11 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Stop_11.setObjectName(u"btn_Player_Stop_11")
        self.btn_Player_Stop_11.setMinimumSize(QSize(0, 30))
        self.btn_Player_Stop_11.setMaximumSize(QSize(80, 80))
        self.btn_Player_Stop_11.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#FFFFFF}QPushButton:hover{background-color:#CD6155}\n"
"QPushButton:pressed{color:white;background-color:#CC0033}")
        self.btn_Player_Stop_11.setIcon(icon2)
        self.btn_Player_Stop_11.setIconSize(QSize(15, 15))
        self.btn_Player_Stop_11.setFlat(True)

        self.hbox_Player_Devices_11.addWidget(self.btn_Player_Stop_11)


        self.vlo_Player_11.addLayout(self.hbox_Player_Devices_11)

        self.hbox_Player_PlayTime_11 = QHBoxLayout()
        self.hbox_Player_PlayTime_11.setObjectName(u"hbox_Player_PlayTime_11")
        self.lbl_Player_RunTime_11 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_RunTime_11.setObjectName(u"lbl_Player_RunTime_11")
        self.lbl_Player_RunTime_11.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_11.addWidget(self.lbl_Player_RunTime_11)

        self.psb_Player_1_PlayTime_9 = QProgressBar(self.main_ScrollAreaWidgetContents)
        self.psb_Player_1_PlayTime_9.setObjectName(u"psb_Player_1_PlayTime_9")
        self.psb_Player_1_PlayTime_9.setMaximumSize(QSize(16777215, 10))
        self.psb_Player_1_PlayTime_9.setStyleSheet(u"QProgressBar {background-color:#D5D8DC; border:1px solid grey; border-radius:5px;}\n"
"QProgressBar::chunk {background-color: #05B8CC; width: 20px;}")
        self.psb_Player_1_PlayTime_9.setValue(24)
        self.psb_Player_1_PlayTime_9.setFormat(u"")

        self.hbox_Player_PlayTime_11.addWidget(self.psb_Player_1_PlayTime_9)

        self.lbl_Player_EndTime_11 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_EndTime_11.setObjectName(u"lbl_Player_EndTime_11")
        self.lbl_Player_EndTime_11.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_11.addWidget(self.lbl_Player_EndTime_11)


        self.vlo_Player_11.addLayout(self.hbox_Player_PlayTime_11)

        self.lbl_Player_Status_11 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Status_11.setObjectName(u"lbl_Player_Status_11")
        self.lbl_Player_Status_11.setMinimumSize(QSize(0, 20))

        self.vlo_Player_11.addWidget(self.lbl_Player_Status_11)


        self.verticalLayout_2.addLayout(self.vlo_Player_11)

        self.vlo_Player_19 = QVBoxLayout()
        self.vlo_Player_19.setObjectName(u"vlo_Player_19")
        self.vlo_Player_19.setContentsMargins(6, 0, 6, 0)
        self.lbl_Player_Name_19 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Name_19.setObjectName(u"lbl_Player_Name_19")
        self.lbl_Player_Name_19.setFont(font)
        self.lbl_Player_Name_19.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.vlo_Player_19.addWidget(self.lbl_Player_Name_19)

        self.hbox_Player_File_19 = QHBoxLayout()
        self.hbox_Player_File_19.setObjectName(u"hbox_Player_File_19")
        self.lbl_Player_FileName_19 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_FileName_19.setObjectName(u"lbl_Player_FileName_19")
        self.lbl_Player_FileName_19.setMinimumSize(QSize(50, 20))
        self.lbl_Player_FileName_19.setFont(font1)
        self.lbl_Player_FileName_19.setAlignment(Qt.AlignCenter)

        self.hbox_Player_File_19.addWidget(self.lbl_Player_FileName_19)

        self.let_Player_FileName_19 = QLineEdit(self.main_ScrollAreaWidgetContents)
        self.let_Player_FileName_19.setObjectName(u"let_Player_FileName_19")
        self.let_Player_FileName_19.setFrame(False)

        self.hbox_Player_File_19.addWidget(self.let_Player_FileName_19)

        self.btn_Player_FileOpen_19 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_FileOpen_19.setObjectName(u"btn_Player_FileOpen_19")
        self.btn_Player_FileOpen_19.setMinimumSize(QSize(50, 30))
        self.btn_Player_FileOpen_19.setIcon(icon)
        self.btn_Player_FileOpen_19.setIconSize(QSize(25, 25))
        self.btn_Player_FileOpen_19.setFlat(True)

        self.hbox_Player_File_19.addWidget(self.btn_Player_FileOpen_19)


        self.vlo_Player_19.addLayout(self.hbox_Player_File_19)

        self.hbox_Player_Devices_19 = QHBoxLayout()
        self.hbox_Player_Devices_19.setObjectName(u"hbox_Player_Devices_19")
        self.lbl_Player_Device_16 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Device_16.setObjectName(u"lbl_Player_Device_16")
        self.lbl_Player_Device_16.setMaximumSize(QSize(50, 16777215))
        self.lbl_Player_Device_16.setFont(font1)
        self.lbl_Player_Device_16.setAlignment(Qt.AlignCenter)

        self.hbox_Player_Devices_19.addWidget(self.lbl_Player_Device_16)

        self.cbb_Player_Device_Sel_19 = QComboBox(self.main_ScrollAreaWidgetContents)
        self.cbb_Player_Device_Sel_19.setObjectName(u"cbb_Player_Device_Sel_19")
        self.cbb_Player_Device_Sel_19.setMinimumSize(QSize(350, 20))

        self.hbox_Player_Devices_19.addWidget(self.cbb_Player_Device_Sel_19)

        self.btn_Player_Play_19 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Play_19.setObjectName(u"btn_Player_Play_19")
        self.btn_Player_Play_19.setMinimumSize(QSize(0, 30))
        self.btn_Player_Play_19.setMaximumSize(QSize(80, 80))
        self.btn_Player_Play_19.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#ffffff}\n"
"QPushButton:hover{background-color:#22BCDD}\n"
"QPushButton:pressed{color:white;background-color:#485152}")
        self.btn_Player_Play_19.setIcon(icon1)
        self.btn_Player_Play_19.setIconSize(QSize(20, 20))
        self.btn_Player_Play_19.setCheckable(True)
        self.btn_Player_Play_19.setFlat(True)

        self.hbox_Player_Devices_19.addWidget(self.btn_Player_Play_19)

        self.btn_Player_Stop_19 = QPushButton(self.main_ScrollAreaWidgetContents)
        self.btn_Player_Stop_19.setObjectName(u"btn_Player_Stop_19")
        self.btn_Player_Stop_19.setMinimumSize(QSize(0, 30))
        self.btn_Player_Stop_19.setMaximumSize(QSize(80, 80))
        self.btn_Player_Stop_19.setStyleSheet(u"QPushButton{border:none;border-radius:10px;background-color:#FFFFFF}QPushButton:hover{background-color:#CD6155}\n"
"QPushButton:pressed{color:white;background-color:#CC0033}")
        self.btn_Player_Stop_19.setIcon(icon2)
        self.btn_Player_Stop_19.setIconSize(QSize(15, 15))
        self.btn_Player_Stop_19.setFlat(True)

        self.hbox_Player_Devices_19.addWidget(self.btn_Player_Stop_19)


        self.vlo_Player_19.addLayout(self.hbox_Player_Devices_19)

        self.hbox_Player_PlayTime_19 = QHBoxLayout()
        self.hbox_Player_PlayTime_19.setObjectName(u"hbox_Player_PlayTime_19")
        self.lbl_Player_RunTime_19 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_RunTime_19.setObjectName(u"lbl_Player_RunTime_19")
        self.lbl_Player_RunTime_19.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_19.addWidget(self.lbl_Player_RunTime_19)

        self.psb_Player_1_PlayTime_16 = QProgressBar(self.main_ScrollAreaWidgetContents)
        self.psb_Player_1_PlayTime_16.setObjectName(u"psb_Player_1_PlayTime_16")
        self.psb_Player_1_PlayTime_16.setMaximumSize(QSize(16777215, 10))
        self.psb_Player_1_PlayTime_16.setStyleSheet(u"QProgressBar {background-color:#D5D8DC; border:1px solid grey; border-radius:5px;}\n"
"QProgressBar::chunk {background-color: #05B8CC; width: 20px;}")
        self.psb_Player_1_PlayTime_16.setValue(24)
        self.psb_Player_1_PlayTime_16.setFormat(u"")

        self.hbox_Player_PlayTime_19.addWidget(self.psb_Player_1_PlayTime_16)

        self.lbl_Player_EndTime_19 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_EndTime_19.setObjectName(u"lbl_Player_EndTime_19")
        self.lbl_Player_EndTime_19.setMinimumSize(QSize(0, 20))

        self.hbox_Player_PlayTime_19.addWidget(self.lbl_Player_EndTime_19)


        self.vlo_Player_19.addLayout(self.hbox_Player_PlayTime_19)

        self.lbl_Player_Status_19 = QLabel(self.main_ScrollAreaWidgetContents)
        self.lbl_Player_Status_19.setObjectName(u"lbl_Player_Status_19")
        self.lbl_Player_Status_19.setMinimumSize(QSize(0, 20))

        self.vlo_Player_19.addWidget(self.lbl_Player_Status_19)


        self.verticalLayout_2.addLayout(self.vlo_Player_19)

        self.line_4 = QFrame(self.main_ScrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.main_scrollArea.setWidget(self.main_ScrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.main_scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 689, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_Main_Lable.setText(QCoreApplication.translate("MainWindow", u"Multi Channel Player", None))
        self.lbl_Iind_Player_1.setText(QCoreApplication.translate("MainWindow", u"P1", None))
        self.lbl_Iind_Player_2.setText(QCoreApplication.translate("MainWindow", u"P2", None))
        self.lbl_Iind_Player_3.setText(QCoreApplication.translate("MainWindow", u"P3", None))
        self.lbl_Iind_Player_4.setText(QCoreApplication.translate("MainWindow", u"P4", None))
        self.lbl_Iind_Player_5.setText(QCoreApplication.translate("MainWindow", u"P5", None))
        self.lbl_Iind_Player_6.setText(QCoreApplication.translate("MainWindow", u"P6", None))
        self.lbl_Iind_Player_7.setText(QCoreApplication.translate("MainWindow", u"P7", None))
        self.lbl_Iind_Player_8.setText(QCoreApplication.translate("MainWindow", u"P8", None))
        self.lbl_Player_1_Status.setText("")
        self.lbl_Player_Name_1.setText(QCoreApplication.translate("MainWindow", u"Player 1", None))
        self.lbl_Player_FileName_1.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.btn_Player_FileOpen_1.setText("")
        self.lbl_Player_1_Device.setText(QCoreApplication.translate("MainWindow", u"Device", None))
        self.btn_Player_Play_1.setText("")
        self.btn_Player_Stop_1.setText("")
        self.lbl_Player_RunTime_1.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_EndTime_1.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_Status_1.setText("")
        self.lbl_Player_Name_2.setText(QCoreApplication.translate("MainWindow", u"Player 2", None))
        self.lbl_Player_FileName_2.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.btn_Player_FileOpen_2.setText("")
        self.lbl_Player_Device_2.setText(QCoreApplication.translate("MainWindow", u"Device", None))
        self.btn_Player_Play_2.setText("")
        self.btn_Player_Stop_2.setText("")
        self.lbl_Player_RunTime_2.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_EndTime_2.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_Status_2.setText("")
        self.lbl_Player_Name_3.setText(QCoreApplication.translate("MainWindow", u"Player 3", None))
        self.lbl_Player_FileName_7.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.btn_Player_FileOpen_7.setText("")
        self.lbl_Player_Device_5.setText(QCoreApplication.translate("MainWindow", u"Device", None))
        self.btn_Player_Play_7.setText("")
        self.btn_Player_Stop_7.setText("")
        self.lbl_Player_RunTime_7.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_EndTime_7.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_Status_7.setText("")
        self.lbl_Player_Name_8.setText(QCoreApplication.translate("MainWindow", u"Player 4", None))
        self.lbl_Player_FileName_8.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.btn_Player_FileOpen_8.setText("")
        self.lbl_Player_Device_6.setText(QCoreApplication.translate("MainWindow", u"Device", None))
        self.btn_Player_Play_8.setText("")
        self.btn_Player_Stop_8.setText("")
        self.lbl_Player_RunTime_8.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_EndTime_8.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_Status_8.setText("")
        self.lbl_Player_Name_9.setText(QCoreApplication.translate("MainWindow", u"Player 5", None))
        self.lbl_Player_FileName_9.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.btn_Player_FileOpen_9.setText("")
        self.lbl_Player_Device_7.setText(QCoreApplication.translate("MainWindow", u"Device", None))
        self.btn_Player_Play_9.setText("")
        self.btn_Player_Stop_9.setText("")
        self.lbl_Player_RunTime_9.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_EndTime_9.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_Status_9.setText("")
        self.lbl_Player_Name_10.setText(QCoreApplication.translate("MainWindow", u"Player 6", None))
        self.lbl_Player_FileName_10.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.btn_Player_FileOpen_10.setText("")
        self.lbl_Player_Device_8.setText(QCoreApplication.translate("MainWindow", u"Device", None))
        self.btn_Player_Play_10.setText("")
        self.btn_Player_Stop_10.setText("")
        self.lbl_Player_RunTime_10.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_EndTime_10.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_Status_10.setText("")
        self.lbl_Player_Name_11.setText(QCoreApplication.translate("MainWindow", u"Player 7", None))
        self.lbl_Player_FileName_11.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.btn_Player_FileOpen_11.setText("")
        self.lbl_Player_Device_9.setText(QCoreApplication.translate("MainWindow", u"Device", None))
        self.btn_Player_Play_11.setText("")
        self.btn_Player_Stop_11.setText("")
        self.lbl_Player_RunTime_11.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_EndTime_11.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_Status_11.setText("")
        self.lbl_Player_Name_19.setText(QCoreApplication.translate("MainWindow", u"Player 8", None))
        self.lbl_Player_FileName_19.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.btn_Player_FileOpen_19.setText("")
        self.lbl_Player_Device_16.setText(QCoreApplication.translate("MainWindow", u"Device", None))
        self.btn_Player_Play_19.setText("")
        self.btn_Player_Stop_19.setText("")
        self.lbl_Player_RunTime_19.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_EndTime_19.setText(QCoreApplication.translate("MainWindow", u"--/--", None))
        self.lbl_Player_Status_19.setText("")
    # retranslateUi

