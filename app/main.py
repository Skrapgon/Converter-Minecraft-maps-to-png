from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon, QPixmap

from interface.controller.MainWindowController import MainWindow
import assets.icons.resources

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    icon = QIcon()
    icon.addPixmap(QPixmap(':icon.ico'), QIcon.Mode.Normal, QIcon.State.Off)
    window.setWindowIcon(icon)
    window.show()
    app.exec()