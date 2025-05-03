from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon

import os

from interface.controller.MainWindowController import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.setWindowIcon(QIcon(os.path.join(os.path.curdir, 'app/assets/icons/icon.ico')))
    window.show()
    app.exec()