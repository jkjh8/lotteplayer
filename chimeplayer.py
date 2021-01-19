# -*- coding: utf-8 -*-
import sys, vlc, socket, os.path, json, os
from PyQt5.QtCore import QCoreApplication, pyqtSlot, pyqtSignal, QThread
from PyQt5.QtWidgets import *

class Ui_MainWindow(QMainWindow):
    chimeplay = pyqtSignal(str)

    def __init__(self):
        super().__init__()        
        #Variable
        self.setup = ({'boothNum':'1'})

        self.setupUi(self)
        self.setWindowTitle('Audio Player - 224.1.128.128 : 5007')

        self.setup_file_road()

        #Thread Class
        self.udp_server = udp_server()
        self.chimeplayer = chimeplayer()
        #Signal & Slot

        self.chimeplay.connect(self.chimeplayer.play)
        self.udp_server.udp_data.connect(self.server_data_parcing)
        self.show()

        #Thread Start
        self.udp_server.start()
        self.chimeplayer.start()
        #Start Set Value

    def setupUi(self, MainWindow):

    #Main Windwos
        #MainWindow.resize(1280, 800)
        MainWindow.setStyleSheet("QMainWindow{background-color:#ffffff};")
        self.centralwidget = QWidget(MainWindow)

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0,0,0,0)

############################################################# End UI ############################################################

    #Udp Mulicast Callback
    def server_data_parcing(self, data):
        print(data)
        if data == 'c0{}'.format(self.setup['boothNum']):
            self.chimeplay.emit('chime.wav')

    def setup_file_road(self):
        with open('chime.json','r') as file:
            self.setup = json.load(file)

############################################################# Audio Player #############################################################

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

############################################################# udp server #############################################################

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
    main = Ui_MainWindow()
    sys.exit(app.exec_())
