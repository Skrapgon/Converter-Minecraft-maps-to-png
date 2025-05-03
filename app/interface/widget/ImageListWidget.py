from PyQt6.QtWidgets import QListWidget, QListWidgetItem
from PyQt6.QtGui import QDrag, QIcon, QPixmap
from PyQt6.QtCore import Qt, QMimeData, QSize, QByteArray

import io

from PIL.ImageQt import ImageQt

class ImageListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.file_names = []
        self.orig_images = []
        self.setDragEnabled(True)

    def add_image(self, file_path, image):
        self.file_names.append(file_path)
        self.orig_images.append(image)
        tempImage = ImageQt(image)
        tempTableItem = QListWidgetItem(QIcon(QPixmap.fromImage(tempImage).scaled(QSize(256, 256))), '', None)
        self.addItem(tempTableItem)
        
    def remove_image(self, index):
        self.file_names.pop(index)
        self.orig_images.pop(index)
        self.takeItem(index)

    def startDrag(self, action):
        index = self.currentRow()
        
        image = self.orig_images[index]
        
        pixmap = QPixmap.fromImage(ImageQt(image))

        mime_data = QMimeData()
        buffer = io.BytesIO()
        image.save(buffer, 'PNG')
        mime_data.setData('image/png', QByteArray(buffer.getvalue()))

        drag = QDrag(self)
        drag.setMimeData(mime_data)
        drag.setPixmap(pixmap)
        drag.exec(Qt.DropAction.CopyAction)