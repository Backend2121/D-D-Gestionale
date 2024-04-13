import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from Classes.Adventure import Adventure
from Classes.Entity import Entity
import jsonpickle
from Utils import *


class Bestiary(QWidget):
    
    def delete(self) -> None:
        if self.selected is not None:
            for monster in self.adventure.entities:
                if monster == self.selected:
                    cnf = confirmDialogue()
                    if cnf.exec():
                        self.adventure.entities.remove(monster)
                        self.bestiaryList.takeItem(self.bestiaryList.currentRow())

                        if os.path.isfile(f"{os.getcwd()}\\DB\\Monsters\\{monster.name}.json"):
                            os.remove(f"{os.getcwd()}\\DB\\Monsters\\{monster.name}.json")
                        self.adventure.save()
                        break

    def createNew(self) -> None:
        # Check if the Monster the user wants to create already exists in the adventure's bestiary
        for monsterPresent in self.adventure.entities:
            if monsterPresent.entityType == "Monster":
                if not nameExists(self.bestiaryNameLineEdit.text(), monsterPresent.name):
                    return
        if not validateName(self.bestiaryNameLineEdit.text()):
            return
        monster = Entity(entityType="Monster")
        # Set all the parameters to the new ones
        monster.name = self.bestiaryNameLineEdit.text()
        monster.alignment = self.bestiaryAlignmentLineEdit.text()
        monster.size = self.bestiarySizeLineEdit.text()
        monster.profilePic = self.bestiaryProfilePicLineEdit.text()
        # This solution allows the use of multiple : but they get removed
        attacksDict = {}
        line: str
        for line in self.bestiaryAttacksTextEdit.toPlainText().splitlines():
            if ":" in line:
                key = line.split(':')[0]
                value = ""
                for x in line.split(':'):
                    if x != key:
                        value += x
            else:
                key = line
                value = ""
            attacksDict.update({key: value})
        monster.attacks = attacksDict
        equipDict = {}
        line: str
        for line in self.bestiaryEquipTextEdit.toPlainText().splitlines():
            if ":" in line:
                key = line.split(':')[0]
                value = ""
                for x in line.split(':'):
                    if x != key:
                        value += x
            else:
                key = line
                value = ""
            equipDict.update({key: value})
        monster.equip = equipDict

        skillsDict = {}
        line: str
        for line in self.bestiarySkillsTextEdit.toPlainText().splitlines():
            if ":" in line:
                key = line.split(':')[0]
                value = ""
                for x in line.split(':'):
                    if x != key:
                        value += x
            else:
                key = line
                value = ""
            skillsDict.update({key: value})
        monster.skills = skillsDict

        extrasDict = {}
        line: str
        for line in self.bestiaryExtrasTextEdit.toPlainText().splitlines():
            if ":" in line:
                key = line.split(':')[0]
                value = ""
                for x in line.split(':'):
                    if x != key:
                        value += x
            else:
                key = line
                value = ""
            extrasDict.update({key: value})
        monster.skills = extrasDict
        try:
            monster.hp = int(self.bestiaryHpLineEdit.text())
            monster.maxHp = int(self.bestiaryHpLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Hp is invalid!")
            return
        try:
            monster.armorClass = int(self.bestiaryACLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Armor class is invalid!")
            return
        try:
            monster.speed = int(self.bestiarySpeedLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Speed is invalid!")
            return
        try:
            monster.strength = int(self.bestiaryStrengthLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Strength is invalid!")
            return
        try:
            monster.dexterity = int(self.bestiaryDexterityLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Dexterity is invalid!")
            return
        try:
            monster.constitution = int(self.bestiaryConstitutionLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Constitution is invalid!")
            return
        try:
            monster.intelligence = int(self.bestiaryIntelligenceLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Intelligence is invalid!")
            return
        try:
            monster.wisdom = int(self.bestiaryWisdomLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Wisdom is invalid!")
            return
        try:
            monster.charisma = int(self.bestiaryCharismaLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Charisma is invalid!")
            return
        
        self.adventure.entities.append(monster)
        item = QListWidgetItem(monster.name)
        item.setData(Qt.UserRole + 1, monster)
        self.bestiaryList.addItem(item)
        monster.save()

    def save(self) -> None:
        monster: Entity = self.selected
        oldName = monster.name
        if monster != None:
            if validateName(self.bestiaryNameLineEdit.text()):
                # Set all the parameters to the new ones
                monster.name = self.bestiaryNameLineEdit.text()
                monster.alignment = self.bestiaryAlignmentLineEdit.text()
                monster.size = self.bestiarySizeLineEdit.text()
                monster.profilePic = self.bestiaryProfilePicLineEdit.text()
                # This solution allows the use of multiple : but they get removed
                attacksDict = {}
                line: str
                for line in self.bestiaryAttacksTextEdit.toPlainText().splitlines():
                    if ":" in line:
                        key = line.split(':')[0]
                        value = ""
                        for x in line.split(':'):
                            if x != key:
                                value += x
                    else:
                        key = line
                        value = ""
                    attacksDict.update({key: value})
                monster.attacks = attacksDict
                equipDict = {}
                line: str
                for line in self.bestiaryEquipTextEdit.toPlainText().splitlines():
                    if ":" in line:
                        key = line.split(':')[0]
                        value = ""
                        for x in line.split(':'):
                            if x != key:
                                value += x
                    else:
                        key = line
                        value = ""
                    equipDict.update({key: value})
                monster.equip = equipDict

                skillsDict = {}
                line: str
                for line in self.bestiarySkillsTextEdit.toPlainText().splitlines():
                    if ":" in line:
                        key = line.split(':')[0]
                        value = ""
                        for x in line.split(':'):
                            if x != key:
                                value += x
                    else:
                        key = line
                        value = ""
                    skillsDict.update({key: value})
                monster.skills = skillsDict

                extrasDict = {}
                line: str
                for line in self.bestiaryExtrasTextEdit.toPlainText().splitlines():
                    if ":" in line:
                        key = line.split(':')[0]
                        value = ""
                        for x in line.split(':'):
                            if x != key:
                                value += x
                    else:
                        key = line
                        value = ""
                    extrasDict.update({key: value})
                monster.extras = extrasDict
                try:
                    monster.hp = int(self.bestiaryHpLineEdit.text())
                    monster.maxHp = int(self.bestiaryHpLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Hp is invalid!")
                    return
                try:
                    monster.armorClass = int(self.bestiaryACLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Armor Class is invalid!")
                    return
                try:
                    monster.speed = int(self.bestiarySpeedLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Speed is invalid!")
                    return
                try:
                    monster.strength = int(self.bestiaryStrengthLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Strength is invalid!")
                    return
                try:
                    monster.dexterity = int(self.bestiaryDexterityLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Dexterity is invalid!")
                    return
                try:
                    monster.constitution = int(self.bestiaryConstitutionLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Constitution is invalid!")
                    return
                try:
                    monster.intelligence = int(self.bestiaryIntelligenceLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Intelligence is invalid!")
                    return
                try:
                    monster.wisdom = int(self.bestiaryWisdomLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Wisdom is invalid!")
                    return
                try:
                    monster.charisma = int(self.bestiaryCharismaLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Charisma is invalid!")
                    return

                # Remove old .json file
                try:
                    if oldName != monster.name:
                        os.remove(f"{os.getcwd()}\\DB\\Monsters\\{oldName}.json")
                except FileNotFoundError:
                    pass
                # Create new .json file
                monster.save()
                # Update UI and self.adventure data
                for k, i in enumerate(self.adventure.entities):
                    if i.name == monster.name:
                        self.adventure.entities[k] = monster
                        self.bestiaryList.item(self.bestiaryList.currentRow()).setText(monster.name)
                        self.bestiaryList.item(self.bestiaryList.currentRow()).setData(Qt.UserRole + 1, monster)

    def __init__(self, adv: Adventure) -> None:
        """Bestiary tab"""
        super().__init__()
        self.adventure = adv
        self.selected: Entity = None

        self.bestiaryList = QListWidget()
        self.selected = None
        self.bestiarySizeLineEdit = QLineEdit()
        self.bestiaryAlignmentLineEdit = QLineEdit()
        self.bestiaryNameLineEdit = QLineEdit()
        self.bestiaryProfilePicLineEdit = QLineEdit()
        self.bestiaryAttacksTextEdit = QTextEdit()
        self.bestiaryEquipTextEdit = QTextEdit()
        self.bestiarySkillsTextEdit = QTextEdit()
        self.bestiaryExtrasTextEdit = QTextEdit()
        self.bestiaryHpLineEdit = QLineEdit()
        self.bestiaryACLineEdit = QLineEdit()
        self.bestiarySpeedLineEdit = QLineEdit()
        self.bestiaryStrengthLineEdit = QLineEdit()
        self.bestiaryDexterityLineEdit = QLineEdit()
        self.bestiaryConstitutionLineEdit = QLineEdit()
        self.bestiaryIntelligenceLineEdit = QLineEdit()
        self.bestiaryWisdomLineEdit = QLineEdit()
        self.bestiaryCharismaLineEdit = QLineEdit()

        self.initBestiary()

    def getMonsterInfo(self, item):
        self.selected = item.data(Qt.UserRole + 1)
        for monster in self.adventure.entities:
            if monster.entityType == "Monster":
                if monster.name == self.selected.name:
                    # Populate info on the right
                    self.bestiaryProfilePicLineEdit.setText(monster.profilePic)
                    self.bestiaryNameLineEdit.setText(monster.name)
                    self.bestiarySizeLineEdit.setText(monster.size)
                    self.bestiaryAlignmentLineEdit.setText(monster.alignment)

                    attackString = ""
                    self.bestiaryAttacksTextEdit.setText(attackString)
                    if monster.attacks is not None:
                        for k in monster.attacks:
                            attackString += f"{k}:{monster.attacks[k]}\n"
                        self.bestiaryAttacksTextEdit.setText(attackString)

                    skillsString = ""
                    self.bestiarySkillsTextEdit.setText(skillsString)
                    if monster.skills is not None:
                        for k in monster.skills:
                            skillsString += f"{k}:{monster.skills[k]}\n"
                    self.bestiarySkillsTextEdit.setText(skillsString)

                    extrasString = ""
                    self.bestiaryExtrasTextEdit.setText(extrasString)
                    if monster.extras is not None:
                        for k in monster.extras:
                            extrasString += f"{k}:{monster.extras[k]}\n"
                    self.bestiaryExtrasTextEdit.setText(extrasString)

                    equipString = ""
                    self.bestiaryEquipTextEdit.setText(equipString)
                    if monster.equip is not None:
                        for k in monster.equip:
                            equipString += f"{k}:{monster.equip[k]}\n"
                    self.bestiaryEquipTextEdit.setText(equipString)

                    if str(monster.maxHp) != "None":
                        self.bestiaryHpLineEdit.setText(str(monster.maxHp))
                    else:
                        self.bestiaryHpLineEdit.setText(str(0))

                    if str(monster.armorClass) != "None":
                        self.bestiaryACLineEdit.setText(str(monster.armorClass))
                    else:
                        self.bestiaryACLineEdit.setText(str(0))

                    if str(monster.speed) != "None":
                        self.bestiarySpeedLineEdit.setText(str(monster.speed))
                    else:
                        self.bestiarySpeedLineEdit.setText(str(0))

                    if str(monster.strength) != "None":
                        self.bestiaryStrengthLineEdit.setText(str(monster.strength))
                    else:
                        self.bestiaryStrengthLineEdit.setText(str(0))

                    if str(monster.dexterity) != "None":
                        self.bestiaryDexterityLineEdit.setText(str(monster.dexterity))
                    else:
                        self.bestiaryDexterityLineEdit.setText(str(0))

                    if str(monster.constitution) != "None":
                        self.bestiaryConstitutionLineEdit.setText(str(monster.constitution))
                    else:
                        self.bestiaryConstitutionLineEdit.setText(str(0))

                    if str(monster.intelligence) != "None":
                        self.bestiaryIntelligenceLineEdit.setText(str(monster.intelligence))
                    else:
                        self.bestiaryIntelligenceLineEdit.setText(str(0))

                    if str(monster.wisdom) != "None":
                        self.bestiaryWisdomLineEdit.setText(str(monster.wisdom))
                    else:
                        self.bestiaryWisdomLineEdit.setText(str(0))

                    if str(monster.charisma) != "None":
                        self.bestiaryCharismaLineEdit.setText(str(monster.charisma))
                    else:
                        self.bestiaryCharismaLineEdit.setText(str(0))

    def initBestiary(self):
        directoryExistsCreate(f"{os.getcwd()}\\DB\\")
        directoryExistsCreate(f"{os.getcwd()}\\DB\\Monsters")
        directoryExistsCreate(f"{os.getcwd()}\\DB\\Monsters\\Images")
        verticalLayout = QVBoxLayout()
        buttonsGridLayout = QGridLayout()
        horizontalLayout = QHBoxLayout()
        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addLayout(buttonsGridLayout)
        self.bestiaryList.itemClicked.connect(self.getMonsterInfo)
        bestiaryInfo = QVBoxLayout()
        # region Bestiary Info
        profilePicLayout = QHBoxLayout()
        nameLayout = QHBoxLayout()
        alignmentLayout = QHBoxLayout()
        sizeLayout = QHBoxLayout()

        profilePicLabel = QLabel("Propic")
        nameLabel = QLabel("Name")
        alignmentLabel = QLabel("Alignment")
        sizeLabel = QLabel("Size")

        profilePicLayout.addWidget(profilePicLabel)
        profilePicLayout.addWidget(self.bestiaryProfilePicLineEdit)

        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(self.bestiaryNameLineEdit)

        alignmentLayout.addWidget(alignmentLabel)
        alignmentLayout.addWidget(self.bestiaryAlignmentLineEdit)

        sizeLayout.addWidget(sizeLabel)
        sizeLayout.addWidget(self.bestiarySizeLineEdit)

        bestiaryInfo.addLayout(profilePicLayout)
        bestiaryInfo.addLayout(nameLayout)
        bestiaryInfo.addLayout(alignmentLayout)
        bestiaryInfo.addLayout(sizeLayout)
        # region Stats
        statsLayout = QHBoxLayout()
        hpLayout = QHBoxLayout()
        acLayout = QHBoxLayout()
        speedLayout = QHBoxLayout()
        strengthLayout = QHBoxLayout()
        dexterityLayout = QHBoxLayout()
        constitutionLayout = QHBoxLayout()
        intelligenceLayout = QHBoxLayout()
        wisdomLayout = QHBoxLayout()
        charismaLayout = QHBoxLayout()

        hpLabel = QLabel("Hp")
        acLabel = QLabel("AC")
        speedLabel = QLabel("Speed")
        strengthLabel = QLabel("Str")
        dexterityLabel = QLabel("Dex")
        constitutionLabel = QLabel("Con")
        intelligenceLabel = QLabel("Int")
        wisdomLabel = QLabel("Wis")
        charismaLabel = QLabel("Cha")

        hpLayout.addWidget(hpLabel)
        hpLayout.addWidget(self.bestiaryHpLineEdit)

        acLayout.addWidget(acLabel)
        acLayout.addWidget(self.bestiaryACLineEdit)

        speedLayout.addWidget(speedLabel)
        speedLayout.addWidget(self.bestiarySpeedLineEdit)

        strengthLayout.addWidget(strengthLabel)
        strengthLayout.addWidget(self.bestiaryStrengthLineEdit)

        dexterityLayout.addWidget(dexterityLabel)
        dexterityLayout.addWidget(self.bestiaryDexterityLineEdit)

        constitutionLayout.addWidget(constitutionLabel)
        constitutionLayout.addWidget(self.bestiaryConstitutionLineEdit)

        intelligenceLayout.addWidget(intelligenceLabel)
        intelligenceLayout.addWidget(self.bestiaryIntelligenceLineEdit)

        wisdomLayout.addWidget(wisdomLabel)
        wisdomLayout.addWidget(self.bestiaryWisdomLineEdit)

        charismaLayout.addWidget(charismaLabel)
        charismaLayout.addWidget(self.bestiaryCharismaLineEdit)

        statsLayout.addLayout(hpLayout)
        statsLayout.addLayout(acLayout)
        statsLayout.addLayout(speedLayout)
        statsLayout.addLayout(strengthLayout)
        statsLayout.addLayout(dexterityLayout)
        statsLayout.addLayout(constitutionLayout)
        statsLayout.addLayout(intelligenceLayout)
        statsLayout.addLayout(wisdomLayout)
        statsLayout.addLayout(charismaLayout)
        bestiaryInfo.addLayout(statsLayout)

        # endregion

        attacksLayout = QHBoxLayout()
        equipLayout = QHBoxLayout()
        skillsLayout = QHBoxLayout()
        extrasLayout = QHBoxLayout()

        attacksLabel = QLabel("Attacks")
        equipLabel = QLabel("Equipment")
        skillsLabel = QLabel("Skills")
        extrasLabel = QLabel("Extras")

        attacksLayout.addWidget(attacksLabel)
        attacksLayout.addWidget(self.bestiaryAttacksTextEdit)

        equipLayout.addWidget(equipLabel)
        equipLayout.addWidget(self.bestiaryEquipTextEdit)

        skillsLayout.addWidget(skillsLabel)
        skillsLayout.addWidget(self.bestiarySkillsTextEdit)

        extrasLayout.addWidget(extrasLabel)
        extrasLayout.addWidget(self.bestiaryExtrasTextEdit)

        bestiaryInfo.addLayout(attacksLayout)
        bestiaryInfo.addLayout(equipLayout)
        bestiaryInfo.addLayout(skillsLayout)
        bestiaryInfo.addLayout(extrasLayout)

        # endregion
        horizontalLayout.addWidget(self.bestiaryList)
        horizontalLayout.addLayout(bestiaryInfo)

        deleteButton = QPushButton("Delete")
        createButton = QPushButton("Create")
        saveButton = QPushButton("Save")

        deleteButton.clicked.connect(self.delete)
        createButton.clicked.connect(self.createNew)
        saveButton.clicked.connect(self.save)

        buttonsGridLayout.addWidget(deleteButton, 0, 0)
        buttonsGridLayout.addWidget(createButton, 0, 1)
        buttonsGridLayout.addWidget(saveButton, 0, 2)

        self.setLayout(verticalLayout)

        for monster in self.adventure.entities:
            if monster.entityType == "Monster":
                item = QListWidgetItem(monster.name)
                item.setData(Qt.UserRole + 1, monster)
                self.bestiaryList.addItem(item)
