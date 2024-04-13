from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from Classes.Adventure import Adventure
from Classes.Map import Map
from Utils import *
import os

class Maps(QWidget):
    def __init__(self, adv: Adventure, communicator) -> None:
        super().__init__()
        self.adventure = adv
        self.selected: Map = None
        self.communicator = communicator

        self.mapsList = QListWidget()

        self.mapNameLineEdit = QLineEdit()
        self.mapSizeXLineEdit = QLineEdit()
        self.mapSizeYLineEdit = QLineEdit()
        self.mapWeatherLineEdit = QLineEdit()

        self.initMap()

    def load(self) -> None:
        if self.selected != None:
            self.adventure.loadedMap = self.selected
            self.communicator.updateMap.emit()
        else:
            sendAlert("Warning", "No map is selected!", QMessageBox.Warning)

    def delete(self) -> None:
        if self.selected is not None:
            for selectedMap in self.adventure.maps:
                if selectedMap == self.selected:
                    cnf = confirmDialogue()
                    if cnf.exec():
                        self.adventure.maps.remove(selectedMap)
                        self.mapsList.takeItem(self.mapsList.currentRow())
                        # TODO Add confirmation prompt
                        if os.path.isfile(f"{os.getcwd()}\\DB\\Maps\\{selectedMap.name}.json"):
                            os.remove(f"{os.getcwd()}\\DB\\Maps\\{selectedMap.name}.json")
                        self.adventure.save()
                        break

    def createNew(self) -> None:
        # Check if the map the user wants to create already exists in the adventure's mapsList
        print(self.mapNameLineEdit.text())
        for mapPresent in self.adventure.maps:
            if not nameExists(self.mapNameLineEdit.text(), mapPresent.name):
                return
        if not validateName(self.mapNameLineEdit.text()):
            return
        newMap = Map()

        newMap.name = self.mapNameLineEdit.text()
        newMap.weather = self.mapWeatherLineEdit.text()

        sizeX = None
        try:
            sizeX = int(self.mapSizeXLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Width is invalid!")
            return
        
        sizeY = None
        try:
            sizeY = int(self.mapSizeYLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Height is invalid!")
            return
        
        newMap.size = (sizeX, sizeY)
        self.adventure.maps.append(newMap)
        item = QListWidgetItem(newMap.name)
        item.setData(Qt.UserRole + 1, newMap)
        self.mapsList.addItem(item)
        newMap.save()

    def save(self) -> None:
        newMap: Map = self.selected
        oldName = newMap.name
        if newMap != None:
            if validateName(self.mapNameLineEdit.text()):
                newMap.name = self.mapNameLineEdit.text()
                newMap.weather = self.mapWeatherLineEdit.text()

                sizeX = None
                try:
                    sizeX = int(self.mapSizeXLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Width is invalid!")
                    return
                
                sizeY = None
                try:
                    sizeY = int(self.mapSizeYLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Height is invalid!")
                    return
                
                newMap.size = (sizeX, sizeY)
                # Remove old .json file
                try:
                    if oldName != newMap.name:
                        os.remove(f"{os.getcwd()}\\DB\\Maps\\{oldName}.json")
                except FileNotFoundError:
                    pass
                # Create new .json file
                newMap.save()
                # Update UI and self.adventure data
                for k, i in enumerate(self.adventure.maps):
                    if i.name == newMap.name:
                        self.adventure.maps[k] = newMap
                        self.mapsList.item(self.mapsList.currentRow()).setText(newMap.name)
                        self.mapsList.item(self.mapsList.currentRow()).setData(Qt.UserRole + 1, newMap)

    def getMapInfo(self, item) -> None: 
        self.selected = item.data(Qt.UserRole + 1)
        for newMap in self.adventure.maps:
            if newMap.name == self.selected.name:
                # Populate info on the right
                self.mapNameLineEdit.setText(newMap.name)
                self.mapWeatherLineEdit.setText(newMap.weather)
                
                if str(newMap.size[0]) != "None":
                    self.mapSizeXLineEdit.setText(str(newMap.size[0]))
                else:
                    self.mapSizeXLineEdit.setText(str(0))
                if str(newMap.size[1]) != "None":
                    self.mapSizeYLineEdit.setText(str(newMap.size[1]))
                else:
                    self.mapSizeYLineEdit.setText(str(0))

    def initMap(self) -> None:
        # Create all necessary directories
        directoryExistsCreate(f"{os.getcwd()}\\DB\\")
        directoryExistsCreate(f"{os.getcwd()}\\DB\\Maps")

        verticalLayout = QVBoxLayout()
        buttonsGridLayout = QGridLayout()
        horizontalLayout = QHBoxLayout()
        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addLayout(buttonsGridLayout)
        self.mapsList.itemClicked.connect(self.getMapInfo)

        deleteButton = QPushButton("Delete")
        createButton = QPushButton("Create")
        saveButton = QPushButton("Save")
        loadButton = QPushButton("Load")

        deleteButton.clicked.connect(self.delete)
        createButton.clicked.connect(self.createNew)
        saveButton.clicked.connect(self.save)
        loadButton.clicked.connect(self.load)

        buttonsGridLayout.addWidget(deleteButton, 0, 0)
        buttonsGridLayout.addWidget(createButton, 0, 1)
        buttonsGridLayout.addWidget(saveButton, 0, 2)
        buttonsGridLayout.addWidget(loadButton, 0, 3)

        # region Map Infos
        mapInfo = QVBoxLayout()

        mapNameLayout = QHBoxLayout()
        mapNameLabel = QLabel("Name")
        mapNameLayout.addWidget(mapNameLabel)
        mapNameLayout.addWidget(self.mapNameLineEdit)

        mapSizeXLayout = QHBoxLayout()
        mapSizeXLabel = QLabel("Width")
        mapSizeXLayout.addWidget(mapSizeXLabel)
        mapSizeXLayout.addWidget(self.mapSizeXLineEdit)

        mapSizeYLayout = QHBoxLayout()
        mapSizeYLabel = QLabel("Height")
        mapSizeYLayout.addWidget(mapSizeYLabel)
        mapSizeYLayout.addWidget(self.mapSizeYLineEdit)

        mapWeatherLayout = QHBoxLayout()
        mapWeatherLabel = QLabel("Weather")
        mapWeatherLayout.addWidget(mapWeatherLabel)
        mapWeatherLayout.addWidget(self.mapWeatherLineEdit)

        mapInfo.addLayout(mapNameLayout)
        mapInfo.addLayout(mapSizeXLayout)
        mapInfo.addLayout(mapSizeYLayout)
        mapInfo.addLayout(mapWeatherLayout)

        # endregion

        horizontalLayout.addWidget(self.mapsList)
        horizontalLayout.addLayout(mapInfo)

        self.setLayout(verticalLayout)

        for newMap in self.adventure.maps:
            item = QListWidgetItem(newMap.name)
            item.setData(Qt.UserRole + 1, newMap)
            self.mapsList.addItem(item)

