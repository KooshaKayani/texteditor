import sys

#PYQT5 PyQt4’s QtGui module has been split into PyQt5’s QtGui, QtPrintSupport and QtWidgets modules

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 

#PYQT5 QSpinBox, QMessageBox, QDialog, QPushButton, QGridLayout, QLabel



from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
global Tcolor 
class Table(QtWidgets.QDialog):

    def __init__(self,parent = None):
        QtWidgets.QDialog.__init__(self, parent)

        self.parent = parent
         
        self.initUI()

 
    def initUI(self):
        global Tcolor
        Tcolor = '#ffffff'
        # Rows
        rowsLabel = QtWidgets.QLabel("Rows: ",self)
        
        self.rows = QtWidgets.QSpinBox(self)

        # Columns
        colsLabel = QtWidgets.QLabel("Columns",self)
        
        self.cols = QtWidgets.QSpinBox(self)

        # Cell spacing (distance between cells)
        spaceLabel = QtWidgets.QLabel("Cell spacing",self)

        self.space = QtWidgets.QSpinBox(self)
        self.space.setButtonSymbols(QAbstractSpinBox.NoButtons)
        
        # Cell padding (distance between cell and inner text)
        padLabel = QtWidgets.QLabel("Cell padding",self)

        self.pad = QtWidgets.QSpinBox(self)
        
        self.pad.setValue(10)

        #color button
        colorLable = QtWidgets.QLabel("Color: ",self)
        
        self.color = QtWidgets.QPushButton(self)
        self.color.setMinimumSize(QtCore.QSize(0, 25))
        self.color.setStyleSheet("border: 1px solid;")
        self.color.clicked.connect(self.colorD)

        # Button
        insertButton = QtWidgets.QPushButton("Insert",self)
        insertButton.clicked.connect(self.insert)

        # Layout
        layout = QtWidgets.QGridLayout()

        layout.addWidget(rowsLabel,0,0)
        layout.addWidget(self.rows,0,1)

        layout.addWidget(colsLabel,1,0)
        layout.addWidget(self.cols,1,1)

        layout.addWidget(padLabel,2,0)
        layout.addWidget(self.pad,2,1)
        
        layout.addWidget(spaceLabel,3,0)
        layout.addWidget(self.space,3,1)

        layout.addWidget(colorLable,4,0)
        layout.addWidget(self.color,4,1)

        layout.addWidget(insertButton,5,0,1,2)

        self.setWindowTitle("Insert Table")
        self.setGeometry(300,300,250,180)
        self.setLayout(layout)

    def colorD(self):
        global Tcolor
        Tcolor = QColorDialog.getColor().name()
        self.color.setStyleSheet("border: 1px solid;\n background-color: " + Tcolor + ';' )
        
    def insert(self):
        global Tcolor
        cursor = self.parent.ui.textEdit.textCursor()

        # Get the configurations
        rows = self.rows.value()

        cols = self.cols.value()

        if not rows or not cols:

            popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,
                                      "Parameter error",
                                      "Row and column numbers may not be zero!",
                                      QtWidgets.QMessageBox.Ok,
                                      self)
            popup.show()

        else:

            padding = self.pad.value()

            space = self.space.value()

            # Set the padding and spacing
            fmt = QtGui.QTextTableFormat()
            
            fmt.setCellPadding(padding)

            fmt.setCellSpacing(space)

            fmt.setBackground(QColor(Tcolor))
            fmt.setWidth(QtGui.QTextLength(QtGui.QTextLength.PercentageLength, 100))
            
            
            # Inser the new table
            cursor.insertTable(rows,cols,fmt)






