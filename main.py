from gui import Window

import sys

from PyQt5.QtWidgets import (

    QApplication, QDialog, QMainWindow, QMessageBox

)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    win = Window()

    win.show()

    app.exec()