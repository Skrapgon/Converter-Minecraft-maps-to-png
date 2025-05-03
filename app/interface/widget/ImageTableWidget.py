from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QSize

import io

from PIL import Image
from PIL.ImageQt import ImageQt

class ImageTableWidget(QTableWidget):
    def __init__(self, rows, columns, parent=None):
        super().__init__(rows, columns, parent)
        self.images = [[None]]
        self.setIconSize(QSize(128, 128))
        for r in range(rows):
            self.setRowHeight(r, 128)
        for c in range(columns):
            self.setColumnWidth(c, 128)
        
        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DropOnly)
        
    def add_row(self):
        rows = self.rowCount()
        columns = self.columnCount()
        
        self.setRowCount(rows+1)
        self.images.append([None for _ in range(columns)])
        for c in range(columns):
            self.setCellWidget(rows, c, None)
        self.setRowHeight(rows, 128)
    
    def remove_row(self):
        rows = self.rowCount()
        if rows > 1:
            self.removeRow(rows-1)
            self.images.pop()
    
    def add_column(self):
        rows = self.rowCount()
        columns = self.columnCount()
        
        self.setColumnCount(columns+1)
        for r in range(rows):
            self.setCellWidget(r, columns, None)
            self.images[r].append(None)
        self.setColumnWidth(columns, 128)
        
        
    def remove_column(self):
        columns = self.columnCount()
        if columns > 1:
            self.removeColumn(columns-1)
            for image in self.images:
                image.pop()
                
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('image/png'):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasFormat('image/png'):
            data = event.mimeData().data('image/png').data()
            buffer = io.BytesIO(data)
            image = Image.open(buffer).convert('RGBA')
            
            qt_image = ImageQt(image)
            
            pixmap = QPixmap().fromImage(qt_image)

            pos = event.position().toPoint()
            row = self.rowAt(pos.y())
            column = self.columnAt(pos.x())

            if row >= 0 and column >= 0:
                item = QTableWidgetItem()
                item.setIcon(QIcon(pixmap))
                self.setItem(row, column, item)
                self.images[row][column] = image

            event.acceptProposedAction()