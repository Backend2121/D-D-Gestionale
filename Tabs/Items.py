from PyQt5.QtWidgets import *
from Classes.Adventure import Adventure
from Classes.Item import Item
from Classes.ItemTypes.Armour import Armour
from Classes.ItemTypes.Potion import Potion
from Classes.ItemTypes.Spell import Spell
from Classes.ItemTypes.Weapon import Weapon
from Utils import *
import os
from Utils import validateName, nameExists


class Items(QWidget):

    def disableLineEdits(self) -> None:
        self.effectLineEdit.setEnabled(False)
        self.castingTimeLineEdit.setEnabled(False)
        self.castingTypeLineEdit.setEnabled(False)
        self.damageTypeLineEdit.setEnabled(False)
        self.damageDiceLineEdit.setEnabled(False)
        self.armorClassLineEdit.setEnabled(False)
        self.resistancesLineEdit.setEnabled(False)
        self.extrasLineEdit.setEnabled(False)

    def delete(self) -> None:
        if self.selected is not None:
            for item in self.adventure.items:
                if item == self.selected:
                    cnf = confirmDialogue()
                    if cnf.exec():
                        self.adventure.items.remove(item)
                        self.itemList.takeItem(self.itemList.currentRow())
                        if os.path.isfile(f"{os.getcwd()}\\DB\\Items\\{item.name}.json"):
                            os.remove(f"{os.getcwd()}\\DB\\Items\\{item.name}.json")
                        self.adventure.save()
                        break

    def save(self) -> None:
        item: Item = self.selected
        oldName = item.name
        if item != None:
            if validateName(self.itemNameLineEdit.text()):
                item.profilePic = self.itemPropicLineEdit.text()
                item.name = self.itemNameLineEdit.text()
                item.description = self.itemDescriptionLineEdit.text()
                item.type = self._type
                match item.type:
                    case "Potion":
                        item.type = Potion(
                            effect=self.effectLineEdit.text(),
                            extra=self.extrasLineEdit.text()
                        )
                    case "Spell":
                        item.type = Spell(
                            effect=self.effectLineEdit.text(),
                            castingType= self.castingTypeLineEdit.text(),
                            castingTime=self.castingTimeLineEdit.text(),
                            damageType=self.damageTypeLineEdit.text(),
                            damageDice=self.damageDiceLineEdit.text(),
                            extra=self.extrasLineEdit.text()
                        )
                    case "Armor":
                        try:
                            int(self.armorClassLineEdit.text())
                        except:
                            sendAlert("Error", "Invalid Armor Class value!")
                            return
                        item.type = Armour(
                            AC=int(self.armorClassLineEdit.text()),
                            extras=self.extrasLineEdit.text(),
                            resistances=self.resistancesLineEdit.text()
                        )
                    case "Weapon":
                        item.type = Weapon(
                            damageType=self.damageDiceLineEdit.text(),
                            damageDice=self.damageDiceLineEdit.text(),
                            extras=self.extrasLineEdit.text()
                        )
                # Remove old .json file
                try:
                    if oldName != item.name:
                        os.remove(f"{os.getcwd()}\\DB\\Items\\{oldName}.json")
                except FileNotFoundError:
                    pass
                # Create new .json file
                item.save()
                # Update UI and self.adventure data
                for k, i in enumerate(self.adventure.items):
                    if i.name == item.name:
                        self.adventure.items[k] = item
                        self.itemList.item(self.itemList.currentRow()).setText(item.name)
                        self.itemList.item(self.itemList.currentRow()).setData(Qt.UserRole + 1, item)

    def createNew(self) -> None:
        # Check if the item the user wants to create already exists in the adventure's inventory
        for itemPresent in self.adventure.items:
            if not nameExists(self.itemNameLineEdit.text(), itemPresent.name):
                return
        if not validateName(self.itemNameLineEdit.text()):
            return
        item = Item(
            name=self.itemNameLineEdit.text(),
            description=self.itemDescriptionLineEdit.text(),
            profilePic=self.itemPropicLineEdit.text()
            )
        item.type = self._type
        match item.type:
            case "Potion":
                item.type = Potion(
                    effect=self.effectLineEdit.text(),
                    extra=self.extrasLineEdit.text()
                )
            case "Spell":
                item.type = Spell(
                    effect=self.effectLineEdit.text(),
                    castingType= self.castingTypeLineEdit.text(),
                    castingTime=self.castingTimeLineEdit.text(),
                    damageType=self.damageTypeLineEdit.text(),
                    damageDice=self.damageDiceLineEdit.text(),
                    extra=self.extrasLineEdit.text()
                )
            case "Armor":
                try:
                    int(self.armorClassLineEdit.text())
                except:
                    sendAlert("Error", "Invalid Armor Class value!")
                    return
                item.type = Armour(
                    AC=int(self.armorClassLineEdit.text()),
                    extras=self.extrasLineEdit.text(),
                    resistances=self.resistancesLineEdit.text()
                )
            case "Weapon":
                item.type = Weapon(
                    damageType=self.damageDiceLineEdit.text(),
                    damageDice=self.damageDiceLineEdit.text(),
                    extras=self.extrasLineEdit.text()
                )

        self.adventure.items.append(item)
        itemWidget = QListWidgetItem(item.name)
        itemWidget.setData(Qt.UserRole + 1, item)
        self.itemList.addItem(itemWidget)
        item.save()

    def changeLayout(self) -> None:
        radioButton = self.sender()
        if radioButton.isChecked():
            self.disableLineEdits()
            match self.sender().objectName():
                case "PotionButton":
                    self.effectLineEdit.setEnabled(True)
                    self.extrasLineEdit.setEnabled(True)
                    self._type = "Potion"
                case "SpellButton":
                    self.castingTimeLineEdit.setEnabled(True)
                    self.castingTypeLineEdit.setEnabled(True)
                    self.damageDiceLineEdit.setEnabled(True)
                    self.damageTypeLineEdit.setEnabled(True)
                    self.effectLineEdit.setEnabled(True)
                    self.extrasLineEdit.setEnabled(True)
                    self._type = "Spell"
                case "ArmorButton":
                    self.armorClassLineEdit.setEnabled(True)
                    self.resistancesLineEdit.setEnabled(True)
                    self.extrasLineEdit.setEnabled(True)
                    self._type = "Armor"
                case "WeaponButton":
                    self.damageDiceLineEdit.setEnabled(True)
                    self.damageTypeLineEdit.setEnabled(True)
                    self.extrasLineEdit.setEnabled(True)
                    self._type = "Weapon"

    def getItemInfo(self, item) -> None:
        """Retrieves info from clicked item and shows them in the proper lineEdits"""
        # Disable everything
        self.disableLineEdits()
        self.potionRadioButton.setChecked(False)
        self.spellRadioButton.setChecked(False)
        self.armorRadioButton.setChecked(False)
        self.weaponRadioButton.setChecked(False)
        # Not needed but activates intellisense
        self.selected = item.data(Qt.UserRole + 1)
        item : Item
        for item in self.adventure.items:
            if item.name == self.selected.name:
                # Logic code
                self.itemPropicLineEdit.setText(item.profilePic)
                self.itemNameLineEdit.setText(item.name)
                self.itemDescriptionLineEdit.setText(item.description)
                # Switch to determine the type of item.type -> populate respective fields and check correct RadioButton
                if isinstance(item.type, Potion):
                    self.effectLineEdit.setEnabled(True)
                    self.extrasLineEdit.setEnabled(True)

                    self.effectLineEdit.setText(item.type.effect)
                    self.extrasLineEdit.setText(item.type.extra)

                    self.potionRadioButton.setChecked(True)
                elif isinstance(item.type, Spell):
                    self.effectLineEdit.setEnabled(True)
                    self.extrasLineEdit.setEnabled(True)
                    self.castingTimeLineEdit.setEnabled(True)
                    self.castingTypeLineEdit.setEnabled(True)
                    self.damageDiceLineEdit.setEnabled(True)
                    self.damageTypeLineEdit.setEnabled(True)

                    self.effectLineEdit.setText(item.type.effect)
                    self.extrasLineEdit.setText(item.type.extra)
                    self.castingTimeLineEdit.setText(item.type.castingTime)
                    self.castingTypeLineEdit.setText(item.type.castingType)
                    self.damageDiceLineEdit.setText(item.type.damageDice)
                    self.damageTypeLineEdit.setText(item.type.damageType)

                    self.spellRadioButton.setChecked(True)
                elif isinstance(item.type, Armour):
                    self.extrasLineEdit.setEnabled(True)
                    self.armorClassLineEdit.setEnabled(True)
                    self.resistancesLineEdit.setEnabled(True)

                    self.armorClassLineEdit.setText(str(item.type.AC))
                    self.resistancesLineEdit.setText(item.type.resistances)
                    self.extrasLineEdit.setText(item.type.extras)

                    self.armorRadioButton.setChecked(True)
                elif isinstance(item.type, Weapon):
                    self.extrasLineEdit.setEnabled(True)
                    self.damageDiceLineEdit.setEnabled(True)
                    self.damageTypeLineEdit.setEnabled(True)

                    self.damageDiceLineEdit.setText(item.type.damageDice)
                    self.damageTypeLineEdit.setText(item.type.damageType)
                    self.extrasLineEdit.setText(item.type.extras)

                    self.weaponRadioButton.setChecked(True)

    def __init__(self, adv: Adventure) -> None:
        """Items tab"""
        super().__init__()
        self.adventure = adv
        self.selected = None
        self.itemList = QListWidget()
        self._type = "Potion"
        # Changed when an item gets clicked
        self.itemLayout = QVBoxLayout()

        self.itemPropicLayout = QHBoxLayout()
        self.itemPropicLabel = QLabel("Propic")
        self.itemPropicLineEdit = QLineEdit()
        self.itemPropicLayout.addWidget(self.itemPropicLabel)
        self.itemPropicLayout.addWidget(self.itemPropicLineEdit)

        self.itemNameLayout = QHBoxLayout()
        self.itemNameLabel = QLabel("Name")
        self.itemNameLineEdit = QLineEdit()
        self.itemNameLayout.addWidget(self.itemNameLabel)
        self.itemNameLayout.addWidget(self.itemNameLineEdit)

        self.itemDescriptionLayout = QHBoxLayout()
        self.itemDescriptionLabel = QLabel("Description")
        self.itemDescriptionLineEdit = QLineEdit()
        self.itemDescriptionLayout.addWidget(self.itemDescriptionLabel)
        self.itemDescriptionLayout.addWidget(self.itemDescriptionLineEdit)

        self.itemTypeLayout = QGridLayout()
        self.potionRadioButton = QRadioButton("Potion")
        self.potionRadioButton.setObjectName("PotionButton")
        self.spellRadioButton = QRadioButton("Spell")
        self.spellRadioButton.setObjectName("SpellButton")
        self.armorRadioButton = QRadioButton("Armor")
        self.armorRadioButton.setObjectName("ArmorButton")
        self.weaponRadioButton = QRadioButton("Weapon")
        self.weaponRadioButton.setObjectName("WeaponButton")

        self.potionRadioButton.toggled.connect(self.changeLayout)
        self.spellRadioButton.toggled.connect(self.changeLayout)
        self.armorRadioButton.toggled.connect(self.changeLayout)
        self.weaponRadioButton.toggled.connect(self.changeLayout)

        self.itemTypeLayout.addWidget(self.potionRadioButton, 0, 0)
        self.itemTypeLayout.addWidget(self.spellRadioButton, 0, 1)
        self.itemTypeLayout.addWidget(self.armorRadioButton, 0, 2)
        self.itemTypeLayout.addWidget(self.weaponRadioButton, 0, 3)

        # Create multiple layouts and show them based on the item.itemType's class
        # SPELL LAYOUT
        self.itemSubLayout = QVBoxLayout()

        self.castingTimeLayout = QHBoxLayout()
        self.CastingTimeLabel = QLabel("Casting Time")
        self.castingTimeLineEdit = QLineEdit()
        self.castingTimeLayout.addWidget(self.CastingTimeLabel)
        self.castingTimeLayout.addWidget(self.castingTimeLineEdit)

        self.castingTypeLayout = QHBoxLayout()
        self.castingTypeLabel = QLabel("Casting Type")
        self.castingTypeLineEdit = QLineEdit()
        self.castingTypeLayout.addWidget(self.castingTypeLabel)
        self.castingTypeLayout.addWidget(self.castingTypeLineEdit)

        self.effectLayout = QHBoxLayout()
        self.effectLabel = QLabel("Effect")
        self.effectLineEdit = QLineEdit()
        self.effectLayout.addWidget(self.effectLabel)
        self.effectLayout.addWidget(self.effectLineEdit)

        self.damageTypeLayout = QHBoxLayout()
        self.damageTypeLabel = QLabel("Damage Type")
        self.damageTypeLineEdit = QLineEdit()
        self.damageTypeLayout.addWidget(self.damageTypeLabel)
        self.damageTypeLayout.addWidget(self.damageTypeLineEdit)

        self.damageDiceLayout = QHBoxLayout()
        self.damageDiceLabel = QLabel("Damage Dice")
        self.damageDiceLineEdit = QLineEdit()
        self.damageDiceLayout.addWidget(self.damageDiceLabel)
        self.damageDiceLayout.addWidget(self.damageDiceLineEdit)

        self.armorClassLayout = QHBoxLayout()
        self.armorClassLabel = QLabel("CA")
        self.armorClassLineEdit = QLineEdit()
        self.armorClassLayout.addWidget(self.armorClassLabel)
        self.armorClassLayout.addWidget(self.armorClassLineEdit)

        self.extrasLayout = QHBoxLayout()
        self.extrasLabel = QLabel("Extras")
        self.extrasLineEdit = QLineEdit()
        self.extrasLayout.addWidget(self.extrasLabel)
        self.extrasLayout.addWidget(self.extrasLineEdit)

        self.resistancesLayout = QHBoxLayout()
        self.resistancesLabel = QLabel("Resistances")
        self.resistancesLineEdit = QLineEdit()
        self.resistancesLayout.addWidget(self.resistancesLabel)
        self.resistancesLayout.addWidget(self.resistancesLineEdit)

        self.itemSubLayout.addLayout(self.effectLayout)
        self.itemSubLayout.addLayout(self.castingTimeLayout)
        self.itemSubLayout.addLayout(self.castingTypeLayout)
        self.itemSubLayout.addLayout(self.damageTypeLayout)
        self.itemSubLayout.addLayout(self.damageDiceLayout)
        self.itemSubLayout.addLayout(self.armorClassLayout)
        self.itemSubLayout.addLayout(self.extrasLayout)
        self.itemSubLayout.addLayout(self.resistancesLayout)

        self.initItems()
        # Disable all LineEdits
        self.disableLineEdits()

    def initItems(self):
        directoryExistsCreate(f"{os.getcwd()}\\DB\\")
        directoryExistsCreate(f"{os.getcwd()}\\DB\\Items")
        directoryExistsCreate(f"{os.getcwd()}\\DB\\Items\\Images")
        verticalLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        buttonsGridLayout = QGridLayout()
        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addLayout(buttonsGridLayout)

        self.itemList.itemClicked.connect(self.getItemInfo)

        self.itemLayout.addLayout(self.itemPropicLayout)
        self.itemLayout.addLayout(self.itemNameLayout)
        self.itemLayout.addLayout(self.itemDescriptionLayout)
        self.itemLayout.addLayout(self.itemTypeLayout)
        self.itemLayout.addLayout(self.itemSubLayout)

        horizontalLayout.addWidget(self.itemList)
        horizontalLayout.addLayout(self.itemLayout)

        deleteButton = QPushButton("Delete")
        deleteButton.clicked.connect(self.delete)
        createButton = QPushButton("Create")
        createButton.clicked.connect(self.createNew)
        saveButton = QPushButton("Save")
        saveButton.clicked.connect(self.save)

        buttonsGridLayout.addWidget(deleteButton, 0, 0)
        buttonsGridLayout.addWidget(createButton, 0, 1)
        buttonsGridLayout.addWidget(saveButton, 0, 2)

        self.setLayout(verticalLayout)

        for item in self.adventure.items:
            itemWidget = QListWidgetItem(item.name)
            itemWidget.setData(Qt.UserRole + 1, item)
            self.itemList.addItem(itemWidget)
