
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget
from .mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    '''
    
    '''

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
