from PySide6 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg
import sys


# function that turns array of tiles in text form into array of QPixmaps
def meld(choice, vertical=False):
    # convert plain text to QPixmap and store results in images
    images = []
    # Populate images array with pixmap
    for tile in range(len(choice)):
        images.append(qtg.QPixmap(f"mahjong_tiles/{choice[tile]}.png"))
    # Go through list of choice and return a list of QPiximages
    if vertical is False:
        
        # Create a combined pixmap
        width = images[0].width()*len(images)
        height = images[0].height()
        combined = qtg.QPixmap(width, height)
        combined.fill()  # optional: transparent background
        # Paint both pixmaps into the combined one
        painter = qtg.QPainter(combined)
        currWidth = 0

        for pix in images:   
            painter.drawPixmap(currWidth, 0, pix)
            currWidth += pix.width()

        painter.end()
        return combined
    else:

        # Create a combined pixmap
        height = images[0].height()*len(images)
        width = images[0].width()
        combined = qtg.QPixmap(width, height)
        combined.fill()  # optional: transparent background
        # Paint both pixmaps into the combined one
        painter = qtg.QPainter(combined)
        currheight = 0

        for pix in images:   
            painter.drawPixmap(0, currheight, pix)
            currheight += pix.height()

        painter.end()
        return combined


class ActionInterface(qtw.QWidget):

    submitted = qtc.Signal(list)
    picked = qtc.Signal(int)

    # loop through the list and create the buttons for each meld
    def __init__(self, choices):
        super().__init__()

        self.setWindowTitle("Action Window")
        self.setLayout(qtw.QHBoxLayout())
        # there will be multiple buttons, dependent on how many choices of chows there are
        # test choices
        choices = [
            ["red", "red", "red"],
            ["green", "green", "green"],
            ["white", "white", "white"],
            ["wan1", "wan1", "wan1"]
        ]
        for choice in range(len(choices)):
            currentMeld = meld(choices[choice]) # placeholder QPixmap
            self.choice = qtw.QPushButton(f"{choice}", icon=qtg.QIcon(currentMeld))
            # n ensures current value of choice is captured and not the final one after the loop
            self.choice.clicked.connect(lambda checked, n=choices[choice], decision=choice: self.submit(n, decision)) 
            self.choice.setIconSize(qtc.QSize(currentMeld.width(), currentMeld.height()))
            self.layout().addWidget(self.choice)
        
        self.resize(400, 200)

    def submit(self, tiles, decision):
        # will return a pixmap for now, this will represent what meld was chosen
        self.submitted.emit(tiles)
        self.picked.emit(decision)
        print("success")
        self.close()


if __name__ == "__main__":
    base = qtw.QApplication(sys.argv)
    actionTester = ActionInterface(list[list])
    actionTester.show()
    sys.exit(base.exec())
