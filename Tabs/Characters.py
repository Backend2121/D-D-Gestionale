import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import jsonpickle
from Classes.Adventure import Adventure
from Classes.Character import Character
from Classes.User import User
from Utils import sendAlert, confirmDialogue
from Utils import validateName, directoryExistsCreate


class Characters(QWidget):
    
    def delete(self) -> None:
        if self.selected is not None:
            for character in self.adventure.entities:
                if character == self.selected:
                    cnf = confirmDialogue()
                    if cnf.exec():
                        self.adventure.entities.remove(character)
                        self.characterList.takeItem(self.characterList.currentRow())
                        # Remove this character from it's owner's charactersList
                        for path in os.listdir(f"{os.getcwd()}\\DB\\Users"):
                            if path.replace(".json", "") == self.selected.owner.name:
                                u: User
                                with open(f"{os.getcwd()}\\DB\\Users\\{path}") as f:
                                    u = jsonpickle.loads(f.read())
                                try:
                                    u.load()
                                    u.removeCharacter(self.selected.name)
                                    u.removeAdventure(self.adventure.name)
                                except Exception as e:
                                    # Not the user who owns the Character
                                    print(e)
                                    pass
                                u.save()
                        if os.path.isfile(f"{os.getcwd()}\\DB\\Characters\\{character.name}.json"):
                            os.remove(f"{os.getcwd()}\\DB\\Characters\\{character.name}.json")
                        self.adventure.save()
                        break

    def save(self) -> None:
        character: Character = self.selected
        oldName = character.name
        if character != None:
            if validateName(self.characterNameLineEdit.text()):
                # Set all the parameters to the new ones
                character.name = self.characterNameLineEdit.text()
                character.alignment = self.characterAlignmentLineEdit.text()
                character.size = self.characterSizeLineEdit.text()
                character.profilePic = self.characterProfilePicLineEdit.text()
                character.gameClass = self.characterGameClassLineEdit.text()
                character.race = self.characterRaceLineEdit.text()
                character.playerName = self.characterPlayerNameLineEdit.text()
                # This solution allows the use of multiple : but they get removed
                attacksDict = {}
                line: str
                for line in self.characterAttacksTextEdit.toPlainText().splitlines():
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
                character.attacks = attacksDict
                equipDict = {}
                line: str
                for line in self.characterEquipTextEdit.toPlainText().splitlines():
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
                character.equip = equipDict

                skillsDict = {}
                line: str
                for line in self.characterSkillsTextEdit.toPlainText().splitlines():
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
                character.skills = skillsDict

                extrasDict = {}
                line: str
                for line in self.characterExtraTextEdit.toPlainText().splitlines():
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
                character.extras = extrasDict
                try:
                    character.strength = int(self.characterStrengthLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Strength is invalid!")
                    return
                try:
                    character.dexterity = int(self.characterDexterityLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Dexterity is invalid!")
                    return
                try:
                    character.constitution = int(self.characterConstitutionLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Constitution is invalid!")
                    return
                try:
                    character.intelligence = int(self.characterIntelligenceLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Intelligence is invalid!")
                    return
                try:
                    character.wisdom = int(self.characterWisdomLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Wisdom is invalid!")
                    return
                try:
                    character.charisma = int(self.characterCharismaLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Charisma is invalid!")
                    return
                try:
                    character.level = int(self.characterLevelLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Level is invalid!")
                    return
                try:
                    character.AC = int(self.characterArmorClassLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "AC is invalid!")
                    return
                try:
                    character.speed = int(self.characterSpeedLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Speed is invalid!")
                    return
                try:
                    character.hp = int(self.characterHpLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Hp is invalid!")
                    return
                try:
                    character.maxHp = int(self.characterMaxHpLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Max Hp is invalid!")
                    return

                # Remove old .json file
                try:
                    if oldName != character.name:
                        os.remove(f"{os.getcwd()}\\DB\\Characters\\{oldName}.json")
                except FileNotFoundError:
                    pass
                # Create new .json file
                character.save()
                # Update UI and self.adventure data
                for k, i in enumerate(self.adventure.entities):
                    if i.name == character.name:
                        self.adventure.entities[k] = character
                        self.characterList.item(self.characterList.currentRow()).setText(character.name)
                        self.characterList.item(self.characterList.currentRow()).setData(Qt.UserRole + 1, character)
                self.adventure.save()

    def __init__(self, adv: Adventure, user: User) -> None:
        """Characters tab"""
        super().__init__()
        self.adventure = adv
        self.selected: Character = None
        self.user = user

        self.characterList = QListWidget()
        self.characterNameLineEdit = QLineEdit()
        self.characterGameClassLineEdit = QLineEdit()
        self.characterLevelLineEdit = QLineEdit()
        self.characterRaceLineEdit = QLineEdit()
        self.characterAlignmentLineEdit = QLineEdit()
        self.characterSizeLineEdit = QLineEdit()
        self.characterProfilePicLineEdit = QLineEdit()
        self.characterArmorClassLineEdit = QLineEdit()
        self.characterSpeedLineEdit = QLineEdit()
        self.characterHpLineEdit = QLineEdit()
        self.characterMaxHpLineEdit = QLineEdit()
        self.characterPlayerNameLineEdit = QLineEdit()

        self.characterAttacksTextEdit = QTextEdit()
        self.characterEquipTextEdit = QTextEdit()
        self.characterSkillsTextEdit = QTextEdit()
        self.characterExtraTextEdit = QTextEdit()
        self.characterStrengthLineEdit = QLineEdit()
        self.characterDexterityLineEdit = QLineEdit()
        self.characterConstitutionLineEdit = QLineEdit()
        self.characterIntelligenceLineEdit = QLineEdit()
        self.characterWisdomLineEdit = QLineEdit()
        self.characterCharismaLineEdit = QLineEdit()

        self.initCharacters()

    def getCharacterInfo(self, item):
        self.selected = item.data(Qt.UserRole + 1)
        for character in self.adventure.entities:
            if character.entityType == "Character":
                if character.name == self.selected.name:
                    # Populate info on the right
                    self.characterProfilePicLineEdit.setText(character.profilePic)
                    self.characterNameLineEdit.setText(character.name)
                    self.characterSizeLineEdit.setText(character.size)
                    self.characterAlignmentLineEdit.setText(character.alignment)
                    self.characterGameClassLineEdit.setText(character.gameClass)
                    self.characterRaceLineEdit.setText(character.race)
                    self.characterPlayerNameLineEdit.setText(character.playerName)

                    attackString = ""
                    self.characterAttacksTextEdit.setText(attackString)
                    if character.attacks is not None:
                        for k in character.attacks:
                            attackString += f"{k}:{character.attacks[k]}\n"
                        self.characterAttacksTextEdit.setText(attackString)

                    skillsString = ""
                    self.characterSkillsTextEdit.setText(skillsString)
                    if character.skills is not None:
                        for k in character.skills:
                            skillsString += f"{k}:{character.skills[k]}\n"
                    self.characterSkillsTextEdit.setText(skillsString)

                    equipString = ""
                    self.characterEquipTextEdit.setText(equipString)
                    if character.equip is not None:
                        for k in character.equip:
                            equipString += f"{k}:{character.equip[k]}\n"
                    self.characterEquipTextEdit.setText(equipString)

                    extraString = ""
                    self.characterExtraTextEdit.setText(extraString)
                    if character.extras is not None:
                        for k in character.extras:
                            extraString += f"{k}:{character.extras[k]}\n"
                    self.characterExtraTextEdit.setText(extraString)

                    if str(character.strength) != "None":
                        self.characterStrengthLineEdit.setText(str(character.strength))
                    else:
                        self.characterStrengthLineEdit.setText(str(0))

                    if str(character.dexterity) != "None":
                        self.characterDexterityLineEdit.setText(str(character.dexterity))
                    else:
                        self.characterDexterityLineEdit.setText(str(0))

                    if str(character.constitution) != "None":
                        self.characterConstitutionLineEdit.setText(str(character.constitution))
                    else:
                        self.characterConstitutionLineEdit.setText(str(0))

                    if str(character.intelligence) != "None":
                        self.characterIntelligenceLineEdit.setText(str(character.intelligence))
                    else:
                        self.characterIntelligenceLineEdit.setText(str(0))

                    if str(character.wisdom) != "None":
                        self.characterWisdomLineEdit.setText(str(character.wisdom))
                    else:
                        self.characterWisdomLineEdit.setText(str(0))

                    if str(character.charisma) != "None":
                        self.characterCharismaLineEdit.setText(str(character.charisma))
                    else:
                        self.characterCharismaLineEdit.setText(str(0))

                    if str(character.level) != "None":
                        self.characterLevelLineEdit.setText(str(character.level))
                    else:
                        self.characterLevelLineEdit.setText(str(0))

                    if str(character.armorClass) != "None":
                        self.characterArmorClassLineEdit.setText(str(character.armorClass))
                    else:
                        self.characterArmorClassLineEdit.setText(str(0))

                    if str(character.speed) != "None":
                        self.characterSpeedLineEdit.setText(str(character.speed))
                    else:
                        self.characterSpeedLineEdit.setText(str(0))

                    if str(character.hp) != "None":
                        self.characterHpLineEdit.setText(str(character.hp))
                    else:
                        self.characterHpLineEdit.setText(str(0))

                    if str(character.maxHp) != "None":
                        self.characterMaxHpLineEdit.setText(str(character.maxHp))
                    else:
                        self.characterMaxHpLineEdit.setText(str(0))

    def initCharacters(self):
        # Create all necessary directories
        directoryExistsCreate(f"{os.getcwd()}\\DB\\")
        directoryExistsCreate(f"{os.getcwd()}\\DB\\Characters")
        directoryExistsCreate(f"{os.getcwd()}\\DB\\Characters\\Images")
        verticalLayout = QVBoxLayout()
        buttonsGridLayout = QGridLayout()
        horizontalLayout = QHBoxLayout()
        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addLayout(buttonsGridLayout)
        self.characterList.itemClicked.connect(self.getCharacterInfo)
        charactersInfo = QVBoxLayout()
        # region Character Info
        profilePicLayout = QHBoxLayout()
        nameLayout = QHBoxLayout()
        alignmentLayout = QHBoxLayout()
        sizeLayout = QHBoxLayout()
        gameClassLayout = QHBoxLayout()
        levelLayout = QHBoxLayout()
        raceLayout = QHBoxLayout()
        playerNameLayout = QHBoxLayout()

        profilePicLabel = QLabel("Propic")
        nameLabel = QLabel("Name")
        alignmentLabel = QLabel("Alignment")
        sizeLabel = QLabel("Size")
        gameClassLabel = QLabel("Class")
        levelLabel = QLabel("Level")
        raceLabel = QLabel("Race")
        playerNameLabel = QLabel("Player Name")

        gameClassLayout.addWidget(gameClassLabel)
        gameClassLayout.addWidget(self.characterGameClassLineEdit)

        levelLayout.addWidget(levelLabel)
        levelLayout.addWidget(self.characterLevelLineEdit)

        raceLayout.addWidget(raceLabel)
        raceLayout.addWidget(self.characterRaceLineEdit)

        playerNameLayout.addWidget(playerNameLabel)
        playerNameLayout.addWidget(self.characterPlayerNameLineEdit)

        profilePicLayout.addWidget(profilePicLabel)
        profilePicLayout.addWidget(self.characterProfilePicLineEdit)

        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(self.characterNameLineEdit)

        alignmentLayout.addWidget(alignmentLabel)
        alignmentLayout.addWidget(self.characterAlignmentLineEdit)

        sizeLayout.addWidget(sizeLabel)
        sizeLayout.addWidget(self.characterSizeLineEdit)

        charactersInfo.addLayout(profilePicLayout)
        charactersInfo.addLayout(nameLayout)
        charactersInfo.addLayout(alignmentLayout)
        charactersInfo.addLayout(sizeLayout)
        charactersInfo.addLayout(gameClassLayout)
        charactersInfo.addLayout(levelLayout)
        charactersInfo.addLayout(raceLayout)
        charactersInfo.addLayout(playerNameLayout)
        # region Stats

        stats1Layout = QHBoxLayout()
        ACLayout = QHBoxLayout()
        speedLayout = QHBoxLayout()
        hpLayout = QHBoxLayout()
        maxHpLayout = QHBoxLayout()

        ACLabel = QLabel("AC")
        speedLabel = QLabel("Speed")
        hpLabel = QLabel("Hp")
        maxHpLabel = QLabel("Max Hp")

        ACLayout.addWidget(ACLabel)
        ACLayout.addWidget(self.characterArmorClassLineEdit)

        speedLayout.addWidget(speedLabel)
        speedLayout.addWidget(self.characterSpeedLineEdit)

        hpLayout.addWidget(hpLabel)
        hpLayout.addWidget(self.characterHpLineEdit)

        maxHpLayout.addWidget(maxHpLabel)
        maxHpLayout.addWidget(self.characterMaxHpLineEdit)

        stats1Layout.addLayout(ACLayout)
        stats1Layout.addLayout(speedLayout)
        stats1Layout.addLayout(hpLayout)
        stats1Layout.addLayout(maxHpLayout)

        statsLayout = QHBoxLayout()
        strengthLayout = QHBoxLayout()
        dexterityLayout = QHBoxLayout()
        constitutionLayout = QHBoxLayout()
        intelligenceLayout = QHBoxLayout()
        wisdomLayout = QHBoxLayout()
        charismaLayout = QHBoxLayout()

        strengthLabel = QLabel("Str")
        dexterityLabel = QLabel("Dex")
        constitutionLabel = QLabel("Con")
        intelligenceLabel = QLabel("Int")
        wisdomLabel = QLabel("Wis")
        charismaLabel = QLabel("Cha")

        strengthLayout.addWidget(strengthLabel)
        strengthLayout.addWidget(self.characterStrengthLineEdit)

        dexterityLayout.addWidget(dexterityLabel)
        dexterityLayout.addWidget(self.characterDexterityLineEdit)

        constitutionLayout.addWidget(constitutionLabel)
        constitutionLayout.addWidget(self.characterConstitutionLineEdit)

        intelligenceLayout.addWidget(intelligenceLabel)
        intelligenceLayout.addWidget(self.characterIntelligenceLineEdit)

        wisdomLayout.addWidget(wisdomLabel)
        wisdomLayout.addWidget(self.characterWisdomLineEdit)

        charismaLayout.addWidget(charismaLabel)
        charismaLayout.addWidget(self.characterCharismaLineEdit)

        statsLayout.addLayout(strengthLayout)
        statsLayout.addLayout(dexterityLayout)
        statsLayout.addLayout(constitutionLayout)
        statsLayout.addLayout(intelligenceLayout)
        statsLayout.addLayout(wisdomLayout)
        statsLayout.addLayout(charismaLayout)

        charactersInfo.addLayout(stats1Layout)
        charactersInfo.addLayout(statsLayout)

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
        attacksLayout.addWidget(self.characterAttacksTextEdit)

        equipLayout.addWidget(equipLabel)
        equipLayout.addWidget(self.characterEquipTextEdit)

        skillsLayout.addWidget(skillsLabel)
        skillsLayout.addWidget(self.characterSkillsTextEdit)

        extrasLayout.addWidget(extrasLabel)
        extrasLayout.addWidget(self.characterExtraTextEdit)

        charactersInfo.addLayout(attacksLayout)
        charactersInfo.addLayout(equipLayout)
        charactersInfo.addLayout(skillsLayout)
        charactersInfo.addLayout(extrasLayout)

        # endregion
        horizontalLayout.addWidget(self.characterList)
        horizontalLayout.addLayout(charactersInfo)

        deleteButton = QPushButton("Delete")
        # createButton = QPushButton("Create")
        saveButton = QPushButton("Save")

        deleteButton.clicked.connect(self.delete)
        # createButton.clicked.connect(self.createNew)
        saveButton.clicked.connect(self.save)

        # TODO Only if DM
        if self.adventure.owner.name == self.user.name:
            buttonsGridLayout.addWidget(deleteButton, 0, 0)
        # buttonsGridLayout.addWidget(createButton, 0, 1)
        buttonsGridLayout.addWidget(saveButton, 0, 1)

        self.setLayout(verticalLayout)

        for character in self.adventure.entities:
            if character.entityType == "Character":
                item = QListWidgetItem(character.name)
                item.setData(Qt.UserRole + 1, character)
                self.characterList.addItem(item)
