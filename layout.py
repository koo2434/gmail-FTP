# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Louis\Desktop\Projects\gmail@ftp\layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(770, 284)
        self.boundEmailLabel = QtWidgets.QLabel(mainDialog)
        self.boundEmailLabel.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.boundEmailLabel.setObjectName("boundEmailLabel")
        self.boundEmailTextEdit = QtWidgets.QTextEdit(mainDialog)
        self.boundEmailTextEdit.setEnabled(False)
        self.boundEmailTextEdit.setGeometry(QtCore.QRect(10, 90, 321, 31))
        self.boundEmailTextEdit.setReadOnly(False)
        self.boundEmailTextEdit.setObjectName("boundEmailTextEdit")
        self.credentialsRememberCheckBox = QtWidgets.QCheckBox(mainDialog)
        self.credentialsRememberCheckBox.setGeometry(QtCore.QRect(220, 120, 111, 20))
        self.credentialsRememberCheckBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.credentialsRememberCheckBox.setObjectName("credentialsRememberCheckBox")
        self.inboxCheckRateSpinBox = QtWidgets.QSpinBox(mainDialog)
        self.inboxCheckRateSpinBox.setGeometry(QtCore.QRect(260, 150, 41, 22))
        self.inboxCheckRateSpinBox.setMinimum(1)
        self.inboxCheckRateSpinBox.setMaximum(30)
        self.inboxCheckRateSpinBox.setObjectName("inboxCheckRateSpinBox")
        self.inboxCheckRateLabel = QtWidgets.QLabel(mainDialog)
        self.inboxCheckRateLabel.setGeometry(QtCore.QRect(130, 150, 101, 20))
        self.inboxCheckRateLabel.setObjectName("inboxCheckRateLabel")
        self.inboxCheckRateUnitLabel = QtWidgets.QLabel(mainDialog)
        self.inboxCheckRateUnitLabel.setGeometry(QtCore.QRect(300, 150, 21, 20))
        self.inboxCheckRateUnitLabel.setObjectName("inboxCheckRateUnitLabel")
        self.trustedEmailLabel = QtWidgets.QLabel(mainDialog)
        self.trustedEmailLabel.setGeometry(QtCore.QRect(340, 10, 151, 20))
        self.trustedEmailLabel.setObjectName("trustedEmailLabel")
        self.logLabel = QtWidgets.QLabel(mainDialog)
        self.logLabel.setGeometry(QtCore.QRect(540, 10, 31, 20))
        self.logLabel.setObjectName("logLabel")
        self.accessibleDirectoryLabel = QtWidgets.QLabel(mainDialog)
        self.accessibleDirectoryLabel.setGeometry(QtCore.QRect(10, 180, 121, 16))
        self.accessibleDirectoryLabel.setObjectName("accessibleDirectoryLabel")
        self.accessibleDirectoryTextEdit = QtWidgets.QTextEdit(mainDialog)
        self.accessibleDirectoryTextEdit.setGeometry(QtCore.QRect(10, 200, 321, 31))
        self.accessibleDirectoryTextEdit.setObjectName("accessibleDirectoryTextEdit")
        self.refreshButton = QtWidgets.QPushButton(mainDialog)
        self.refreshButton.setGeometry(QtCore.QRect(110, 240, 93, 31))
        self.refreshButton.setObjectName("refreshButton")
        self.toggleButton = QtWidgets.QPushButton(mainDialog)
        self.toggleButton.setGeometry(QtCore.QRect(10, 240, 93, 31))
        self.toggleButton.setObjectName("toggleButton")
        self.credentialsLabel = QtWidgets.QLabel(mainDialog)
        self.credentialsLabel.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.credentialsLabel.setObjectName("credentialsLabel")
        self.credentialsDirectoryTextEdit = QtWidgets.QTextEdit(mainDialog)
        self.credentialsDirectoryTextEdit.setEnabled(True)
        self.credentialsDirectoryTextEdit.setGeometry(QtCore.QRect(10, 30, 321, 31))
        self.credentialsDirectoryTextEdit.setReadOnly(False)
        self.credentialsDirectoryTextEdit.setObjectName("credentialsDirectoryTextEdit")
        self.trustedEmailListWidget = QtWidgets.QListWidget(mainDialog)
        self.trustedEmailListWidget.setGeometry(QtCore.QRect(340, 30, 191, 201))
        self.trustedEmailListWidget.setObjectName("trustedEmailListWidget")
        self.logListWidget = QtWidgets.QListWidget(mainDialog)
        self.logListWidget.setGeometry(QtCore.QRect(540, 30, 221, 201))
        self.logListWidget.setObjectName("logListWidget")
        self.trustedEmailAddressesEditButton = QtWidgets.QPushButton(mainDialog)
        self.trustedEmailAddressesEditButton.setGeometry(QtCore.QRect(342, 240, 191, 31))
        self.trustedEmailAddressesEditButton.setObjectName("trustedEmailAddressesEditButton")
        self.logClearButton = QtWidgets.QPushButton(mainDialog)
        self.logClearButton.setGeometry(QtCore.QRect(540, 240, 221, 31))
        self.logClearButton.setObjectName("logClearButton")

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
        self.refreshButton.setText(_translate("mainDialog", "Refresh"))
        self.toggleButton.setText(_translate("mainDialog", "Start"))
        self.credentialsLabel.setText(_translate("mainDialog", "Credentials"))
        self.trustedEmailAddressesEditButton.setText(_translate("mainDialog", "Edit"))
        self.logClearButton.setText(_translate("mainDialog", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainDialog = QtWidgets.QDialog()
    ui = Ui_mainDialog()
    ui.setupUi(mainDialog)
    mainDialog.show()
    sys.exit(app.exec_())
