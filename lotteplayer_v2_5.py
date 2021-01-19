# -*- coding: utf-8 -*-
import sys, vlc, time, socket, math, struct, datetime, lotteplayer_rc, re, json, os, urllib.request
from lotteplayer_ui_v2_5 import Ui_MainWindow, Dialog_Zone_Sel, Dialog_Message
from _thread import *
from PyQt5.QtCore import QCoreApplication, QMetaObject, QObject, pyqtSlot, pyqtSignal, QSize, Qt, QRect, QThread, QTime, QTimer
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import *

class Main(QMainWindow, Ui_MainWindow, Dialog_Zone_Sel, Dialog_Message):
    play = pyqtSignal(str,str);pause = pyqtSignal();stop = pyqtSignal();
    tts_play = pyqtSignal(str,str);tts_stop = pyqtSignal(int);
    get_vol = pyqtSignal();set_vol = pyqtSignal(int)
    auidodevice_call = pyqtSignal()
    audioDevice_Change = pyqtSignal(int)

    def __init__(self):
        super().__init__()        
        #Variable
        """
        self.setup = ({'serverip':'172.28.242.216','serverport':5008,'boothNum':10,'audioDeviceId':0,'vol':70,
                        'zone_name_1':'센텀시티','zone_name_2':'이시아폴리스','zone_name_3':'상인점','zone_name_4':'대구점','zone_name_5':'포항점','zone_name_6':'아쿠아몰','zone_name_7':'광복점','zone_name_8':'광주점',
                        'zone_name_9':'전주점','zone_name_10':'청주영플라자','zone_name_11':'대전점','zone_name_12':'서울역점','zone_name_13':'영등포점','zone_name_14':'중동점','zone_name_15':'관악점','zone_name_16':'창원점',
                        'zone_name_17':'창원영패션관','zone_name_18':'일산점','zone_name_19':'구리점','zone_name_20':'평촌점','zone_name_21':'안산점','zone_name_22':'미아점','zone_name_23':'스타시티','zone_name_24':'노원점',
                        'zone_name_25':'분당점','zone_name_26':'잠실점','zone_name_27':'동래점','zone_name_28':'청량지점','zone_name_29':'에비뉴엘','zone_name_30':'영플라자','zone_name_31':'본점','zone_name_32':'강남점',
                        'zone_name_33':'청주아울렛','zone_name_34':'울산점','zone_name_35':'김해아울렛','zone_name_36':'파주아울렛','zone_name_37':'서면점','zone_name_38':'율하점','zone_name_39':'수완아울렛','zone_name_40':'광주월드컵점',
                        'zone_name_41':'부여아울렛','zone_name_42':'이천아울렛','zone_name_43':'고양터미널','zone_name_44':'에비뉴엘\n월드타워','zone_name_45':'수원점','zone_name_46':'광명점','zone_name_47':'구리아울렛','zone_name_48':'동부산점',
                        'zone_name_49':'마산점','zone_name_50':'광교아울렛','zone_name_51':'가산아울렛','zone_name_52':'진주아울렛','zone_name_53':'남악아울렛','zone_name_54':'고양아울렛','zone_name_55':'군산아울렛','zone_name_56':'기흥아울렛',
                        'zone_name_57':'인천터미널'})
        """
        self.logserver = ('172.28.242.40',9999)
        self.zone_status = ({1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0,32:0,33:0,
                            34:0,35:0,36:0,37:0,38:0,39:0,40:0,41:0,42:0,43:0,44:0,45:0,46:0,47:0,48:0,49:0,50:0,51:0,52:0,53:0,54:0,55:0,56:0,57:0,58:0,59:0,60:0,61:0,62:0,63:0,64:0,65:0,66:0})
        self.zone_state = (['대기중','방송중\nBooth 1','방송중\nBooth 2','방송중\nBooth 3','방송중\nBooth 4','방송중\nBooth 5','방송중\nBooth 6','방송중\nBooth 7','방송중\nBooth 8','방송중\nBooth 9',
                            '방송중\nPlayer 1','방송중\nPlayer 2','방송중\nPlayer 3','방송중\nPlayer 4','방송중\nPlayer 5','방송중\nPlayer 6','방송중\nPlayer 7','방송중\nPlayer 8','방송중\nPlayer 9'])

        self.tts_Lang = ['nara','clara','shinji','meimei']

        self.playIndex = 0
        self.playLoop = 0
        self.player_Play_List =[]
        self.zone_list =[]
        self.copy_ID = 99

        self.tts_Message = ""

        self.player_Flag = "live"

        self.days = ["매일","월~목","금~일","월~수","목~일","월","화","수","목","금","토","일"]
        self.days_value = [[0,1,2,3,4,5,6],[0,1,2,3],[4,5,6],[0,1,2],[3,4,5,6],[0],[1],[2],[3],[4],[5],[6]]

        self.dialog = QDialog()
        self.dialog.Qui = Dialog_Zone_Sel()
        self.dialog.Qui.setupUi(self.dialog)
        self.dialog_Message = QDialog()
        self.dialog_Message.Qui = Dialog_Message()
        self.dialog_Message.Qui.setupUi(self.dialog_Message)

        self.setupUi(self)
        self.setWindowTitle('Audio Player - 224.1.128.128 : 5007')

        self.setup_file_road()

        self.timerVar = QTimer()
        self.timerVar.setInterval(1000)

        #Thread Class
        self.audioplayer = audioplayer()
        self.TTS_Player = TTS_Player()
        self.udp_server = udp_server()

        #Signal & Slot
        self.Sld_Vol.valueChanged.connect(self.lbl_Vol_Value.setNum)
        self.Sld_Vol.valueChanged.connect(self.vol_Set)

        self.btn_Tab_Player.clicked.connect(lambda: self.stacked_Wiget_Page_Change(0))
        self.btn_Tab_Tts.clicked.connect(lambda: self.stacked_Wiget_Page_Change(1))
        self.btn_Tab_Schduler.clicked.connect(lambda: self.stacked_Wiget_Page_Change(2))
        self.btn_Setup.clicked.connect(lambda: self.stacked_Wiget_Page_Change(3))

        self.btn_Playlist_Add.clicked.connect(self.addList)
        self.btn_Playlist_Del.clicked.connect(self.delList)
        #self.tw_Play_List_Table.cellClicked.connect(self.select_Playlist_row)
        self.tw_Play_List_Table.cellDoubleClicked.connect(self.doubleClick_Playlist)

        self.btn_Stop.clicked.connect(self.player_Stop)
        self.btn_Play.clicked.connect(self.player_Play)
        self.btn_RW.clicked.connect(self.player_Rew)
        self.btn_FF.clicked.connect(self.player_FF)

        self.btn_schedule_Reset.clicked.connect(self.scheduler_reset)
        self.btn_Audiodecive_Refrash.clicked.connect(self.audio_Device_Refrash)

        self.play.connect(self.audioplayer.play)
        self.pause.connect(self.audioplayer.pause)
        self.stop.connect(self.audioplayer.stop)
        self.audioplayer.player_Status.connect(self.player_state_change)
        self.audioplayer.audio_devices.connect(self.audio_devices)

        self.btn_Tts_preview.clicked.connect(self.tts_Preview_Play)

        self.tts_play.connect(self.TTS_Player.play)
        self.tts_stop.connect(self.TTS_Player.stop)
        self.TTS_Player.player_Stop.connect(self.tts_Player_Stop)

        self.auidodevice_call.connect(self.audioplayer.get_Audio_Devices)
        self.get_vol.connect(self.audioplayer.audio_Vol_Get)
        self.set_vol.connect(self.audioplayer.audio_Vol_Set)
        self.cb_AudioDevice.currentIndexChanged.connect(self.set_Audio_Device)
        self.audioDevice_Change.connect(self.audioplayer.set_Audio_Device)

        self.cb_Booth.currentIndexChanged.connect(self.set_Booth_Index)

        self.udp_server.udp_data.connect(self.server_data_parcing)

        self.btn_Tts_Load_Text.clicked.connect(self.tts_File_Open)
        self.btn_Tts_Save_Text.clicked.connect(self.tts_File_Save)
        self.btn_Tts_preview.clicked.connect(self.tts_Preview)
        self.btn_Tts_Start.clicked.connect(self.tts_Player_Play)

        self.schedule_file_btn_grp.buttonClicked[int].connect(self.schedule_file_load)
        self.schedule_zone_sel_grp.buttonClicked[int].connect(self.schedule_zone_sel)
        self.schedule_del_btn_grp.buttonClicked[int].connect(self.schedule_List_del)
        self.schedule_copy_btn_grp.buttonClicked[int].connect(self.schedule_copy)

        for i in range(200):
            self.schedule_List[i][7].stateChanged.connect(self.schedule_value_change)
            self.schedule_List[i][5].currentIndexChanged.connect(self.schedule_value_change)
            self.schedule_List[i][6].timeChanged.connect(self.schedule_value_change)

        #self.schedulePlay.Timer_Receive_String.connect(self.schedule_parcing)
        self.btn_Set_Ip.clicked.connect(self.server_ip_setup)
        self.timerVar.timeout.connect(self.udp_Schedule_Parcing)
        self.show()

        #Thread Start
        self.udp_server.start()
        #self.schedulePlay.start()
        self.timerVar.start()

        #Start Set Value
        
        self.set_vol.emit(self.setup['vol'])
        self.get_vol.emit()
        self.set_ButtonName()
        self.setup_file_road()
        self.cb_Booth.setCurrentIndex(self.setup['boothNum']-10)
        #self.cb_AudioDevice.setCurrentIndex(self.setup['audioDeviceId'])
        try:
            self.le_Serverip.setText(self.setup['serverip'])
            self.le_Serverport.setText(str(self.setup['serverport']))
            self.qle_TTS_ID.setText(self.setup['ttsID'])
            self.qle_TTS_Secret.setText(self.setup['ttsPass'])
        except:
            pass
        start_new_thread(self.server_call,('t:request,!',))
        start_new_thread(self.server_call,('t:booth{},!'.format(self.setup['boothNum']),))
        start_new_thread(self.log_server_call,('0,{}번 부스 이벤트 플레이가 실행되었습니다.'.format(self.setup['boothNum']-9),))
 
        self.set_vol.emit(self.setup['vol'])
        self.device_Setup_State = True
        self.auidodevice_call.emit()

        self.chime_File = "Chaim_3 Bounced.wav"
        self.tts_File = "ttslive.mp3"

################################################################ TTS FN ########################################################################

    def tts_File_Open(self):
        file = QFileDialog.getOpenFileName(self, 'Select one or more files to open', os.path.expanduser("~\\Documents"), 'Text files (*.txt)',None)
        if file[0]:            
            with open(file[0],'rt',encoding='utf8') as f:
                self.qte_tts_text.setText(f.read())

    def tts_File_Save(self):
        file = QFileDialog.getSaveFileName(self, 'Save TTS Text File',os.path.expanduser("~\\Documents"),'Text Files (*.txt)')
        if file[0]:
            with open(file[0],'wt', encoding='utf8') as f:
                f.write(self.qte_tts_text.toPlainText())
            print(file[0])

    def tts_Preview(self):
        if self.btn_Tts_preview.isChecked():
            self.btn_Tts_preview.setText("미리듣기 중지")
        else:
            self.btn_Tts_preview.setText("미리듣기")

    @pyqtSlot(int)
    def tts_Player_Stop(self, value):
        if value == 0:            
            self.btn_Tts_preview.setChecked(False)
            self.btn_Tts_preview.setText('미리듣기')
        else:
            self.tts_play.emit(self.tts_File,'TTS_Stop')

    def tts_Preview_Play(self):
        if self.btn_Tts_preview.isChecked():
            if self.qte_tts_text.toPlainText() == self.tts_Message:
                if self.btn_Tts_Chime.isChecked():
                    self.tts_play.emit(self.chime_File,'TTS')
                else:
                    self.tts_play.emit(self.tts_File,'TTS_Stop')
            else:
                self.tts_Request(self.tts_Lang[self.btn_Tts_Lang.checkedId()], self.qte_tts_text.toPlainText())

                if self.btn_Tts_Chime.isChecked():
                    self.tts_play.emit(self.chime_File,'TTS')
                else:
                    self.tts_play.emit(self.tts_File,'TTS_Stop')
        else:
            self.tts_stop.emit()

    @pyqtSlot()
    def tts_Player_Play(self):
        buttonReply = QMessageBox.information(self, 'TTS 방송', "TTS 방송을 송출 하시겠습니까?", QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
        if buttonReply == QMessageBox.Ok:
            print("TTS Start")

            self.zone_list = []
            __broadcast_zone = []

            for i in range(len(self.zone_Buttons)):
                if self.zone_Buttons[i].isChecked():
                    self.zone_list.append(i+1)
                    __broadcast_zone.append('{}:{}'.format(i+1,self.setup['boothNum']))
            if not self.find_zone_overlap(self.zone_list):
                start_new_thread(self.server_call,('t:onair,{},!'.format(','.join(__broadcast_zone)),))
                try:
                    if self.qte_tts_text.toPlainText() == self.tts_Message:
                        if self.btn_Tts_Chime.isChecked():
                            start_new_thread(self.wait_play,(self.chime_File,'TTS'))
                        else:
                            start_new_thread(self.wait_play,(self.tts_File,'TTS_Stop'))
                    else:
                        self.tts_Request(self.tts_Lang[self.btn_Tts_Lang.checkedId()], self.qte_tts_text.toPlainText())
                        
                        if self.btn_Tts_Chime.isChecked():
                            start_new_thread(self.wait_play,(self.chime_File,'TTS'))
                        else:
                            start_new_thread(self.wait_play,(self.tts_File,'TTS_Stop'))

                except:
                    self.statusBar().showMessage('Player에 문제가 발생하여 파일을 재생할 수 없습니다.',5000)
                    start_new_thread(self.log_server_call,('0, {}부스 Player에 문제가 발생하여 파일을 재생할 수 없습니다.'.format(self.setup['boothNum']-9),))
                    self.song_finished()
        else:
            self.btn_Tts_Start.setChecked(False)           


##################################################################### INIT FN ######################################################################
    def setup_file_save(self):
        with open('setup.json','w') as file:
            json.dump(self.setup,file,ensure_ascii=False)

    def setup_file_road(self):
        try:
            with open('setup.json','r') as file:
                self.setup = json.load(file)
                #setup = json.dumps(json_setup)
            self.setup_Schedule_Parcing()
        except:
            self.overlapzone_popup('셋업 파일을 읽어 올 수 없어 초기화 되었습니다.', '에러','셋업 파일을 읽어 올 수 없습니다.')

    def setup_Schedule_Parcing(self):
        for i in range(200):
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

    #Set Button Name
    def set_ButtonName(self):
        for i in range(66):
            zonestate_index = self.zone_status[i+1]
            if 'zone_name_{}'.format(i+1) in self.setup:
                if zonestate_index <= 18:
                    self.zone_Buttons[i].setText('{}\n-{}-'.format(self.setup['zone_name_{}'.format(i+1)],self.zone_state[zonestate_index]))
                else:
                    self.zone_Buttons[i].setText('{}\n-{}-'.format(self.setup['zone_name_{}'.format(i+1)],"외부 방송"))
                if zonestate_index == 0:
                    self.zone_Buttons[i].setStyleSheet(self.btn_style_nomal)
                elif zonestate_index == self.setup['boothNum']-9:
                    self.zone_Buttons[i].setStyleSheet(self.btn_style_self)
                else:
                    self.zone_Buttons[i].setStyleSheet(self.btn_style_checked)

    #Select booth
    def set_Booth_Index(self, index):
        self.setup['boothNum'] = index + 10
        self.set_ButtonName()
        self.setup_file_save()

    def stacked_Wiget_Page_Change(self, pageNum):
        if pageNum == 0:
            self.stackedWidget.setCurrentIndex(0)
            self.stack_Page_1_1.setCurrentIndex(0)
            self.lbl_PlayList.setText("플레이 리스트")
        elif pageNum == 1:
            self.stackedWidget.setCurrentIndex(0)
            self.stack_Page_1_1.setCurrentIndex(1)
            self.lbl_PlayList.setText("TTS")
        else:
            self.stackedWidget.setCurrentIndex(pageNum-1)

    def song_length(self,value):
        self.lbl_MediaTime.setText(self.format_time(value))
        self.media_length = value

    #Play time return
    def format_time(self, milliseconds):
        self.position = milliseconds / 1000
        m, s = divmod(self.position, 60)
        h, m = divmod(m, 60)
        return ("%02d/%02d" % (m, s))


    #Audio Device List Retrun
    def audio_Device_Refrash(self):
        self.cb_AudioDevice.clear()
        self.auidodevice_call.emit()
        #self.audioDevice_Change.emit(0)

    @pyqtSlot(list)
    def audio_devices(self, devicelist):
        self.device_Setup_State = False
        for i in range(len(devicelist)):
            self.cb_AudioDevice.addItem(devicelist[i])
        self.find_device()

    def find_device(self):
        self.device_Setup_State = True
        for i in range(self.cb_AudioDevice.count()):
            #if 'ADAT' in self.cb_AudioDevice.itemText(i):
            if self.setup['audioDeviceId'] == self.cb_AudioDevice.itemText(i):
                self.cb_AudioDevice.setCurrentIndex(i)
                self.audioDevice_Change.emit(i)

    @pyqtSlot(int)
    def set_Audio_Device(self,id):
        if id > -1 and self.device_Setup_State:        
            self.audioDevice_Change.emit(id)
            self.setup['audioDeviceId'] = self.cb_AudioDevice.currentText()
            self.setup_file_save()

    #Audio Vol Set
    def vol_Set(self,volValue):
        self.set_vol.emit(volValue)
        self.setup['vol'] = volValue
        self.setup_file_save()

################################################################### Play List FN ######################################################################


    #Play List
    def addList(self):
        files = QFileDialog.getOpenFileNames(self, 'Select one or more files to open', os.path.expanduser("~\\Documents"), 'Sound (*.mp3 *.wav *.ogg *.flac *.wma)',None)
        cnt = len(files[0])
        row = len(self.player_Play_List)

        for i in range(row, row+cnt):
            self.player_Play_List.append(files[0][i-row])
        self.play_List_Refrash()
        self.tw_Play_List_Table.selectRow(0)

    def delList(self):
        row = self.tw_Play_List_Table.rowCount()
        index = []
        for item in self.tw_Play_List_Table.selectedIndexes():
            index.append(item.row())
        index = list(set(index))
        index.reverse()
        for i in index:
            del self.player_Play_List[i]
        self.play_List_Refrash()
        
    def play_List_Refrash(self):
        self.tw_Play_List_Table.setRowCount(len(self.player_Play_List))
        for i in range(len(self.player_Play_List)):
            self.tw_Play_List_Table.setItem(i,0, QTableWidgetItem(os.path.basename(self.player_Play_List[i])))

    def select_Playlist_row(self, row, colum):
        #self.playIndex = row
        print(self.tw_Play_List_Table.currentRow())

    def doubleClick_Playlist(self, row, colum):
        if self.btn_Play.isChecked == True:
            self.player_Stop()
            time.sleep(1)
        self.playIndex = row
        self.btn_Play.setChecked(True)
        self.player_Play()

################################################################### PLAYER FN ######################################################################
    def wait_play(self, playlist, mode):
        self.find_device()
        self.btn_Play.setChecked(True)
        time.sleep(2)
        self.play.emit(playlist,mode)
        self.statusbar.showMessage(playlist)

    def player_Stop(self):
        self.stop.emit()
        self.song_finished()

    def player_Play(self):          
        if self.btn_Play.isChecked():
            if self.player_Play_List:
                self.zone_list = []
                __broadcast_zone = []
                for i in range(len(self.zone_Buttons)):
                    if self.zone_Buttons[i].isChecked():
                        self.zone_list.append(i+1)
                        __broadcast_zone.append('{}:{}'.format(i+1,self.setup['boothNum']))
                if not self.find_zone_overlap(self.zone_list):
                    start_new_thread(self.server_call,('t:onair,{},!'.format(','.join(__broadcast_zone)),))
                    try:
                        start_new_thread(self.wait_play,(self.player_Play_List[self.tw_Play_List_Table.currentRow()],'player'))
                    except:
                        self.statusBar().showMessage('Player에 문제가 발생하여 파일을 재생할 수 없습니다.',5000)
                        start_new_thread(self.log_server_call,('0, {}부스 Player에 문제가 발생하여 파일을 재생할 수 없습니다.'.format(self.setup['boothNum']-9),))
                        self.song_finished()                   
            else:
                self.song_finished()
                self.addList()
        else:
            self.pause.emit()

    def player_Rew(self):
            self.tw_Play_List_Table.selectRow(self.tw_Play_List_Table.currentRow()-1)

            if self.btn_Play.isChecked():
                self.play.emit(self.player_Play_List[self.tw_Play_List_Table.currentRow()-1])

    def player_FF(self):
            if self.tw_Play_List_Table.rowCount()-1 == self.tw_Play_List_Table.currentRow():

                self.tw_Play_List_Table.selectRow(0)
            else:
                self.tw_Play_List_Table.selectRow(self.tw_Play_List_Table.currentRow()+1)

            if self.btn_Play.isChecked():
                self.play.emit(self.player_Play_List[self.tw_Play_List_Table.currentRow()+1])

    #Player Callback
    @pyqtSlot(str, int)
    def player_state_change(self, key, value):
        #파일길이
        if key == 'length':
            self.lbl_MediaTime.setText(self.format_time(value))
            self.pgb_CurrentTime.setMaximum(value)
        #현재 시간
        elif  key == 'current_time':
            self.lbl_CurrentTime.setText(self.format_time(value))
            self.pgb_CurrentTime.setValue(value)
        #정지
        elif key == 'stop' and value == 1:
            loop = self.btn_Loop.isChecked()
            playlistplay = self.btn_PlaylistPlay.isChecked()

            if loop == True and playlistplay == False:
                self.loop_Play()

            elif loop == False and playlistplay == True:
                self.playlist_Play()

            elif loop == True and playlistplay == True:
                self.play_next()
            else:
                self.song_finished()
                start_new_thread(self.log_server_call,('0, {}번 이벤트 플레이어 방송이 종료되었습니다.'.format(self.setup['boothNum']-9),))

        elif key == "stop" and value == 2:
            self.play.emit(self.tts_File,"TTS_Stop")
        elif key == "stop" and value == 3:
            self.song_finished()
            self.btn_Tts_Start.setChecked(False)
            start_new_thread(self.log_server_call,('0, {}번 이벤트 플레이어 TTS방송이 종료 되었습니다.'.format(self.setup['boothNum']-9),))
        elif key == 'stop' and value == 0:
            self.song_finished()
            start_new_thread(self.log_server_call,('0, {}번 이벤트 플레이어 방송을 정지 하였습니다.'.format(self.setup['boothNum']-9),))
        #볼륨
        elif key == 'vol':
            self.Sld_Vol.setValue(value)

    def loop_Play(self):
        self.play.emit(self.player_Play_List[self.tw_Play_List_Table.currentRow()])
        self.statusbar.showMessage(self.tw_Play_List_Table.item(self.tw_Play_List_Table.currentRow(),0).text())

    def playlist_Play(self):
        if self.tw_Play_List_Table.currentRow() == self.tw_Play_List_Table.rowCount()-1:
            self.tw_Play_List_Table.selectRow(0)
            self.song_finished()
        else:
            self.play_next()

    def play_next(self):
        self.play_FF()
        self.statusbar.showMessage(self.tw_Play_List_Table.item(self.tw_Play_List_Table.currentRow(),0).text())

    def song_finished(self):
        self.lbl_MediaTime.setText('--/--')
        self.lbl_CurrentTime.setText('--/--')
        self.pgb_CurrentTime.setValue(0)
        self.btn_Play.setChecked(False)
        self.statusbar.clearMessage()
        if self.zone_list:
            broadcast_zone=[]
            for i in range(len(self.zone_list)):
                broadcast_zone.append('{}:{}'.format(self.zone_list[i],0))
            start_new_thread(self.server_call,('t:onair,{},!'.format(','.join(broadcast_zone)),))
            start_new_thread(self.log_server_call,('0,{} 부스 방송이 종료 되었습니다.'.format(self.setup['boothNum']-9),))
            self.zone_list = []
        #self.auidodevice_call.emit()

    def server_ip_setup(self):
        self.setup['serverip'] = self.le_Serverip.text()
        self.setup['serverport'] = int(self.le_Serverport.text())
        self.setup['ttsID'] = self.qle_TTS_ID.text()
        self.setup['ttsPass'] = self.qle_TTS_Secret.text()
        self.setup_file_save()

################################################################### Coummunication FN ######################################################################
    #Udp Mulicast Callback
    def server_data_parcing(self, data):
        #print(data)
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


################################################################### Scheduler FN ######################################################################
    #Scheduler
    @pyqtSlot(int)
    def schedule_file_load(self, index):
        file = QFileDialog.getOpenFileName(self, 'Select one or more files to open', os.path.expanduser("~\\Documents"), 'Sound (*.mp3 *.wav *.ogg *.flac *.wma)',None)
        self.schedule_List[index][1].setText(file[0])
        self.setup['schedule_file_{}'.format(index)] = file[0]
        self.setup_file_save()

    @pyqtSlot(int)
    def schedule_zone_sel(self, index):
        #print(index)
        select_zone = []
        for i in range(66):
            if 'zone_name_{}'.format(i+1) in self.setup:
                self.dialog.Qui.btn_zone_sel[i].setText(self.setup['zone_name_{}'.format(i+1)])
            self.dialog.Qui.btn_zone_sel[i].setChecked(False)

        selected_zone = self.schedule_List[index][3].text().split(',')
        try:
            for i in range(len(selected_zone)):
                select_zone = [item for item, value in self.setup.items() if value == selected_zone[i]]
                if 'zone_name_' in select_zone[0] and select_zone[0] in self.setup:
                    self.dialog.Qui.btn_zone_sel[int((re.findall('\d+', select_zone[0]))[0])-1].setChecked(True)
        except:
            pass

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
            for i in range(200):
                self.schedule_List[i][9].setStyleSheet(self.btn_style_nomal)

    def schedule_value_change(self):
        for i in range(200):
            self.setup['schedule_days_{}'.format(i)] = self.schedule_List[i][5].currentIndex()
            self.setup['schedule_time_{}'.format(i)] = ('{},{},{}'.format(self.schedule_List[i][6].time().hour(),self.schedule_List[i][6].time().minute(),self.schedule_List[i][6].time().second()))
            self.setup['schedule_act_{}'.format(i)] = self.schedule_List[i][7].isChecked()
        self.setup_file_save()

    @pyqtSlot()
    def udp_Schedule_Parcing(self):
        print(QTime.currentTime().toString("hh:mm:ss"))
        for i in range(200):
            if self.schedule_List[i][7].isChecked():

                #Weekday check
                dt = datetime.datetime.now().weekday()
                for n in range(len(self.days_value[self.schedule_List[i][5].currentIndex()])):
                    if self.days_value[self.schedule_List[i][5].currentIndex()][n] == dt:
                        __weekday = True
                        break
                    else:
                        __weekday = False

                if self.schedule_List[i][6].time().toString("hh:mm:ss")== QTime.currentTime().toString("hh:mm:ss") and __weekday == True:                    
                    if self.btn_Play.isChecked() == False:
                        self.zone_list = self.schedule_zone_check(i)

                        overlap_zone_name = self.find_zone_overlap(self.zone_list)

                        #방송구간 중복 확인
                        if overlap_zone_name:
                            pass
                            #start_new_thread(self.log_server_call,('0, {}부스 방송구간 중복으로 {}번 스케줄 방송이 실행되지 않았습니다. -{}-'.format(self.setup['boothNum']-9,i+1,','.join(overlap_zone_name)),))
                            #self.overlapzone_popup(overlap_zone_name, '스케줄 방송','방송구간 중복으로 스케쥴 방송이 중단됩니다.')
                        else:
                            if os.path.isfile(self.schedule_List[i][1].text()):
                                broadcast_zone=[]
                                broadcast_zone_name=[]
                                
                                for n in range(len(self.zone_list)):
                                    broadcast_zone.append('{}:{}'.format(self.zone_list[n],self.setup['boothNum']))
                                    broadcast_zone_name.append(self.setup['zone_name_{}'.format(self.zone_list[n])])
                                start_new_thread(self.server_call,('t:onair,{},!'.format(','.join(broadcast_zone)),))
                                start_new_thread(self.log_server_call,('0, {}부스 이벤트 방송 실행. -{}-'.format(self.setup['boothNum']-9,','.join(broadcast_zone_name)),))
                                self.overlapzone_popup('{}번 스케줄이 실행되었습니다.'.format(i+1), '스케줄 방송','스케쥴 방송 실행중')
                                try:
                                    start_new_thread(self.wait_play, (self.schedule_List[i][1].text(),'schedule'))
                                except:
                                    self.statusbar.showMessage('플레이어에 문제가 발생했습니다.',5000)
                                    self.song_finished()
                            else:
                                self.song_finished()
                                start_new_thread(self.log_server_call,('0, {}부스 재생 파일 문제로 {}번 스케줄 방송이 실행되지 않았습니다.'.format(self.setup['boothNum']-9,i+1),))
                                self.overlapzone_popup(self.schedule_List[i][1].text(), '스케줄 방송','재생 파일 문제로 방송이 실행되지 않았습니다.')      
                    else:
                        start_new_thread(self.log_server_call,('0, 플레이어가 사용중이어서 {}번 부스 스케줄 방송이 실행되지 않았습니다.'.format(self.setup['boothNum']-9),))
                        self.overlapzone_popup('스케줄 방송이 실행되지 않았습니다.', '스케줄 방송','플레이어가 사용중 입니다.')


    @pyqtSlot()
    def scheduler_reset(self):
        buttonReply = QMessageBox.information(self, '스케줄 리셋', "전체 스케줄을 리셋 하시겠습니까?", QMessageBox.Ok | QMessageBox.Cancel )

        if buttonReply == QMessageBox.Ok:            
            for i in range(200):
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



    def find_zone_overlap(self, zone_list):
        zone_overlap=[]
        for i in range(len(zone_list)):
            if self.zone_status[zone_list[i]] > 0 and self.zone_status[zone_list[i]] != self.setup['boothNum']:
                zone_overlap.append(self.setup['zone_name_{}'.format(zone_list[i])])
        if zone_overlap:
            start_new_thread(self.log_server_call,('0, {}부스 방송구간 중복으로 이벤트 방송이 실행되지 않았습니다. -{}-'.format(self.setup['boothNum']-9,','.join(zone_overlap)),))
            self.overlapzone_popup(','.join(zone_overlap), '이벤트 방송', '방송구간 중복으로 방송이 중단됩니다.')
            self.stop.emit()
            return (True)
        else:
            return (False)

    def schedule_zone_check(self,index):
        zone_sel_status = []
        schedule_zone_sel = self.schedule_List[index][3].text().split(',')
        for i in range(len(schedule_zone_sel)):
            select_zone = [item for item, value in self.setup.items() if value == schedule_zone_sel[i]]
            if 'zone_name_' in select_zone[0] and select_zone[0] in self.setup:
                zone_sel_status.append(int(re.findall('\d+', select_zone[0])[0]))
        return zone_sel_status

############################################################### popup ##################################################################

    def overlapzone_popup(self, overlap_zone_name, title, message):
        self.dialog_Message.setWindowTitle(title)
        self.dialog_Message.Qui.lbl_Message.setText(message)
        if str(type(overlap_zone_name)) == "<class 'list'>":
            print_Message = ','.join(overlap_zone_name)
        else:
            print_Message = overlap_zone_name
        self.dialog_Message.Qui.lbl_Message_Zone.setText(print_Message)
        self.dialog_Message.show()
        start_new_thread(self.popup_close,(10,))
        #self.btn_Play.setChecked(False)

    def popup_close(self,timer):
        time.sleep(timer)
        self.dialog_Message.close()
################################################################ TTS ##################################################################

    def tts_Request(self, lang, text):
        client_id = "bh51u91nlo"
        client_secret = "0zRDttwNbszDNeBMgBrzJsSmmOPtZDRzr6du9Hst"

        enc_Text = urllib.parse.quote(text)
        data = "speaker=mijin&speed=0&text={}".format(enc_Text)
        url = "https://naveropenapi.apigw.ntruss.com/voice/v1/tts"
        request = urllib.request.Request(url)
        request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
        request.add_header("X-NCP-APIGW-API-KEY", client_secret)
        response = urllib.request.urlopen(request, data=data.encode('utf-8'))
        rescode = response.getcode()
        if(rescode==200):
            print("TTS mp3 저장")
            response_body = response.read()
            with open('ttslive.mp3', 'wb') as f:
                f.write(response_body)
        else:
            print("Error Code:" + rescode) 


############################################################# Audio Player #############################################################

class audioplayer(QThread):
    player_Status = pyqtSignal(str,int)
    audio_devices = pyqtSignal(list)
    def __init__(self, parent = None):
        super(audioplayer, self).__init__(parent)
        self.play_Mode = ''
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
        #print(self.devices_name)
        self.audio_devices.emit(self.devices_name)
        #print("audioplayer get devices")

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
        #print ("change Audio Device = {}".format(deviceId))

    @pyqtSlot(str,str)
    def play(self, music, mode):
        if os.path.isfile(music):
            self.play_Mode = mode
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
        if self.play_Mode == 'player':
            self.player_Status.emit('stop',1)
        elif self.play_Mode == "TTS":
            self.player_Status.emit('stop',2)
        elif self.play_Mode == "TTS_Stop":
            self.player_Status.emit('stop',3)
        else:
            self.player_Status.emit('stop',0)

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



class TTS_Player(QThread):
    player_Stop = pyqtSignal(int)
    def __init__(self, parent = None):
        super(TTS_Player, self).__init__(parent)
        self.new_Player()
        
    def new_Player(self):
        self.instance = vlc.Instance()
        self._player = self.instance.media_player_new()
        self.Event_Manager = self._player.event_manager()      
        self.Event_Manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.songFinished)
        
    @pyqtSlot(str,str)
    def play(self, music, mode):
        self.mode = mode

        if os.path.isfile(music):
            media = self.instance.media_new(music)
            self._player.set_media(media)
            self._player.play()

    @pyqtSlot()
    def stop(self):
        self._player.stop()
        self.new_Player()

    def songFinished(self, event):
        time.sleep(1)
        if self.mode == "TTS":
            self.player_Stop.emit(1)
        else:
            self.player_Stop.emit(0)


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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
