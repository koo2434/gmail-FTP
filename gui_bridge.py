import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from layout import Ui_mainDialog
from driver import Driver
import requests

#layout_ui = uic.loadUiType("layout.ui")[0]

class MyWindow(QMainWindow, Ui_mainDialog):
    def __init__(self):
        super().__init__()
        self.mainDialog = QDialog()
        self.setupUi(self.mainDialog)
        self.setCentralWidget(self.mainDialog)
        self.setGeometry(400, 200, 720, 284)

        self.credentialsDirectoryTextEdit.mousePressEvent = self.on_click_credential_browse
        self.accessibleDirectoryTextEdit.mousePressEvent = self.on_click_accessible_directory
        self.refreshButton.clicked.connect(self.on_click_refresh)
        self.toggleButton.clicked.connect(self.on_click_start)

    # TODO: Display a file browser.
    #       The selected OAuth credentials file's directory
    #       is to be displayed in replacement of the credentialsBrowseButton.
    #       The email address to which the credentials is bound will also
    #       be displayed on boundEmailTextEdit.
    def on_click_credential_browse(self, event):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, fileType = QFileDialog.getOpenFileName(self,"Files", "./","JSON Files (*.json);;All Files (*)", options=options)
        if fileName:
            self.credentialsDirectoryTextEdit.setPlainText(fileName)

    # TODO: Display a driectory browser.
    #       Only the selected directory and its child directories and files
    #       will be available for access to remote clients.
    #       The selected directory is to be displayed on
    #       accessibleDirectoryTextEdit.
    def on_click_accessible_directory(self, event):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        directoryName = QFileDialog.getExistingDirectory(self,"Directory", "./", options=options)
        if directoryName:
            self.accessibleDirectoryTextEdit.setPlainText(directoryName)

    # TODO: Remove all log data?
    # TODO: Make save profile button to save the settings.
    def on_click_refresh(self):
        self.credentialsDirectoryTextEdit.setPlainText("")
        self.accessibleDirectoryTextEdit.setPlainText("")
        self.credentialsRememberCheckBox.setCheckState(False)

    # TODO: Start the program. Connect this to the Driver class.
    def on_click_start(self):
        if self._is_internet_on():
            d = Driver()
            d.begin()
        else:
            print("Check internet connection.")

    def _is_internet_on(self):
        try:
            r = requests.get('https://8.8.8.8')
            return True
        except (requests.ConnectionError, requests.Timeout) as err:
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
