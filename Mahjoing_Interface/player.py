from PySide6 import QtWidgets as qtw, QtCore as qtc


class player(qtw.QWidget):

    affirm = qtc.Signal(int)

    def __init__(self, form):
        super().__init__()
        self.number = None
        self.hand = qtw.QWidget()
        self.sets = qtw.QWidget()
        self.buttons = qtw.QWidget()
        self.cancel = qtw.QPushButton("Cancel")
        self.pong = qtw.QPushButton("Pong")
        self.chow = qtw.QPushButton("Chow")
        self.kong = qtw.QPushButton("Kong")
        self.hu = qtw.QPushButton("Hu")
        self.zimo = qtw.QPushButton("Zimo")
        self.interacts = [self.pong, self.chow, self.kong, self.hu, self.zimo, self.cancel]
        for button in self.interacts:
            # button.setEnabled(False)
            if button == self.cancel:
                button.clicked.connect(self.canceled)
            else:
                button.clicked.connect(self.pressed)
            button.setStyleSheet("""
                QPushButton {
                    background-color: lightgreen;
                    color: black;
                    border-radius: 5px;
                    padding: 5px;
                }
                QPushButton:disabled {
                    background-color: lightgray;
                    color: darkgray;
                }
                """)
        if form == 1:
            self.__player1Layout()
        elif form == 2:
            self.__player2Layout()
        elif form == 3:
            self.__player3Layout()
        elif form == 4:
            self.__player4Layout()

    def __player1Layout(self):
        self.number = 1
        self.setLayout(qtw.QVBoxLayout())
        self.hand.setLayout(qtw.QHBoxLayout())
        self.sets.setLayout(qtw.QHBoxLayout())
        self.buttons.setLayout(qtw.QHBoxLayout())
        self.__constructButtons()
        self.layout().addWidget(self.buttons)
        self.layout().addWidget(self.sets)
        self.layout().addWidget(self.hand)

    def __player2Layout(self):
        self.number = 2
        self.setLayout(qtw.QHBoxLayout())
        self.hand.setLayout(qtw.QVBoxLayout())
        self.sets.setLayout(qtw.QVBoxLayout())
        self.buttons.setLayout(qtw.QVBoxLayout())
        self.__constructButtons()
        self.layout().addWidget(self.buttons)
        self.layout().addWidget(self.sets)
        self.layout().addWidget(self.hand)

    def __player3Layout(self):
        self.number = 3
        self.setLayout(qtw.QVBoxLayout())
        self.hand.setLayout(qtw.QHBoxLayout())
        self.sets.setLayout(qtw.QHBoxLayout())
        self.buttons.setLayout(qtw.QHBoxLayout())
        self.__constructButtons()
        self.layout().addWidget(self.hand)
        self.layout().addWidget(self.sets)
        self.layout().addWidget(self.buttons)

    def __player4Layout(self):
        self.number = 4
        self.setLayout(qtw.QHBoxLayout())
        self.hand.setLayout(qtw.QVBoxLayout())
        self.sets.setLayout(qtw.QVBoxLayout())
        self.buttons.setLayout(qtw.QVBoxLayout())
        self.__constructButtons()
        self.layout().addWidget(self.hand)
        self.layout().addWidget(self.sets)
        self.layout().addWidget(self.buttons)

    def __constructButtons(self):
        self.buttons.layout().addWidget(self.cancel)
        self.buttons.layout().addWidget(self.pong)
        self.buttons.layout().addWidget(self.chow)
        self.buttons.layout().addWidget(self.kong)
        self.buttons.layout().addWidget(self.hu)
        self.buttons.layout().addWidget(self.zimo)

    def pressed(self, checked):
        for button in self.interacts:
            button.setEnabled(False)
        self.cancel.setEnabled(False)
        if button != self.chow:
            self.affirm.emit(1)

    def canceled(self, checked):
        for button in self.interacts:
            button.setEnabled(False)
        self.cancel.setEnabled(False)
        self.affirm.emit(0)