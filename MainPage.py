import json.decoder
import os
import random
from PyQt5.QtWidgets import QWidget
import jsonpickle

from Utils import sendAlert, updateMapSignalObject
from Tabs.Bestiary import Bestiary
from Tabs.NPCs import NPCs
from Tabs.Items import Items
from Tabs.Characters import Characters
from Tabs.Maps import Maps

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QCursor, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

from Classes.Adventure import Adventure
from Classes.Character import Character
from Classes.Item import Item
from Classes.Entity import Entity
from Classes.Chat import Chat
from Classes.User import User
from Classes.Tile import Tile


class setHpDialogue(QDialog):
    """Dialoge window to accept user's input for adding or subtracting Hp"""

    def accept(self) -> None:
        """Add is pressed"""
        try:
            int(self.valueLineEdit.text())
        except:
            sendAlert("Error", "Value is invalid!", QMessageBox.Critical)
            return
        return super().accept()

    def reject(self) -> None:
        """Subtract is pressed"""
        try:
            int(self.valueLineEdit.text())
        except:
            sendAlert("Error", "Value is invalid!", QMessageBox.Critical)
            return
        return super().reject()

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Damaging")

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Yes | QDialogButtonBox.No)
        self.buttonBox.button(QDialogButtonBox.Yes).setText('Add')
        self.buttonBox.button(QDialogButtonBox.No).setText('Subtract')
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        valueLabel = QLabel("Amount")
        self.valueLineEdit = QLineEdit()
        horizontalLayout.addWidget(valueLabel)
        horizontalLayout.addWidget(self.valueLineEdit)
        self.layout.addLayout(horizontalLayout)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def getValue(self) -> int:
        return int(self.valueLineEdit.text())


class setStateDialogue(QDialog):
    """Dialog window to accept user's input for adding or removing states"""

    def accept(self) -> None:
        """Add is pressed"""
        if self.valueComboBox.currentText() == None:
            sendAlert("Error", "Choose a value!", QMessageBox.Critical)
        return super().accept()

    def reject(self) -> None:
        """Remove is pressed"""
        if self.valueComboBox.currentText() == None:
            sendAlert("Error", "Choose a value!", QMessageBox.Critical)
        return super().reject()

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Damaging")

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Yes | QDialogButtonBox.No)
        self.buttonBox.button(QDialogButtonBox.Yes).setText('Add')
        self.buttonBox.button(QDialogButtonBox.No).setText('Remove')
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        valueLabel = QLabel("State")
        self.valueComboBox = QComboBox()
        self.valueComboBox.addItem("State 1")
        self.valueComboBox.addItem("State 2")
        self.valueComboBox.addItem("State 3")
        horizontalLayout.addWidget(valueLabel)
        horizontalLayout.addWidget(self.valueComboBox)
        self.layout.addLayout(horizontalLayout)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def getValue(self) -> str:
        return self.valueComboBox.currentText()


class Dice:
    """A Dice class"""

    def __init__(self, faces: int) -> None:
        """Takes an int that defines the number of (virtual) faces the dice has"""
        self.faces = faces

    def getResult(self) -> int:
        """Returns a random number between 1 and faces, both inclusive"""
        return random.randrange(1, self.faces + 1)


class MainWindow(QWidget):

    def setState(self) -> None:
        dlg = setStateDialogue()
        if dlg.exec():
            try:
                if dlg.getValue() in self.selectedTile.occupiedBy.states:
                    pass
                else:
                    self.selectedTile.occupiedBy.setState(f"+{dlg.getValue()}")
            except TypeError:
                self.selectedTile.occupiedBy.states = []
                self.selectedTile.occupiedBy.setState(f"+{dlg.getValue()}")
        else:
            try:
                self.selectedTile.occupiedBy.setState(f"-{dlg.getValue()}")
            except:
                pass
        self.currentMap.save()
        self.adventure.loadedMap = self.currentMap
        self.adventure.save()

    def setHp(self) -> None:
        dlg = setHpDialogue()
        if dlg.exec():
            self.selectedTile.occupiedBy.setHp(-dlg.getValue())
        else:
            self.selectedTile.occupiedBy.setHp(dlg.getValue())
        self.currentMap.save()
        self.adventure.loadedMap = self.currentMap
        self.adventure.save()

    def contextMenuClicked(self) -> None:
        # Only do this if User is DM
        action = self.sender().objectName()
        # action contains in [0] the name of the QAction, in [1], [2] the xCoord, yCoord of the clicked button
        name = action.split(',')[0]
        xCoord = action.split(',')[1]
        yCoord = action.split(',')[2]
        # Find the clicked Tile
        for row in self.currentMap.tileList:
            for tile in row:
                if (int(xCoord), int(yCoord)) == tile.coords:
                    match name:
                        case "AddMonster":
                            if self.bestiaryPage.selected != None:
                                # Monster image
                                pm1 = QPixmap(
                                    f"{os.getcwd()}\\DB\\Monsters\\Images\\{self.bestiaryPage.selected.profilePic}")
                                if pm1.size().isEmpty():
                                    sendAlert("Warning", "Image tied to this monster was not found!",
                                              QMessageBox.Warning)
                                    return
                                pm = pm1.scaled(64, 64, Qt.KeepAspectRatio)
                                self.clickedButton.setIconSize(QSize(64, 64))
                                self.clickedButton.setIcon(QIcon(pm))
                                n: Entity = self.bestiaryPage.selected
                                tile.occupiedBy = Entity(alignment=n.alignment, entityType="Monster", name=n.name,
                                                         hp=n.hp, states=[],
                                                         armorClass=n.armorClass, attacks=n.attacks, strength=n.strength,
                                                         dexterity=n.dexterity, constitution=n.constitution,
                                                         intelligence=n.intelligence, wisdom=n.wisdom,
                                                         charisma=n.charisma, equip=n.equip, skills=n.skills,
                                                         size=n.size, profilePic=n.profilePic)
                            else:
                                sendAlert("Warning", "No monster is selected from the Bestiary", QMessageBox.Warning)
                        case "AddNPC":
                            if self.npcPage.selected != None:
                                # Monster image
                                pm1 = QPixmap(f"{os.getcwd()}\\DB\\NPCs\\Images\\{self.npcPage.selected.profilePic}")
                                if pm1.size().isEmpty():
                                    sendAlert("Warning", "Image tied to this npc was not found!", QMessageBox.Warning)
                                    return
                                pm = pm1.scaled(64, 64, Qt.KeepAspectRatio)
                                self.clickedButton.setIconSize(QSize(64, 64))
                                self.clickedButton.setIcon(QIcon(pm))
                                n: Entity = self.npcPage.selected
                                tile.occupiedBy = Entity(alignment=n.alignment, entityType="NPC", name=n.name, hp=n.hp,
                                                         states=[], armorClass=n.armorClass,
                                                         attacks=n.attacks, strength=n.strength, dexterity=n.dexterity,
                                                         constitution=n.constitution, intelligence=n.intelligence,
                                                         wisdom=n.wisdom, charisma=n.charisma, equip=n.equip,
                                                         skills=n.skills, size=n.size, profilePic=n.profilePic)
                            else:
                                sendAlert("Warning", "No npc is selected from the Bestiary", QMessageBox.Warning)
                        case "AddItem":
                            if self.itemsPage.selected != None:
                                # Monster image
                                pm1 = QPixmap(f"{os.getcwd()}\\DB\\Items\\Images\\{self.itemsPage.selected.profilePic}")
                                if pm1.size().isEmpty():
                                    sendAlert("Warning", "Image tied to this item was not found!", QMessageBox.Warning)
                                    return
                                pm = pm1.scaled(64, 64, Qt.KeepAspectRatio)
                                self.clickedButton.setIconSize(QSize(64, 64))
                                self.clickedButton.setIcon(QIcon(pm))
                                n: Item = self.itemsPage.selected
                                tile.occupiedBy = Item(name=n.name, description=n.description, itemType=n.type,
                                                       profilePic=n.profilePic)
                            else:
                                sendAlert("Warning", "No item is selected from the Bestiary", QMessageBox.Warning)
                        case "AddCharacter":
                            if self.charactersPage.selected != None:
                                # Monster image
                                pm1 = QPixmap(
                                    f"{os.getcwd()}\\DB\\Characters\\Images\\{self.charactersPage.selected.profilePic}")
                                if pm1.size().isEmpty():
                                    sendAlert("Warning", "Image tied to this character was not found!",
                                              QMessageBox.Warning)
                                    return
                                pm = pm1.scaled(64, 64, Qt.KeepAspectRatio)
                                self.clickedButton.setIconSize(QSize(64, 64))
                                self.clickedButton.setIcon(QIcon(pm))
                                n: Character = self.charactersPage.selected
                                tile.occupiedBy = Character(name=n.name, playerName=n.playerName,
                                                            entityType="Character",
                                                            profilePic=n.profilePic, size=n.size, gameClass=n.gameClass,
                                                            level=n.level, race=n.race, alignment=n.alignment,
                                                            strength=n.strength, dexterity=n.dexterity,
                                                            constitution=n.constitution, intelligence=n.intelligence,
                                                            wisdom=n.wisdom, charisma=n.charisma, armorClass=n.armorClass,
                                                            speed=n.speed, hp=n.hp, states=[],
                                                            attacks=n.attacks, equip=n.equip, skills=n.skills,
                                                            extras=n.extras, owner=User("DM"))
                            else:
                                sendAlert("Warning", "No item is selected from the Characters list",
                                          QMessageBox.Warning)
                        case "Clear":
                            # Simply clear the clickedButton's icon
                            self.clickedButton.setIcon(QIcon())
                            tile.occupiedBy = None
                    self.currentMap.save()
                    self.adventure.loadedMap = self.currentMap
                    self.adventure.save()

    def showContextMenu(self) -> None:
        """Definition of the context menu opened when the user right clicks any Tile in the Map"""
        self.menu = QMenu(self)
        self.clickedButton = self.sender()
        nameLabel = QAction('', self)
        hpLabel = QAction('', self)
        stateLabel = QAction('', self)

        # Set labels
        # Only do this if User is DM
        # In [0], [1] the xCoord, yCoord of the clicked button
        xCoord = self.clickedButton.objectName().split(',')[0]
        yCoord = self.clickedButton.objectName().split(',')[1]
        # Find the clicked Tile
        for row in self.currentMap.tileList:
            for tile in row:
                if (int(xCoord), int(yCoord)) == tile.coords:
                    self.selectedTile = tile
                    if tile.occupiedBy != None:
                        nameLabel.setText(self.selectedTile.occupiedBy.name)
                        hpLabel.setText('')
                        stateLabel.setText('')
                        if not isinstance(self.selectedTile.occupiedBy, Item):
                            hpLabel.setText(
                                f'Hp: {self.selectedTile.occupiedBy.hp}/{self.selectedTile.occupiedBy.maxHp}')
                            if self.selectedTile.occupiedBy.states == None:
                                statesString = 'None'
                            elif len(self.selectedTile.occupiedBy.states) == 0:
                                statesString = 'None'
                            else:
                                statesString = str(self.selectedTile.occupiedBy.states)
                                statesString = statesString.replace('[', '')
                                statesString = statesString.replace(']', '')
                                statesString = statesString.replace("'", '')
                                statesString = statesString.replace(",", ', ')
                            stateLabel.setText(statesString)

        setHpAction = QAction('Set Hp', self)
        setStateAction = QAction('Set State', self)
        addMonsterAction = QAction('Add Monster', self)
        addMonsterAction.setObjectName(f"AddMonster,{self.sender().objectName()}")
        addNpcAction = QAction('Add NPC', self)
        addNpcAction.setObjectName(f"AddNPC,{self.sender().objectName()}")
        addItemAction = QAction('Add Item', self)
        addItemAction.setObjectName(f"AddItem,{self.sender().objectName()}")
        addCharacterAction = QAction('Add Character', self)
        addCharacterAction.setObjectName(f"AddCharacter,{self.sender().objectName()}")
        clearAction = QAction('Clear', self)
        clearAction.setObjectName(f"Clear,{self.sender().objectName()}")

        setHpAction.triggered.connect(self.setHp)
        setStateAction.triggered.connect(self.setState)
        addMonsterAction.triggered.connect(self.contextMenuClicked)
        addNpcAction.triggered.connect(self.contextMenuClicked)
        addItemAction.triggered.connect(self.contextMenuClicked)
        addCharacterAction.triggered.connect(self.contextMenuClicked)
        clearAction.triggered.connect(self.contextMenuClicked)

        self.menu.addAction(nameLabel)
        self.menu.addAction(hpLabel)
        self.menu.addAction(stateLabel)

        self.menu.addSeparator()
        if not isinstance(self.selectedTile.occupiedBy, Item):
            self.menu.addAction(setHpAction)
            self.menu.addAction(setStateAction)
        self.menu.addAction(addMonsterAction)
        self.menu.addAction(addNpcAction)
        self.menu.addAction(addItemAction)
        self.menu.addAction(addCharacterAction)
        self.menu.addAction(clearAction)

        self.menu.popup(QCursor.pos())

    def modifyMap(self) -> None:
        self.clickedButton = self.sender()

        for row in self.currentMap.tileList:
            for tile in row:
                xCoord = int(self.clickedButton.objectName().split(',')[0])
                yCoord = int(self.clickedButton.objectName().split(',')[1])
                if (xCoord, yCoord) == tile.coords:
                    # Found the tile corresponding the pressed button
                    try:
                        nextImage = self.currentMap.tilePalette.index(f"{tile.image}") + 1
                        self.sender().setStyleSheet(
                            f"background-image: url('{self.currentMap.tilePalette[nextImage]}');")
                        tile.image = self.currentMap.tilePalette[nextImage]
                    except IndexError:
                        self.sender().setStyleSheet(f"background-image: url('{self.currentMap.tilePalette[0]}');")
                        tile.image = self.currentMap.tilePalette[0]
        self.currentMap.save()

    def sendMessage(self) -> None:
        self.chat.sendMessage(self.user.name)
        self.adventure.save()

    def resetDiceList(self):
        self.diceList.clear()
        self.dicesLabel.setText("")

    def throwDiceList(self):
        self.dicesLabel.setText("")
        tot = 0
        for dice in self.diceList:
            tot += dice.getResult()
        self.chat.sendAutomatedMessage(self.user.name, f"result is {tot}")
        self.diceList.clear()
        self.adventure.save()

    def addDiceList(self):

        self.dicesLabel.setText(self.dicesLabel.text() + f" + {self.sender().text()}")

        match self.sender().text():
            case 'd4':
                self.diceList.append(Dice(4))
            case 'd6':
                self.diceList.append(Dice(6))
            case 'd8':
                self.diceList.append(Dice(8))
            case 'd10':
                self.diceList.append(Dice(10))
            case 'd12':
                self.diceList.append(Dice(12))
            case 'd20':
                self.diceList.append(Dice(20))

    def loadData(self, path: str) -> Adventure:
        try:
            with open(f"{os.getcwd()}\\DB\\{path}.json", 'rb') as f:
                jsonpickle.loads(f.read())
        except FileNotFoundError as e:
            sendAlert("Error", "Invalid adventure loaded!")
            return Adventure()
        except json.decoder.JSONDecodeError:
            sendAlert("Error", "Invalid JSON file loaded!")
            return Adventure()

    def loadAdventure(self, name: str) -> Adventure:
        with open(f"{os.getcwd()}\\DB\\Adventures\\{name}.json") as f:
            adventure = jsonpickle.loads(f.read())

        if adventure.entities == None:
            adventure.entities = []
        if adventure.maps == None:
            adventure.maps = []
        adventure.loadChat()
        adventure.loadItems()
        adventure.loadMaps()
        adventure.loadEntities()
        adventure.save()
        return adventure

    def __init__(self, adventureName: str, user: User) -> None:
        """Used as a Repository (Pattern)"""
        super().__init__()
        # Used to trigger self.buildMap from the Maps tab when a new map gets loaded
        self.updateMapSignal = updateMapSignalObject()
        self.updateMapSignal.updateMap.connect(self.buildMap)
        # Used to identify which button of the map gets pressed
        self.clickedButton = None
        self.selectedTile = None
        self.mainPageWidget = QWidget()

        self.chatMessageLineEdit = QLineEdit()
        self.chatListWidget = QListWidget()
        self.mapGrid = QGridLayout()
        self.mapWidget = QWidget()
        self.diceGrid = QGridLayout()
        self.diceList = []
        self.dicesLabel = QLabel()
        self.tabSelector = QTabWidget()
        self.scrollableMapArea = QScrollArea()
        self.user = user

        # If player wants to join the adventure, the adventure is known due to join adventure's ID
        # Load the adventure and append the new character to characters[]
        # Doing this should allow the adventure to be always loaded and saved with joined Characters
        self.chat = Chat(self.chatListWidget, self.chatMessageLineEdit, self.diceList)
        self.adventure = self.loadAdventure(adventureName)
        self.bestiaryPage = Bestiary(self.adventure)
        self.npcPage = NPCs(self.adventure)
        self.itemsPage = Items(self.adventure)
        self.charactersPage = Characters(self.adventure, user)
        self.mapsPage = Maps(self.adventure, self.updateMapSignal)

        self.initUI()

    def buildMap(self) -> None:
        """Runs when updateMap signal gets emitted by the Load button on the Maps tab"""
        self.currentMap = self.adventure.loadedMap
        if self.currentMap != None:
            tileList = []
            for x in range(0, self.currentMap.size[0]):
                row = []
                for y in range(0, self.currentMap.size[1]):
                    # Instantiate buttons and Tiles
                    try:
                        t = self.currentMap.tileList[x][y]
                    except:
                        # Default tile initialization
                        t = Tile(image="DB/Images/test.jpg", terrainType=None, coords=(x, y))
                    row.append(t)
                    b = QPushButton("")
                    b.setFixedSize(50, 50)
                    # Used to create a linking between the QPushButton and the Tile object
                    b.setObjectName(f"{str(x)},{str(y)}")
                    b.setStyleSheet(f"background-image: url('{t.image}');")
                    b.setContextMenuPolicy(Qt.CustomContextMenu)
                    b.customContextMenuRequested.connect(self.showContextMenu)
                    b.clicked.connect(self.modifyMap)

                    # occupiedBy rebuilding
                    if t.occupiedBy != None:
                        if isinstance(t.occupiedBy, Character):
                            pm1 = QPixmap(f"{os.getcwd()}\\DB\\Characters\\Images\\{t.occupiedBy.profilePic}")
                            print(t.occupiedBy.profilePic)

                        elif isinstance(t.occupiedBy, Entity):
                            if t.occupiedBy.entityType == "Monster":
                                pm1 = QPixmap(f"{os.getcwd()}\\DB\\Monsters\\Images\\{t.occupiedBy.profilePic}")
                            if t.occupiedBy.entityType == "NPC":
                                pm1 = QPixmap(f"{os.getcwd()}\\DB\\NPCs\\Images\\{t.occupiedBy.profilePic}")

                        elif isinstance(t.occupiedBy, Item):
                            # Item image
                            pm1 = QPixmap(f"{os.getcwd()}\\DB\\Items\\Images\\{t.occupiedBy.profilePic}")
                        try:
                            pm = pm1.scaled(64, 64, Qt.KeepAspectRatio)
                            b.setIconSize(QSize(64, 64))
                            b.setIcon(QIcon(pm))
                        except:
                            pass
                    self.mapGrid.addWidget(b, x, y)
                tileList.append(row)
            self.currentMap.tileList = tileList
            self.currentMap.save()

    def initUI(self):
        generalVerticalLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        chatVerticalLayout = QVBoxLayout()
        mapVerticalLayout = QVBoxLayout()

        self.mapGrid.setHorizontalSpacing(0)
        self.mapGrid.setVerticalSpacing(0)
        # Populate Map with empty Tiles, used only if the DM doesn't load a preexisting Map

        self.mapWidget.setLayout(self.mapGrid)
        chatSendMessageLayout = QHBoxLayout()
        sendButton = QPushButton("Send")
        chatSendMessageLayout.addWidget(self.chatMessageLineEdit)
        chatSendMessageLayout.addWidget(sendButton)
        chatVerticalLayout.addWidget(self.chatListWidget)
        chatVerticalLayout.addLayout(chatSendMessageLayout)
        # Scroll Area Properties
        self.scrollableMapArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollableMapArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollableMapArea.setWidgetResizable(True)
        self.scrollableMapArea.setWidget(self.mapWidget)

        mapVerticalLayout.addWidget(self.scrollableMapArea)
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        mapVerticalLayout.addItem(spacer)

        mapVerticalLayout.addWidget(self.dicesLabel)
        # region Dices
        resetButton = QPushButton("Reset")
        D4Button = QPushButton("d4")
        D6Button = QPushButton("d6")
        D8Button = QPushButton("d8")
        D10Button = QPushButton("d10")
        D12Button = QPushButton("d12")
        D20Button = QPushButton("d20")
        throwButton = QPushButton("Throw")

        resetButton.setFixedSize(100, 100)
        D4Button.setFixedSize(100, 100)
        D6Button.setFixedSize(100, 100)
        D8Button.setFixedSize(100, 100)
        D10Button.setFixedSize(100, 100)
        D12Button.setFixedSize(100, 100)
        D20Button.setFixedSize(100, 100)
        throwButton.setFixedSize(100, 100)

        self.diceGrid.addWidget(resetButton, 0, 0)
        self.diceGrid.addWidget(D4Button, 0, 1)
        self.diceGrid.addWidget(D6Button, 0, 2)
        self.diceGrid.addWidget(D8Button, 0, 3)
        self.diceGrid.addWidget(D10Button, 0, 4)
        self.diceGrid.addWidget(D12Button, 0, 5)
        self.diceGrid.addWidget(D20Button, 0, 6)
        self.diceGrid.addWidget(throwButton, 0, 7)

        resetButton.clicked.connect(self.resetDiceList)
        D4Button.clicked.connect(self.addDiceList)
        D6Button.clicked.connect(self.addDiceList)
        D8Button.clicked.connect(self.addDiceList)
        D10Button.clicked.connect(self.addDiceList)
        D12Button.clicked.connect(self.addDiceList)
        D20Button.clicked.connect(self.addDiceList)
        throwButton.clicked.connect(self.throwDiceList)
        # endregion

        mapVerticalLayout.addLayout(self.diceGrid)
        horizontalLayout.addLayout(chatVerticalLayout)
        horizontalLayout.addLayout(mapVerticalLayout)

        sendButton.clicked.connect(self.sendMessage)

        self.mainPageWidget.setLayout(horizontalLayout)

        self.tabSelector.addTab(self.mainPageWidget, "Main")
        self.tabSelector.addTab(self.charactersPage, "Characters")
        # The logged user is the DM?
        if self.user.name == self.adventure.owner.name:
            self.tabSelector.addTab(self.bestiaryPage, "Bestiary")
            self.tabSelector.addTab(self.npcPage, "NPCs")
            self.tabSelector.addTab(self.itemsPage, "Items")
            self.tabSelector.addTab(self.mapsPage, "Maps")

        generalVerticalLayout.addWidget(self.tabSelector)
        self.setLayout(generalVerticalLayout)
        self.setWindowTitle('D&D Manager')
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    adv = Adventure(name="Refactor", owner=User("Ale"))
    adv.save()
    # Only gets used if main gets executed first
    mainWindow = MainWindow("Refactor", User("Ale"))
    app.exec()
