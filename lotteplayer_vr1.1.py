# -*- coding: utf-8 -*-
import sys, vlc, time, socket, os.path, math, socket, struct, datetime, lotteplayer_rc
from PySide2.QtCore import QCoreApplication, QMetaObject, QObject, Slot, Signal, QSize, Qt, QRect, QThread
from PySide2.QtGui import QFont, QIcon, QPixmap
from PySide2.QtWidgets import *



zone_Name = (['센텀시티','이시아폴리스','상인점','대구점','포항점','아쿠아몰','광복점','광주점','전주점','청주영플라자','대전점','서울역점',
                           '영등포점','중동점','관악점','창원점','창원영패션관','일산점','구리점','평촌점','안산점','미아점','스타시티','노원점',
                           '분당점','잠실점','동래점','청량지점','에비뉴엘','영플라자','본점','강남점','청주아울렛','울산점','김해아울렛','파주아울렛',
                           '서면점','율하점','수완아울렛','광주월드컵점','부여아울렛','이천아울렛','고양터미널','에비뉴엘\n월드타워','수원점','광명점','구리아울렛','동부산점',
                           '마산점','광교아울렛','가산아울렛','진주아울렛','남악아울렛','고양아울렛','군산아울렛','기흥아울렛','인천터미널'])

class Ui_MainWindow(QMainWindow):
    play = Signal(str);pause = Signal();stop = Signal()
    get_vol = Signal();set_vol = Signal(int)
    auidodevice_call = Signal()
    global zone_Name

    def __init__(self):
        super().__init__()       
        
        #Variable
        self.setup = {'serverip':'127.0.0.1','serverport':8888}
        self.booth_Index = 0
        self.zone_status = [0]*66
        self.zone_state = ['대기중','방송중','PC 송출중']
        self.Play_Button_Status = 0
        self.playIndex = 0
        self.playLoop = 0
        self.playlist =[]

        self.dialog = QDialog()
        self.dialog.Qui = Dialog_Zone_Sel()
        self.dialog.Qui.setupUi(self.dialog)


        self.setupUi(self)
        self.setWindowTitle('Audio Player - Port : 12303')

        #Thread Class
        self.audioplayer = audioplayer()
        self.udp_server = udp_server()
        self.schedulePlay = schedulePlay()
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
        
        self.play.connect(self.audioplayer.play)
        self.pause.connect(self.audioplayer.pause)
        self.stop.connect(self.audioplayer.stop)
        self.auidodevice_call.connect(self.audioplayer.get_Audio_Devices)
        self.get_vol.connect(self.audioplayer.audio_Vol_Get)
        self.set_vol.connect(self.audioplayer.audio_Vol_Set)

        self.cb_AudioDevice.currentIndexChanged.connect(self.audioplayer.set_Audio_Device)
        self.cb_Booth.currentIndexChanged.connect(self.set_Booth_Index)

        self.audioplayer.player_Status.connect(self.player_state_change)
        self.audioplayer.audio_devices.connect(self.audio_devices)

        self.udp_server.udp_data.connect(self.server_data_parcing)

        self.schedule_file_btn_grp.buttonClicked[int].connect(self.schedule_file_load)
        self.schedule_zone_sel_grp.buttonClicked[int].connect(self.schedule_zone_sel)

        self.schedulePlay.Timer_Receive_String.connect(self.schedule_parcing)
        self.show()

        #Thread Start
        self.udp_server.start()
        self.schedulePlay.start()
        self.auidodevice_call.emit()
        self.get_vol.emit()
        self.set_ButtonName()

    def setupUi(self, MainWindow):
        font_Label = QFont();font_Label.setFamily(u"NanumBarunGothic");font_Label.setPointSize(14)
        font_10 = QFont();font_10.setPointSize(10)
        font_12 = QFont();font_12.setFamily(u"NanumBarunGothic");font_12.setPointSize(12)

    #Main Windwos
        MainWindow.resize(1280, 800)
        self.centralwidget = QWidget(MainWindow)
        self.gridLayout = QGridLayout(self.centralwidget)

        self.hline_5 = QFrame(self.centralwidget)
        self.hline_5.setFrameShape(QFrame.HLine)
        self.hline_5.setFrameShadow(QFrame.Sunken)
        self.gridLayout.addWidget(self.hline_5, 1, 0, 1, 1)
    #Main Window Vbox Layout
        self.vbox_MainWindow = QVBoxLayout()
    #1st Line
        self.hbox_Booth = QHBoxLayout()
        #Player Stacked Sel Button
        self.btn_Tab_Player = QPushButton('Player',self.centralwidget)
        self.btn_Tab_Player.setMinimumSize(QSize(0, 30))
        self.btn_Tab_Player.setMaximumSize(QSize(100, 16777215))
        self.hbox_Booth.addWidget(self.btn_Tab_Player)
        #Scheduler Stacked Sel Button
        self.btn_Tab_Schduler = QPushButton('Scheduler',self.centralwidget)
        self.btn_Tab_Schduler.setMinimumSize(QSize(0, 30))
        self.btn_Tab_Schduler.setMaximumSize(QSize(100, 16777215))
        self.hbox_Booth.addWidget(self.btn_Tab_Schduler)

        self.vline_1 = QFrame(self.centralwidget)
        self.vline_1.setFrameShape(QFrame.VLine)
        self.vline_1.setFrameShadow(QFrame.Sunken)
        self.hbox_Booth.addWidget(self.vline_1)
        #Booth Sel
        self.lbl_Booth = QLabel('부스 선택',self.centralwidget)
        self.lbl_Booth.setMinimumSize(QSize(0, 30))
        self.lbl_Booth.setMaximumSize(QSize(60, 16777215))
        self.lbl_Booth.setFont(font_10)
        self.hbox_Booth.addWidget(self.lbl_Booth)

        self.cb_Booth = QComboBox(self.centralwidget)
        self.cb_Booth.setFont(font_10)
        for i in range(9):
            self.cb_Booth.addItem('Booth {}'.format(i+1))
        self.cb_Booth.setMinimumSize(QSize(0, 30))
        self.cb_Booth.setMaximumSize(QSize(100, 16777215))
        self.hbox_Booth.addWidget(self.cb_Booth)

        self.lbl_blank = QLabel(self.centralwidget)
        self.hbox_Booth.addWidget(self.lbl_blank)

        self.vline_2 = QFrame(self.centralwidget)
        self.vline_2.setFrameShape(QFrame.VLine)
        self.vline_2.setFrameShadow(QFrame.Sunken)
        self.hbox_Booth.addWidget(self.vline_2)
        #Audio Device Sel
        self.lbl_AudioDevice = QLabel('오디오 디바이스 선택',self.centralwidget)
        self.lbl_AudioDevice.setMinimumSize(QSize(120, 30))
        self.lbl_AudioDevice.setMaximumSize(QSize(130, 16777215))
        self.lbl_AudioDevice.setFont(font_10)
        self.hbox_Booth.addWidget(self.lbl_AudioDevice)

        self.cb_AudioDevice = QComboBox(self.centralwidget)
        self.cb_AudioDevice.setMinimumSize(QSize(0, 30))
        self.hbox_Booth.addWidget(self.cb_AudioDevice)
        self.vbox_MainWindow.addLayout(self.hbox_Booth)

        self.btn_Setup = QPushButton(self.centralwidget)
        icon = QIcon();icon.addFile(u":/icons/system.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Setup.setIcon(icon)
        self.btn_Setup.setIconSize(QSize(25, 25))
        self.btn_Setup.setFlat(True)
        self.btn_Setup.setMaximumSize(QSize(30, 16777215))
        self.hbox_Booth.addWidget(self.btn_Setup)

        self.hline_1 = QFrame(self.centralwidget)
        self.hline_1.setFrameShape(QFrame.HLine)
        self.hline_1.setFrameShadow(QFrame.Sunken)
        self.vbox_MainWindow.addWidget(self.hline_1)
    #2nd Line
        #Stack Widget
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        #Stack Page 1
        self.page_1 = QWidget()
        self.gl_Stack_Page_1 = QGridLayout(self.page_1)

    ### Playlist
        #Label Playlist
        self.lbl_PlayList = QLabel('플레이 리스트',self.page_1)
        self.lbl_PlayList.setFont(font_Label)
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
        self.gw_Playlist.addWidget(self.tw_Playlist, 0, 0, 1, 1)
        #hbox Playlist buttons
        self.hbox_Playlist_add_del = QHBoxLayout()
        self.gw_Playlist.addLayout(self.hbox_Playlist_add_del, 2, 0, 1, 1)        

        self.btn_Playlist_Add = QPushButton('Add List',self.page_1)
        icon = QIcon();icon.addFile(u":/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Playlist_Add.setIcon(icon)
        self.btn_Playlist_Add.setIconSize(QSize(25, 25))
        self.hbox_Playlist_add_del.addWidget(self.btn_Playlist_Add)

        self.btn_Playlist_Del = QPushButton('Del List',self.page_1)
        icon1 = QIcon();icon1.addFile(u":/icons/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Playlist_Del.setIcon(icon1)
        self.btn_Playlist_Del.setIconSize(QSize(25, 25))
        self.hbox_Playlist_add_del.addWidget(self.btn_Playlist_Del)
        #Playlist Play Continue
        self.btn_PlaylistPlay = QPushButton('플레이 리스트 연속 재생',self.page_1)
        icon2 = QIcon();icon2.addFile(u":/icons/continue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_PlaylistPlay.setIcon(icon2)
        self.btn_PlaylistPlay.setIconSize(QSize(25, 25))
        self.btn_PlaylistPlay.setCheckable(True)
        self.gw_Playlist.addWidget(self.btn_PlaylistPlay, 3, 0, 1, 1)

        self.hline_3 = QFrame(self.page_1)
        self.hline_3.setFrameShape(QFrame.HLine)
        self.hline_3.setFrameShadow(QFrame.Sunken)
        self.gw_Playlist.addWidget(self.hline_3, 4, 0, 1, 1)
        
    ### Zone Selector
        self.lbl_Zone = QLabel('방송 구간 선택/방송 구간 상태',self.page_1)
        self.lbl_Zone.setFont(font_Label)

        self.gl_Stack_Page_1.addWidget(self.lbl_Zone, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.page_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setSizeIncrement(QSize(1, 2))
        self.scrollArea.setWidgetResizable(True)
        self.gw_Zone_Sel = QWidget()
        self.gw_Zone_Sel.setObjectName(u"gw_Zone_Sel")
        self.gw_Zone_Sel.setGeometry(QRect(0, 0, 498, 908))
        self.gridLayout_ZoneSel = QGridLayout(self.gw_Zone_Sel)
        self.gridLayout_ZoneSel.setObjectName(u"gridLayout_ZoneSel")

        self.zone_Buttons = [str(i) for i in range(66)]

        for i in range(len(self.zone_Buttons)):
            self.zone_Buttons[i] = QPushButton('{}'.format(i+1),self.gw_Zone_Sel)
            self.zone_Buttons[i].setMinimumSize(QSize(0, 40))
            self.zone_Buttons[i].setMaximumSize(QSize(200, 100))
            self.zone_Buttons[i].setCheckable(True)
            self.gridLayout_ZoneSel.addWidget(self.zone_Buttons[i],i/6,i%6,1,1)

        self.scrollArea.setWidget(self.gw_Zone_Sel)

        self.gl_Stack_Page_1.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_1)

        #Stack Page 2
    ### Scheduler
        self.page_2 = QWidget()
        self.stackedWidget.addWidget(self.page_2)

        self.gl_Stack_Page2 = QGridLayout(self.page_2)

        self.vbox_Schedule = QVBoxLayout()
        self.gl_Stack_Page2.addLayout(self.vbox_Schedule, 0, 0, 1, 1)

        self.lbl_Schedule = QLabel('Scheduler',self.page_2)
        self.lbl_Schedule.setFont(font_Label)
        self.vbox_Schedule.addWidget(self.lbl_Schedule)

        self.sa_Schedule = QScrollArea(self.page_2)
        self.sa_Schedule.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 654, 904))
        self.sa_Schedule.setWidget(self.scrollAreaWidgetContents)
        self.vbox_Schedule.addWidget(self.sa_Schedule)

        self.gl_Schedule = QGridLayout(self.scrollAreaWidgetContents)

        self.lbl_Name_1 = QLabel('파일',self.scrollAreaWidgetContents)
        self.lbl_Name_1.setMaximumSize(QSize(1000, 20))
        self.gl_Schedule.addWidget(self.lbl_Name_1, 0, 1, 1, 2)

        self.lbl_Name_2 = QLabel('방송구간',self.scrollAreaWidgetContents)
        self.gl_Schedule.addWidget(self.lbl_Name_2, 0, 3, 1, 2)

        self.lbl_Name_3 = QLabel('요일',self.scrollAreaWidgetContents)
        self.lbl_Name_3.setFixedSize(100,20)
        self.gl_Schedule.addWidget(self.lbl_Name_3, 0, 5, 1, 1)

        self.lbl_Name_4 = QLabel('시간',self.scrollAreaWidgetContents)
        self.lbl_Name_4.setMaximumSize(QSize(100, 20))
        self.gl_Schedule.addWidget(self.lbl_Name_4, 0, 6, 1, 1)

        self.lbl_Name_5 = QLabel('활성화',self.scrollAreaWidgetContents)
        self.lbl_Name_5.setFixedSize(40,20)
        self.gl_Schedule.addWidget(self.lbl_Name_5, 0, 7, 1, 1)

        self.days = ["매일","월~목","금~일","월","화","수","목","금","토","일"]
        self.days_value = [[0,1,2,3,4,5,6],[0,1,2,3,],[4,5,6],[0],[1],[2],[3],[4],[5],[6]]

        self.schedule_List = [['i' for col in range(8)] for row in range(15)]
        self.schedule_Line = ['i']*16

        self.schedule_file_btn_grp = QButtonGroup()
        self.schedule_zone_sel_grp = QButtonGroup()

        for i in range(15):
            self.schedule_List[i][0] = QLabel('{}'.format(i+1),self.scrollAreaWidgetContents)
            self.schedule_List[i][0].setMaximumSize(QSize(15, 100))
            self.schedule_List[i][1] = QLabel("--",self.scrollAreaWidgetContents)
            self.schedule_List[i][1].setWordWrap(True)
            self.schedule_List[i][2] = QPushButton(self.scrollAreaWidgetContents)
            self.schedule_List[i][2].setIcon(icon2)
            self.schedule_List[i][2].setFlat(True)
            self.schedule_List[i][2].setMaximumSize(QSize(20, 100))
            self.schedule_file_btn_grp.addButton(self.schedule_List[i][2], i)
            self.schedule_List[i][3] = QLabel("--", self.scrollAreaWidgetContents)
            self.schedule_List[i][3].setWordWrap(True)
            self.schedule_List[i][4] = QPushButton(self.scrollAreaWidgetContents)
            self.schedule_List[i][4].setIcon(icon2)
            self.schedule_List[i][4].setFlat(True)
            self.schedule_List[i][4].setMaximumSize(QSize(20, 100))
            self.schedule_zone_sel_grp.addButton(self.schedule_List[i][4], i)
            self.schedule_List[i][5] = QComboBox(self.scrollAreaWidgetContents)
            self.schedule_List[i][5].setFixedSize(100,20)
            for day in range(len(self.days)):
                self.schedule_List[i][5].addItem(self.days[day])
            self.schedule_List[i][6] = QTimeEdit(self.scrollAreaWidgetContents)
            self.schedule_List[i][7] = QCheckBox(self.scrollAreaWidgetContents)

        for i in range(16):
        	self.schedule_Line[i] = QFrame(self.scrollAreaWidgetContents)
        	self.schedule_Line[i].setFrameShape(QFrame.HLine)
        	self.schedule_Line[i].setFrameShadow(QFrame.Sunken)
        t=0
        q=0

        for i in range(2,33):
        	if i%2 == 1:
        		for j in range(8):
        			if j == 7:
        				self.gl_Schedule.addWidget(self.schedule_List[t][j], i,j,1,1,Qt.AlignHCenter)
        			else:
        				self.gl_Schedule.addWidget(self.schedule_List[t][j], i,j,1,1)
        		t += 1
        	else:
        		self.gl_Schedule.addWidget(self.schedule_Line[q], i,0,1,8)
        		q += 1

        self.btn_schedule_Reset = QPushButton('Reset', self.page_2)
        self.vbox_Schedule.addWidget(self.btn_schedule_Reset)

    #Setup Page
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

        self.hline_2 = QFrame(self.centralwidget)
        self.hline_2.setFrameShape(QFrame.HLine)
        self.hline_2.setFrameShadow(QFrame.Sunken)
        self.vbox_MainWindow.addWidget(self.hline_2)
    #3rd Line
    ###Player Control
        self.vbox_Player = QVBoxLayout()
        self.vbox_MainWindow.addLayout(self.vbox_Player)
        #Player Timeline
        self.hbox_PlayTime = QHBoxLayout()
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
        self.hbox_PlayerControl.setSizeConstraint(QLayout.SetFixedSize)

        self.vbox_Player.addLayout(self.hbox_PlayerControl)

        self.btn_Play = QPushButton(self.centralwidget)
        self.btn_Play.setMinimumSize(QSize(40, 40))
        icon3 = QIcon();icon3.addFile(u":/icons/play.png", QSize(), QIcon.Normal, QIcon.Off);icon3.addFile(u":/icons/pause.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_Play.setIcon(icon3)
        self.btn_Play.setIconSize(QSize(25, 25))
        self.btn_Play.setCheckable(True)
        self.hbox_PlayerControl.addWidget(self.btn_Play)

        self.btn_RW = QPushButton(self.centralwidget)
        self.btn_RW.setMinimumSize(QSize(30, 30))
        icon4 = QIcon();icon4.addFile(u":/icons/rewind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_RW.setIcon(icon4)
        self.hbox_PlayerControl.addWidget(self.btn_RW)

        self.btn_Stop = QPushButton(self.centralwidget)
        self.btn_Stop.setMinimumSize(QSize(30, 30))
        icon5 = QIcon();icon5.addFile(u":/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Stop.setIcon(icon5)

        self.hbox_PlayerControl.addWidget(self.btn_Stop)

        self.btn_FF = QPushButton(self.centralwidget)
        self.btn_FF.setMinimumSize(QSize(30, 30))
        icon6 = QIcon();icon6.addFile(u":/icons/FF.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_FF.setIcon(icon6)

        self.hbox_PlayerControl.addWidget(self.btn_FF)

        self.btn_Loop = QPushButton(self.centralwidget)
        self.btn_Loop.setMinimumSize(QSize(30, 30))
        icon7 = QIcon();icon7.addFile(u":/icons/loop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Loop.setIcon(icon7)
        self.btn_Loop.setCheckable(True)
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

    ######################################################### End UI #########################################################

    def stacked_Wiget_Page_Change(self, pageNum):
        self.stackedWidget.setCurrentIndex(pageNum)

    def set_Booth_Index(self, index):
        self.booth_Index = index

    def set_ButtonName(self):
        for i in range(len(zone_Name)):
            zonestate_index = self.zone_status[i]
            self.zone_Buttons[i].setText('{}\n-{}-'.format(zone_Name[i],self.zone_state[zonestate_index]))
            if zonestate_index == 0:
                self.zone_Buttons[i].setStyleSheet("QPushButton{color:black;}")
            else:
                self.zone_Buttons[i].setStyleSheet("QPushButton{color:red;}")

    def play_audio(self, index):
        if index == 0:
            self.stop.emit()
            self.statusbar.clearMessage()
        elif index == 1:            
            if self.Play_Button_Status == 0:
                self.Play_Button_Status = 1
                print(self.playIndex)
                try:
                    self.play.emit(self.playlist[self.playIndex])
                    self.statusbar.showMessage(self.tw_Playlist.item(self.playIndex,0).text())
                    self.tw_Playlist.selectRow(self.playIndex)
                    self.btn_Play.setChecked(True)
                except:
                    self.addList()
                    self.Play_Button_Status = 0;
                    self.btn_Play.setChecked(False)
            else:
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
        self.play_audio(0)
        self.playIndex = row
        self.play_audio(1)

    def format_time(self, milliseconds):
        self.position = milliseconds / 1000
        m, s = divmod(self.position, 60)
        h, m = divmod(m, 60)
        return ("%02d/%02d" % (m, s))

    @Slot(str, int)
    def player_state_change(self, key, value):
        if key == 'length':
            self.lbl_MediaTime.setText(self.format_time(value))
            self.media_length = value
        elif  key == 'current_time':
            self.lbl_CurrentTime.setText(self.format_time(value))
            self.pgb_CurrentTime.setValue(math.ceil(value/self.media_length*100))
        elif key == 'stop' and value == 1:
            self.Play_Button_Status = 0
            if self.playLoop == 1:
                self.play_audio(1)
            elif self.playLoop == 2:
                if self.playIndex == self.tw_Playlist.rowCount():
                    self.play_audio(0)
                else:
                    self.play_audio(3)
                    self.play_audio(1)
            elif self.playLoop == 3:
                self.play_audio(3)
                self.play_audio(1)
            else:
                self.lbl_MediaTime.setText('--/--')
                self.lbl_CurrentTime.setText('--/--')
                self.pgb_CurrentTime.setValue(0)
                self.btn_Play.setChecked(False)
                self.statusbar.clearMessage()
        elif key == 'stop' and value == 0:
            self.Play_Button_Status = 0
            self.lbl_MediaTime.setText('--/--')
            self.lbl_CurrentTime.setText('--/--')
            self.pgb_CurrentTime.setValue(0)
            self.btn_Play.setChecked(False)
            self.statusbar.clearMessage()

        elif key == 'vol':
            self.Sld_Vol.setValue(value)

    @Slot()
    def audio_devices(self, devicelist):
        for i in range(len(devicelist)):
            self.cb_AudioDevice.addItem(devicelist[i])

    def vol_Set(self,volValue):
        self.set_vol.emit(volValue)

    def server_data_parcing(self, data):
        print (data)

    @Slot()
    def schedule_file_load(self, index):
        file = QFileDialog.getOpenFileName(self, 'Select one or more files to open', '', 'Sound (*.mp3 *.wav *.ogg *.flac *.wma)')
        self.schedule_List[index][1].setText(file[0])
    
    @Slot()
    def schedule_zone_sel(self, index):
        print("Zone sel index {}".format(index))
        if self.dialog.exec_():
            self.sel_zone=[]
            print(self.dialog.Qui.btn_zone_sel_status)
            for i in range(len(self.dialog.Qui.btn_zone_sel_status)):
                if self.dialog.Qui.btn_zone_sel_status[i] == 1:
                    self.sel_zone.append(zone_Name[i])
            self.schedule_List[index][3].setText(','.join(self.sel_zone))
    
    @Slot(int,int)
    def schedule_parcing(self,hour, minute):
        for i in range(15):
            if self.schedule_List[i][6].time().hour() == hour and self.schedule_List[i][6].time().minute() == minute:
                dt = datetime.datetime.now().weekday()
                combobox_index = self.schedule_List[i][5].currentIndex()
                print(len(self.days_value[combobox_index]))
                for i in range(len(self.days_value[combobox_index])):
                    if self.days_value[combobox_index][i] == dt:
                        print('weekday = {}'.format(dt))







############################################################# Audio Player #############################################################

class audioplayer(QThread):
    player_Status = Signal(str,int)
    audio_devices = Signal(list)
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

    @Slot()
    def get_Audio_Devices(self):
        self.devices_name = []
        self.mods = self._player.audio_output_device_enum()
        if self.mods:
            mod = self.mods
            while mod:
                mod = mod.contents
                self.devices_name.append((mod.description).decode())
                mod = mod.next
        self.audio_devices.emit(self.devices_name)

    @Slot(int)
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

    @Slot(str)
    def play(self, music):
        if os.path.isfile(music):
            media = self.instance.media_new(music)
            self._player.set_media(media)
            self._player.play()

    @Slot()
    def pause(self):
        self._player.pause()
    @Slot()
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
        print(time.u.new_time)
        self.player_Status.emit('length',time.u.new_length)

    @Slot(int)
    def audio_Vol_Set(self, vol):
        self._player.audio_set_volume(vol)

    @Slot()
    def audio_Vol_Get(self):
        self.player_Status.emit('vol',self._player.audio_get_volume())

class udp_server(QThread):
    udp_data = Signal(str)
    def __init__(self, parent = None):
        super(udp_server, self).__init__(parent)
        MCAST_GRP = '224.1.128.128'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', 5007))
        group = socket.inet_aton(MCAST_GRP)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)

    def run(self):
        while True:
            try:
                data, addr = self.sock.recvfrom(1024)
                self.udp_data.emit(data.decode())
                print(data, addr)
            except (socket.error, e):
                print ('Expection')
                hexdata = binascii.hexlify(data)
                print ('Data = %s' % hexdata)

class schedulePlay(QThread):
    Timer_Receive_String = Signal(int,int)
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
    global zone_Name
    def setupUi(self,Dialog):
        font_Label = QFont();font_Label.setFamily(u"NanumBarunGothic");font_Label.setPointSize(14)
        self.btn_zone_sel = ['i']*66
        self.btn_zone_sel_status = [0]*66
        self.popup_btn_grp = QButtonGroup()
        self.popup_btn_grp.setExclusive(False)
        Dialog.resize(600,600)
        
        self.vbox_popup = QVBoxLayout(Dialog)
        self.lbl_popup_title = QLabel("지점 선택",Dialog)
        self.lbl_popup_title.setFont(font_Label)
        self.vbox_popup.addWidget(self.lbl_popup_title)

        self.popup_line_1 = QFrame(Dialog)
        self.popup_line_1.setFrameShape(QFrame.HLine)
        self.popup_line_1.setFrameShadow(QFrame.Sunken)
        self.vbox_popup.addWidget(self.popup_line_1)

        self.gl_popup = QGridLayout()
        self.vbox_popup.addLayout(self.gl_popup)
        for i in range(66):
            self.btn_zone_sel[i] = QPushButton("{}".format(i+1), Dialog)
            self.btn_zone_sel[i].setMinimumSize(QSize(0, 40))
            self.btn_zone_sel[i].setMaximumSize(QSize(200, 100))
            self.btn_zone_sel[i].setCheckable(True)
            self.btn_zone_sel[i].setChecked(False)
            self.popup_btn_grp.addButton(self.btn_zone_sel[i],i)
            
            self.gl_popup.addWidget(self.btn_zone_sel[i],i/6,i%6,1,1)
        for i in range(len(zone_Name)):
            self.btn_zone_sel[i].setText(zone_Name[i])
        self.popup_btn_grp.buttonClicked[int].connect(self.popup_zone_button_clicked)

        self.popup_line_2 = QFrame(Dialog)
        self.popup_line_2.setFrameShape(QFrame.HLine)
        self.popup_line_2.setFrameShadow(QFrame.Sunken)
        self.vbox_popup.addWidget(self.popup_line_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.vbox_popup.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)  

        QMetaObject.connectSlotsByName(Dialog)

    def popup_zone_button_clicked(self, index):
        if self.btn_zone_sel[index].isChecked():
            self.btn_zone_sel_status[index] = 1
        else:
            self.btn_zone_sel_status[index] = 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Ui_MainWindow()
    sys.exit(app.exec_())