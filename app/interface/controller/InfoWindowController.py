from PyQt6.QtWidgets import QDialog

from interface.view.InfoWindow_ui import Ui_infoWindow


class InfoWindow(QDialog, Ui_infoWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.info.setText('''<h2>Converter dat-files to png</h2>
        <br>This application converts .dat files of in-game maps into a png file.
        <br>Author: Skrapgon
        <br><a href="https://github.com/Skrapgon/Converter-Minecraft-maps-to-png">github repository</a>
        ''')
        
        self.info.setWordWrap(True)
        self.info.setOpenExternalLinks(True)
        
        self.closeButton.clicked.connect(self.close)
        
        self.setModal(True)
        self.setWindowTitle('About app')