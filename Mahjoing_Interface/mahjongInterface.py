from PySide6 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg
from borderlayout import BorderLayout, Position
from action_interface import ActionInterface, meld
from player import player as plyr
import os
import random


BASEDIR = os.path.dirname("__file__")


class MahjongInterface(qtw.QWidget):

    pingPong = qtc.Signal(plyr)
    pingKong = qtc.Signal(plyr)
    pingChow = qtc.Signal(plyr, list[list])
    pingHu = qtc.Signal(plyr)
    pingZimo = qtc.Signal(plyr)
    discarded = qtc.Signal(int)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bootleg Mahjong")

        # place holder lables, self.player3 will have tiles hidden from other players and self.player3Sets will have sets shown to players
        # test buttons will be replaced by custom signals
        
        self.player1 = plyr(1)
        self.player1.chow.clicked.connect(lambda checked: self.chow(self.player1))
        self.player1.chow.setEnabled(True) # will be enabled at the start of the game for testing purposes

        self.player2 = plyr(2)
        self.player2.chow.clicked.connect(lambda checked: self.chow(self.player2))
        self.player2.chow.setEnabled(True) # will be enabled at the start of the game for testing purposes

        self.player3 = plyr(3)
        self.player3.chow.clicked.connect(lambda checked: self.chow(self.player3))
        self.player3.chow.setEnabled(True) # will be enabled at the start of the game for testing purposes

        self.player4 = plyr(4)
        self.player4.chow.clicked.connect(lambda checked: self.chow(self.player4))
        self.player4.chow.setEnabled(True) # will be enabled at the start of the game for testing purposes

        self.discard = qtw.QWidget()
        self.discard.setStyleSheet("background-color: rgb(0, 80, 0);")
        self.discard.setLayout(qtw.QHBoxLayout())
        self.discard.layout().addWidget(qtw.QLabel("discard", alignment=qtc.Qt.AlignCenter))
        # border layout for whole mahjong game layout-----------------------
        self.layout = BorderLayout()

        self.layout.addWidget(self.player1, Position.South)
        self.layout.addWidget(self.player2, Position.East)
        self.layout.addWidget(self.player3, Position.North)
        self.layout.addWidget(self.player4, Position.West)

        self.layout.addWidget(self.discard, Position.Center)

        self.setLayout(self.layout)

        self.resize(1910, 1000)

        self.currentChow = list[list] # stores the current chow that is to be shown to player
        # Buttons will become enabled when their repsective Signal is emitted
        self.pingChow.connect(lambda player, setChoices: self.enable_chow(player, setChoices))
        self.pingPong.connect(lambda player: self.enable_pong(player))
        self.pingKong.connect(lambda player: self.enable_kong(player))
        self.pingZimo.connect(lambda player: self.enable_zimo(player))
        self.pingHu.connect(lambda player: self.enable_hu(player))

    # Actions(chow, pung, win, etc) will first be prompted by buttons. if chow is chosen; action window gets prompted
    # choices for Chow will be in this seperate window.
    def enable_chow(self, player, sets):
        self.currentChow = sets
        player.chow.setEnabled(True)

    def enable_pong(self, player):
        player.pong.setEnabled(True)

    def enable_kong(self, player):
        player.kong.setEnabled(True)

    def enable_zimo(self, player):
        player.zimo.setEnabled(True)

    def enable_hu(self, player):
        player.hu.setEnabled(True)

    def chow(self, player): # array of sets stored in self.currentChow
        self.actionWindow = ActionInterface(self.currentChow)
        self.actionWindow.submitted.connect(lambda choice: self.updateSets(player, choice))
        self.actionWindow.submitted.connect(lambda: self.refreshHand(player.hand))
        self.actionWindow.show()

    def updateSets(self, player, chosen):
        if player.number == 2 or player.number == 4:
            player.sets.layout().addWidget(qtw.QLabel(pixmap=meld(chosen, True)))  # appends the new set to current set
        else:
            player.sets.layout().addWidget(qtw.QLabel(pixmap=meld(chosen)))  # appends the new set to current set

    # loops through array hand to refresh tiles being displayed
    def refreshHand(self, playerHand, hand=[1]*14):
        # clearing hand
        while playerHand.layout().count():
            item = playerHand.layout().takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        # Regenerating Hand
        for times in range(len(hand)): # test loop, ment to loop through array hand
            randnum = random.randint(1, 9) # remove when hand array has actual tile names
            newbutton = qtw.QPushButton(f"{times}",icon=qtg.QIcon(meld([f"wan{randnum}"]))) # replace meld input with tile name in array hand when not testing
            newbutton.setIconSize(qtc.QSize(128, 64))
            newbutton.clicked.connect(lambda checked: self.remove(playerHand, times))
            playerHand.layout().addWidget(newbutton)

    # playerHand can be removed from parameters for finished product
    def remove(self, playerHand, tileNumber):
        self.discarded.emit(tileNumber)
        self.refreshHand(playerHand=playerHand) # for testing purposes, to force a refresh on the hand after clicking

# custom signals, Master pyqt part 4
# Moving data between signals between windows, Master pyqt part 5
'''
TO DO:
# implement actions(pong, kong, etc) except chow
'''
