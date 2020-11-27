# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tablev2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(350, 350))
        Dialog.setMaximumSize(QtCore.QSize(350, 350))
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(-1, 10, -1, 0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.rowlable = QtWidgets.QLabel(self.frame)
        self.rowlable.setObjectName("rowlable")
        self.gridLayout.addWidget(self.rowlable, 0, 0, 1, 1)
        self.Rows = QtWidgets.QSpinBox(self.frame)
        self.Rows.setMinimumSize(QtCore.QSize(100, 25))
        self.Rows.setStyleSheet("border:1px solid;\n"
"border-color: rgb(0, 0, 0);")
        self.Rows.setObjectName("Rows")
        self.gridLayout.addWidget(self.Rows, 0, 1, 1, 1)
        self.columnlable = QtWidgets.QLabel(self.frame)
        self.columnlable.setObjectName("columnlable")
        self.gridLayout.addWidget(self.columnlable, 1, 0, 1, 1)
        self.Column = QtWidgets.QSpinBox(self.frame)
        self.Column.setMinimumSize(QtCore.QSize(100, 25))
        self.Column.setStyleSheet("border:1px solid;\n"
"border-color: rgb(0, 0, 0);")
        self.Column.setObjectName("Column")
        self.gridLayout.addWidget(self.Column, 1, 1, 1, 1)
        self.paddinglable = QtWidgets.QLabel(self.frame)
        self.paddinglable.setObjectName("paddinglable")
        self.gridLayout.addWidget(self.paddinglable, 2, 0, 1, 1)
        self.padding = QtWidgets.QSpinBox(self.frame)
        self.padding.setMinimumSize(QtCore.QSize(100, 25))
        self.padding.setStyleSheet("border:1px solid;\n"
"border-color: rgb(0, 0, 0);")
        self.padding.setObjectName("padding")
        self.gridLayout.addWidget(self.padding, 2, 1, 1, 1)
        self.spacinglable = QtWidgets.QLabel(self.frame)
        self.spacinglable.setObjectName("spacinglable")
        self.gridLayout.addWidget(self.spacinglable, 3, 0, 1, 1)
        self.spacing = QtWidgets.QSpinBox(self.frame)
        self.spacing.setMinimumSize(QtCore.QSize(100, 25))
        self.spacing.setStyleSheet("border:1px solid;\n"
"border-color: rgb(0, 0, 0);")
        self.spacing.setObjectName("spacing")
        self.gridLayout.addWidget(self.spacing, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.color = QtWidgets.QPushButton(self.frame)
        self.color.setMinimumSize(QtCore.QSize(0, 25))
        self.color.setStyleSheet("border: 1px solid;")
        self.color.setText("")
        self.color.setObjectName("color")
        self.gridLayout.addWidget(self.color, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ok = QtWidgets.QPushButton(self.frame_2)
        self.ok.setMinimumSize(QtCore.QSize(80, 25))
        self.ok.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ok.setFont(font)
        self.ok.setStyleSheet("border : 1px solid;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.ok.setObjectName("ok")
        self.verticalLayout_2.addWidget(self.ok)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.rowlable.setText(_translate("Dialog", "Rows:"))
        self.columnlable.setText(_translate("Dialog", "Column:"))
        self.paddinglable.setText(_translate("Dialog", "Padding:"))
        self.spacinglable.setText(_translate("Dialog", "Spacing:"))
        self.label.setText(_translate("Dialog", "Color:"))
        self.ok.setText(_translate("Dialog", "ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())