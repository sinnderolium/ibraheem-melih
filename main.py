from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pytube


def show_popup():
    msg = QMessageBox()
    msg.setWindowTitle("Download Completed!")
    msg.setText("Your download is ready!")

    msg.exec_()


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("YouTube Downloader")
        Main.resize(800, 576)
        self.SubmitBtn = QtWidgets.QPushButton(Main)
        self.SubmitBtn.setGeometry(QtCore.QRect(310, 520, 131, 51))
        self.SubmitBtn.setObjectName("SubmitBtn")
        self.SubmitBtn.clicked.connect(self.submit)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SubmitBtn.setFont(font)

        self.YouTubePlaylistView = QtWidgets.QListView(Main)
        self.YouTubePlaylistView.setGeometry(QtCore.QRect(490, 130, 281, 331))
        self.YouTubePlaylistView.setObjectName("YouTubePlaylistView")
        self.inputUrl = QtWidgets.QTextEdit(Main)
        self.inputUrl.setGeometry(QtCore.QRect(20, 410, 451, 51))
        self.inputUrl.setObjectName("inputUrl")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputUrl.setFont(font)
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(100, 10, 581, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Main)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Main)
        self.label_3.setGeometry(QtCore.QRect(20, 360, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Main)
        self.label_4.setGeometry(QtCore.QRect(510, 100, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Main)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.fileDir = QtWidgets.QTextEdit(Main)
        self.fileDir.setGeometry(QtCore.QRect(20, 210, 281, 51))
        self.fileDir.setObjectName("fileDir")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fileDir.setFont(font)
        self.BrowseBtn = QtWidgets.QPushButton(Main)
        self.BrowseBtn.setGeometry(QtCore.QRect(350, 210, 121, 51))
        self.BrowseBtn.setObjectName("BrowseBtn")
        self.BrowseBtn.clicked.connect(self.browse)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BrowseBtn.setFont(font)

        self.label_6 = QtWidgets.QLabel(Main)
        self.label_6.setGeometry(QtCore.QRect(20, 280, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.groupBox = QtWidgets.QGroupBox(Main)
        self.groupBox.setGeometry(QtCore.QRect(20, 120, 281, 51))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(200, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Main)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 310, 281, 51))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 10, 97, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(180, 10, 97, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.comboBox = QtWidgets.QComboBox(Main)
        self.comboBox.setGeometry(QtCore.QRect(30, 520, 171, 51))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.label_7 = QtWidgets.QLabel(Main)
        self.label_7.setGeometry(QtCore.QRect(30, 480, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "YouTube Downloader"))
        self.SubmitBtn.setText(_translate("Main", "Download"))
        self.label.setText(_translate("Main", "Ibraheem safa graduation project"))
        self.label_2.setText(_translate("Main", "Select format"))
        self.label_3.setText(_translate("Main", "Enter Playlist/Video Url here:"))
        self.label_4.setText(_translate("Main", "YouTube Video Name/url:"))
        self.label_5.setText(_translate("Main", "Enter Directory:"))
        self.BrowseBtn.setText(_translate("Main", "Browse"))
        self.label_6.setText(_translate("Main", "Select video or playlist:"))
        self.radioButton.setText(_translate("Main", "Mp4"))
        self.radioButton_2.setText(_translate("Main", "Mp3"))
        self.radioButton_3.setText(_translate("Main", "Video"))
        self.radioButton_4.setText(_translate("Main", "Playlist"))
        self.label_6.setText(_translate("Main", "Select video or playlist:"))
        self.radioButton.setText(_translate("Main", "Mp4"))
        self.radioButton_2.setText(_translate("Main", "Mp3"))
        self.radioButton_3.setText(_translate("Main", "Video"))
        self.radioButton_4.setText(_translate("Main", "Playlist"))
        self.comboBox.setItemText(0, _translate("Main", "360p"))
        self.comboBox.setItemText(1, _translate("Main", "480p"))
        self.comboBox.setItemText(2, _translate("Main", "720p"))
        self.comboBox.setItemText(3, _translate("Main", "1080p"))
        self.label_7.setText(_translate("Main", "Select resolution:"))

    def submit(self):

        inputText = self.inputUrl.toPlainText()

        model = QtGui.QStandardItemModel()
        self.YouTubePlaylistView.setModel(model)

        item = QtGui.QStandardItem(inputText)
        model.appendRow(item)

        if self.radioButton.isChecked():
            # for MP4

            from pytube import Playlist
            playlistLink = inputText
            playlist = Playlist(playlistLink)
            downloadDirectory = self.fileDir.toPlainText()

            if self.comboBox.currentText() == "1080p":
                i_tag = 137
            elif self.comboBox.currentText() == "720p":
                i_tag = 22
            elif self.comboBox.currentText() == "480p":
                i_tag = 135
            else:
                i_tag = 18

            if self.radioButton_3.isChecked():
                # for single MP4
                yt = pytube.YouTube(inputText)
                stream = yt.streams.get_by_itag(i_tag)
                stream.download(downloadDirectory)

                s1 = 'Downloaded : {} with url : {}'.format(stream.title, stream.url)
                item = QtGui.QStandardItem(s1)
                model.appendRow(item)

                show_popup()

            elif self.radioButton_4.isChecked():
                # For mp4 playlist
                for video_url in playlist.video_urls:
                    yt = pytube.YouTube(video_url)
                    stream = yt.streams.get_by_itag(i_tag)
                    stream.download(downloadDirectory)

                    s1 = 'Downloaded : {} with url : {}'.format(stream.title, video_url)
                    item = QtGui.QStandardItem(s1)
                    model.appendRow(item)

                show_popup()

            else:
                item = QtGui.QStandardItem("check video or playlist")
                model.appendRow(item)

        elif self.radioButton_2.isChecked():
            # For mp3

            from pytube import Playlist
            playlistLink = inputText
            playlist = Playlist(playlistLink)
            downloadDirectory = self.fileDir.toPlainText()
            if self.radioButton_3.isChecked():
                # for single MP3
                yt = pytube.YouTube(inputText)
                stream = yt.streams.get_by_itag(251)
                stream.download(downloadDirectory, filename=stream.title + ".mp3")

                s1 = 'Downloaded : {} with url : {}'.format(stream.title, stream.url)
                item = QtGui.QStandardItem(s1)
                model.appendRow(item)
                show_popup()

            elif self.radioButton_4.isChecked():
                # for MP3 playlist
                for video_url in playlist.video_urls:
                    yt = pytube.YouTube(video_url)
                    stream = yt.streams.get_by_itag(251)
                    stream.download(downloadDirectory, filename=stream.title + ".mp3")
                    s1 = 'Downloaded : {} with url : {}'.format(stream.title, video_url)
                    item = QtGui.QStandardItem(s1)
                    model.appendRow(item)
                show_popup()

            else:
                item = QtGui.QStandardItem("check video or playlist")
                model.appendRow(item)

        else:
            item = QtGui.QStandardItem("check mp3 or mp4")
            model.appendRow(item)

    def browse(self):
        from os.path import expanduser
        input_dir = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        self.fileDir.setText(input_dir)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
