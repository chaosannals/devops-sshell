import sys
from PySide6.QtWidgets import QApplication
from dossh.view.mainwindow import MainWindow

def main():
    '''
    
    '''

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    return app.exec()

if '__main__' == __name__:
    main()