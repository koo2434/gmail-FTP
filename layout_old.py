# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Louis/Desktop/Projects/gmail@ftp/layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(563, 284)
        self.boundEmailLabel = QtWidgets.QLabel(mainDialog)
        self.boundEmailLabel.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.boundEmailLabel.setObjectName("boundEmailLabel")
        self.boundEmailTextEdit = QtWidgets.QTextEdit(mainDialog)
        self.boundEmailTextEdit.setEnabled(False)
        self.boundEmailTextEdit.setGeometry(QtCore.QRect(10, 90, 181, 31))
        self.boundEmailTextEdit.setReadOnly(False)
        self.boundEmailTextEdit.setObjectName("boundEmailTextEdit")
        self.credentialsRememberCheckBox = QtWidgets.QCheckBox(mainDialog)
        self.credentialsRememberCheckBox.setGeometry(QtCore.QRect(80, 120, 111, 20))
        self.credentialsRememberCheckBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.credentialsRememberCheckBox.setObjectName("credentialsRememberCheckBox")
        self.inboxCheckRateSpinBox = QtWidgets.QSpinBox(mainDialog)
        self.inboxCheckRateSpinBox.setGeometry(QtCore.QRect(150, 150, 31, 22))
        self.inboxCheckRateSpinBox.setMinimum(1)
        self.inboxCheckRateSpinBox.setMaximum(30)
        self.inboxCheckRateSpinBox.setObjectName("inboxCheckRateSpinBox")
        self.inboxCheckRateLabel = QtWidgets.QLabel(mainDialog)
        self.inboxCheckRateLabel.setGeometry(QtCore.QRect(50, 150, 101, 20))
        self.inboxCheckRateLabel.setObjectName("inboxCheckRateLabel")
        self.inboxCheckRateUnitLabel = QtWidgets.QLabel(mainDialog)
        self.inboxCheckRateUnitLabel.setGeometry(QtCore.QRect(180, 150, 21, 20))
        self.inboxCheckRateUnitLabel.setObjectName("inboxCheckRateUnitLabel")
        self.trustedEmailLabel = QtWidgets.QLabel(mainDialog)
        self.trustedEmailLabel.setGeometry(QtCore.QRect(200, 10, 151, 20))
        self.trustedEmailLabel.setObjectName("trustedEmailLabel")
        self.trustedEmailListView = QtWidgets.QListView(mainDialog)
        self.trustedEmailListView.setGeometry(QtCore.QRect(200, 30, 161, 161))
        self.trustedEmailListView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.trustedEmailListView.setViewMode(QtWidgets.QListView.ListMode)
        self.trustedEmailListView.setObjectName("trustedEmailListView")
        self.logLabel = QtWidgets.QLabel(mainDialog)
        self.logLabel.setGeometry(QtCore.QRect(370, 10, 101, 20))
        self.logLabel.setObjectName("logLabel")
        self.logListView = QtWidgets.QListView(mainDialog)
        self.logListView.setGeometry(QtCore.QRect(370, 30, 181, 161))
        self.logListView.setObjectName("logListView")
        self.accessibleDirectoryLabel = QtWidgets.QLabel(mainDialog)
        self.accessibleDirectoryLabel.setGeometry(QtCore.QRect(20, 210, 121, 16))
        self.accessibleDirectoryLabel.setObjectName("accessibleDirectoryLabel")
        self.accessibleDirectoryTextEdit = QtWidgets.QTextEdit(mainDialog)
        self.accessibleDirectoryTextEdit.setGeometry(QtCore.QRect(140, 200, 311, 31))
        self.accessibleDirectoryTextEdit.setObjectName("accessibleDirectoryTextEdit")
        self.accessibleDirectoryButton = QtWidgets.QPushButton(mainDialog)
        self.accessibleDirectoryButton.setGeometry(QtCore.QRect(460, 200, 91, 31))
        self.accessibleDirectoryButton.setObjectName("accessibleDirectoryButton")
        self.refreshButton = QtWidgets.QPushButton(mainDialog)
        self.refreshButton.setGeometry(QtCore.QRect(360, 240, 93, 31))
        self.refreshButton.setObjectName("refreshButton")
        self.toggleButton = QtWidgets.QPushButton(mainDialog)
        self.toggleButton.setGeometry(QtCore.QRect(460, 240, 93, 31))
        self.toggleButton.setObjectName("toggleButton")
        self.credentialsLabel = QtWidgets.QLabel(mainDialog)
        self.credentialsLabel.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.credentialsLabel.setObjectName("credentialsLabel")
        self.credentialsDirectoryTextEdit = QtWidgets.QTextEdit(mainDialog)
        self.credentialsDirectoryTextEdit.setEnabled(True)
        self.credentialsDirectoryTextEdit.setGeometry(QtCore.QRect(10, 30, 181, 31))
        self.credentialsDirectoryTextEdit.setReadOnly(False)
        self.credentialsDirectoryTextEdit.setObjectName("credentialsDirectoryTextEdit")

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        _translate = QtCore.QCoreApplication.translate
        mainDialog.setWindowTitle(_translate("mainDialog", "Gmail @ FTP"))
        self.boundEmailLabel.setText(_translate("mainDialog", "Bound email address"))
        self.credentialsRememberCheckBox.setText(_translate("mainDialog", "Remember me"))
        self.inboxCheckRateLabel.setText(_translate("mainDialog", "Inbox check rate"))
        self.inboxCheckRateUnitLabel.setText(_translate("mainDialog", "/s"))
        self.trustedEmailLabel.setText(_translate("mainDialog", "Trusted email addresses"))
        self.logLabel.setText(_translate("mainDialog", "Log"))
        self.accessibleDirectoryLabel.setText(_translate("mainDialog", "Accessible directory"))
        self.accessibleDirectoryButton.setText(_translate("mainDialog", "Browse"))
        self.refreshButton.setText(_translate("mainDialog", "Refresh"))
        self.toggleButton.setText(_translate("mainDialog", "Start"))
        self.credentialsLabel.setText(_translate("mainDialog", "Credentials"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainDialog = QtWidgets.QDialog()
    ui = Ui_mainDialog()
    ui.setupUi(mainDialog)
    mainDialog.show()
    sys.exit(app.exec_())
