import sys
import os

from command import CommandModule

import PySide6.QtCore as QtCore
from PySide6.QtCore import QDate, QFile, Qt, QTextStream
from PySide6.QtGui import (QAction, QFont, QIcon, QKeySequence,
                           QTextCharFormat, QTextCursor, QTextTableFormat)
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtWidgets import (QApplication, QDialog, QDockWidget,
                               QFileDialog, QListWidget, QMainWindow,
                               QMessageBox, QTextEdit, QLineEdit)
from PySide6.QtCore import QTime, QTimer
from PySide6.QtWidgets import QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._text_edit = QTextEdit()
        self._text_edit.setFont(QFont("Courier", 9))
        self.setCentralWidget(self._text_edit)

        self.create_actions()
        self.create_menus()
        self.create_tool_bars()
        self.create_status_bar()
        self.create_dock_windows()

        self.cm = CommandModule(parent=self)

        self.setWindowTitle('Command Lab')

        self.new_letter()
        self._text_edit.setReadOnly(True)

        self.command_history = []
        self.command_history_index = -1

        self.init_timer()
        self.showTime()

        self.showMaximized()

    def console_log(self, msg, err=False):
        if err:
            self._text_edit.setTextColor('red')
        else:
            self._text_edit.setTextColor('white')
        self._text_edit.insertPlainText(msg + '\n')
        # color = ''
        # if err:
        #     color = ' style="color:red"'
        # self._text_edit.insertHtml(f'<p{color}>{msg}</p>')
        # self._text_edit.insertPlainText('\n')

    def init_timer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

    def create_actions(self):
        icon = QIcon.fromTheme('document-new', QIcon(':/images/new.png'))
        self._new_letter_act = QAction(icon, "&New Letter", self, shortcut=QKeySequence.New,
                                       statusTip="Create a new form letter",
                                       triggered=self.new_letter)

        icon = QIcon.fromTheme('document-save', QIcon(':/images/save.png'))
        self._save_act = QAction(icon, "&Save...", self, shortcut=QKeySequence.Save,
                                 statusTip="Save the current form letter", triggered=self.save)

        icon = QIcon.fromTheme('document-print', QIcon(':/images/print.png'))
        self._print_act = QAction(icon, "&Print...", self, shortcut=QKeySequence.Print,
                                  statusTip="Print the current form letter",
                                  triggered=self.print_)

        icon = QIcon.fromTheme('edit-undo', QIcon(':/images/undo.png'))
        self._undo_act = QAction(icon, "&Undo", self, shortcut=QKeySequence.Undo,
                                 statusTip="Undo the last editing action", triggered=self.undo)

        self._quit_act = QAction("&Quit", self, shortcut="Ctrl+Q",
                                 statusTip="Quit the application", triggered=self.close)

        self._about_act = QAction("&About", self, statusTip="Show the application's About box",
                                  triggered=self.about)

        self._about_qt_act = QAction("About &Qt", self, statusTip="Show the Qt library's About box",
                                     triggered=QApplication.instance().aboutQt)

    def create_menus(self):
        self._file_menu = self.menuBar().addMenu("&File")
        self._file_menu.addAction(self._new_letter_act)
        self._file_menu.addAction(self._save_act)
        self._file_menu.addAction(self._print_act)
        self._file_menu.addSeparator()
        self._file_menu.addAction(self._quit_act)

        self._edit_menu = self.menuBar().addMenu("&Edit")
        self._edit_menu.addAction(self._undo_act)

        self._view_menu = self.menuBar().addMenu("&View")

        self.menuBar().addSeparator()

        self._help_menu = self.menuBar().addMenu("&Help")
        self._help_menu.addAction(self._about_act)
        self._help_menu.addAction(self._about_qt_act)

    def create_tool_bars(self):
        self._file_tool_bar = self.addToolBar("File")
        self._file_tool_bar.addAction(self._new_letter_act)
        self._file_tool_bar.addAction(self._save_act)
        self._file_tool_bar.addAction(self._print_act)

        self._edit_tool_bar = self.addToolBar("Edit")
        self._edit_tool_bar.addAction(self._undo_act)

    def create_status_bar(self):
        self.statusBar().showMessage(f'{os.getcwd()}\t\t\tmain display: command line log')

    def create_dock_windows(self):
        dock = QDockWidget("Clock", self)
        dock.setAllowedAreas(QtCore.Qt.DockWidgetArea.AllDockWidgetAreas)
        self._clock = QLineEdit()
        self._clock.setTextMargins(5, 5, 5, 5)
        self._clock.installEventFilter(self)
        dock.setWidget(self._clock)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        self._view_menu.addAction(dock.toggleViewAction())
        self._clock.setDisabled(True)

        dock = QDockWidget("Customers", self)
        dock.setAllowedAreas(QtCore.Qt.DockWidgetArea.AllDockWidgetAreas)
        self._customer_list = QListWidget(dock)
        self._customer_list.addItems(('x', 'y', 'z'))
        self._customer_list.setWordWrap(True)
        dock.setWidget(self._customer_list)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        self._view_menu.addAction(dock.toggleViewAction())

        dock = QDockWidget("File System", self)
        dock.setAllowedAreas(QtCore.Qt.DockWidgetArea.AllDockWidgetAreas)
        self._customer_list2 = QListWidget(dock)
        self._customer_list2.addItems(('x', 'y', 'z'))
        self._customer_list2.setWordWrap(True)
        dock.setWidget(self._customer_list2)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        self._view_menu.addAction(dock.toggleViewAction())

        dock = QDockWidget('Command Line', self)
        dock.setAllowedAreas(QtCore.Qt.DockWidgetArea.AllDockWidgetAreas)
        self.command_box = QLineEdit()
        self.command_box.setTextMargins(5, 5, 5, 5)
        self.command_box.installEventFilter(self)
        dock.setWidget(self.command_box)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        self._view_menu.addAction(dock.toggleViewAction())

        # self._customer_list.currentTextChanged.connect(self.insert_customer)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.command_box:
            if event.key() == QtCore.Qt.Key_Return and self.command_box.hasFocus():
                self.run_cmd()
            if event.key() == QtCore.Qt.Key_Up and self.command_box.hasFocus():
                self.scroll_history_back()
            if event.key() == QtCore.Qt.Key_Down and self.command_box.hasFocus():
                self.scroll_history_forward()
        return super().eventFilter(obj, event)

    def run_cmd(self):
        text = self.command_box.text()
        if text == '':
            return
        self.command_history.insert(0, text)
        self.console_log(f'> {text}')
        self.cm.exec(text)

        self.command_box.clear()

    def scroll_history_back(self):
        cmd = ''
        if self.command_history_index < len(self.command_history) - 1:
            self.command_history_index += 1
        if self.command_history_index > -1:
            cmd = self.command_history[self.command_history_index]
        self.command_box.setText(cmd)

    def scroll_history_forward(self):
        cmd = ''
        if self.command_history_index > -1:
            self.command_history_index -= 1
            cmd = self.command_history[self.command_history_index]
        self.command_box.setText(cmd)


    def new_letter(self):
        self._text_edit.clear()

        cursor = self._text_edit.textCursor()
        cursor.movePosition(QTextCursor.Start)

    def print_(self):
        document = self._text_edit.document()
        printer = QPrinter()

        dlg = QPrintDialog(printer, self)
        if dlg.exec() != QDialog.Accepted:
            return

        document.print_(printer)

        self.statusBar().showMessage(os.getcwd(), 2000)

    def save(self):
        dialog = QFileDialog(self, "Choose a file name")
        dialog.setMimeTypeFilters(['text/html'])
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setDefaultSuffix('html')
        if dialog.exec() != QDialog.Accepted:
            return

        filename = dialog.selectedFiles()[0]
        file = QFile(filename)
        if not file.open(QFile.WriteOnly | QFile.Text):
            reason = file.errorString()
            QMessageBox.warning(self, "Dock Widgets",
                                f"Cannot write file {filename}:\n{reason}.")
            return

        out = QTextStream(file)
        with QApplication.setOverrideCursor(Qt.WaitCursor):
            out << self._text_edit.toHtml()

        self.statusBar().showMessage(f"Saved '{filename}'", 2000)

    def undo(self):
        document = self._text_edit.document()
        document.undo()

    def insert_customer(self, customer):
        if not customer:
            return
        customer_list = customer.split(', ')
        document = self._text_edit.document()
        cursor = document.find('NAME')
        if not cursor.isNull():
            cursor.beginEditBlock()
            cursor.insertText(customer_list[0])
            oldcursor = cursor
            cursor = document.find('ADDRESS')
            if not cursor.isNull():
                for i in customer_list[1:]:
                    cursor.insertBlock()
                    cursor.insertText(i)
                cursor.endEditBlock()
            else:
                oldcursor.endEditBlock()

    def add_paragraph(self, paragraph):
        if not paragraph:
            return
        document = self._text_edit.document()
        cursor = document.find("Yours sincerely,")
        if cursor.isNull():
            return
        cursor.beginEditBlock()
        cursor.movePosition(QTextCursor.PreviousBlock,
                            QTextCursor.MoveAnchor, 2)
        cursor.insertBlock()
        cursor.insertText(paragraph)
        cursor.insertBlock()
        cursor.endEditBlock()

    def about(self):
        QMessageBox.about(self, "About Dock Widgets",
                          "The <b>Dock Widgets</b> example demonstrates how to use "
                          "Qt's dock widgets. You can enter your own text, click a "
                          "customer to add a customer name and address, and click "
                          "standard paragraphs to add them.")

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh  :  mm  :  ss')
        self._clock.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())



# autocomplete example: https://stackoverflow.com/questions/28956693/pyqt5-qtextedit-auto-completion