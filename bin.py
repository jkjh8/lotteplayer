
def schedule_file_load(self, index):
	file = QFileDialog.getOpenFileName(self, 'Select one or more files to open', '', 'Sound (*.mp3 *.wav *.ogg *.flac *.wma)')
	print(index,file[0])
	self.schedule_List[index][0].setText(file[0])
