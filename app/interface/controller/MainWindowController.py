from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from core.service.convert_dat_to_png import get_image_map, save_images_map
from interface.controller.InfoWindowController import InfoWindow
from interface.view.MainWindow_ui import Ui_mainWindow


class MainWindow(QMainWindow, Ui_mainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.rowNumber.setText('1')
        self.columnNumber.setText('1')
        
        self.addButton.clicked.connect(self.add_files)
        self.deleteButton.clicked.connect(self.delete_files)
        
        self.rowNumberIncrease.clicked.connect(self.change_row)
        self.rowNumberDecrease.clicked.connect(self.change_row)
        
        self.columnNumberIncrease.clicked.connect(self.change_column)
        self.columnNumberDecrease.clicked.connect(self.change_column)
        
        self.saveButton.clicked.connect(self.save_to_png)
        
        self.infoButton.clicked.connect(self.show_info)
        
        self.infoDialog = InfoWindow()
        
        self.setWindowTitle('Converter Minecraft in-game maps to png')
        self.setFixedSize(800, 600)
        
        
    def add_files(self):
        try:
            open_files, _ = QFileDialog.getOpenFileNames(self, 'Open files', './','Dat files (*.dat)')
            for file in open_files:
                if file not in self.mapList.file_names:
                    self.mapList.add_image(file, get_image_map(file))
        except Exception as e:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setWindowTitle('Error')
            msg_box.setText('An error occurred while reading the dat file:')
            msg_box.setInformativeText(str(e))
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
        

    def delete_files(self):
        index = self.mapList.currentRow()
        if index != -1:
            self.mapList.remove_image(index)
          
            
    def change_column(self):
        sender = self.sender()
        if sender == self.columnNumberIncrease:
            self.imageTemporaryTable.add_column()
        else:
            self.imageTemporaryTable.remove_column()
        self.columnNumber.setText(str(self.imageTemporaryTable.columnCount()))


    def change_row(self):
        sender = self.sender()
        if sender == self.rowNumberIncrease:
            self.imageTemporaryTable.add_row()
        else:
            self.imageTemporaryTable.remove_row()
        self.rowNumber.setText(str(self.imageTemporaryTable.rowCount()))
       
                
    def save_to_png(self):
        save_file_path, _ = QFileDialog.getSaveFileName(self, 'Save file', './result.png', 'PNG file (.png)')
        if save_file_path:
            if not save_file_path.lower().endswith('png'):
                save_file_path += '.png'
            save_images_map(self.imageTemporaryTable.images, save_file_path)
        
        
    def show_info(self):
        self.infoDialog.show()