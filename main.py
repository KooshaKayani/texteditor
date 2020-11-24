
import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# GUI FILE
from ui_main import Ui_MainWindow
#from table_sample import Ui_Table
from ext import table_sample
FONT_SIZES = [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288]

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self,parent)
        self.filename = ""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        
    # We need references to these actions/settings to update as selection changes, so attach to self.
        self.fonts = QFontComboBox()
        self.fonts.currentFontChanged.connect(self.ui.textEdit.setCurrentFont)
        self.ui.toolBar.addWidget(self.fonts)

        self.fontsize = QComboBox()
        self.fontsize.addItems([str(s) for s in FONT_SIZES])

    # Connect to the signal producing the text of the current selection. Convert the string to float
    # and set as the pointsize. We could also use the index + retrieve from FONT_SIZES.
        self.fontsize.currentIndexChanged[str].connect(lambda s: self.ui.textEdit.setFontPointSize(float(s)) )
        self.ui.toolBar.addWidget(self.fontsize)
    # connecting all the actions 
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionOpen.triggered.connect(self.open)
        self.ui.actioncolor.triggered.connect(self.Changecolor)
        self.ui.actionHighlight_text.triggered.connect(self.Highlight)
        self.ui.actionIndents.triggered.connect(self.addIndents)
        self.ui.actionTable.triggered.connect(self.inserttable)
        self.ui.actionBullet_Points.triggered.connect(self.BulletList)
        self.ui.actionalignLeft.triggered.connect(self.alignLeft)
        self.ui.actionAlignRight.triggered.connect(self.alignRight)
        self.ui.actionAlign_center.triggered.connect(self.alignCenter)
        self.ui.actionNumber_List.triggered.connect(self.NumberedList)
        self.ui.actionUnderline.triggered.connect(self.Underl)
        self.ui.actionItalic.triggered.connect(self.Italic)
        self.ui.actionimage.triggered.connect(self.insertImage)
        self.ui.actionBold.triggered.connect(self.Bold)
        self.ui.actionHTML.triggered.connect(self.HTML)
        self.ui.actionTEXT.triggered.connect(self.HTtoText)
        self.ui.textEdit.textChanged.connect(self.HTML)
        #self.ui.htmlEdit.textChanged.connect(self.HTtoText)
        
        # We need our own context menu for tables
        self.ui.textEdit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.textEdit.customContextMenuRequested.connect(self.context)


    # all the functions for the tool bar
    def HTML(self):
        self.ui.htmlEdit.setPlainText(str(self.ui.textEdit.toHtml()))
    
    def HTtoText(self):
        self.savecode()
        with open(self.filename +' code.txt',"r") as filec:
            self.ui.textEdit.setText(filec.read())


    def Changecolor(self):
        color = QColorDialog.getColor()
        self.ui.textEdit.setTextColor(color)
    
    def Highlight(self):
        color = QColorDialog.getColor()
        self.ui.textEdit.setTextBackgroundColor(color)

    def inserttable(self):
        """Launch the employee dialog."""
        dlg = EmployeeDlg(self)
        dlg.exec()

    def addIndents(self):
        # Grab the cursor
        cursor = self.ui.textEdit.textCursor()

        if cursor.hasSelection():

            # Store the current line/block number
            temp = cursor.blockNumber()

            # Move to the selection's end
            cursor.setPosition(cursor.anchor())

            # Calculate range of selection
            diff = cursor.blockNumber() - temp

            direction = QtGui.QTextCursor.Up if diff > 0 else QtGui.QTextCursor.Down

            # Iterate over lines (diff absolute value)
            for n in range(abs(diff) + 1):

                # Move to start of each line
                cursor.movePosition(QtGui.QTextCursor.StartOfLine)

                # Insert tabbing
                cursor.insertText("\t")

                # And move back up
                cursor.movePosition(direction)

        # If there is no selection, just insert a tab
        else:
            cursor.insertText("\t")

    def context(self,pos):

        # Grab the cursor
        cursor = self.ui.textEdit.textCursor()

        # Grab the current table, if there is one
        table = cursor.currentTable()

        # Above will return 0 if there is no current table, in which case
        # we call the normal context menu. If there is a table, we create
        # our own context menu specific to table interaction
        if table:

            menu = QtWidgets.QMenu(self)

            appendRowAction = QtWidgets.QAction("Append row",self)
            appendRowAction.triggered.connect(lambda: table.appendRows(1))

            appendColAction = QtWidgets.QAction("Append column",self)
            appendColAction.triggered.connect(lambda: table.appendColumns(1))


            removeRowAction = QtWidgets.QAction("Remove row",self)
            removeRowAction.triggered.connect(self.removeRow)

            removeColAction = QtWidgets.QAction("Remove column",self)
            removeColAction.triggered.connect(self.removeCol)


            insertRowAction = QtWidgets.QAction("Insert row",self)
            insertRowAction.triggered.connect(self.insertRow)

            insertColAction = QtWidgets.QAction("Insert column",self)
            insertColAction.triggered.connect(self.insertCol)


            mergeAction = QtWidgets.QAction("Merge cells",self)
            mergeAction.triggered.connect(lambda: table.mergeCells(cursor))

            # Only allow merging if there is a selection
            if not cursor.hasSelection():
                mergeAction.setEnabled(False)


            splitAction = QtWidgets.QAction("Split cells",self)

            cell = table.cellAt(cursor)

            # Only allow splitting if the current cell is larger
            # than a normal cell
            if cell.rowSpan() > 1 or cell.columnSpan() > 1:

                splitAction.triggered.connect(lambda: table.splitCell(cell.row(),cell.column(),1,1))

            else:
                splitAction.setEnabled(False)


            menu.addAction(appendRowAction)
            menu.addAction(appendColAction)

            menu.addSeparator()

            menu.addAction(removeRowAction)
            menu.addAction(removeColAction)

            menu.addSeparator()

            menu.addAction(insertRowAction)
            menu.addAction(insertColAction)

            menu.addSeparator()

            menu.addAction(mergeAction)
            menu.addAction(splitAction)

            # Convert the widget coordinates into global coordinates
            pos = self.mapToGlobal(pos)

            # Add pixels for the tool and formatbars, which are not included
            # in mapToGlobal(), but only if the two are currently visible and
            # not toggled by the user

            '''if self.toolbar.isVisible():
                pos.setY(pos.y() + 45)

            if self.formatbar.isVisible():
                pos.setY(pos.y() + 45)'''
                
            # Move the menu to the new position
            menu.move(pos)

            menu.show()

        else:

            event = QtGui.QContextMenuEvent(QtGui.QContextMenuEvent.Mouse,QtCore.QPoint())

            self.ui.textEdit.contextMenuEvent(event)

    def removeRow(self):

        # Grab the cursor
        cursor = self.ui.textEdit.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Delete the cell's row
        table.removeRows(cell.row(),1)

    def removeCol(self):

        # Grab the cursor
        cursor = self.ui.textEdit.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Delete the cell's column
        table.removeColumns(cell.column(),1)

    def insertRow(self):

        # Grab the cursor
        cursor = self.ui.textEdit.textCursor()


        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Insert a new row at the cell's position
        table.insertRows(cell.row(),1)

    def insertCol(self):

        # Grab the cursor
        cursor = self.ui.textEdit.textCursor()


        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Insert a new row at the cell's position
        table.insertColumns(cell.column(),1)

    def insertImage(self):

        # Get image file name
        #PYQT5 Returns a tuple in PyQt5
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Insert image',".","Images (*.png *.xpm *.jpg *.bmp *.gif)")[0]

        if filename:
            
            # Create image object
            image = QtGui.QImage(filename)

            # Error if unloadable
            if image.isNull():

                popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                          "Image load error",
                                          "Could not load image file!",
                                          QtWidgets.QMessageBox.Ok,
                                          self)
                popup.show()

            else:

                cursor = self.ui.textEdit.textCursor()

                cursor.insertImage(image,filename)
                cursor.insertTable(12,12)
    
    def Underl(self):
        ul = self.ui.textEdit.fontUnderline()
 
        if ul == False:
            self.ui.textEdit.setFontUnderline(True) 
        elif ul == True:
            self.ui.textEdit.setFontUnderline(False)

    def Bold(self):
        w = self.ui.textEdit.fontWeight()
        if w == 50:
            self.ui.textEdit.setFontWeight(QFont.Bold)
        elif w == 75:
            self.ui.textEdit.setFontWeight(QFont.Normal)
         
    def Italic(self):
        i = self.ui.textEdit.fontItalic()
         
        if i == False:
            self.ui.textEdit.setFontItalic(True)
        elif i == True:
            self.ui.textEdit.setFontItalic(False)
        
    def alignLeft(self):
        self.ui.textEdit.setAlignment(Qt.AlignLeft)
 
    def alignRight(self):
        self.ui.textEdit.setAlignment(Qt.AlignRight)
 
    def alignCenter(self):
        self.ui.textEdit.setAlignment(Qt.AlignCenter)

    def BulletList(self):
        print("bullet connects!")
        self.ui.textEdit.insertHtml("<ul><li>&nbsp;</li></ul>")

    def NumberedList(self):
        print("numbered connects!")
        self.ui.textEdit.insertHtml("<ol><li>&nbsp;</li></ol>")

    def open(self):
        try:        
            self.filename = QFileDialog.getOpenFileName(self, 'Open File')[0]
            if self.filename:
                with open(self.filename,"r") as file:
                    self.ui.textEdit.setText(file.read())
        except:
            print("Open Error")


    def save(self):
        try:
        
            if str(self.filename) == "":
                self.filename =QFileDialog.getSaveFileName(self, 'Save File')[0]
            print(self.filename)
            if str(self.filename).endswith(".txt") == False and len(str(self.filename)) > 0:
                self.filename = str(self.filename) + ".txt"
            
            with open(self.filename, 'w') as file:
                file.write(self.ui.textEdit.toPlainText())
            
        except:
            print("Save Error")

    def savecode(self):
        try:
        
            if str(self.filename) == "":
                self.filename =QFileDialog.getSaveFileName(self, 'Save File')[0]
            print(self.filename)
            if str(self.filename).endswith(".txt") == False and len(str(self.filename)) > 0:
                self.filename = str(self.filename) + ".txt"
            
            with open(self.filename+' code.txt', 'w') as file:
                file.write(self.ui.htmlEdit.toPlainText())
            
        except:
            print("Save Error")

class EmployeeDlg(QDialog):
    """Employee dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = table_sample.Table()
        # Run the .setupUi() method to show the GUI
        self.ui.initUI(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
