# -*- coding: utf-8 -*-
import sys, vlc, time, socket, os.path, math, struct, datetime, lotteplayer_rc, re, json, os
from lotteplayer_ui import Ui_MainWindow
from _thread import *
from PyQt5.QtCore import QCoreApplication, QMetaObject, QObject, pyqtSlot, pyqtSignal, QSize, Qt, QRect, QThread, QTime
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import *

class Main(QMainWindow, Ui_MainWindow):
    play = pyqtSignal(str);pause = pyqtSignal();stop = pyqtSignal();
    #chimeplay = pyqtSignal(str)
    get_vol = pyqtSignal();set_vol = pyqtSignal(int)
    auidodevice_call = pyqtSignal()
    audioDevice_Change = pyqtSignal(int)

    def __init__(self):
        super().__init__()        
        #Variable
        self.setup = ({'serverip':'172.28.242.216','serverport':5008,'boothNum':10,'audioDeviceId':0,'vol':70,
                        'zone_name_1':'센텀시티','zone_name_2':'이시아폴리스','zone_name_3':'상인점','zone_name_4':'대구점','zone_name_5':'포항점','zone_name_6':'아쿠아몰','zone_name_7':'광복점','zone_name_8':'광주점',
                        'zone_name_9':'전주점','zone_name_10':'청주영플라자','zone_name_11':'대전점','zone_name_12':'서울역점','zone_name_13':'영등포점','zone_name_14':'중동점','zone_name_15':'관악점','zone_name_16':'창원점',
                        'zone_name_17':'창원영패션관','zone_name_18':'일산점','zone_name_19':'구리점','zone_name_20':'평촌점','zone_name_21':'안산점','zone_name_22':'미아점','zone_name_23':'스타시티','zone_name_24':'노원점',
                        'zone_name_25':'분당점','zone_name_26':'잠실점','zone_name_27':'동래점','zone_name_28':'청량지점','zone_name_29':'에비뉴엘','zone_name_30':'영플라자','zone_name_31':'본점','zone_name_32':'강남점',
                        'zone_name_33':'청주아울렛','zone_name_34':'울산점','zone_name_35':'김해아울렛','zone_name_36':'파주아울렛','zone_name_37':'서면점','zone_name_38':'율하점','zone_name_39':'수완아울렛','zone_name_40':'광주월드컵점',
                        'zone_name_41':'부여아울렛','zone_name_42':'이천아울렛','zone_name_43':'고양터미널','zone_name_44':'에비뉴엘\n월드타워','zone_name_45':'수원점','zone_name_46':'광명점','zone_name_47':'구리아울렛','zone_name_48':'동부산점',
                        'zone_name_49':'마산점','zone_name_50':'광교아울렛','zone_name_51':'가산아울렛','zone_name_52':'진주아울렛','zone_name_53':'남악아울렛','zone_name_54':'고양아울렛','zone_name_55':'군산아울렛','zone_name_56':'기흥아울렛',
                        'zone_name_57':'인천터미널'})
        self.logserver = ('172.28.242.40',9999)
        self.zone_status = ({1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0,32:0,33:0,
                            34:0,35:0,36:0,37:0,38:0,39:0,40:0,41:0,42:0,43:0,44:0,45:0,46:0,47:0,48:0,49:0,50:0,51:0,52:0,53:0,54:0,55:0,56:0,57:0,58:0,59:0,60:0,61:0,62:0,63:0,64:0,65:0,66:0})
        self.zone_state = (['대기중','방송중\nBooth 1','방송중\nBooth 2','방송중\nBooth 3','방송중\nBooth 4','방송중\nBooth 5','방송중\nBooth 6','방송중\nBooth 7','방송중\nBooth 8','방송중\nBooth 9',
                            '방송중\nPlayer 1','방송중\nPlayer 2','방송중\nPlayer 3','방송중\nPlayer 4','방송중\nPlayer 5','방송중\nPlayer 6','방송중\nPlayer 7','방송중\nPlayer 8','방송중\nPlayer 9'])
        self.playIndex = 0
        self.playLoop = 0
        self.playlist =[]
        self.zone_list =[]
        self.copy_ID = 99

        self.dialog = QDialog()
        self.dialog.Qui = Dialog_Zone_Sel()
        self.dialog.Qui.setupUi(self.dialog)
        self.dialog_Message = QDialog()
        self.dialog_Message.Qui = Dialog_Message()
        self.dialog_Message.Qui.setupUi(self.dialog_Message)

        self.setupUi(self)
        self.setWindowTitle('Audio Player - 224.1.128.128 : 5007')

        self.setup_file_road()

        #Thread Class
        self.audioplayer = audioplayer()
        self.udp_server = udp_server()
        self.schedulePlay = schedulePlay()
        #self.chimeplayer = chimeplayer()
        #Signal & Slot
        self.Sld_Vol.valueChanged.connect(self.lbl_Vol_Value.setNum)
        self.Sld_Vol.valueChanged.connect(self.vol_Set)
        self.btn_Tab_Player.clicked.connect(lambda: self.stacked_Wiget_Page_Change(0))
        self.btn_Tab_Schduler.clicked.connect(lambda: self.stacked_Wiget_Page_Change(1))
        self.btn_Setup.clicked.connect(lambda: self.stacked_Wiget_Page_Change(2))
        self.btn_Playlist_Add.clicked.connect(self.addList)
        self.btn_Playlist_Del.clicked.connect(self.delList)
        self.tw_Playlist.cellClicked.connect(self.select_Playlist_row)
        self.tw_Playlist.cellDoubleClicked.connect(self.doubleClick_Playlist)
        self.btn_Stop.clicked.connect(lambda: self.play_audio(0))
        self.btn_Play.clicked.connect(lambda: self.play_audio(1))
        self.btn_RW.clicked.connect(lambda: self.play_audio(2))
        self.btn_FF.clicked.connect(lambda: self.play_audio(3))
        self.btn_Loop.clicked.connect(lambda: self.play_audio(4))
        self.btn_PlaylistPlay.clicked.connect(lambda: self.play_audio(4))
        self.btn_schedule_Reset.clicked.connect(self.scheduler_reset)
        self.btn_Audiodecive_Refrash.clicked.connect(self.audio_Device_Refrash)        
        self.play.connect(self.audioplayer.play)
        self.pause.connect(self.audioplayer.pause)
        self.stop.connect(self.audioplayer.stop)
        self.auidodevice_call.connect(self.audioplayer.get_Audio_Devices)
        self.get_vol.connect(self.audioplayer.audio_Vol_Get)
        self.set_vol.connect(self.audioplayer.audio_Vol_Set)

        #self.chimeplay.connect(self.chimeplayer.play)

        self.cb_Booth.currentIndexChanged.connect(self.set_Booth_Index)

        self.audioplayer.player_Status.connect(self.player_state_change)
        self.audioplayer.audio_devices.connect(self.audio_devices)

        self.udp_server.udp_data.connect(self.server_data_parcing)

        self.schedule_file_btn_grp.buttonClicked[int].connect(self.schedule_file_load)
        self.schedule_zone_sel_grp.buttonClicked[int].connect(self.schedule_zone_sel)
        self.schedule_del_btn_grp.buttonClicked[int].connect(self.schedule_List_del)
        self.schedule_copy_btn_grp.buttonClicked[int].connect(self.schedule_copy)

        for i in range(15):
            self.schedule_List[i][7].stateChanged.connect(self.schedule_value_change)
            self.schedule_List[i][5].currentIndexChanged.connect(self.schedule_value_change)
            self.schedule_List[i][6].timeChanged.connect(self.schedule_value_change)

        self.schedulePlay.Timer_Receive_String.connect(self.schedule_parcing)
        self.btn_Set_Ip.clicked.connect(self.server_ip_setup)
        self.show()

        #Thread Start
        self.udp_server.start()
        self.schedulePlay.start()
        #self.chimeplayer.start()
        #Start Set Value
        self.auidodevice_call.emit()
        self.set_vol.emit(self.setup['vol'])
        self.get_vol.emit()
        self.set_ButtonName()
        self.setup_file_road()
        self.cb_Booth.setCurrentIndex(self.setup['boothNum']-10)
        self.cb_AudioDevice.setCurrentIndex(self.setup['audioDeviceId'])
        self.le_Serverip.setText(self.setup['serverip'])
        self.le_Serverport.setText(str(self.setup['serverport']))
        start_new_thread(self.server_call,('t:request,!',))
        start_new_thread(self.server_call,('t:booth{},!'.format(self.setup['boothNum']),))
        start_new_thread(self.log_server_call,('0,{}번 부스 이벤트 플레이가 실행되었습니다.'.format(self.setup['boothNum']-9),))

        self.cb_AudioDevice.currentIndexChanged.connect(self.set_Audio_Device)
        self.audioDevice_Change.connect(self.audioplayer.set_Audio_Device)
        self.set_vol.emit(self.setup['vol'])


    def setupUi(self, MainWindow):
        font_Label = QFont()
        font_Label.setFamily(u"NanumBarunGothic");
        font_Label.setPointSize(14)
        font_10 = QFont();font_10.setPointSize(10)
        #font_10.setFamily(u"NanumBarunGothic")
        font_12 = QFont()
        #font_12.setFamily(u"NanumBarunGothic");font_12.setPointSize(12)
        windowIcon = QIcon();windowIcon.addFile(u":/icons/volume.png", QSize(), QIcon.Normal, QIcon.Off)

        self.btn_style_nomal = ("""
                                QPushButton{border:none;border-radius:15px;background-color:#f8f9f9}
                                QPushButton:checked{color:white;background-color:#566573}
                                QPushButton:hover{background-color:#EBF5FB}
                                QPushButton:checked:hover{color:white;background-color:#1C2833}
                                QPushButton:pressed{color:white;background-color:#503131}
                                QPushButton:checked:pressed{color:white;background-color:#503131}
                                """)
        self.btn_style_checked = ("""
                                QPushButton{border:none;border-radius:15px;color:white;background-color:#ff5050}
                                QPushButton:checked{color:white;background-color:#ff3300}
                                QPushButton:hover{background-color:#800000}
                                QPushButton:checked:hover{color:white;background-color:#800000}
                                QPushButton:pressed{color:white;background-color:#270B02}
                                QPushButton:checked:pressed{color:black;background-color:#E7E7E7}
                                """)
        self.btn_style_self = ("""
                                QPushButton{border:none;border-radius:15px;color:white;background-color:#0099ff}
                                QPushButton:checked{color:white;background-color:#ff0000}
                                QPushButton:hover{background-color:#FF0000}
                                QPushButton:checked:hover{color:white;background-color:#FF0000}
                                QPushButton:pressed{color:white;background-color:#28B463}
                                QPushButton:checked:pressed{color:black;background-color:#28B463}
                                """)
        self.combobox_style = ("""
                                QComboBox{color:black; border:1px solid #f8f9f9;}
                                QComboBox::drop-down {border:none; width:20px}
                                QComboBox:down-arrow {image: url(:/icons/down-arrow.png); width: 15px; height: 15px;}
                                QListView::item{height:30px;}
                                QListView::item:selected {color: white; background-color: #4D6C95}");
                                """)

    #Main Windwos
        MainWindow.resize(1280, 800)
        MainWindow.setStyleSheet("QMainWindow{background-color:#ffffff};")
        MainWindow.setWindowIcon(windowIcon)
        self.centralwidget = QWidget(MainWindow)

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0,0,0,0)

    #Main Window Vbox Layout
        self.vbox_MainWindow = QVBoxLayout()
### 1st Line
        self.hbox_Booth = QHBoxLayout()
        self.hbox_Booth.setContentsMargins(20,5,20,5)
        self.hbox_Booth.setSpacing(10)
        #Player Stacked Sel Button
        self.btn_Tab_Player = QPushButton('Player',self.centralwidget)
        playIcon = QIcon();playIcon.addFile(u":/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Tab_Player.setIcon(playIcon)
        self.btn_Tab_Player.setMinimumSize(QSize(0, 30))
        self.btn_Tab_Player.setMaximumSize(QSize(150, 16777215))
        self.btn_Tab_Player.setFlat(True)
        self.btn_Tab_Player.setFocusPolicy(Qt.NoFocus)
        self.btn_Tab_Player.setStyleSheet("QPushButton{border:none}")
        self.hbox_Booth.addWidget(self.btn_Tab_Player)
        #Scheduler Stacked Sel Button
        self.btn_Tab_Schduler = QPushButton('스케줄러',self.centralwidget)
        calendar_icon = QIcon();calendar_icon.addFile(u":/icons/calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Tab_Schduler.setIcon(calendar_icon)
        self.btn_Tab_Schduler.setMinimumSize(QSize(0, 30))
        self.btn_Tab_Schduler.setMaximumSize(QSize(150, 16777215))
        self.btn_Tab_Schduler.setFlat(True)
        self.btn_Tab_Schduler.setFocusPolicy(Qt.NoFocus)
        self.btn_Tab_Schduler.setStyleSheet("QPushButton{border:none}")
        self.hbox_Booth.addWidget(self.btn_Tab_Schduler)

        self.btn_Setup = QPushButton('설정',self.centralwidget)
        setup_icon = QIcon();setup_icon.addFile(u":/icons/system.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Setup.setIcon(setup_icon)
        self.btn_Setup.setMaximumSize(QSize(150, 16777215))
        self.btn_Setup.setIconSize(QSize(25, 25))
        self.btn_Setup.setFlat(True)
        self.btn_Setup.setFocusPolicy(Qt.NoFocus)
        self.btn_Setup.setStyleSheet("QPushButton{border:none}")      
        self.hbox_Booth.addWidget(self.btn_Setup)

        #Booth Sel
        self.lbl_Booth = QLabel('부스 선택',self.centralwidget)
        self.lbl_Booth.setMinimumSize(QSize(0, 25))
        self.lbl_Booth.setMaximumSize(QSize(60, 16777215))
        self.lbl_Booth.setFont(font_10)
        self.hbox_Booth.addWidget(self.lbl_Booth)

        self.cb_Booth = QComboBox(self.centralwidget)
        self.cb_Booth.setView(QListView())
        self.cb_Booth.setFont(font_10)
        for i in range(9):
            self.cb_Booth.addItem('Booth {}'.format(i+1))
            self.cb_Booth.setItemData(i,font_10,Qt.FontRole)
        self.cb_Booth.setMinimumSize(QSize(0, 30))
        self.cb_Booth.setMaximumSize(QSize(200, 16777215))
        self.cb_Booth.setStyleSheet(self.combobox_style)
        self.cb_Booth.setInsertPolicy(QComboBox.InsertAtBottom)
        self.cb_Booth.setFrame(False)
        self.hbox_Booth.addWidget(self.cb_Booth)

        self.lbl_blank = QLabel(self.centralwidget)
        self.hbox_Booth.addWidget(self.lbl_blank)

        #Audio Device Sel
        self.lbl_AudioDevice = QLabel('오디오 디바이스 선택',self.centralwidget)
        self.lbl_AudioDevice.setMinimumSize(QSize(120, 30))
        self.lbl_AudioDevice.setMaximumSize(QSize(130, 16777215))
        self.lbl_AudioDevice.setFont(font_10)
        self.hbox_Booth.addWidget(self.lbl_AudioDevice)

        self.cb_AudioDevice = QComboBox(self.centralwidget)
        self.cb_AudioDevice.setView(QListView())
        self.cb_AudioDevice.setMinimumSize(QSize(0, 30))
        self.cb_AudioDevice.setStyleSheet(self.combobox_style)
        self.cb_AudioDevice.setInsertPolicy(QComboBox.InsertAtBottom)
        self.cb_AudioDevice.setFrame(False)
        self.hbox_Booth.addWidget(self.cb_AudioDevice)
        self.vbox_MainWindow.addLayout(self.hbox_Booth)

        self.btn_Audiodecive_Refrash = QPushButton(self.centralwidget)
        self.btn_Audiodecive_Refrash.setMinimumSize(QSize(0, 30))
        self.btn_Audiodecive_Refrash.setMaximumSize(QSize(30, 16777215))
        self.btn_Audiodecive_Refrash.setIconSize(QSize(15, 15))
        icon7 = QIcon();icon7.addFile(u":/icons/loop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Audiodecive_Refrash.setIcon(icon7)
        self.btn_Audiodecive_Refrash.setFlat(True)
        self.btn_Audiodecive_Refrash.setFont(font_10)
        self.hbox_Booth.addWidget(self.btn_Audiodecive_Refrash)

    #2nd Line
        #Stack Widget
        self.stackedWidget = QStackedWidget(self.centralwidget)
        #self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setStyleSheet("background-color:#f8f9f9")
        #Stack Page 1
        self.page_1 = QWidget()
        self.gl_Stack_Page_1 = QGridLayout(self.page_1)
### Playlist
        #Label Playlist
        self.lbl_PlayList = QLabel('플레이 리스트',self.page_1)
        self.lbl_PlayList.setFont(font_Label)
        self.lbl_PlayList.setIndent(10)
        #self.lbl_PlayList.setStyleSheet("QLabel{color:#ffffff}")
        self.gl_Stack_Page_1.addWidget(self.lbl_PlayList, 0, 1, 1, 1)
        #Grid Widget Playlist
        self.gw_Playlist = QGridLayout()
        self.gl_Stack_Page_1.addLayout(self.gw_Playlist, 1, 1, 1, 1)
        #Playlist Table
        self.tw_Playlist = QTableWidget(0,1,self.page_1)
        self.tw_Playlist.setHorizontalHeaderItem(0, QTableWidgetItem('Title'))
        self.tw_Playlist.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_Playlist.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_Playlist.horizontalHeader().setStretchLastSection(True)
        self.tw_Playlist.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tw_Playlist.setMaximumSize(QSize(600, 16777215))
        #self.tw_Playlist.setStyleSheet("QWidget{color:#ffffff}; QTableWidget{gridline-color: #ffffff};")
        self.tw_Playlist.setFrameShape(QFrame.NoFrame)
        #self.tw_Playlist.setFrameShadow(QFrame.Plain)
        self.tw_Playlist.setStyleSheet("""
                                        QWidget{background-color:#f8f9f9}
                                        QHeaderView::section{padding:5px;border:0px}
                                        QTableView{selection-color:white;selection-background-color:#566573}
                                        QTableView QTableCornerButton::section {background:#f8f9f9}
                                        """)

        self.gw_Playlist.addWidget(self.tw_Playlist, 0, 0, 1, 1)
        #hbox Playlist buttons
        self.hbox_Playlist_add_del = QHBoxLayout()
        self.gw_Playlist.addLayout(self.hbox_Playlist_add_del, 2, 0, 1, 1)        

        self.btn_Playlist_Add = QPushButton('Add List',self.page_1)
        icon = QIcon();icon.addFile(u":/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Playlist_Add.setIcon(icon)
        self.btn_Playlist_Add.setIconSize(QSize(25, 25))
        self.btn_Playlist_Add.setFocusPolicy(Qt.NoFocus)
        self.btn_Playlist_Add.setStyleSheet("QPushButton{border:none}")
        self.hbox_Playlist_add_del.addWidget(self.btn_Playlist_Add)

        self.btn_Playlist_Del = QPushButton('Del List',self.page_1)
        icon1 = QIcon();icon1.addFile(u":/icons/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Playlist_Del.setIcon(icon1)
        self.btn_Playlist_Del.setIconSize(QSize(25, 25))
        self.btn_Playlist_Del.setFocusPolicy(Qt.NoFocus)
        self.btn_Playlist_Del.setStyleSheet("QPushButton{border:none}")
        self.hbox_Playlist_add_del.addWidget(self.btn_Playlist_Del)
        #Playlist Play Continue
        self.btn_PlaylistPlay = QPushButton('플레이 리스트 연속 재생',self.page_1)
        self.btn_PlaylistPlay.setMinimumSize(QSize(250,10))
        self.btn_PlaylistPlay.setMaximumSize(QSize(300, 16777215))
        icon2 = QIcon();icon2.addFile(u":/icons/continue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_PlaylistPlay.setIcon(icon2)
        self.btn_PlaylistPlay.setIconSize(QSize(25, 25))
        self.btn_PlaylistPlay.setCheckable(True)
        self.btn_PlaylistPlay.setStyleSheet("""
                                            QPushButton{border:none;border-radius:10px;background-color:#f8f9f9}
                                            QPushButton:checked{color:white;background-color:#566573}
                                            """)
        self.gw_Playlist.addWidget(self.btn_PlaylistPlay, 3, 0, 1, 1, Qt.AlignCenter)

    ### Zone Selector
        self.lbl_Zone = QLabel('방송 구간 선택/방송 구간 상태',self.page_1)
        self.lbl_Zone.setFont(font_Label)
        self.lbl_Zone.setIndent(10)
        #self.lbl_Zone.setStyleSheet("QLabel{color:#ffffff}")

        self.gl_Stack_Page_1.addWidget(self.lbl_Zone, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.page_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setSizeIncrement(QSize(1, 2))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.gw_Zone_Sel = QWidget()
        self.gw_Zone_Sel.setGeometry(QRect(0, 0, 498, 908))
        self.gridLayout_ZoneSel = QGridLayout(self.gw_Zone_Sel)
        self.gridLayout_ZoneSel.setObjectName(u"gridLayout_ZoneSel")

        self.zone_Buttons = [str(i) for i in range(66)]

        for i in range(len(self.zone_Buttons)):
            self.zone_Buttons[i] = QPushButton('{}'.format(i+1),self.gw_Zone_Sel)
            self.zone_Buttons[i].setMinimumSize(QSize(0, 40))
            self.zone_Buttons[i].setMaximumSize(QSize(200, 100))
            self.zone_Buttons[i].setStyleSheet(self.btn_style_nomal)
            self.zone_Buttons[i].setCheckable(True)
            self.gridLayout_ZoneSel.addWidget(self.zone_Buttons[i],int(i/6),int(i%6),1,1)

        self.scrollArea.setWidget(self.gw_Zone_Sel)

        self.gl_Stack_Page_1.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_1)

        #Stack Page 2
### Scheduler
        self.page_2 = QWidget()
        self.stackedWidget.addWidget(self.page_2)

        self.gl_Stack_Page2 = QGridLayout(self.page_2)

        self.vbox_Schedule = QVBoxLayout()
        self.vbox_Schedule.setContentsMargins(10,0,10,0)
        self.gl_Stack_Page2.addLayout(self.vbox_Schedule, 0, 0, 1, 1)

        self.lbl_Schedule = QLabel('Scheduler',self.page_2)
        self.lbl_Schedule.setIndent(10)
        self.lbl_Schedule.setFont(font_Label)
        self.vbox_Schedule.addWidget(self.lbl_Schedule)

        self.sa_Schedule = QScrollArea(self.page_2)
        self.sa_Schedule.setWidgetResizable(True)
        self.sa_Schedule.setStyleSheet("border:none")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 654, 904))
        self.sa_Schedule.setWidget(self.scrollAreaWidgetContents)
        self.vbox_Schedule.addWidget(self.sa_Schedule)

        self.gl_Schedule = QGridLayout(self.scrollAreaWidgetContents)
        self.gl_Schedule.setSpacing(0)
        self.gl_Schedule.setContentsMargins(0,0,0,0)

        self.scrollAreaWidgetContents.setStyleSheet("[coloredcell=\"true\"] {background-color:#EAECEE}")

        self.lbl_Name_0 = QLabel('No.',self.scrollAreaWidgetContents)
        self.lbl_Name_0.setProperty("coloredcell",True)
        self.lbl_Name_0.setMinimumSize(QSize(30, 40))
        self.lbl_Name_0.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_0, 0, 0, 1, 1)
        
        self.lbl_Name_1 = QLabel('파일',self.scrollAreaWidgetContents)
        self.lbl_Name_1.setProperty("coloredcell",True)
        #self.lbl_Name_1.setMinimumSize(QSize(100, 40))
        self.lbl_Name_1.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_1, 0, 1, 1, 2)

        self.lbl_Name_2 = QLabel('방송구간',self.scrollAreaWidgetContents)
        self.lbl_Name_2.setProperty("coloredcell",True)
        #self.lbl_Name_2.setMinimumSize(QSize(100, 40))
        self.lbl_Name_2.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_2, 0, 3, 1, 2)

        self.lbl_Name_3 = QLabel('요일',self.scrollAreaWidgetContents)
        self.lbl_Name_3.setProperty("coloredcell",True)
        self.lbl_Name_3.setMaximumSize(QSize(100, 40))
        self.lbl_Name_3.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_3, 0, 5, 1, 1)

        self.lbl_Name_4 = QLabel('시간',self.scrollAreaWidgetContents)
        self.lbl_Name_4.setProperty("coloredcell",True)
        #self.lbl_Name_4.setMaximumSize(QSize(100, 20))
        self.lbl_Name_4.setMinimumSize(QSize(100, 40))
        self.lbl_Name_4.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_4, 0, 6, 1, 1)

        self.lbl_Name_5 = QLabel('활성화',self.scrollAreaWidgetContents)
        self.lbl_Name_5.setProperty("coloredcell",True)
        #self.lbl_Name_5.setFixedSize(40,20)
        self.lbl_Name_5.setMinimumSize(QSize(80, 40))
        self.lbl_Name_5.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_5, 0, 7, 1, 1)

        self.lbl_Name_6 = QLabel('삭제',self.scrollAreaWidgetContents)
        self.lbl_Name_6.setProperty("coloredcell",True)
        #self.lbl_Name_5.setFixedSize(40,20)
        self.lbl_Name_6.setMinimumSize(QSize(50, 40))
        self.lbl_Name_6.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_6, 0, 8, 1, 1)

        self.lbl_Name_7 = QLabel('복사',self.scrollAreaWidgetContents)
        self.lbl_Name_7.setProperty("coloredcell",True)
        #self.lbl_Name_5.setFixedSize(40,20)
        self.lbl_Name_7.setMinimumSize(QSize(50, 40))
        self.lbl_Name_7.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.gl_Schedule.addWidget(self.lbl_Name_7, 0, 9, 1, 1)

        self.days = ["매일","월~목","금~일","월~수","목~일","월","화","수","목","금","토","일"]
        self.days_value = [[0,1,2,3,4,5,6],[0,1,2,3],[4,5,6],[0,1,2],[3,4,5,6],[0],[1],[2],[3],[4],[5],[6]]

        self.schedule_List = [['i' for col in range(10)] for row in range(15)]
        self.schedule_Line = ['i']*16

        self.schedule_file_btn_grp = QButtonGroup()
        self.schedule_zone_sel_grp = QButtonGroup()
        self.schedule_del_btn_grp = QButtonGroup()
        self.schedule_copy_btn_grp = QButtonGroup()

        icon_copy = QIcon()
        icon_copy.addFile(u":/icons/copy.png", QSize(), QIcon.Normal, QIcon.Off)

        for i in range(15):
            self.schedule_List[i][0] = QLabel('{}'.format(i+1),self.scrollAreaWidgetContents)
            self.schedule_List[i][0].setMaximumSize(QSize(50, 100))
            self.schedule_List[i][0].setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.schedule_List[i][1] = QLineEdit(self.scrollAreaWidgetContents)
            self.schedule_List[i][1].setAcceptDrops(True)
            #self.schedule_List[i][1].setWordWrap(True)
            self.schedule_List[i][1].setMinimumSize(100,40)
            self.schedule_List[i][2] = QPushButton(self.scrollAreaWidgetContents)
            self.schedule_List[i][2].setIcon(icon2)
            self.schedule_List[i][2].setFlat(True)
            self.schedule_List[i][2].setMaximumSize(QSize(30, 100))
            self.schedule_file_btn_grp.addButton(self.schedule_List[i][2], i)
            self.schedule_List[i][3] = QLineEdit(self.scrollAreaWidgetContents)
            #self.schedule_List[i][3].setWordWrap(True)
            self.schedule_List[i][4] = QPushButton(self.scrollAreaWidgetContents)
            self.schedule_List[i][4].setIcon(icon2)
            self.schedule_List[i][4].setFlat(True)
            self.schedule_List[i][4].setMaximumSize(QSize(30, 100))
            self.schedule_zone_sel_grp.addButton(self.schedule_List[i][4], i)
            self.schedule_List[i][5] = QComboBox(self.scrollAreaWidgetContents)
            self.schedule_List[i][5].setView(QListView())
            self.schedule_List[i][5].setStyleSheet(self.combobox_style)
            for day in range(len(self.days)):
                self.schedule_List[i][5].addItem(self.days[day])
            self.schedule_List[i][6] = QTimeEdit(self.scrollAreaWidgetContents)
            self.schedule_List[i][6].setMinimumSize(100,30)
            self.schedule_List[i][6].setStyleSheet("QTimeEdit{border:none;padding:5px}")
            self.schedule_List[i][7] = QCheckBox(self.scrollAreaWidgetContents)
            self.schedule_List[i][7].setMinimumSize(QSize(50, 30))
            self.schedule_List[i][7].setStyleSheet("QCheckBox{margin-left:50%;margin-right:50%;}")
            self.schedule_List[i][8] = QPushButton(self.scrollAreaWidgetContents)
            self.schedule_List[i][8].setIcon(icon1)
            self.schedule_List[i][8].setFlat(True)
            self.schedule_List[i][8].setMinimumSize(QSize(50, 30))
            self.schedule_del_btn_grp.addButton(self.schedule_List[i][8],i)

            self.schedule_List[i][9] = QPushButton(self.scrollAreaWidgetContents)
            self.schedule_List[i][9].setIcon(icon_copy)
            self.schedule_List[i][9].setFlat(True)
            #self.schedule_List[i][9].setCheckable(True)
            self.schedule_List[i][9].setMinimumSize(QSize(80, 30))
            self.schedule_List[i][9].setStyleSheet(self.btn_style_nomal)
            self.schedule_copy_btn_grp.addButton(self.schedule_List[i][9],i)

            for j in range(10):
                self.gl_Schedule.addWidget(self.schedule_List[i][j], i+1,j,1,1)


        self.btn_schedule_Reset = QPushButton('Reset', self.page_2)
        self.btn_schedule_Reset.setMinimumSize(200,30)
        self.btn_schedule_Reset.setStyleSheet("""
                                            QPushButton{border:none;border-radius:10px;background-color:#EAECEE}
                                            QPushButton:hover{background-color:#CD6155}
                                            QPushButton:pressed{color:white;background-color:#566573}
                                            """)
        self.vbox_Schedule.addWidget(self.btn_schedule_Reset,Qt.AlignCenter)

### Setup Page
        self.page_3 = QWidget()
        self.Ip_Setup_Widget = QWidget(self.page_3)
        self.Ip_Setup_Widget.setGeometry(QRect(10, 20, 391, 171))
        self.gw_IpSetup = QGridLayout(self.Ip_Setup_Widget)
    
        self.lbl_IP_Setup = QLabel('IP Setup',self.Ip_Setup_Widget)
        self.lbl_IP_Setup.setFont(font_Label)
        self.gw_IpSetup.addWidget(self.lbl_IP_Setup, 0, 0, 1, 1)

        self.line_2 = QFrame(self.Ip_Setup_Widget)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.gw_IpSetup.addWidget(self.line_2, 1, 0, 1, 3)

        self.lbl_Serverip = QLabel('서버 IP',self.Ip_Setup_Widget)
        self.gw_IpSetup.addWidget(self.lbl_Serverip, 2, 0, 1, 1)

        self.le_Serverip = QLineEdit(self.Ip_Setup_Widget)
        self.gw_IpSetup.addWidget(self.le_Serverip, 2, 1, 1, 2)

        self.lbl_Serverport = QLabel('서버 포트',self.Ip_Setup_Widget)
        self.gw_IpSetup.addWidget(self.lbl_Serverport, 3, 0, 1, 1)

        self.le_Serverport = QLineEdit(self.Ip_Setup_Widget)
        self.gw_IpSetup.addWidget(self.le_Serverport, 3, 1, 1, 2)

        self.line = QFrame(self.Ip_Setup_Widget)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.gw_IpSetup.addWidget(self.line, 4, 0, 1, 3)

        self.btn_Set_Ip = QPushButton('확인',self.Ip_Setup_Widget)
        self.gw_IpSetup.addWidget(self.btn_Set_Ip, 5, 1, 1, 1)

        self.btn_Set_Ip_Cancel = QPushButton('취소',self.Ip_Setup_Widget)
        self.gw_IpSetup.addWidget(self.btn_Set_Ip_Cancel, 5, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        #End Stack Widget
        self.vbox_MainWindow.addWidget(self.stackedWidget)
### 3rd Line
    ###Player Control
        self.vbox_Player = QVBoxLayout()
        self.vbox_Player.setContentsMargins(20,10,20,20)
        self.vbox_MainWindow.addLayout(self.vbox_Player)
        #Player Timeline
        self.hbox_PlayTime = QHBoxLayout()
        self.hbox_PlayTime.setSpacing(10)
        self.vbox_Player.addLayout(self.hbox_PlayTime)

        self.lbl_CurrentTime = QLabel('--/--',self.centralwidget)
        self.lbl_CurrentTime.setMinimumSize(QSize(40, 0))
        self.lbl_CurrentTime.setMaximumSize(QSize(100, 16777215))
        self.hbox_PlayTime.addWidget(self.lbl_CurrentTime)

        self.pgb_CurrentTime = QProgressBar(self.centralwidget)
        self.pgb_CurrentTime.setMaximumSize(QSize(16777215, 10))
        self.pgb_CurrentTime.setStyleSheet(u"QProgressBar {background-color:#D5D8DC; border:1px solid grey; border-radius:5px;}\nQProgressBar::chunk {background-color: #05B8CC; width: 20px;}")
        #self.pgb_CurrentTime.setValue(24)
        self.pgb_CurrentTime.setTextVisible(False)
        self.hbox_PlayTime.addWidget(self.pgb_CurrentTime)

        self.lbl_MediaTime = QLabel('--/--',self.centralwidget)
        self.lbl_MediaTime.setMinimumSize(QSize(40, 0))
        self.lbl_MediaTime.setMaximumSize(QSize(100, 16777215))
        self.hbox_PlayTime.addWidget(self.lbl_MediaTime)
        #Player Control Buttons
        self.hbox_PlayerControl = QHBoxLayout()
        self.hbox_PlayerControl.setSpacing(20)
        self.hbox_PlayerControl.setContentsMargins(20,10,20,0)
        #self.hbox_PlayerControl.setSizeConstraint(QLayout.SetFixedSize)

        self.vbox_Player.addLayout(self.hbox_PlayerControl)

        self.btn_Play = QPushButton(self.centralwidget)
        self.btn_Play.setMinimumSize(QSize(40, 40))
        icon3 = QIcon();icon3.addFile(u":/icons/play.png", QSize(), QIcon.Normal, QIcon.Off);icon3.addFile(u":/icons/pause.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_Play.setIcon(icon3)
        self.btn_Play.setIconSize(QSize(25, 25))
        self.btn_Play.setCheckable(True)
        self.btn_Play.setStyleSheet("""
            QPushButton{border:none;border-radius:20px;padding-left:10px}
            QPushButton:hover{background-color:#5499C7}
            QPushButton:checked{padding-left:0px;background-color:#ccff99}
            """)
        self.hbox_PlayerControl.addWidget(self.btn_Play)

        self.btn_RW = QPushButton(self.centralwidget)
        self.btn_RW.setMinimumSize(QSize(40, 40))
        icon4 = QIcon();icon4.addFile(u":/icons/rewind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_RW.setIcon(icon4)
        self.btn_RW.setStyleSheet("""
            QPushButton{border:none;border-radius:20px;}
            QPushButton:hover{background-color:#7DCEA0}
            """)
        self.hbox_PlayerControl.addWidget(self.btn_RW)

        self.btn_Stop = QPushButton(self.centralwidget)
        self.btn_Stop.setMinimumSize(QSize(40, 40))
        icon5 = QIcon();icon5.addFile(u":/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Stop.setIcon(icon5)
        self.btn_Stop.setStyleSheet("""
            QPushButton{border:none;border-radius:20px}
            QPushButton:hover{background-color:#C0392B}
            """)
        self.hbox_PlayerControl.addWidget(self.btn_Stop)

        self.btn_FF = QPushButton(self.centralwidget)
        self.btn_FF.setMinimumSize(QSize(40, 40))
        icon6 = QIcon();icon6.addFile(u":/icons/FF.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_FF.setIcon(icon6)
        self.btn_FF.setStyleSheet("""
            QPushButton{border:none;border-radius:20px}
            QPushButton:hover{background-color:#A569BD}
            """)
        self.hbox_PlayerControl.addWidget(self.btn_FF)

        self.btn_Loop = QPushButton(self.centralwidget)
        self.btn_Loop.setMinimumSize(QSize(40, 40))
        icon7 = QIcon();icon7.addFile(u":/icons/loop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Loop.setIcon(icon7)
        self.btn_Loop.setCheckable(True)
        self.btn_Loop.setStyleSheet("""
            QPushButton{border:none;border-radius:20px}
            QPushButton:hover{background-color:#5F6A6A}
            QPushButton:checked{padding-left:0px;background-color:#839192}
            """)
        self.hbox_PlayerControl.addWidget(self.btn_Loop)

        self.hline_4 = QFrame(self.centralwidget)
        self.hline_4.setFrameShape(QFrame.VLine)
        self.hline_4.setFrameShadow(QFrame.Sunken)
        self.hbox_PlayerControl.addWidget(self.hline_4)

        self.lbl_Volume = QLabel(self.centralwidget)
        self.lbl_Volume.setMaximumSize(QSize(25, 25))
        self.lbl_Volume.setPixmap(QPixmap(u":/icons/adjust.png"))
        self.lbl_Volume.setScaledContents(True)
        self.hbox_PlayerControl.addWidget(self.lbl_Volume)

        self.Sld_Vol = QSlider(self.centralwidget)
        self.Sld_Vol.setMaximumSize(QSize(300, 16777215))
        self.Sld_Vol.setStyleSheet(u"QSlider::handle:horizontal {background-color: #05B8CC;border: 1px solid #5c5c5c;width: 18px;margin: -2px 0;border-radius: 5px;}")
        self.Sld_Vol.setMaximum(100)
        self.Sld_Vol.setOrientation(Qt.Horizontal)
        #self.Sld_Vol.setValue(100)
        self.hbox_PlayerControl.addWidget(self.Sld_Vol)

        self.lbl_Vol_Value = QLabel('100%',self.centralwidget)
        self.lbl_Vol_Value.setMinimumSize(QSize(30, 0))
        self.lbl_Vol_Value.setMaximumSize(QSize(50, 16777215))
        self.lbl_Vol_Value.setFont(font_12)
        self.lbl_Vol_Value.setAlignment(Qt.AlignCenter)
        self.hbox_PlayerControl.addWidget(self.lbl_Vol_Value)        

        self.gridLayout.addLayout(self.vbox_MainWindow, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

############################################################# End UI ############################################################
    #Page Change
    def stacked_Wiget_Page_Change(self, pageNum):
        self.stackedWidget.setCurrentIndex(pageNum)

    #Select booth
    def set_Booth_Index(self, index):
        self.setup['boothNum'] = index + 10
        self.set_ButtonName()
        self.setup_file_save()
    #Audio Device List Retrun
    def audio_Device_Refrash(self):
        self.cb_AudioDevice.clear()
        self.auidodevice_call.emit()
        self.audioDevice_Change.emit(0)

    @pyqtSlot(list)
    def audio_devices(self, devicelist):
        for i in range(len(devicelist)):
            self.cb_AudioDevice.addItem(devicelist[i])
        
    @pyqtSlot(int)
    def set_Audio_Device(self,id):
        self.audioDevice_Change.emit(id)
        self.setup['audioDeviceId'] = id
        self.setup_file_save()

    #Set Button Name
    def set_ButtonName(self):
        for i in range(66):
            zonestate_index = self.zone_status[i+1]
            if 'zone_name_{}'.format(i+1) in self.setup:
                self.zone_Buttons[i].setText('{}\n-{}-'.format(self.setup['zone_name_{}'.format(i+1)],self.zone_state[zonestate_index]))
                if zonestate_index == 0:
                    self.zone_Buttons[i].setStyleSheet(self.btn_style_nomal)
                elif zonestate_index == self.setup['boothNum']-9:
                    self.zone_Buttons[i].setStyleSheet(self.btn_style_self)
                else:
                    self.zone_Buttons[i].setStyleSheet(self.btn_style_checked)

    #Play List
    def addList(self):
        files = QFileDialog.getOpenFileNames(self, 'Select one or more files to open', '', 'Sound (*.mp3 *.wav *.ogg *.flac *.wma)')
        cnt = len(files[0])
        row = len(self.playlist)

        for i in range(row, row+cnt):
            self.playlist.append(files[0][i-row])
        self.tw_Playlist.setRowCount(len(self.playlist))

        for i in range(len(self.playlist)):
            self.tw_Playlist.setItem(i,0, QTableWidgetItem(os.path.basename(self.playlist[i])))

        self.tw_Playlist.selectRow(0)
        self.playIndex = 0

    def delList(self):
        row = self.tw_Playlist.rowCount()
        index = []
        for item in self.tw_Playlist.selectedIndexes():
            index.append(item.row())
        index = list(set(index))
        index.reverse()
        for i in index:
            del self.playlist[i]
        self.tw_Playlist.setRowCount(len(self.playlist))
        for i in range(len(self.playlist)):
            self.tw_Playlist.setItem(i,0, QTableWidgetItem(os.path.basename(self.playlist[i])))

    def select_Playlist_row(self, row, colum):
        self.playIndex = row

    def doubleClick_Playlist(self, row, colum):
        if self.btn_Play.isChecked == True:
            self.play_audio(0)
            time.sleep(1)
        self.playIndex = row
        self.btn_Play.setChecked(True)
        self.play_audio(1)
    #Play time return
    def format_time(self, milliseconds):
        self.position = milliseconds / 1000
        m, s = divmod(self.position, 60)
        h, m = divmod(m, 60)
        return ("%02d/%02d" % (m, s))
    #Audio Play
    def play_audio(self, index):
        if index == 0:
            self.stop.emit()
            self.statusbar.clearMessage()
            
        elif index == 1:
            self.audioDevice_Change.emit(self.setup['audioDeviceId'])           
            if self.btn_Play.isChecked() == True:
                try:
                    self.zone_list = []
                    for i in range(len(self.zone_Buttons)):
                        if self.zone_Buttons[i].isChecked():
                            self.zone_list.append(i+1)
                    overlap_zone_name = self.find_zone_overlap(self.zone_list)
                    if overlap_zone_name:
                        self.dialog_Message.setWindowTitle('이벤트 방송')
                        self.dialog_Message.Qui.lbl_Message.setText('방송구간 중복으로 방송이 중단됩니다.')
                        self.dialog_Message.Qui.lbl_Message_Zone.setText(','.join(overlap_zone_name))
                        self.dialog_Message.show()
                        start_new_thread(self.log_server_call,('0, {}부스 방송구간 중복으로 이벤트 방송이 실행되지 않았습니다. -{}-'.format(self.setup['boothNum']-9,','.join(overlap_zone_name)),))
                        start_new_thread(self.popup_close,(5,))
                        self.zone_list = []
                        self.btn_Play.setChecked(False)
                    else:
                        if self.playlist:                            
                            broadcast_zone=[]
                            broadcast_zone_name=[]
                            for n in range(len(self.zone_list)):
                                broadcast_zone.append('{}:{}'.format(self.zone_list[n],self.setup['boothNum']))
                                broadcast_zone_name.append(self.setup['zone_name_{}'.format(self.zone_list[n])])
                            if broadcast_zone:
                                start_new_thread(self.server_call,('t:onair,{},!'.format(','.join(broadcast_zone)),))
                            #start_new_thread(self.log_server_call,('0, {}부스 이벤트 방송 실행. -{}-'.format(self.setup['boothNum']-9,','.join(broadcast_zone_name)),))
                            time.sleep(1)
                            self.play.emit(self.playlist[self.playIndex])
                            self.tw_Playlist.selectRow(self.playIndex)
                            self.btn_Play.setChecked(True)
                            self.statusbar.showMessage(self.tw_Playlist.item(self.playIndex,0).text())
                        else:
                            self.Play_Button_Status = 0
                            self.btn_Play.setChecked(False)
                            self.addList()
                except:
                    self.stop.emit()
                    self.Play_Button_Status = 0
                    self.btn_Play.setChecked(False)
                    self.statusBar().showMessage('Player에 문제가 발생하여 파일을 재생할 수 없습니다.',5000)
                    start_new_thread(self.log_server_call,('0, {}부스 Player에 문제가 발생하여 파일을 재생할 수 없습니다.'.format(self.setup['boothNum']-9),))
            else:
                print('else')
                self.pause.emit()
        elif index == 2:
            self.statusbar.clearMessage()
            self.stop.emit()
            if self.playIndex > 1:
                self.playIndex -= 1
            self.tw_Playlist.selectRow(self.playIndex)
        elif index == 3:
            self.statusbar.clearMessage()
            self.stop.emit()
            if self.playIndex >= self.tw_Playlist.rowCount()-1:
                self.playIndex = 0
            else:
                self.playIndex += 1
            self.tw_Playlist.selectRow(self.playIndex)
            
        elif index == 4:
            loop = self.btn_Loop.isChecked()
            playlistplay = self.btn_PlaylistPlay.isChecked()
            if loop == True and playlistplay == False:
                self.playLoop = 1
            elif loop == False and playlistplay == True:
                self.playLoop = 2
            elif loop == True and playlistplay == True:
                self.playLoop = 3
            else:
                self.playLoop = 0
    #Audio Vol Set
    def vol_Set(self,volValue):
        self.set_vol.emit(volValue)
        self.setup['vol'] = volValue
        self.setup_file_save()

    def play_next(self):
        if self.playIndex >= self.tw_Playlist.rowCount()-1:
            self.playIndex = 0
        else:
            self.playIndex += 1
        self.statusbar.clearMessage()
        self.tw_Playlist.selectRow(self.playIndex)
        self.play.emit(self.playlist[self.playIndex])
        self.statusbar.showMessage(self.tw_Playlist.item(self.playIndex,0).text())

    def song_length(value):
        self.lbl_MediaTime.setText(self.format_time(value))
        self.media_length = value

    #Player Callback
    @pyqtSlot(str, int)
    def player_state_change(self, key, value):
        #파일길이
        if key == 'length':
            self.lbl_MediaTime.setText(self.format_time(value))
            self.media_length = value
        #현재 시간
        elif  key == 'current_time':
            self.lbl_CurrentTime.setText(self.format_time(value))
            self.pgb_CurrentTime.setValue(math.ceil(value/self.media_length*100))
        #정지
        elif key == 'stop' and value == 1:
            loop = self.btn_Loop.isChecked()
            playlistplay = self.btn_PlaylistPlay.isChecked()
            if loop == True and playlistplay == False:
                self.playLoop = 1
            elif loop == False and playlistplay == True:
                self.playLoop = 2
            elif loop == True and playlistplay == True:
                self.playLoop = 3
            else:
                self.playLoop = 0

            if self.playLoop == 1:                
                self.play.emit(self.playlist[self.playIndex])
                self.statusbar.showMessage(self.tw_Playlist.item(self.playIndex,0).text())
            elif self.playLoop == 2:
                if self.playIndex == self.tw_Playlist.rowCount():
                    #self.play_audio(0)
                    self.song_finished()
                else:
                    self.play_next()
            elif self.playLoop == 3:
                self.play_next()
            else:
                self.lbl_MediaTime.setText('--/--')
                self.lbl_CurrentTime.setText('--/--')
                self.pgb_CurrentTime.setValue(0)
                self.btn_Play.setChecked(False)
                self.statusbar.clearMessage()
                self.song_finished()
                start_new_thread(self.log_server_call,('0, {}번 이벤트 플레이어 방송이 종료되었습니다.'.format(self.setup['boothNum']-9),))
        elif key == 'stop' and value == 0:
            self.Play_Button_Status = 0
            self.lbl_MediaTime.setText('--/--')
            self.lbl_CurrentTime.setText('--/--')
            self.pgb_CurrentTime.setValue(0)
            self.btn_Play.setChecked(False)
            self.statusbar.clearMessage()
            self.song_finished()
            start_new_thread(self.log_server_call,('0, {}번 이벤트 플레이어 방송을 정지 하였습니다.'.format(self.setup['boothNum']-9),))
        #볼륨
        elif key == 'vol':
            self.Sld_Vol.setValue(value)

    def server_ip_setup(self):
        self.setup['serverip'] = self.le_Serverip.text()
        self.setup['serverport'] = int(self.le_Serverport.text())
        self.setup_file_save()

    #Udp Mulicast Callback
    def server_data_parcing(self, data):
        print(data)
        """
        if data == 'c0{}'.format(self.setup['boothNum']-9):
            self.chimeplay.emit('chime.wav')
        """

        recv_data = data.split(',')
        for i in range(len(recv_data)):
            try:
                key,value = recv_data[i].split(':')
            except:
                pass
            try:
                self.zone_status[int(key)]=int(value)
            except:
                pass
        self.set_ButtonName()

    #Udp Send Data
    def log_server_call(self, data):
        try:
            udp_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_sender.sendto((data).encode('cp949'),self.logserver)
            udp_sender.close()
        except:
            self.statusBar().showMessage('네트워크가 활성화 되지 않았습니다.',5000)
    #Log Server Call
    def server_call(self, data):
        try:
            udp_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_sender.sendto((data).encode(),(self.setup['serverip'],self.setup['serverport']))
            print(data, self.setup['serverip'],self.setup['serverport'])
            udp_sender.close()
        except:
            self.statusBar().showMessage('네트워크가 활성화 되지 않았습니다.',5000)

    def setup_file_save(self):
        with open('setup.json','w') as file:
            json.dump(self.setup,file,ensure_ascii=False)

    def setup_file_road(self):
        with open('setup.json','r') as file:
            self.setup = json.load(file)
            #setup = json.dumps(json_setup)
        for i in range(15):
            if 'schedule_file_{}'.format(i) in self.setup:
                self.schedule_List[i][1].setText(self.setup['schedule_file_{}'.format(i)])
            if 'schedule_zone_{}'.format(i) in self.setup:
                self.schedule_List[i][3].setText(self.setup['schedule_zone_{}'.format(i)])
            if 'schedule_days_{}'.format(i) in self.setup:
                self.schedule_List[i][5].setCurrentIndex(self.setup['schedule_days_{}'.format(i)])
            if 'schedule_time_{}'.format(i) in self.setup:
                times = self.setup['schedule_time_{}'.format(i)].split(',')
                self.schedule_List[i][6].setTime(QTime(int(times[0]),int(times[1]),int(times[2])))
            if 'schedule_act_{}'.format(i) in self.setup:
                self.schedule_List[i][7].setChecked(self.setup['schedule_act_{}'.format(i)])

    #Scheduler
    @pyqtSlot(int)
    def schedule_file_load(self, index):
        file = QFileDialog.getOpenFileName(self, 'Select one or more files to open', '', 'Sound (*.mp3 *.wav *.ogg *.flac *.wma)')
        self.schedule_List[index][1].setText(file[0])
        self.setup['schedule_file_{}'.format(index)] = file[0]
        self.setup_file_save()

    @pyqtSlot(int)
    def schedule_zone_sel(self, index):
        select_zone = []
        for i in range(66):
            if 'zone_name_{}'.format(i+1) in self.setup:
                self.dialog.Qui.btn_zone_sel[i].setText(self.setup['zone_name_{}'.format(i+1)])
            self.dialog.Qui.btn_zone_sel[i].setChecked(False)

        selected_zone = self.schedule_List[index][3].text().split(',')
        for i in range(len(selected_zone)):
            select_zone = [item for item, value in self.setup.items() if value == selected_zone[i]]
            if 'zone_name_' in select_zone[0] and select_zone[0] in self.setup:
                self.dialog.Qui.btn_zone_sel[int((re.findall('\d+', select_zone[0]))[0])-1].setChecked(True)

        if self.dialog.exec_():
            select_zone=[]
            for i in range(len(self.dialog.Qui.btn_zone_sel)):
                if self.dialog.Qui.btn_zone_sel[i].isChecked():
                    select_zone.append(self.setup['zone_name_{}'.format(i+1)])
            if len(select_zone) == 0:
                select_zone_txt = ""
            else:
                select_zone_txt = ','.join(select_zone)
            self.schedule_List[index][3].setText(select_zone_txt)
            self.setup['schedule_zone_{}'.format(index)] = (select_zone_txt)
            self.setup_file_save()

    @pyqtSlot(int)
    def schedule_List_del(self, i):
        self.schedule_List[i][1].setText("")
        self.schedule_List[i][3].setText("")
        self.schedule_List[i][5].setCurrentIndex(0)
        self.schedule_List[i][6].setTime(QTime(0,0,0))
        self.schedule_List[i][7].setChecked(False)

        self.setup['schedule_file_{}'.format(i)] = ""
        self.setup['schedule_zone_{}'.format(i)] = ""
        self.setup['schedule_days_{}'.format(i)] = 0
        self.setup['schedule_time_{}'.format(i)] = '0,0,0'
        self.setup['schedule_act_{}'.format(i)] = False
        self.setup_file_save()

    @pyqtSlot(int)
    def schedule_copy(self, index):
        if self.copy_ID == 99:
            self.copy_ID = index
            self.schedule_List[index][9].setStyleSheet("QPushButton{border:none;border-radius:15px;background-color:#18A9B4}")
        else:
            self.schedule_List[index][1].setText(self.schedule_List[self.copy_ID][1].text())
            self.schedule_List[index][3].setText(self.schedule_List[self.copy_ID][3].text())
            self.schedule_List[index][5].setCurrentIndex(self.schedule_List[self.copy_ID][5].currentIndex())
            self.schedule_List[index][6].setTime(self.schedule_List[self.copy_ID][6].time())
            self.schedule_List[index][7].setChecked(self.schedule_List[self.copy_ID][7].isChecked())
            self.setup['schedule_file_{}'.format(index)] = self.schedule_List[self.copy_ID][1].text()
            self.setup['schedule_zone_{}'.format(index)] = self.schedule_List[self.copy_ID][3].text()
            self.setup['schedule_days_{}'.format(index)] = self.schedule_List[self.copy_ID][5].currentIndex()
            self.setup['schedule_time_{}'.format(index)] = ('{},{},{}'.format(self.schedule_List[index][6].time().hour(),self.schedule_List[index][6].time().minute(),self.schedule_List[index][6].time().second()))
            self.setup['schedule_act_{}'.format(index)] = self.schedule_List[self.copy_ID][7].isChecked()
            self.setup_file_save()
            self.copy_ID = 99        
            for i in range(15):
                self.schedule_List[i][9].setStyleSheet(self.btn_style_nomal)

    def schedule_value_change(self):
        for i in range(15):
            self.setup['schedule_days_{}'.format(i)] = self.schedule_List[i][5].currentIndex()
            self.setup['schedule_time_{}'.format(i)] = ('{},{},{}'.format(self.schedule_List[i][6].time().hour(),self.schedule_List[i][6].time().minute(),self.schedule_List[i][6].time().second()))
            self.setup['schedule_act_{}'.format(i)] = self.schedule_List[i][7].isChecked()
        self.setup_file_save()

    @pyqtSlot(int,int)
    def schedule_parcing(self, hour, minute):
        self.playLoop = 0
        for i in range(15):
            if self.schedule_List[i][7].isChecked():
                if self.schedule_List[i][6].time().hour() == hour and self.schedule_List[i][6].time().minute() == minute:
                    dt = datetime.datetime.now().weekday()
                    combobox_index = self.schedule_List[i][5].currentIndex()
                    for n in range(len(self.days_value[combobox_index])):
                        if self.days_value[combobox_index][n] == dt:
                            if self.btn_Play.isChecked() == False:
                                self.zone_list = self.schedule_zone_check(i)
                                overlap_zone_name = self.find_zone_overlap(self.zone_list)
                                #방송구간 중복 확인
                                if overlap_zone_name:
                                    self.dialog_Message.setWindowTitle('스케줄 방송')
                                    self.dialog_Message.Qui.lbl_Message.setText('방송구간 중복으로 스케쥴 방송이 중단됩니다.')
                                    self.dialog_Message.Qui.lbl_Message_Zone.setText(','.join(overlap_zone_name))
                                    self.dialog_Message.show()
                                    start_new_thread(self.popup_close,(5,))
                                    start_new_thread(self.log_server_call,('0, {}부스 방송구간 중복으로 {}번 스케줄 방송이 실행되지 않았습니다. -{}-'.format(self.setup['boothNum']-9,i+1,','.join(overlap_zone_name)),))
                                else:
                                    if os.path.isfile(self.schedule_List[i][1].text()):
                                        broadcast_zone=[]
                                        broadcast_zone_name=[]
                                        for n in range(len(self.zone_list)):
                                            broadcast_zone.append('{}:{}'.format(self.zone_list[n],self.setup['boothNum']))
                                            broadcast_zone_name.append(self.setup['zone_name_{}'.format(self.zone_list[n])])
                                        start_new_thread(self.server_call,('t:onair,{},!'.format(','.join(broadcast_zone)),))
                                        start_new_thread(self.log_server_call,('0, {}부스 이벤트 방송 실행. -{}-'.format(self.setup['boothNum']-9,','.join(broadcast_zone_name)),))

                                        self.dialog_Message.setWindowTitle('스케줄 방송')
                                        self.dialog_Message.Qui.lbl_Message.setText('{}번 스케줄이 실행되었습니다.'.format(i+1))
                                        self.dialog_Message.show()
                                        start_new_thread(self.popup_close,(5,))
                                        #play audio
                                        try:
                                            self.audioDevice_Change.emit(self.setup['audioDeviceId'])
                                            time.sleep(1)
                                            self.Play_Button_Status = 1;
                                            self.play.emit(self.schedule_List[i][1].text())
                                            self.statusbar.showMessage(self.schedule_List[i][1].text())
                                            self.btn_Play.setChecked(True)
                                        except:
                                            self.statusbar.showMessage('플레이어에 문제가 발생했습니다.',5000)
                                            self.Play_Button_Status = 0;
                                            self.btn_Play.setChecked(False)
                                    else:
                                        self.Play_Button_Status = 0;
                                        self.btn_Play.setChecked(False)
                                        self.dialog_Message.setWindowTitle('스케줄 방송')
                                        self.dialog_Message.Qui.lbl_Message.setText('재생 파일 문제로 방송이 실행되지 않았습니다.')
                                        self.dialog_Message.Qui.lbl_Message_Zone.setText(self.schedule_List[i][1].text())
                                        self.dialog_Message.show()
                                        start_new_thread(self.popup_close,(5,))
                                        start_new_thread(self.log_server_call,('0, {}부스 재생 파일 문제로 {}번 스케줄 방송이 실행되지 않았습니다.'.format(self.setup['boothNum']-9,i+1),))
                            else:
                                self.dialog_Message.setWindowTitle('스케줄 방송')
                                self.dialog_Message.Qui.lbl_Message.setText('플레이어가 사용중 입니다.')
                                self.dialog_Message.Qui.lbl_Message_Zone.setText('스케줄 방송이 실행되지 않았습니다.')
                                self.dialog_Message.show()
                                start_new_thread(self.popup_close,(5,))
                                start_new_thread(self.log_server_call,('0, 플레이어가 사용중이어서 {}번 부스 스케줄 방송이 실행되지 않았습니다.'.format(self.setup['boothNum']-9),))


    @pyqtSlot()
    def scheduler_reset(self):
        for i in range(15):
            self.schedule_List[i][1].setText("")
            self.schedule_List[i][3].setText("")
            self.schedule_List[i][5].setCurrentIndex(0)
            self.schedule_List[i][6].setTime(QTime(0,0,0))
            self.schedule_List[i][7].setChecked(False)

            self.setup['schedule_file_{}'.format(i)] = ""
            self.setup['schedule_zone_{}'.format(i)] = ""
            self.setup['schedule_days_{}'.format(i)] = 0
            self.setup['schedule_time_{}'.format(i)] = '0,0,0'
            self.setup['schedule_act_{}'.format(i)] = False
        self.setup_file_save()
        start_new_thread(self.log_server_call,('0, {}번 부스 스케줄이 리셋 되었습니다.'.format(self.setup['boothNum']-9),))

    def popup_close(self,timer):
        time.sleep(timer)
        self.dialog_Message.close()

    def find_zone_overlap(self, zone_list):
        zone_overlap=[]
        zone_overlap_state = False
        for i in range(len(zone_list)):
            if self.zone_status[zone_list[i]] > 0 and self.zone_status[zone_list[i]] != self.setup['boothNum']:
                zone_overlap.append(self.setup['zone_name_{}'.format(zone_list[i])])
        if len(zone_overlap) > 0:
            zone_overlap_state = True
        return (zone_overlap)
    
    def schedule_zone_check(self,index):
        zone_sel_status = []
        schedule_zone_sel = self.schedule_List[index][3].text().split(',')
        for i in range(len(schedule_zone_sel)):
            select_zone = [item for item, value in self.setup.items() if value == schedule_zone_sel[i]]
            if 'zone_name_' in select_zone[0] and select_zone[0] in self.setup:
                zone_sel_status.append(int(re.findall('\d+', select_zone[0])[0]))
        return zone_sel_status

    def song_finished(self):
        if self.zone_list:
            broadcast_zone=[]
            for i in range(len(self.zone_list)):
                broadcast_zone.append('{}:{}'.format(self.zone_list[i],0))
            start_new_thread(self.server_call,('t:onair,{},!'.format(','.join(broadcast_zone)),))
            start_new_thread(self.log_server_call,('0,{} 부스 방송이 종료 되었습니다.'.format(self.setup['boothNum']-9),))
            self.zone_list = []
        #self.auidodevice_call.emit()


############################################################# Audio Player #############################################################

class audioplayer(QThread):
    player_Status = pyqtSignal(str,int)
    audio_devices = pyqtSignal(list)
    def __init__(self, parent = None):
        super(audioplayer, self).__init__(parent)
        self.new_Player()
        
    def new_Player(self):
        self.instance = vlc.Instance()
        self._player = self.instance.media_player_new()
        self.Event_Manager = self._player.event_manager()        
        self.Event_Manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.songFinished)
        self.Event_Manager.event_attach(vlc.EventType.MediaPlayerLengthChanged, self.get_Media_Langth, self._player)
        self.Event_Manager.event_attach(vlc.EventType.MediaPlayerTimeChanged, self.pos_Callback, self._player)

    @pyqtSlot()
    def get_Audio_Devices(self):
        self.devices_name = []
        self.mods = self._player.audio_output_device_enum()
        if self.mods:
            mod = self.mods
            while mod:
                mod = mod.contents
                self.devices_name.append((mod.description).decode())
                mod = mod.next
        print(self.devices_name)
        self.audio_devices.emit(self.devices_name)

    @pyqtSlot(int)
    def set_Audio_Device(self, deviceId):
        self.devices = []
        self.mods = self._player.audio_output_device_enum()
        if self.mods:
            mod = self.mods
            while mod:
                mod = mod.contents
                self.devices.append(mod.device)
                self.devices_name.append((mod.description).decode())
                mod = mod.next
        vlc.libvlc_audio_output_device_list_release(self.mods)
        self._player.audio_output_device_set(None, self.devices[deviceId])

    @pyqtSlot(str)
    def play(self, music):
        if os.path.isfile(music):
            media = self.instance.media_new(music)
            self._player.set_media(media)
            self._player.play()

    @pyqtSlot()
    def pause(self):
        self._player.pause()
    @pyqtSlot()
    def stop(self):
        self.player_Status.emit('stop',0)
        self._player.stop()
        self.new_Player()

    def songFinished(self, evnet):
        self.player_Status.emit('stop',1)

    def pos_Callback(self, time, player):
        self.player_Status.emit('current_time',time.u.new_time)
        #print(time.u.new_time)

    def get_Media_Langth(self, time, player):
        self.player_Status.emit('length',time.u.new_length)

    @pyqtSlot(int)
    def audio_Vol_Set(self, vol):
        self._player.audio_set_volume(vol)

    @pyqtSlot()
    def audio_Vol_Get(self):
        self.player_Status.emit('vol',self._player.audio_get_volume())

class chimeplayer(QThread):
    def __init__(self, parent = None):
        super(chimeplayer, self).__init__(parent)
        self.new_Player()
        
    def new_Player(self):
        self.instance = vlc.Instance()
        self._player = self.instance.media_player_new()
        self.Event_Manager = self._player.event_manager()
        
    @pyqtSlot(str)
    def play(self, music):
        media = self.instance.media_new('chime.wav')
        self._player.set_media(media)
        self._player.play()

class udp_server(QThread):
    udp_data = pyqtSignal(str)
    def __init__(self, parent = None):
        super(udp_server, self).__init__(parent)
        MCAST_GRP = '224.1.128.128'
        MCAST_PORT = 5007
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        try:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except AttributeError:
            pass
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
        self.sock.bind(('', MCAST_PORT))
        host = socket.gethostbyname(socket.gethostname())
        self.sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(host))
        self.sock.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP,socket.inet_aton(MCAST_GRP) + socket.inet_aton(host))

    def run(self):
        while True:
            try:
                data, addr = self.sock.recvfrom(1024)
                self.udp_data.emit(data.decode('utf-8'))
                print('recv_data = {}'.format(data.decode('utf-8')))
            except (socket.error, e):
                print ('Expection')
                hexdata = binascii.hexlify(data)
                print ('Data = %s' % hexdata)

class schedulePlay(QThread):
    Timer_Receive_String = pyqtSignal(int,int)
    def __init__(self, parent = None):
        super(schedulePlay, self).__init__(parent)
        self.tm_min = 0

    def run(self):
        while True:
            self.now = time.localtime(time.time())
            if self.tm_min != self.now.tm_min:
                self.tm_min = self.now.tm_min
                self.Timer_Receive_String.emit(self.now.tm_hour,self.now.tm_min)
            time.sleep(1)

class Dialog_Zone_Sel(object):
    def setupUi(self,Dialog):
        self.btn_style_nomal = ("""
                                QPushButton{border:none;border-radius:15px;background-color:#F8F9F9}
                                QPushButton:checked{color:white;background-color:#566573}
                                QPushButton:hover{background-color:#EBF5FB}
                                QPushButton:checked:hover{color:white;background-color:#1C2833}
                                QPushButton:pressed{color:white;background-color:#503131}
                                QPushButton:checked:pressed{color:white;background-color:#503131}
                                """)
        self.btn_style_ok = ("background-color:#EAECEE")
        font_Label = QFont();font_Label.setFamily(u"NanumBarunGothic");font_Label.setPointSize(14)
        self.btn_zone_sel = ['i']*66
        self.btn_zone_sel_status = [0]*66
        self.popup_btn_grp = QButtonGroup()
        self.popup_btn_grp.setExclusive(False)
        Dialog.resize(600,600)
        Dialog.setWindowTitle("방송 구간 선택")
        Dialog.setStyleSheet("background-color:#f8f9f9")
        
        self.vbox_popup = QVBoxLayout(Dialog)
        self.vbox_popup.setContentsMargins(0,0,0,0)
        self.vbox_popup.setSpacing(10)
        self.lbl_popup_title = QLabel("지점 선택",Dialog)
        self.lbl_popup_title.setMinimumSize(100,30)
        self.lbl_popup_title.setFont(font_Label)
        self.lbl_popup_title.setStyleSheet("background-color:white;padding-left:30px")
        self.vbox_popup.addWidget(self.lbl_popup_title)

        self.gl_popup = QGridLayout()
        self.gl_popup.setContentsMargins(10,0,10,0)
        self.vbox_popup.addLayout(self.gl_popup)
        for i in range(66):
            self.btn_zone_sel[i] = QPushButton("{}".format(i+1), Dialog)
            self.btn_zone_sel[i].setMinimumSize(QSize(0, 40))
            self.btn_zone_sel[i].setMaximumSize(QSize(200, 100))
            self.btn_zone_sel[i].setCheckable(True)
            self.btn_zone_sel[i].setChecked(False)
            self.btn_zone_sel[i].setStyleSheet(self.btn_style_nomal)
            self.popup_btn_grp.addButton(self.btn_zone_sel[i],i)
            self.gl_popup.addWidget(self.btn_zone_sel[i],int(i/6),int(i%6),1,1)

        self.button_box_widget = QWidget(Dialog)
        self.button_box_widget.setStyleSheet("background-color:#ffffff")
        self.vbox_buttonbox = QVBoxLayout(self.button_box_widget)
        self.buttonBox = QDialogButtonBox(self.button_box_widget)
        self.buttonBox.setContentsMargins(0,0,20,0)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setMinimumHeight(40)
        self.buttonBox.setStyleSheet(self.btn_style_ok)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.vbox_buttonbox.addWidget(self.buttonBox)
        self.vbox_popup.addWidget(self.button_box_widget)

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)  

        QMetaObject.connectSlotsByName(Dialog)

class Dialog_Message(object):
    def setupUi(self,Dialog):
        font_Label = QFont();font_Label.setFamily(u"NanumBarunGothic");font_Label.setPointSize(14)
        self.btn_style_ok = ("background-color:#EAECEE")

        Dialog.resize(600,300)
        Dialog.setWindowTitle("이벤트 방송")
        Dialog.setStyleSheet("background-color:#f8f9f9")
        
        self.vbox_popup = QVBoxLayout(Dialog)
        self.vbox_popup.setContentsMargins(0,0,0,0)
        #self.vbox_popup.setSpacing(10)
        self.lbl_popup_title = QLabel("스케쥴 방송",Dialog)
        self.lbl_popup_title.setFont(font_Label)
        self.lbl_popup_title.setMinimumHeight(40)
        self.lbl_popup_title.setMaximumHeight(40)
        self.lbl_popup_title.setStyleSheet("background-color:white;padding-left:30px")
        self.vbox_popup.addWidget(self.lbl_popup_title)

        self.lbl_Message = QLabel(Dialog)
        self.lbl_Message.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
        self.vbox_popup.addWidget(self.lbl_Message)

        self.lbl_Message_Zone= QLabel(Dialog)
        self.lbl_Message_Zone.setAlignment(Qt.AlignCenter|Qt.AlignVCenter)
        self.vbox_popup.addWidget(self.lbl_Message_Zone)

        self.button_box_widget = QWidget(Dialog)
        self.button_box_widget.setStyleSheet("background-color:#ffffff")
        self.vbox_buttonbox = QVBoxLayout(self.button_box_widget)
        self.buttonBox = QDialogButtonBox(self.button_box_widget)
        self.buttonBox.setContentsMargins(0,0,20,0)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setMinimumHeight(20)
        self.buttonBox.setMaximumHeight(40)
        self.buttonBox.setStyleSheet(self.btn_style_ok)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.vbox_buttonbox.addWidget(self.buttonBox)
        self.vbox_popup.addWidget(self.button_box_widget)

        self.buttonBox.accepted.connect(Dialog.accept)
        QMetaObject.connectSlotsByName(Dialog)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
