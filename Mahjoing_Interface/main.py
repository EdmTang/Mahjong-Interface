from mahjongInterface import MahjongInterface
from PySide6 import QtWidgets as qtw, QtCore, QtGui
import sys


app = qtw.QApplication(sys.argv)

interface = MahjongInterface()
interface.show()

sys.exit(app.exec())

'''
tile_images = {}

image_dir = "path/to/images"

for filename in os.listdir(image_dir):
    if filename.endswith(".png"):
        key = os.path.splitext(filename)[0]  # removes ".png"
        tile_images[key] = QPixmap(os.path.join(image_dir, filename))
'''