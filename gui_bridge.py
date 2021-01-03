import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

layout = uic.loadUiType("layout.ui")[0]

class MyWindow(QMainWindow, layout):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.on_click_credential_browse()

    # TODO: Display a file browser.
    #       The selected OAuth credentials file's directory
    #       is to be displayed in replacement of the credentialsBrowseButton.
    #       The email address to which the credentials is bound will also
    #       be displayed on boundEmailTextEdit.
    def on_click_credential_browse(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, type = QFileDialog.getOpenFileName(self,"Files", "./","JSON Files (*.json);;All Files (*)", options=options)
        if fileName:
            print(fileName)
            self.removeWidget(self.credentialsBrowseButton)

    # TODO: Display a driectory browser.
    #       Only the selected directory and its child directories and files
    #       will be available for access to remote clients.
    #       The selected directory is to be displayed on
    #       accessibleDirectoryTextEdit.
    def on_click_accessible_directory(self):
        pass

    # TODO: Remove all log data?
    # TODO: Make save profile button to save the settings.
    def on_click_refresh(self):
        pass

    # TODO: Start the program. Connect this to the Driver class.
    def on_click_start(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
