import os

import jsonpickle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from Classes.Adventure import Adventure
from Classes.Character import Character
from Classes.User import User
from Utils import directoryExistsCreate, sendAlert, createFolderStructure, confirmDialogue, validateName
from MainPage import MainWindow


# NOTES: I named the saving throws page the Stats page at code level
class Entry(QWidget):
    def populateAdventuresList(self) -> None:
        # List all adventures
        self.listAdventuresListWidget.clear()
        for adv in self.user.adventuresList:
            item = QListWidgetItem(adv.name)
            self.listAdventuresListWidget.addItem(item)

    def deleteAdventure(self) -> None:
        if self.selected == None:
            sendAlert("Warning", "No adventure is selected", QMessageBox.Warning)
        else:
            for path in os.listdir(f"{os.getcwd()}\\DB\\Adventures\\"):
                if self.selected == path.replace(".json", ""):
                    print(f"{os.getcwd()}\\DB\\Adventures\\{path}")
                    with open(f"{os.getcwd()}\\DB\\Adventures\\{path}") as f:
                        adv: Adventure = jsonpickle.loads(f.read())
                    if adv.owner.name == self.user.name:
                        cnf = confirmDialogue()
                        if cnf.exec():
                            path = f"{os.getcwd()}\\DB\\Adventures\\{self.selected}.json"
                            self.listAdventuresListWidget.takeItem(self.listAdventuresListWidget.currentRow())
                            self.user.removeAdventure(adv)
                            self.user.save()
                            os.remove(path)
                    else:
                        sendAlert("Warning", "You can't delete an adventure you do not own")

    def loadAdventure(self) -> None:
        if self.selected == None:
            sendAlert("Warning", "No adventure is selected", QMessageBox.Warning)
        else:
            self.loadMain()

    def loadMain(self) -> None:
        self.menuWindow.close()
        self.mw = MainWindow(adventureName=self.selected, user=self.user)
        self.mw.show()

    def setSelected(self, name: QListWidgetItem) -> None:
        self.selected = name.text()

    def __init__(self):
        super().__init__()
        # Adventure selected
        self.selected = None
        createFolderStructure()
        # INITIALIZING WINDOWS

        # INITIALIZING LOGIN INTERFACE WINDOW
        loginWindow = QWidget()
        loginWindow.setGeometry(1000, 1000, 800, 800)
        loginWindow.setWindowTitle('Login')

        # INITIALIZING REGISTER WINDOW
        registrationWindow = QWidget()
        registrationWindow.setGeometry(1000, 1000, 800, 800)
        registrationWindow.setWindowTitle('Register')

        # INITIALIZING MENU WINDOW
        self.menuWindow = QWidget()
        self.menuWindow.setGeometry(1000, 1000, 800, 800)
        self.menuWindow.setWindowTitle('Menu')

        # INITIALIZING CREATION WINDOW
        creationWindow = QWidget()
        creationWindow.setGeometry(1000, 1000, 800, 800)
        creationWindow.setWindowTitle('Create Adventure')

        # INITIALIZING JOIN WINDOW
        joinWindow = QWidget()
        joinWindow.setGeometry(1000, 1000, 800, 800)
        joinWindow.setWindowTitle('Join Adventure')

        # INITIALIZING CHARACTER CREATION WINDOW
        characterCreationWindow = QWidget()
        characterCreationWindow.setGeometry(1000, 1000, 800, 800)
        characterCreationWindow.setWindowTitle('Create Character')

        # INITIALIZING STATS WINDOW
        statsWindow = QWidget()
        statsWindow.setGeometry(1000, 1000, 800, 800)
        statsWindow.setWindowTitle('Create Character')

        # INITIALIZING TRAITS WINDOW
        traitsWindow = QWidget()
        traitsWindow.setGeometry(1000, 1000, 800, 800)
        traitsWindow.setWindowTitle('Create Character')

        # INITIALIZING BONUS STATS WINDOW
        bonusStatsWindow = QWidget()
        bonusStatsWindow.setGeometry(1000, 1000, 800, 800)
        bonusStatsWindow.setWindowTitle('Create Character')

        # INITIALIZING SKILLS WINDOW
        skillsWindow = QWidget()
        skillsWindow.setGeometry(1000, 1000, 800, 800)
        skillsWindow.setWindowTitle('Create Character')

        # INITIALIZING SKILLS2 WINDOW
        skills2Window = QWidget()
        skills2Window.setGeometry(1000, 1000, 800, 800)
        skills2Window.setWindowTitle('Create Character')

        # INITIALIZING DICE WINDOW
        diceWindow = QWidget()
        diceWindow.setGeometry(1000, 1000, 800, 800)
        diceWindow.setWindowTitle('Create Character')

        # INITIALIZING ATTACKS WINDOW
        attacksWindow = QWidget()
        attacksWindow.setGeometry(1000, 1000, 800, 800)
        attacksWindow.setWindowTitle('Create Character')

        # INITIALIZING OTHER PROFICIENCIES WINDOW
        otherProficienciesWindow = QWidget()
        otherProficienciesWindow.setGeometry(1000, 1000, 800, 800)
        otherProficienciesWindow.setWindowTitle('Create Character')

        # INITIALIZING FEATURES WINDOW
        featuresWindow = QWidget()
        featuresWindow.setGeometry(1000, 1000, 800, 800)
        featuresWindow.setWindowTitle('Create Character')

        # INITIALIZING EQUIPMENT PIECES WINDOW
        equipmentPiecesWindow = QWidget()
        equipmentPiecesWindow.setGeometry(1000, 1000, 800, 800)
        equipmentPiecesWindow.setWindowTitle('Create Character')

        # INITIALIZING EQUIPMENT WINDOW
        equipmentWindow = QWidget()
        equipmentWindow.setGeometry(1000, 1000, 800, 800)
        equipmentWindow.setWindowTitle('Create Character')

        # INITIALIZING PHYSICAL WINDOW
        physicalWindow = QWidget()
        physicalWindow.setGeometry(1000, 1000, 800, 800)
        physicalWindow.setWindowTitle('Create Character')

        # INITIALIZING CHARACTER APPEARANCE WINDOW
        characterAppearanceWindow = QWidget()
        characterAppearanceWindow.setGeometry(1000, 1000, 800, 800)
        characterAppearanceWindow.setWindowTitle('Create Character')

        # INITIALIZING BACKSTORY WINDOW
        backstoryWindow = QWidget()
        backstoryWindow.setGeometry(1000, 1000, 800, 800)
        backstoryWindow.setWindowTitle('Create Character')

        # INITIALIZING ALLIES WINDOW
        alliesWindow = QWidget()
        alliesWindow.setGeometry(1000, 1000, 800, 800)
        alliesWindow.setWindowTitle('Create Character')

        # INITIALIZING SYMBOL WINDOW
        symbolWindow = QWidget()
        symbolWindow.setGeometry(1000, 1000, 800, 800)
        symbolWindow.setWindowTitle('Create Character')

        # INITIALIZING ADDITIONAL FEATURES WINDOW
        additionalFeaturesWindow = QWidget()
        additionalFeaturesWindow.setGeometry(1000, 1000, 800, 800)
        additionalFeaturesWindow.setWindowTitle('Create Character')

        # INITIALIZING TREASURE WINDOW
        treasureWindow = QWidget()
        treasureWindow.setGeometry(1000, 1000, 800, 800)
        treasureWindow.setWindowTitle('Create Character')

        # INITIALIZING SPELL WINDOW
        spellWindow = QWidget()
        spellWindow.setGeometry(1000, 1000, 800, 800)
        spellWindow.setWindowTitle('Create Character')

        # INITIALIZING CANTRIPS WINDOW
        cantripsWindow = QWidget()
        cantripsWindow.setGeometry(1000, 1000, 800, 800)
        cantripsWindow.setWindowTitle('Create Character')

        # INITIALIZING SPELL LIST WINDOW
        spellListWindow = QWidget()
        spellListWindow.setGeometry(1000, 1000, 800, 800)
        spellListWindow.setWindowTitle('Create Character')

        # CHARACTER CREATION FIRST PAGE SECTION

        # INITIALIZING LAYOUTS
        characterCreationLayout = QVBoxLayout()
        buttonsLayout = QHBoxLayout()

        # TITLE OF THE LOGIN INTERFACE
        characterCreationTitle = QLabel("Character Main Features")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        characterCreationTitle.setFont(font)
        alignment = Qt.AlignHCenter
        characterCreationTitle.setAlignment(alignment)

        # USERNAME
        characterNameLabel = QLabel("Name your character: ")
        characterNameEdit = QLineEdit()
        characterNameEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        characterNameEdit.setFixedWidth(300)
        characterNameEdit.setFixedHeight(30)
        characterNameFont = QFont('Arial')
        characterNameFont.setPointSize(30)
        characterNameLabel.setFont(characterNameFont)

        # CLASS
        characterClassLabel = QLabel("Choose a Class: ")
        characterClassEdit = QLineEdit()
        characterClassEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        characterClassEdit.setFixedWidth(300)
        characterClassEdit.setFixedHeight(30)
        characterClassFont = QFont('Arial')
        characterClassFont.setPointSize(30)
        characterClassLabel.setFont(characterClassFont)

        # LEVEL
        levelLabel = QLabel("Choose a Level: ")
        levelEdit = QLineEdit()
        levelEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        levelEdit.setFixedWidth(300)
        levelEdit.setFixedHeight(30)
        levelLabelFont = QFont('Arial')
        levelLabelFont.setPointSize(30)
        levelLabel.setFont(levelLabelFont)

        # RACE
        raceLabel = QLabel("Choose a Race: ")
        raceEdit = QLineEdit()
        raceEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        raceEdit.setFixedWidth(300)
        raceEdit.setFixedHeight(30)
        raceLabelFont = QFont('Arial')
        raceLabelFont.setPointSize(30)
        raceLabel.setFont(raceLabelFont)

        # BACKGROUND
        backgroundLabel = QLabel("Choose a Background: ")
        backgroundEdit = QLineEdit()
        backgroundEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        backgroundEdit.setFixedWidth(300)
        backgroundEdit.setFixedHeight(30)
        backgroundLabelFont = QFont('Arial')
        backgroundLabelFont.setPointSize(30)
        backgroundLabel.setFont(backgroundLabelFont)

        # ALIGNMENT
        characterAlignmentLabel = QLabel("Choose an Alignment: ")
        characterAlignmentEdit = QLineEdit()
        characterAlignmentEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        characterAlignmentEdit.setFixedWidth(300)
        characterAlignmentEdit.setFixedHeight(30)
        characterAlignmentLabelFont = QFont('Arial')
        characterAlignmentLabelFont.setPointSize(30)
        characterAlignmentLabel.setFont(characterAlignmentLabelFont)

        # PLAYER NAME
        playerNameLabel = QLabel("Player Name: ")
        playerNameEdit = QLineEdit()
        playerNameEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        playerNameEdit.setFixedWidth(300)
        playerNameEdit.setFixedHeight(30)
        playerNameFont = QFont('Arial')
        playerNameFont.setPointSize(30)
        playerNameLabel.setFont(playerNameFont)

        # EXPERIENCE POINTS
        characterExperienceLabel = QLabel("Choose the amount of Experience Points: ")
        characterExperienceEdit = QLineEdit()
        characterExperienceEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        characterExperienceEdit.setFixedWidth(300)
        characterExperienceEdit.setFixedHeight(30)
        characterExperienceLabelFont = QFont('Arial')
        characterExperienceLabelFont.setPointSize(30)
        characterExperienceLabel.setFont(characterExperienceLabelFont)

        # BACK BUTTON
        backButton = QPushButton("Return to Menu")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(
            lambda: goBackToMenuFromCharacterCreationWindow(characterCreationWindow, self.menuWindow))

        def createCharacter() -> Character | None:
            directoryExistsCreate(f"{os.getcwd()}\\DB")
            directoryExistsCreate(f"{os.getcwd()}\\DB\\Characters")
            for file in os.listdir(f"{os.getcwd()}\\DB\\Characters"):
                if file.replace(".json", "") != character.name:
                    if not validateName(nameLineEdit.text()):
                        return
                    character.name = nameLineEdit.text()
                    character.gameClass = gameClassLineEdit.text()
                    try:
                        character.level = int(levelLineEdit.text())
                    except:
                        sendAlert("Invalid number", "Level is invalid!", QMessageBox.Critical)
                        return
                    character.race = raceLineEdit.text()
                    character.alignment = alignmentLineEdit.text()
                    # Can't be None because of previous required login
                    character.playerName = self.user.name
                    character.adventure = codeEdit.text()
                    character.size = sizeLineEdit.text()
                    try:
                        character.strength = int(strengthLineEdit.text())
                    except:
                        sendAlert("Invalid number", "Strength is invalid!", QMessageBox.Critical)
                        return
                    try:
                        character.dexterity = int(dexterityLineEdit.text())
                    except:
                        sendAlert("Invalid number", "Dexterity is invalid!", QMessageBox.Critical)
                        return
                    try:
                        character.constitution = int(constitutionLineEdit.text())
                    except:
                        sendAlert("Invalid number", "Constitution is invalid!", QMessageBox.Critical)
                        return
                    try:
                        character.intelligence = int(strengthLineEdit.text())
                    except:
                        sendAlert("Invalid number", "Intelligence is invalid!", QMessageBox.Critical)
                        return
                    try:
                        character.wisdom = int(strengthLineEdit.text())
                    except:
                        sendAlert("Invalid number", "Wisdom is invalid!", QMessageBox.Critical)
                        return
                    try:
                        character.charisma = int(strengthLineEdit.text())
                    except:
                        sendAlert("Invalid number", "Charisma is invalid!", QMessageBox.Critical)
                        return

                    try:
                        character.armorClass = int(ACLineEdit.text())
                    except:
                        sendAlert("Invalid number", "Armor Class is invalid!", QMessageBox.Critical)
                        return
                    try:
                        character.speed = int(speedLineEdit.text())
                    except:
                        sendAlert("Invalid number", "Speed is invalid!", QMessageBox.Critical)
                        return
                    try:
                        character.maxHp = int(maxHpLineEdit.text())
                        character.hp = character.maxHp
                    except:
                        sendAlert("Invalid number", "MaxHp is invalid!", QMessageBox.Critical)
                        return

                    attacksDict = {}
                    line: str
                    for line in attacksTextEdit.toPlainText().splitlines():
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
                    for line in equipmentTextEdit.toPlainText().splitlines():
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
                    for line in skillsTextEdit.toPlainText().splitlines():
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
                    for line in extrasTextEdit.toPlainText().splitlines():
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
                    character.owner = self.user
                    character.save()
                else:
                    sendAlert("Error", "Character name already exists!", QMessageBox.Critical)
                    return
            self.user.addCharacter(character)
            with open(f"{os.getcwd()}\\DB\\Adventures\\{codeEdit.text()}.json") as f:
                adv: Adventure = jsonpickle.loads(f.read())
                self.user.addAdventure(adv)
            self.user.save()
            # Load Main Page
            self.mw = MainWindow(adventureName=codeEdit.text(), user=self.user)
            characterCreationWindow.close()
            self.mw.show()

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(createCharacter)

        # ADDING WIDGETS TO THE LAYOUT
        characterCreationLayout.addWidget(characterCreationTitle)
        characterCreationLayout.addWidget(characterNameLabel)
        characterCreationLayout.addWidget(characterNameEdit)
        characterCreationLayout.addWidget(characterClassLabel)
        characterCreationLayout.addWidget(characterClassEdit)
        characterCreationLayout.addWidget(levelLabel)
        characterCreationLayout.addWidget(levelEdit)
        characterCreationLayout.addWidget(raceLabel)
        characterCreationLayout.addWidget(raceEdit)
        characterCreationLayout.addWidget(backgroundLabel)
        characterCreationLayout.addWidget(backgroundEdit)
        characterCreationLayout.addWidget(characterAlignmentLabel)
        characterCreationLayout.addWidget(characterAlignmentEdit)
        characterCreationLayout.addWidget(playerNameLabel)
        characterCreationLayout.addWidget(playerNameEdit)
        characterCreationLayout.addWidget(characterExperienceLabel)
        characterCreationLayout.addWidget(characterExperienceEdit)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        characterCreationWindow.setStyleSheet("background-color: #D2B48C")

        # CENTERING THE LAYOUT
        layoutAlignment = Qt.AlignCenter
        characterCreationLayout.setAlignment(layoutAlignment)

        # ATTACHING CHARACTER CREATION LAYOUT TO BUTTONS LAYOUT
        # characterCreationLayout.addLayout(buttonsLayout)

        # region Character Creation Layout
        verticalLayout = QVBoxLayout()
        buttonsGridLayout = QGridLayout()
        horizontalLayout = QHBoxLayout()
        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addLayout(buttonsGridLayout)
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

        nameLabel = QLabel("Name")
        nameLineEdit = QLineEdit()
        alignmentLabel = QLabel("Alignment")
        alignmentLineEdit = QLineEdit()
        sizeLabel = QLabel("Size")
        sizeLineEdit = QLineEdit()
        gameClassLabel = QLabel("Class")
        gameClassLineEdit = QLineEdit()
        levelLabel = QLabel("Level")
        levelLineEdit = QLineEdit()
        raceLabel = QLabel("Race")
        raceLineEdit = QLineEdit()

        gameClassLayout.addWidget(gameClassLabel)
        gameClassLayout.addWidget(gameClassLineEdit)

        levelLayout.addWidget(levelLabel)
        levelLayout.addWidget(levelLineEdit)

        raceLayout.addWidget(raceLabel)
        raceLayout.addWidget(raceLineEdit)

        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(nameLineEdit)

        alignmentLayout.addWidget(alignmentLabel)
        alignmentLayout.addWidget(alignmentLineEdit)

        sizeLayout.addWidget(sizeLabel)
        sizeLayout.addWidget(sizeLineEdit)

        charactersInfo.addLayout(nameLayout)
        charactersInfo.addLayout(alignmentLayout)
        charactersInfo.addLayout(sizeLayout)
        charactersInfo.addLayout(gameClassLayout)
        charactersInfo.addLayout(levelLayout)
        charactersInfo.addLayout(raceLayout)
        # region Stats

        stats1Layout = QHBoxLayout()
        ACLayout = QHBoxLayout()
        speedLayout = QHBoxLayout()
        hpLayout = QHBoxLayout()
        maxHpLayout = QHBoxLayout()

        ACLabel = QLabel("AC")
        ACLineEdit = QLineEdit()
        speedLabel = QLabel("Speed")
        speedLineEdit = QLineEdit()
        maxHpLabel = QLabel("Max Hp")
        maxHpLineEdit = QLineEdit()

        ACLayout.addWidget(ACLabel)
        ACLayout.addWidget(ACLineEdit)

        speedLayout.addWidget(speedLabel)
        speedLayout.addWidget(speedLineEdit)

        maxHpLayout.addWidget(maxHpLabel)
        maxHpLayout.addWidget(maxHpLineEdit)

        stats1Layout.addLayout(ACLayout)
        stats1Layout.addLayout(speedLayout)
        stats1Layout.addLayout(maxHpLayout)

        statsLayout = QHBoxLayout()
        strengthLayout = QHBoxLayout()
        dexterityLayout = QHBoxLayout()
        constitutionLayout = QHBoxLayout()
        intelligenceLayout = QHBoxLayout()
        wisdomLayout = QHBoxLayout()
        charismaLayout = QHBoxLayout()

        strengthLabel = QLabel("Str")
        strengthLineEdit = QLineEdit()
        dexterityLabel = QLabel("Dex")
        dexterityLineEdit = QLineEdit()
        constitutionLabel = QLabel("Con")
        constitutionLineEdit = QLineEdit()
        intelligenceLabel = QLabel("Int")
        intelligenceLineEdit = QLineEdit()
        wisdomLabel = QLabel("Wis")
        wisdomLineEdit = QLineEdit()
        charismaLabel = QLabel("Cha")
        charismaLineEdit = QLineEdit()

        strengthLayout.addWidget(strengthLabel)
        strengthLayout.addWidget(strengthLineEdit)

        dexterityLayout.addWidget(dexterityLabel)
        dexterityLayout.addWidget(dexterityLineEdit)

        constitutionLayout.addWidget(constitutionLabel)
        constitutionLayout.addWidget(constitutionLineEdit)

        intelligenceLayout.addWidget(intelligenceLabel)
        intelligenceLayout.addWidget(intelligenceLineEdit)

        wisdomLayout.addWidget(wisdomLabel)
        wisdomLayout.addWidget(wisdomLineEdit)

        charismaLayout.addWidget(charismaLabel)
        charismaLayout.addWidget(charismaLineEdit)

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
        attacksTextEdit = QTextEdit()
        equipLabel = QLabel("Equipment")
        equipmentTextEdit = QTextEdit()
        skillsLabel = QLabel("Skills")
        skillsTextEdit = QTextEdit()
        extrasLabel = QLabel("Extras")
        extrasTextEdit = QTextEdit()

        attacksLayout.addWidget(attacksLabel)
        attacksLayout.addWidget(attacksTextEdit)

        equipLayout.addWidget(equipLabel)
        equipLayout.addWidget(equipmentTextEdit)

        skillsLayout.addWidget(skillsLabel)
        skillsLayout.addWidget(skillsTextEdit)

        extrasLayout.addWidget(extrasLabel)
        extrasLayout.addWidget(extrasTextEdit)

        charactersInfo.addLayout(attacksLayout)
        charactersInfo.addLayout(equipLayout)
        charactersInfo.addLayout(skillsLayout)
        charactersInfo.addLayout(extrasLayout)

        # endregion
        # endregion

        # ATTACHING THE LAYOUT TO THE WINDOW
        charactersInfo.addLayout(buttonsLayout)
        characterCreationWindow.setLayout(charactersInfo)

        # DEFINING FUNCTIONS
        self.user: User = User("")
        character: Character = Character(entityType="Character", owner=self.user)

        def createAdventure() -> None:
            directoryExistsCreate(f"{os.getcwd()}\\DB")
            directoryExistsCreate(f"{os.getcwd()}\\DB\\Adventures")
            adv = Adventure(name=adventureNameEdit.text(), owner=self.user)
            self.user.addAdventure(adv)
            adv.owner = self.user
            self.user.save()
            adv.save()

            # Load Main Page
            creationWindow.close()
            self.mw = MainWindow(adventureName=adv.name, user=self.user)
            self.mw.show()

        self.creds = {}

        def saveCredentials():
            directoryExistsCreate(f"{os.getcwd()}\\DB")
            path = f"{os.getcwd()}\\DB\\Credentials.json"
            if os.path.exists(path):
                with open(path, "w") as f:
                    f.write(jsonpickle.dumps(self.creds))

        def readCredentials():
            directoryExistsCreate(f"{os.getcwd()}\\DB")
            path = f"{os.getcwd()}\\DB\\Credentials.json"
            if os.path.exists(path):
                with open(path, "r") as f:
                    self.creds = jsonpickle.loads(f.read())
            else:
                with open(path, "w") as f:
                    f.write(jsonpickle.dumps(self.creds))

        def goToMenu(loginWindow, menuWindow):
            readCredentials()
            if len(self.creds.keys()) == 0:
                sendAlert("Error", "Invalid credentials", QMessageBox.Critical)
                return
            for k in self.creds.keys():
                if username_login_edit.text() != "" and password_login_edit.text() != "":
                    if username_login_edit.text() == k and password_login_edit.text() == self.creds[k]:
                        self.user.name = username_login_edit.text()
                        self.user.load()
                        self.populateAdventuresList()
                        loginWindow.close()
                        menuWindow.show()
                        return
                else:
                    sendAlert("Warning", "Invalid Credentials", QMessageBox.Critical)
                    return
            sendAlert("Error", "Invalid credentials", QMessageBox.Critical)

        def goToCreationAdventure(menuWindow, creationWindow):
            menuWindow.close()
            creationWindow.show()

        def goToJoinAdventure(menuWindow, joinWindow):
            menuWindow.close()
            joinWindow.show()

        def goToLoginFromMenu(menuWindow, loginWindow):
            menuWindow.close()
            loginWindow.show()

        def goBackToMenuWindowFromCreationWindow(creationWindow, menuWindow):
            creationWindow.close()
            menuWindow.show()

        def goToCharacterCreationWindowFromJoinWindow(joinWindow, characterCreationWindow):
            directoryExistsCreate(f"{os.getcwd()}\\DB")
            directoryExistsCreate(f"{os.getcwd()}\\DB\\Adventures")
            for path in os.listdir(f"{os.getcwd()}\\DB\\Adventures"):
                if codeEdit.text() == path.replace(".json", ""):
                    joinWindow.close()
                    characterCreationWindow.show()
                    return
            sendAlert("Error", "Adventure not found", QMessageBox.Critical)

        def goBackToMenuWindowFromJoinWindow(joinWindow, menuWindow):
            joinWindow.close()
            menuWindow.show()

        def goBackToMenuFromCharacterCreationWindow(characterCreationWindow, menuWindow):
            characterCreationWindow.close()
            menuWindow.show()

        def goToRegistrationWindowFromLoginWindow(loginWindow, registrationWindow):
            loginWindow.close()
            registrationWindow.show()

        def goBackToLoginWindowFromRegistrationWindow(registrationWindow, loginWindow):
            registrationWindow.close()
            loginWindow.show()

        def goToMenuWindowFromRegistrationWindow(registrationWindow, menuWindow):
            """Registration logic"""
            readCredentials()
            if len(self.creds) == 0:
                self.creds.update({"": ""})
            for k in self.creds:
                if username_edit.text() == "":
                    sendAlert("Error", "Username can't be blank!", QMessageBox.Critical)
                    return
                elif password_edit.text() == "":
                    sendAlert("Error", "Password can't be blank!", QMessageBox.Critical)
                    return
                elif k == username_edit.text():
                    sendAlert("Error", "Username already taken!", QMessageBox.Critical)
                    return
                elif password_edit.text() != password_confirmation_edit.text():
                    sendAlert("Warning", "Password doesn't match!", QMessageBox.Warning)
                    return
            self.creds.update({f"{username_edit.text()}": f"{password_edit.text()}"})
            saveCredentials()
            self.user.name = username_edit.text()
            self.user = User(name=username_edit.text())
            self.user.load()
            self.user.save()
            self.populateAdventuresList()
            registrationWindow.close()
            menuWindow.show()

        def exitFromMenuWindow():
            exit()

        # JOIN ADVENTURE PAGE SECTION

        joinLayout = QVBoxLayout()

        # TITLE OF THE JOIN INTERFACE
        joinTitle = QLabel('Join Adventure')
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        joinTitle.setFont(font)
        alignment = Qt.AlignHCenter
        joinTitle.setAlignment(alignment)

        # ADVENTURE NAME
        codeLabel = QLabel('Insert Name:')
        codeEdit = QLineEdit()
        codeEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        codeEdit.setFixedWidth(300)
        codeEdit.setFixedHeight(30)
        codeFont = QFont('Arial')
        codeFont.setPointSize(30)
        codeLabel.setFont(codeFont)

        # JOIN BUTTON
        joinButton = QPushButton('Join')
        joinButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        joinButton.clicked.connect(
            lambda: goToCharacterCreationWindowFromJoinWindow(joinWindow, characterCreationWindow))

        # JOIN BACK BUTTON
        joinBackButton = QPushButton('Back')
        joinBackButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        joinBackButton.clicked.connect(lambda: goBackToMenuWindowFromJoinWindow(joinWindow, self.menuWindow))

        # ADDING WIDGETS TO THE LAYOUT
        joinLayout.addWidget(joinTitle)
        joinLayout.addWidget(codeLabel)
        joinLayout.addWidget(codeEdit)
        joinLayout.addWidget(joinButton)
        joinLayout.addWidget(joinBackButton)

        # COLORING THE WINDOW BACKGROUND
        joinWindow.setStyleSheet("background-color: #D2B48C")

        # CENTERING THE LAYOUT
        layoutAlignment = Qt.AlignCenter
        joinLayout.setAlignment(layoutAlignment)

        # ATTACHING THE LAYOUT TO THE WINDOW
        joinWindow.setLayout(joinLayout)

        # ADVENTURE CREATION PAGE SECTION

        creationLayout = QVBoxLayout()

        # TITLE OF THE MENU INTERFACE
        creationTitle = QLabel('Create Adventure')
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        creationTitle.setFont(font)
        alignment = Qt.AlignHCenter
        creationTitle.setAlignment(alignment)

        # ADVENTURE NAME
        adventureNameLabel = QLabel('Adventure Name:')
        adventureNameEdit = QLineEdit()
        adventureNameEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        adventureNameEdit.setFixedWidth(300)
        adventureNameEdit.setFixedHeight(30)
        adventureFont = QFont('Arial')
        adventureFont.setPointSize(30)
        adventureNameLabel.setFont(adventureFont)

        # CREATION BUTTON
        creationButton = QPushButton("Create")
        creationButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        creationButton.clicked.connect(createAdventure)

        # CREATION BACK BUTTON
        creationBackButton = QPushButton("Back")
        creationBackButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        creationBackButton.clicked.connect(
            lambda: goBackToMenuWindowFromCreationWindow(creationWindow, self.menuWindow))

        # ADDING WIDGETS TO THE LAYOUT
        creationLayout.addWidget(creationTitle)
        creationLayout.addWidget(adventureNameLabel)
        creationLayout.addWidget(adventureNameEdit)
        creationLayout.addWidget(creationButton)
        creationLayout.addWidget(creationBackButton)

        # COLORING THE WINDOW BACKGROUND
        creationWindow.setStyleSheet("background-color: #D2B48C")

        # CENTERING THE LAYOUT
        layoutAlignment = Qt.AlignCenter
        creationLayout.setAlignment(layoutAlignment)

        # ATTACHING THE LAYOUT TO THE WINDOW
        creationWindow.setLayout(creationLayout)

        # MENU SECTION

        menuLayout = QVBoxLayout()

        # TITLE OF THE MENU INTERFACE
        menuTitle = QLabel('Menu')
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        menuTitle.setFont(font)
        alignment = Qt.AlignHCenter
        menuTitle.setAlignment(alignment)

        # CREATE EXIT BUTTON
        exitButton = QPushButton('Exit')
        exitButton.setStyleSheet('background-color: #FFFFFF; color: black;')
        exitButton.clicked.connect(lambda: exitFromMenuWindow())

        # CREATE LOGOUT BUTTON
        logoutButton = QPushButton('Logout')
        logoutButton.setStyleSheet('background-color: #FFFFFF; color: black;')
        logoutButton.clicked.connect(lambda: goToLoginFromMenu(self.menuWindow, loginWindow))

        # CREATE JOIN BUTTON
        joinButton = QPushButton('Join Adventure')
        joinButton.setStyleSheet('background-color: #FFFFFF; color: black;')
        joinButton.clicked.connect(lambda: goToJoinAdventure(self.menuWindow, joinWindow))

        # CREATE BUTTON
        createButton = QPushButton('Create Adventure')
        createButton.setStyleSheet('background-color: #FFFFFF; color: black;')
        createButton.clicked.connect(lambda: goToCreationAdventure(self.menuWindow, creationWindow))

        # LIST VIEW
        self.listAdventuresListWidget = QListWidget()
        self.listAdventuresListWidget.itemClicked.connect(self.setSelected)

        # LOAD DELETE BUTTONS
        self.loadButton = QPushButton("Load adventure")
        self.loadButton.setStyleSheet('background-color: #FFFFFF; color: black;')
        self.deleteButton = QPushButton("Delete adventure")
        self.deleteButton.setStyleSheet('background-color: #FFFFFF; color: black;')

        self.loadButton.clicked.connect(self.loadAdventure)
        self.deleteButton.clicked.connect(self.deleteAdventure)

        # ADDING WIDGETS TO THE LAYOUT
        menuLayout.addWidget(menuTitle)
        menuLayout.addWidget(self.listAdventuresListWidget)
        menuLayout.addWidget(self.loadButton)
        menuLayout.addWidget(self.deleteButton)
        menuLayout.addWidget(createButton)
        menuLayout.addWidget(joinButton)
        menuLayout.addWidget(logoutButton)
        menuLayout.addWidget(exitButton)

        # COLORING THE WINDOW BACKGROUND
        self.menuWindow.setStyleSheet("background-color: #D2B48C")

        # CENTERING THE LAYOUT
        layoutAlignment = Qt.AlignCenter
        menuLayout.setAlignment(layoutAlignment)

        # ATTACHING THE LAYOUT TO THE WINDOW
        self.menuWindow.setLayout(menuLayout)

        # STATS SECTION
        # CREATING LAYOUTS
        statsLayout = QVBoxLayout()
        buttonsLayout = QHBoxLayout()

        # TITLE OF THE LOGIN INTERFACE
        statsTitle = QLabel("Character Saving Throws")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        statsTitle.setFont(font)
        alignment = Qt.AlignHCenter
        statsTitle.setAlignment(alignment)

        # STRENGTH
        strengthLabel = QLabel("Strength: ")
        strengthEdit = QLineEdit()
        strengthEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        strengthEdit.setFixedWidth(120)
        strengthEdit.setFixedHeight(30)
        strengthFont = QFont('Arial')
        strengthFont.setPointSize(20)
        strengthLabel.setFont(strengthFont)

        # DEXTERITY
        dexterityLabel = QLabel("Dexterity: ")
        dexterityEdit = QLineEdit()
        dexterityEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        dexterityEdit.setFixedWidth(120)
        dexterityEdit.setFixedHeight(30)
        dexterityFont = QFont('Arial')
        dexterityFont.setPointSize(20)
        dexterityLabel.setFont(dexterityFont)

        # CONSTITUTION
        constitutionLabel = QLabel("Constitution: ")
        constitutionEdit = QLineEdit()
        constitutionEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        constitutionEdit.setFixedWidth(120)
        constitutionEdit.setFixedHeight(30)
        constitutionFont = QFont('Arial')
        constitutionFont.setPointSize(20)
        constitutionLabel.setFont(constitutionFont)

        # INTELLIGENCE
        intelligenceLabel = QLabel("Intelligence: ")
        intelligenceEdit = QLineEdit()
        intelligenceEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        intelligenceEdit.setFixedWidth(120)
        intelligenceEdit.setFixedHeight(30)
        intelligenceFont = QFont('Arial')
        intelligenceFont.setPointSize(20)
        intelligenceLabel.setFont(intelligenceFont)

        # WISDOM
        wisdomLabel = QLabel("Wisdom: ")
        wisdomEdit = QLineEdit()
        wisdomEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        wisdomEdit.setFixedWidth(120)
        wisdomEdit.setFixedHeight(30)
        wisdomFont = QFont('Arial')
        wisdomFont.setPointSize(20)
        wisdomLabel.setFont(wisdomFont)

        # CHARISMA
        charismaLabel = QLabel("Charisma: ")
        charismaEdit = QLineEdit()
        charismaEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        charismaEdit.setFixedWidth(120)
        charismaEdit.setFixedHeight(30)
        charismaFont = QFont('Arial')
        charismaFont.setPointSize(20)
        charismaLabel.setFont(charismaFont)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(
            lambda: goBackToCharacterCreationWindowFromStatsWindow(statsWindow, characterCreationWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(lambda: goToTraitsWindowFromStatsWindow(statsWindow, traitsWindow))

        # ADDING WIDGETS TO THE STATS LAYOUT
        statsLayout.addWidget(statsTitle)
        statsLayout.addWidget(strengthLabel)
        statsLayout.addWidget(strengthEdit)
        statsLayout.addWidget(dexterityLabel)
        statsLayout.addWidget(dexterityEdit)
        statsLayout.addWidget(constitutionLabel)
        statsLayout.addWidget(constitutionEdit)
        statsLayout.addWidget(intelligenceLabel)
        statsLayout.addWidget(intelligenceEdit)
        statsLayout.addWidget(wisdomLabel)
        statsLayout.addWidget(wisdomEdit)
        statsLayout.addWidget(charismaLabel)
        statsLayout.addWidget(charismaEdit)

        # ATTTACHING WIDGETS TO THE BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        statsWindow.setStyleSheet("background-color: #D2B48C")

        # CENTERING THE LAYOUT
        layoutAlignment = Qt.AlignCenter
        statsLayout.setAlignment(layoutAlignment)

        # ATTACHING STATS LAYOUT TO BUTTONS LAYOUT
        statsLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        statsWindow.setLayout(statsLayout)

        # TRAITS SECTION
        # INITIALIZING LAYOUTS
        traitsLayout = QVBoxLayout()
        buttonsLayout = QHBoxLayout()

        # TITLE OF THE LOGIN INTERFACE
        traitsTitle = QLabel("Character Traits")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        traitsTitle.setFont(font)
        alignment = Qt.AlignHCenter
        traitsTitle.setAlignment(alignment)

        # PERSONALITY TRAITS LABEL
        personalityLabel = QLabel("Personality Traits: ")
        personalityFont = QFont('Arial')
        personalityFont.setPointSize(30)
        personalityLabel.setFont(personalityFont)

        # PERSONALITY TRAITS EDIT
        personalityEdit = QLineEdit()
        personalityEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        personalityEdit.setFixedWidth(300)
        personalityEdit.setFixedHeight(30)

        # IDEALS LABEL
        idealsLabel = QLabel("Ideals: ")
        idealsFont = QFont('Arial')
        idealsFont.setPointSize(30)
        idealsLabel.setFont(idealsFont)

        # IDEALS EDIT
        idealsEdit = QLineEdit()
        idealsEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        idealsEdit.setFixedWidth(300)
        idealsEdit.setFixedHeight(30)

        # BONDS LABEL
        bondsLabel = QLabel("Bonds: ")
        bondsLabelFont = QFont('Arial')
        bondsLabelFont.setPointSize(30)
        bondsLabel.setFont(bondsLabelFont)

        # BONDS EDIT
        bondsEdit = QLineEdit()
        bondsEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        bondsEdit.setFixedWidth(300)
        bondsEdit.setFixedHeight(30)

        # FLAWS LABEL
        flawsLabel = QLabel("Flaws: ")
        flawsLabelFont = QFont('Arial')
        flawsLabelFont.setPointSize(30)
        flawsLabel.setFont(flawsLabelFont)

        # FLAWS EDIT
        flawsEdit = QLineEdit()
        flawsEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        flawsEdit.setFixedWidth(300)
        flawsEdit.setFixedHeight(30)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(lambda: goBackToStatsWindowFromTraitsWindow(traitsWindow, statsWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(lambda: goToBonusStatsWindowFromTraitsWindow(traitsWindow, bonusStatsWindow))

        # ADDING WIDGETS TO THE TRAITS LAYOUT
        traitsLayout.addWidget(traitsTitle)
        traitsLayout.addWidget(personalityLabel)
        traitsLayout.addWidget(personalityEdit)
        traitsLayout.addWidget(idealsLabel)
        traitsLayout.addWidget(idealsEdit)
        traitsLayout.addWidget(bondsLabel)
        traitsLayout.addWidget(bondsEdit)
        traitsLayout.addWidget(flawsLabel)
        traitsLayout.addWidget(flawsEdit)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        traitsWindow.setStyleSheet("background-color: #D2B48C")

        # CENTERING THE LAYOUT
        layoutAlignment = Qt.AlignCenter
        traitsLayout.setAlignment(layoutAlignment)

        # ATTACHING BUTTONS LAYOUT TO TRAITS LAYOUT
        traitsLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        traitsWindow.setLayout(traitsLayout)

        # BONUS STATS SECTION

        # INITIALIZING LAYOUTS
        bonusStatsLayout = QVBoxLayout()
        buttonsLayout = QHBoxLayout()

        # TITLE OF THE INTERFACE
        bonusStatsTitle = QLabel("Bonus Stats")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        bonusStatsTitle.setFont(font)
        alignment = Qt.AlignHCenter
        bonusStatsTitle.setAlignment(alignment)

        # INSPIRATION LABEL
        inspirationLabel = QLabel("Inspiration: ")
        inspirationLabelFont = QFont('Arial')
        inspirationLabelFont.setPointSize(30)
        inspirationLabel.setFont(inspirationLabelFont)

        # INSPIRATION EDIT
        inspirationEdit = QLineEdit()
        inspirationEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        inspirationEdit.setFixedWidth(300)
        inspirationEdit.setFixedHeight(30)

        # PROFICIENCY BONUS
        proficiencyBonusLabel = QLabel("Proficiency Bonus: ")
        proficiencyBonusLabelFont = QFont('Arial')
        proficiencyBonusLabelFont.setPointSize(30)
        proficiencyBonusLabel.setFont(proficiencyBonusLabelFont)

        # PROFICIENCY EDIT
        proficiencyEdit = QLineEdit()
        proficiencyEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        proficiencyEdit.setFixedWidth(300)
        proficiencyEdit.setFixedHeight(30)

        # ARMOR CLASS LABEL
        armorClassLabel = QLabel("Armor Class: ")
        armorClassLabelFont = QFont('Ariel')
        armorClassLabelFont.setPointSize(30)
        armorClassLabel.setFont(armorClassLabelFont)

        # ARMOR CLASS EDIT
        armorClassEdit = QLineEdit()
        armorClassEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        armorClassEdit.setFixedWidth(300)
        armorClassEdit.setFixedHeight(30)

        # INITIATIVE LABEL
        initiativeLabel = QLabel("Initiative: ")
        initiativeLabelFont = QFont('Arial')
        initiativeLabelFont.setPointSize(30)
        initiativeLabel.setFont(initiativeLabelFont)

        # INITIATIVE EDIT
        initiativeEdit = QLineEdit()
        initiativeEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        initiativeEdit.setFixedWidth(300)
        initiativeEdit.setFixedHeight(30)

        # SPEED LABEL
        speedLabel = QLabel("Speed: ")
        speedLabelFont = QFont('Arial')
        speedLabelFont.setPointSize(30)
        speedLabel.setFont(speedLabelFont)

        # SPEED EDIT
        speedEdit = QLineEdit()
        speedEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        speedEdit.setFixedWidth(300)
        speedEdit.setFixedHeight(30)

        # PASSIVE WISDOM LABEL
        passiveWisdomLabel = QLabel("Passive Wisdom: ")
        passiveWisdomLabelFont = QFont('Arial')
        passiveWisdomLabelFont.setPointSize(30)
        passiveWisdomLabel.setFont(passiveWisdomLabelFont)

        # PASSIVE WISDOM EDIT
        passiveWisdomEdit = QLineEdit()
        passiveWisdomEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        passiveWisdomEdit.setFixedWidth(300)
        passiveWisdomEdit.setFixedHeight(30)

        # HIT POINT MAXIMUM LABEL
        hitPointMaximumLabel = QLabel("Hit Point Maximum: ")
        hitPointMaximumFont = QFont('Arial')
        hitPointMaximumFont.setPointSize(30)
        hitPointMaximumLabel.setFont(hitPointMaximumFont)

        # HIT POINT MAXIMUM EDIT
        hitPointMaximumEdit = QLineEdit()
        hitPointMaximumEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        hitPointMaximumEdit.setFixedWidth(300)
        hitPointMaximumEdit.setFixedWidth(30)

        # CURRENT HITPOINTS LABEL
        currentHitpointsLabel = QLabel("Current Hitpoints: ")
        currentHitpointsLabelFont = QFont('Arial')
        currentHitpointsLabelFont.setPointSize(30)
        currentHitpointsLabel.setFont(currentHitpointsLabelFont)

        # CURRENT HITPOINTS EDIT
        currentHitpointsEdit = QLineEdit()
        currentHitpointsEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        currentHitpointsEdit.setFixedWidth(300)
        currentHitpointsEdit.setFixedHeight(30)

        # TEMPORARY HITPOINTS LABEL
        temporaryHitpointsLabel = QLabel("Temporary Hitpoints: ")
        temporaryHitpointsLabelFont = QFont('Arial')
        temporaryHitpointsLabelFont.setPointSize(30)
        temporaryHitpointsLabel.setFont(temporaryHitpointsLabelFont)

        # TEMPORARY HITPOINTS EDIT
        temporaryHitpointsEdit = QLineEdit()
        temporaryHitpointsEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        temporaryHitpointsEdit.setFixedWidth(300)
        temporaryHitpointsEdit.setFixedHeight(30)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(lambda: goBackToTraitsWindowFromBonusStats(bonusStatsWindow, traitsWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(lambda: goToSkillsWindowFromBonusStatsWIndow(bonusStatsWindow, skillsWindow))

        # ADDING WIDGETS TO THE BONUS STATS LAYOUT
        bonusStatsLayout.addWidget(bonusStatsTitle)
        bonusStatsLayout.addWidget(inspirationLabel)
        bonusStatsLayout.addWidget(inspirationEdit)
        bonusStatsLayout.addWidget(proficiencyBonusLabel)
        bonusStatsLayout.addWidget(proficiencyEdit)
        bonusStatsLayout.addWidget(armorClassLabel)
        bonusStatsLayout.addWidget(armorClassEdit)
        bonusStatsLayout.addWidget(initiativeLabel)
        bonusStatsLayout.addWidget(initiativeEdit)
        bonusStatsLayout.addWidget(speedLabel)
        bonusStatsLayout.addWidget(speedEdit)
        bonusStatsLayout.addWidget(passiveWisdomLabel)
        bonusStatsLayout.addWidget(passiveWisdomEdit)
        bonusStatsLayout.addWidget(hitPointMaximumLabel)
        bonusStatsLayout.addWidget(hitPointMaximumEdit)
        bonusStatsLayout.addWidget(currentHitpointsLabel)
        bonusStatsLayout.addWidget(currentHitpointsEdit)
        bonusStatsLayout.addWidget(temporaryHitpointsLabel)
        bonusStatsLayout.addWidget(temporaryHitpointsEdit)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        bonusStatsWindow.setStyleSheet("background-color: #D2B48C")

        # CENTERING THE LAYOUT
        layoutAlignment = Qt.AlignCenter
        bonusStatsLayout.setAlignment(layoutAlignment)

        # ATTACHING BUTTONS LAYOUT TO BONUS STATS LAYOUT
        bonusStatsLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        bonusStatsWindow.setLayout(bonusStatsLayout)

        # SKILLS SECTION
        # INITIALIZING LAYOUTS
        skillsLayout = QVBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        skillsLayout.setAlignment(layoutAlignment)

        # TITLE OF THE INTERFACE
        skillsTitle = QLabel("Skills")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        skillsTitle.setFont(font)
        alignment = Qt.AlignHCenter
        skillsTitle.setAlignment(alignment)

        # ACROBATICS LABEL
        acrobaticsLabel = QLabel("Acrobatics: ")
        acrobaticsLabelFont = QFont('Arial')
        acrobaticsLabelFont.setPointSize(20)
        acrobaticsLabel.setFont(acrobaticsLabelFont)

        # ACROBATICS EDIT
        acrobaticsEdit = QLineEdit()
        acrobaticsEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        acrobaticsEdit.setFixedWidth(120)
        acrobaticsEdit.setFixedHeight(30)

        # ANIMAL HANDLING LABEL
        animalHandlingLabel = QLabel("Animal Handling: ")
        animalHandlingLabelFont = QFont('Arial')
        animalHandlingLabelFont.setPointSize(20)
        animalHandlingLabel.setFont(animalHandlingLabelFont)

        # ANIMAL HANDLING EDIT
        animalHandlingEdit = QLineEdit()
        animalHandlingEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        animalHandlingEdit.setFixedWidth(120)
        animalHandlingEdit.setFixedHeight(30)

        # ARCANA LABEL
        arcanaLabel = QLabel("Arcana: ")
        arcanaLabelFont = QFont('Arial')
        arcanaLabelFont.setPointSize(20)
        arcanaLabel.setFont(arcanaLabelFont)

        # ARCANA EDIT
        arcanaEdit = QLineEdit()
        arcanaEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        arcanaEdit.setFixedWidth(120)
        arcanaEdit.setFixedHeight(30)

        # ATHLETICS LABEL
        athleticsLabel = QLabel("Athletics: ")
        athleticsLabelFont = QFont()
        athleticsLabelFont.setPointSize(20)
        athleticsLabel.setFont(athleticsLabelFont)

        # ATHLETICS EDIT
        athleticsEdit = QLineEdit()
        athleticsEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        athleticsEdit.setFixedWidth(120)
        athleticsEdit.setFixedHeight(30)

        # DECEPTION LABEL
        deceptionLabel = QLabel("Deception: ")
        deceptionLabelFont = QFont('Arial')
        deceptionLabelFont.setPointSize(20)
        deceptionLabel.setFont(deceptionLabelFont)

        # DECEPTION EDIT
        deceptionEdit = QLineEdit()
        deceptionEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        deceptionEdit.setFixedWidth(120)
        deceptionEdit.setFixedHeight(30)

        # HISTORY LABEL
        historyLabel = QLabel("History: ")
        historyLabelFont = QFont('Arial')
        historyLabelFont.setPointSize(20)
        historyLabel.setFont(historyLabelFont)

        # HISTORY EDIT
        historyEdit = QLineEdit()
        historyEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        historyEdit.setFixedWidth(120)
        historyEdit.setFixedHeight(30)

        # INSIGHT LABEL
        insightLabel = QLabel("Insight: ")
        insightLabelFont = QFont('Arial')
        insightLabelFont.setPointSize(20)
        insightLabel.setFont(insightLabelFont)

        # INSIGHT EDIT
        insightEdit = QLineEdit()
        insightEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        insightEdit.setFixedWidth(120)
        insightEdit.setFixedHeight(30)

        # INTIMIDATION LABEL
        intimidationLabel = QLabel("Intimidation: ")
        intimidationLabelFont = QFont('Arial')
        intimidationLabelFont.setPointSize(20)
        intimidationLabel.setFont(intimidationLabelFont)

        # INTIMIDATION EDIT
        intimidationEdit = QLineEdit()
        intimidationEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        intimidationEdit.setFixedWidth(120)
        intimidationEdit.setFixedHeight(30)

        # INVESTIGATION LABEL
        investigationLabel = QLabel("Investigation: ")
        investigationLabelFont = QFont('Arial')
        investigationLabelFont.setPointSize(20)
        investigationLabel.setFont(investigationLabelFont)

        # INVESTIGATION EDIT
        investigationEdit = QLineEdit()
        investigationEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        investigationEdit.setFixedWidth(120)
        investigationEdit.setFixedHeight(30)

        # MEDICINE LABEL
        medicineLabel = QLabel("Medicine: ")
        medicineLabelFont = QFont('Arial')
        medicineLabelFont.setPointSize(20)
        medicineLabel.setFont(medicineLabelFont)

        # MEDICINE EDIT
        medicineEdit = QLineEdit()
        medicineEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        medicineEdit.setFixedWidth(120)
        medicineEdit.setFixedHeight(30)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(lambda: goBackToBonusStatsWindowFromSkillsWindow(skillsWindow, bonusStatsWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(lambda: goToSkills2WindowFromSkillsWindow(skillsWindow, skills2Window))

        # ADDING WIDGETS TO THE SKILLS LAYOUT
        skillsLayout.addWidget(skillsTitle)
        skillsLayout.addWidget(acrobaticsLabel)
        skillsLayout.addWidget(acrobaticsEdit)
        skillsLayout.addWidget(animalHandlingLabel)
        skillsLayout.addWidget(animalHandlingEdit)
        skillsLayout.addWidget(arcanaLabel)
        skillsLayout.addWidget(arcanaEdit)
        skillsLayout.addWidget(athleticsLabel)
        skillsLayout.addWidget(athleticsEdit)
        skillsLayout.addWidget(deceptionLabel)
        skillsLayout.addWidget(deceptionEdit)
        skillsLayout.addWidget(historyLabel)
        skillsLayout.addWidget(historyEdit)
        skillsLayout.addWidget(insightLabel)
        skillsLayout.addWidget(insightEdit)
        skillsLayout.addWidget(intimidationLabel)
        skillsLayout.addWidget(intimidationEdit)
        skillsLayout.addWidget(investigationLabel)
        skillsLayout.addWidget(investigationEdit)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        skillsWindow.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO SKILLS LAYOUT
        skillsLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        skillsWindow.setLayout(skillsLayout)

        # SKILLS2 SECTION

        # INITIALIZING LAYOUTS
        skills2Layout = QVBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        skills2Layout.setAlignment(layoutAlignment)

        # TITLE OF THE INTERFACE
        skills2Title = QLabel("Skills")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        skills2Title.setFont(font)
        alignment = Qt.AlignHCenter
        skills2Title.setAlignment(alignment)

        # MEDICINE LABEL
        medicineLabel = QLabel("Medicine: ")
        medicineLabelFont = QFont('Arial')
        medicineLabelFont.setPointSize(20)
        medicineLabel.setFont(medicineLabelFont)

        # MEDICINE EDIT
        medicineEdit = QLineEdit()
        medicineEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        medicineEdit.setFixedWidth(120)
        medicineEdit.setFixedHeight(30)

        # NATURE LABEL
        natureLabel = QLabel("Nature: ")
        natureLabelFont = QFont('Arial')
        natureLabelFont.setPointSize(20)
        natureLabel.setFont(natureLabelFont)

        # NATURE EDIT
        natureEdit = QLineEdit()
        natureEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        natureEdit.setFixedWidth(120)
        natureEdit.setFixedHeight(30)

        # PERCEPTION LABEL
        perceptionLabel = QLabel("Perception: ")
        perceptionLabelFont = QFont('Arial')
        perceptionLabelFont.setPointSize(20)
        perceptionLabel.setFont(perceptionLabelFont)

        # PERCEPTION EDIT
        perceptionEdit = QLineEdit()
        perceptionEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        perceptionEdit.setFixedWidth(120)
        perceptionEdit.setFixedHeight(30)

        # PERFORMANCE LABEL
        performanceLabel = QLabel("Performance: ")
        performanceLabelFont = QFont('Arial')
        performanceLabelFont.setPointSize(20)
        performanceLabel.setFont(performanceLabelFont)

        # PERFORMANCE EDIT
        performanceEdit = QLineEdit()
        performanceEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        performanceEdit.setFixedWidth(120)
        performanceEdit.setFixedHeight(30)

        # PERSUASION LABEL
        persuasionLabel = QLabel("Persuasion: ")
        persuasionLabelFont = QFont('Arial')
        persuasionLabelFont.setPointSize(20)
        persuasionLabel.setFont(persuasionLabelFont)

        # PERSUASION EDIT
        persuasionEdit = QLineEdit()
        persuasionEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        persuasionEdit.setFixedWidth(120)
        persuasionEdit.setFixedHeight(30)

        # RELIGION LABEL
        religionLabel = QLabel("Religion: ")
        religionLabelFont = QFont('Arial')
        religionLabelFont.setPointSize(20)
        religionLabel.setFont(religionLabelFont)

        # RELIGION EDIT
        religionEdit = QLineEdit()
        religionEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        religionEdit.setFixedWidth(120)
        religionEdit.setFixedHeight(30)

        # SLEIGHT OF HAND LABEL
        sleightOfHandLabel = QLabel("Sleight Of Hand: ")
        sleightOfHandLabelFont = QFont('Arial')
        sleightOfHandLabelFont.setPointSize(20)
        sleightOfHandLabel.setFont(sleightOfHandLabelFont)

        # SLEIGHT OF HAND EDIT
        sleightOfHandEdit = QLineEdit()
        sleightOfHandEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        sleightOfHandEdit.setFixedWidth(120)
        sleightOfHandEdit.setFixedHeight(30)

        # STEALTH LABEL
        stealthLabel = QLabel("Stealth: ")
        stealthLabelFont = QFont('Arial')
        stealthLabelFont.setPointSize(20)
        stealthLabel.setFont(stealthLabelFont)

        # STEALTH EDIT
        stealthEdit = QLineEdit()
        stealthEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        stealthEdit.setFixedWidth(120)
        stealthEdit.setFixedHeight(30)

        # SURVIVAL LABEL
        survivalLabel = QLabel("Survival: ")
        survivalLabelFont = QFont('Arial')
        survivalLabelFont.setPointSize(20)
        survivalLabel.setFont(survivalLabelFont)

        # SURVIVAL EDIT
        survivalEdit = QLineEdit()
        survivalEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        survivalEdit.setFixedWidth(120)
        survivalEdit.setFixedHeight(30)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(lambda: goBackToSkillsWindowFromSkills2Window(skills2Window, skillsWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(lambda: goToDiceWindowFromSkills2Window(skills2Window, diceWindow))

        # ADDING WIDGETS TO THE SKILLS2 LAYOUT
        skills2Layout.addWidget(skills2Title)
        skills2Layout.addWidget(medicineLabel)
        skills2Layout.addWidget(medicineEdit)
        skills2Layout.addWidget(natureLabel)
        skills2Layout.addWidget(natureEdit)
        skills2Layout.addWidget(perceptionLabel)
        skills2Layout.addWidget(perceptionEdit)
        skills2Layout.addWidget(performanceLabel)
        skills2Layout.addWidget(performanceEdit)
        skills2Layout.addWidget(persuasionLabel)
        skills2Layout.addWidget(persuasionEdit)
        skills2Layout.addWidget(religionLabel)
        skills2Layout.addWidget(religionEdit)
        skills2Layout.addWidget(sleightOfHandLabel)
        skills2Layout.addWidget(sleightOfHandEdit)
        skills2Layout.addWidget(stealthLabel)
        skills2Layout.addWidget(stealthEdit)
        skills2Layout.addWidget(survivalLabel)
        skills2Layout.addWidget(survivalEdit)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        skills2Window.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO SKILLS LAYOUT
        skills2Layout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        skills2Window.setLayout(skills2Layout)

        # DICE SECTION

        # INITIALIZING LAYOUTS
        diceLayout = QVBoxLayout()
        buttonsLayout = QHBoxLayout()

        # TITLE OF THE INTERFACE
        diceTitle = QLabel("Dice And Death Saves")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        diceTitle.setFont(font)
        alignment = Qt.AlignHCenter
        diceTitle.setAlignment(alignment)

        # TOTAL HIT DICE
        totalHitLabel = QLabel("Total Hit Dice: ")
        totalHitLabelFont = QFont('Arial')
        totalHitLabelFont.setPointSize(30)
        totalHitLabel.setFont(totalHitLabelFont)

        # TOTAL HIT LABEL EDIT
        totalHitLabelEdit = QLineEdit()
        totalHitLabelEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        totalHitLabelEdit.setFixedWidth(300)
        totalHitLabelEdit.setFixedHeight(30)

        # HIT DICE LABEL
        hitDiceLabel = QLabel("Hit Dice: ")
        hitDiceLabelFont = QFont('Arial')
        hitDiceLabelFont.setPointSize(30)
        hitDiceLabel.setFont(hitDiceLabelFont)

        # HIT DICE EDIT
        hitDiceEdit = QLineEdit()
        hitDiceEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        hitDiceEdit.setFixedWidth(300)
        hitDiceEdit.setFixedHeight(30)

        # DEATH SAVES SUCCESSES LABEL
        deathSavesSuccessesLabel = QLabel("Death Saves Successes: ")
        deathSavesSuccessesLabelFont = QFont('Arial')
        deathSavesSuccessesLabelFont.setPointSize(30)
        deathSavesSuccessesLabel.setFont(deathSavesSuccessesLabelFont)

        # DEATH SAVES SUCCESSES EDIT
        deathSavesSuccessesEdit = QLineEdit()
        deathSavesSuccessesEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        deathSavesSuccessesEdit.setFixedWidth(300)
        deathSavesSuccessesEdit.setFixedHeight(30)

        # DEATH SAVES FAILURES LABEL
        deathSavesFailuresLabel = QLabel("Death Saves Failures: ")
        deathSavesFailuresFont = QFont('Arial')
        deathSavesFailuresFont.setPointSize(30)
        deathSavesFailuresLabel.setFont(deathSavesFailuresFont)

        # DEATH SAVES FAILURES EDIT
        deathSavesFailuresEdit = QLineEdit()
        deathSavesFailuresEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        deathSavesFailuresEdit.setFixedWidth(300)
        deathSavesFailuresEdit.setFixedHeight(30)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(lambda: goBackToSkills2WindowFromDiceWindow(diceWindow, skills2Window))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(lambda: goToAttacksWindowFromDiceWindow(diceWindow, attacksWindow))

        # ADDING WIDGETS TO THE HIT DICE LAYOUT
        diceLayout.addWidget(diceTitle)
        diceLayout.addWidget(totalHitLabel)
        diceLayout.addWidget(totalHitLabelEdit)
        diceLayout.addWidget(hitDiceLabel)
        diceLayout.addWidget(hitDiceEdit)
        diceLayout.addWidget(deathSavesSuccessesLabel)
        diceLayout.addWidget(deathSavesSuccessesEdit)
        diceLayout.addWidget(deathSavesFailuresLabel)
        diceLayout.addWidget(deathSavesFailuresEdit)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        diceWindow.setStyleSheet("background-color: #D2B48C")

        # CENTERING THE LAYOUT
        layoutAlignment = Qt.AlignCenter
        diceLayout.setAlignment(layoutAlignment)

        # ATTACHING BUTTONS LAYOUT TO HITDICE LAYOUT
        diceLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        diceWindow.setLayout(diceLayout)

        # ATTACKS AND SPELLCASTING SECTION

        # INITIALIZING LAYOUTS
        attacksLayout = QVBoxLayout()
        verticalLayout1 = QVBoxLayout()
        verticalLayout2 = QVBoxLayout()
        verticalLayout3 = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        buttonsLayout = QHBoxLayout()

        # TITLE OF THE INTERFACE
        attacksTitle = QLabel("Attacks and Spellcasting")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        attacksTitle.setFont(font)
        alignment = Qt.AlignHCenter
        attacksTitle.setAlignment(alignment)

        # NAME LABEL
        nameLabel = QLabel("Name:")
        nameLabelFont = QFont('Arial')
        nameLabelFont.setPointSize(30)
        nameLabel.setFont(nameLabelFont)

        # TEXTBOX1 LAYOUT1
        textBox1Layout1 = QLineEdit()
        textBox1Layout1.setStyleSheet("background-color: #FFFFFF; color: black;")
        textBox1Layout1.setFixedWidth(300)
        textBox1Layout1.setFixedHeight(30)

        # TEXTBOX2 LAYOUT1
        textBox2Layout1 = QLineEdit()
        textBox2Layout1.setStyleSheet("background-color: #FFFFFF; color: black;")
        textBox2Layout1.setFixedWidth(300)
        textBox2Layout1.setFixedHeight(30)

        # TEXTBOX3 LAYOUT1
        textBox3Layout1 = QLineEdit()
        textBox3Layout1.setStyleSheet("background-color: #FFFFFF; color: black;")
        textBox3Layout1.setFixedWidth(300)
        textBox3Layout1.setFixedHeight(30)

        # ATK BONUS LABEL
        atkBonusLabel = QLabel("Atk Bonus:")
        atkBonusLabelFont = QFont('Arial')
        atkBonusLabelFont.setPointSize(30)
        atkBonusLabel.setFont(atkBonusLabelFont)

        # TEXTBOX1 LAYOUT2
        textBox1Layout2 = QLineEdit()
        textBox1Layout2.setStyleSheet("background-color: #FFFFFF; color: black;")
        textBox1Layout2.setFixedWidth(300)
        textBox1Layout2.setFixedHeight(30)

        # TEXTBOX2 LAYOUT2
        textBox2Layout2 = QLineEdit()
        textBox2Layout2.setStyleSheet("background-color: #FFFFFF; color: black;")
        textBox2Layout2.setFixedWidth(300)
        textBox2Layout2.setFixedHeight(30)

        # TEXTBOX3 LAYOUT2
        textBox3Layout2 = QLineEdit()
        textBox3Layout2.setStyleSheet("background-color: #FFFFFF; color: black;")
        textBox3Layout2.setFixedWidth(300)
        textBox3Layout2.setFixedHeight(30)

        # DAMAGE/TYPE LABEL
        damageLabel = QLabel("Damage/Type")
        damageLabelFont = QFont('Arial')
        damageLabelFont.setPointSize(30)
        damageLabel.setFont(damageLabelFont)

        # TEXTBOX1 LAYOUT3
        textBox1Layout3 = QLineEdit()
        textBox1Layout3.setStyleSheet("background-color: #FFFFFF; color: black;")
        textBox1Layout3.setFixedWidth(300)
        textBox1Layout3.setFixedHeight(30)

        # TEXTBOX2 LAYOUT3
        textBox2Layout3 = QLineEdit()
        textBox2Layout3.setStyleSheet("background-color: #FFFFFF; color: black;")
        textBox2Layout3.setFixedWidth(300)
        textBox2Layout3.setFixedHeight(30)

        # TEXTBOX3 LAYOUT3
        textBox3Layout3 = QLineEdit()
        textBox3Layout3.setStyleSheet("background-color: #FFFFFF; color: black;")
        textBox3Layout3.setFixedWidth(300)
        textBox3Layout3.setFixedHeight(30)

        # TOTAL HIT DICE LABEL
        totalHitLabel = QLabel("Total Hit Dice: ")
        totalHitLabelFont = QFont('Arial')
        totalHitLabelFont.setPointSize(30)
        totalHitLabel.setFont(totalHitLabelFont)

        # TOTAL HIT LABEL EDIT
        totalHitLabelEdit = QLineEdit()
        totalHitLabelEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        totalHitLabelEdit.setFixedWidth(300)
        totalHitLabelEdit.setFixedHeight(30)

        # ATTACKS AND SPELLCASTING LABEL
        attacksAndSpellcastingLabel = QLabel("Attacks and Spellcasting: ")
        attacksAndSpellcastingLabelFont = QFont('Arial')
        attacksAndSpellcastingLabelFont.setPointSize(30)
        attacksAndSpellcastingLabel.setFont(attacksAndSpellcastingLabelFont)

        # ATTACKS AND SPELLCASTING EDIT
        attacksAndSpellcastingEdit = QLineEdit()
        attacksAndSpellcastingEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        attacksAndSpellcastingEdit.setFixedWidth(300)
        attacksAndSpellcastingEdit.setFixedHeight(30)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(lambda: goBackToDiceWindowFromAttacksWindow(attacksWindow, diceWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(
            lambda: goToOtherProficienciesWindowFromAttacksWindow(attacksWindow, otherProficienciesWindow))

        # ADDING WIDGETS TO ATTACKS LAYOUT
        attacksLayout.addWidget(attacksTitle)
        attacksLayout.addWidget(attacksAndSpellcastingLabel)
        attacksLayout.addWidget(attacksAndSpellcastingEdit)

        # ADDING WIDGETS TO VERTICAL LAYOUT 1
        verticalLayout1.addWidget(nameLabel)
        verticalLayout1.addWidget(textBox1Layout1)
        verticalLayout1.addWidget(textBox2Layout1)
        verticalLayout1.addWidget(textBox3Layout1)

        # ADDING WIDGETS TO VERTICAL LAYOUT 2
        verticalLayout2.addWidget(atkBonusLabel)
        verticalLayout2.addWidget(textBox1Layout2)
        verticalLayout2.addWidget(textBox2Layout2)
        verticalLayout2.addWidget(textBox3Layout2)

        # ADDING WIDGETS TO VERTICAL LAYOUT 3
        verticalLayout3.addWidget(damageLabel)
        verticalLayout3.addWidget(textBox1Layout3)
        verticalLayout3.addWidget(textBox2Layout3)
        verticalLayout3.addWidget(textBox3Layout3)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        attacksWindow.setStyleSheet("background-color: #D2B48C")

        # CENTERING THE LAYOUT
        layoutAlignment = Qt.AlignCenter
        attacksLayout.setAlignment(layoutAlignment)

        # ATTACHING LAYOUTS TO HORIZONTAL LAYOUT
        horizontalLayout.addLayout(verticalLayout1)
        horizontalLayout.addLayout(verticalLayout2)
        horizontalLayout.addLayout(verticalLayout3)

        # ATTACHING LAYOUTS TO MAIN LAYOUT
        attacksLayout.addLayout(horizontalLayout)
        attacksLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        attacksWindow.setLayout(attacksLayout)

        # OTHER PROFICIENCIES SECTION

        # INITIALIZING LAYOUTS
        otherProficienciesLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        otherProficienciesLayout.setAlignment(layoutAlignment)

        # TITLE OF THE INTERFACE
        otherProficienciesTitle = QLabel("Other Proficiencies and Languages:")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        otherProficienciesTitle.setFont(font)
        alignment = Qt.AlignHCenter
        otherProficienciesTitle.setAlignment(alignment)

        # OTHER PROFICIENCIES EDIT
        otherProficienciesEdit = QTextEdit()
        otherProficienciesEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        otherProficienciesEdit.setFixedWidth(1200)
        otherProficienciesEdit.setFixedHeight(900)
        otherProficienciesEdit.setAlignment(Qt.AlignTop)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(
            lambda: goBackToDiceWindowFromOtherProficienciesWindow(otherProficienciesWindow, diceWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(
            lambda: goToFeaturesWindowFromOtherProficienciesWindow(otherProficienciesWindow, featuresWindow))

        # ADDING WIDGETS TO THE OTHERPROFICIENCIES LAYOUT
        otherProficienciesLayout.addWidget(otherProficienciesTitle)

        # ADDING WIDGETS TO HORIZONTAL LAYOUT
        horizontalLayout.addWidget(otherProficienciesEdit)

        # ADDING HORIZONTAL LAYOUT TO MAIN LAYOUT
        otherProficienciesLayout.addLayout(horizontalLayout)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        otherProficienciesWindow.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO OTHER PROFICIENCIES LAYOUT
        otherProficienciesLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        otherProficienciesWindow.setLayout(otherProficienciesLayout)

        # FEATURES SECTION

        # INITIALIZING LAYOUTS
        featuresLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        featuresLayout.setAlignment(layoutAlignment)

        # TITLE OF THE INTERFACE
        featuresTitle = QLabel("Features and Traits: ")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        featuresTitle.setFont(font)
        alignment = Qt.AlignHCenter
        featuresTitle.setAlignment(alignment)

        # FEATURES EDIT
        featuresEdit = QTextEdit()
        featuresEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        featuresEdit.setFixedWidth(1200)
        featuresEdit.setFixedHeight(900)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(
            lambda: goBackToOtherProficienciesWindowFromFeaturesWindow(featuresWindow, otherProficienciesWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(
            lambda: goToEquipmentPiecesWindowFromFeaturesWindow(featuresWindow, equipmentPiecesWindow))

        # ADDING WIDGETS TO THE FEATURES LAYOUT
        featuresLayout.addWidget(featuresTitle)

        # ADDING WIDGETS TO HORIZONTAL LAYOUT
        horizontalLayout.addWidget(featuresEdit)

        # ADDING HORIZONTAL LAYOUT TO MAIN LAYOUT
        featuresLayout.addLayout(horizontalLayout)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        featuresWindow.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO FEATURES LAYOUT
        featuresLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        featuresWindow.setLayout(featuresLayout)

        # EQUIPMENT PIECES

        # INITIALIZING LAYOUTS
        equipmentPiecesLayout = QVBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        equipmentPiecesLayout.setAlignment(layoutAlignment)

        # TITLE OF THE INTERFACE
        equipmentPiecesTitle = QLabel("Equipment Pieces")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        equipmentPiecesTitle.setFont(font)
        alignment = Qt.AlignHCenter
        equipmentPiecesTitle.setAlignment(alignment)

        # COPPER PIECES LABEL
        cpLabel = QLabel("Copper Pieces: ")
        cpLabelFont = QFont('Arial')
        cpLabelFont.setPointSize(30)
        cpLabel.setFont(cpLabelFont)

        # COPPER PIECES EDIT
        cpEdit = QLineEdit()
        cpEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        cpEdit.setFixedWidth(120)
        cpEdit.setFixedHeight(30)

        # SILVER PIECES LABEL
        spLabel = QLabel("Silver Pieces: ")
        spLabelFont = QFont('Arial')
        spLabelFont.setPointSize(30)
        spLabel.setFont(spLabelFont)

        # SILVER PIECES EDIT
        spEdit = QLineEdit()
        spEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        spEdit.setFixedWidth(120)
        spEdit.setFixedHeight(30)

        # ELECTRUM PIECES LABEL
        epLabel = QLabel("Electrum Pieces: ")
        epLabelFont = QFont('Arial')
        epLabelFont.setPointSize(30)
        epLabel.setFont(epLabelFont)

        # ELECTRUM PIECES EDIT
        epEdit = QLineEdit()
        epEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        epEdit.setFixedWidth(120)
        epEdit.setFixedHeight(30)

        # GOLD PIECES LABEL
        gpLabel = QLabel("Gold Pieces: ")
        gpLabelFont = QFont('Arial')
        gpLabelFont.setPointSize(30)
        gpLabel.setFont(gpLabelFont)

        # GOLD PIECES EDIT
        gpEdit = QLineEdit()
        gpEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        gpEdit.setFixedWidth(120)
        gpEdit.setFixedHeight(30)

        # PLATINUM PIECES LABEL
        ppLabel = QLabel("Platinum  Pieces: ")
        ppLabelFont = QFont('Arial')
        ppLabelFont.setPointSize(30)
        ppLabel.setFont(ppLabelFont)

        # PLATINUM PIECES EDIT
        ppEdit = QLineEdit()
        ppEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        ppEdit.setFixedWidth(120)
        ppEdit.setFixedHeight(30)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(
            lambda: goBackToFeaturesWindowFromEquipmentPiecesWindow(equipmentPiecesWindow, featuresWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(
            lambda: goToEquipmentWindowFromEquipmentPiecesWindow(equipmentPiecesWindow, equipmentWindow))

        # ADDING WIDGETS TO THE SKILLS2 LAYOUT
        equipmentPiecesLayout.addWidget(equipmentPiecesTitle)
        equipmentPiecesLayout.addWidget(cpLabel)
        equipmentPiecesLayout.addWidget(cpEdit)
        equipmentPiecesLayout.addWidget(spLabel)
        equipmentPiecesLayout.addWidget(spEdit)
        equipmentPiecesLayout.addWidget(epLabel)
        equipmentPiecesLayout.addWidget(epEdit)
        equipmentPiecesLayout.addWidget(gpLabel)
        equipmentPiecesLayout.addWidget(gpEdit)
        equipmentPiecesLayout.addWidget(ppLabel)
        equipmentPiecesLayout.addWidget(ppEdit)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        equipmentPiecesWindow.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO EQUIPMENT LAYOUT
        equipmentPiecesLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        equipmentPiecesWindow.setLayout(equipmentPiecesLayout)

        # EQUIPMENT SECTION

        # INITIALIZING LAYOUTS
        equipmentLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        equipmentLayout.setAlignment(layoutAlignment)

        # TITLE OF THE INTERFACE
        equipmentTitle = QLabel("Equipment: ")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        equipmentTitle.setFont(font)
        alignment = Qt.AlignHCenter
        equipmentTitle.setAlignment(alignment)

        # EQUIPMENT EDIT
        equipmentEdit = QTextEdit()
        equipmentEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        equipmentEdit.setFixedWidth(1000)
        equipmentEdit.setFixedHeight(900)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(
            lambda: goBackToEquipmentPiecesWindowFromEquipmentWindow(equipmentWindow, equipmentPiecesWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(lambda: goToPhysicalWindowFromEquipmentWindow(equipmentWindow, physicalWindow))

        # ADDING WIDGETS TO THE FEATURES LAYOUT
        equipmentLayout.addWidget(equipmentTitle)

        # ADDING WIDGETS TO HORIZONTAL LAYOUT
        horizontalLayout.addWidget(equipmentEdit)

        # ADDING HORIZONTAL LAYOUT TO MAIN LAYOUT
        equipmentLayout.addLayout(horizontalLayout)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        equipmentWindow.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO FEATURES LAYOUT
        equipmentLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        equipmentWindow.setLayout(equipmentLayout)

        # PHYSICAL SECTION

        # INITIALIZING LAYOUTS
        physicalLayout = QVBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        physicalLayout.setAlignment(layoutAlignment)

        # TITLE OF THE INTERFACE
        physicalTitle = QLabel("Physical Features")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        physicalTitle.setFont(font)
        alignment = Qt.AlignHCenter
        physicalTitle.setAlignment(alignment)

        # AGE LABEL
        ageLabel = QLabel("Age: ")
        ageLabelFont = QFont('Arial')
        ageLabelFont.setPointSize(30)
        ageLabel.setFont(ageLabelFont)

        # AGE EDIT
        ageEdit = QLineEdit()
        ageEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        ageEdit.setFixedWidth(300)
        ageEdit.setFixedHeight(30)

        # HEIGHT LABEL
        heightLabel = QLabel("Height: ")
        heightLabelFont = QFont('Arial')
        heightLabelFont.setPointSize(30)
        heightLabel.setFont(heightLabelFont)

        # HEIGHT EDIT
        heightEdit = QLineEdit()
        heightEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        heightEdit.setFixedWidth(300)
        heightEdit.setFixedHeight(30)

        # WEIGHT LABEL
        weightLabel = QLabel("Weight: ")
        weightLabelFont = QFont('Arial')
        weightLabelFont.setPointSize(30)
        weightLabel.setFont(weightLabelFont)

        # WEIGHT EDIT
        weightEdit = QLineEdit()
        weightEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        weightEdit.setFixedWidth(300)
        weightEdit.setFixedHeight(30)

        # EYES LABEL
        eyesLabel = QLabel("Eyes: ")
        eyesLabelFont = QFont('Arial')
        eyesLabelFont.setPointSize(30)
        eyesLabel.setFont(eyesLabelFont)

        # EYES EDIT
        eyesEdit = QLineEdit()
        eyesEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        eyesEdit.setFixedWidth(300)
        eyesEdit.setFixedHeight(30)

        # SKIN LABEL
        skinLabel = QLabel("Skin: ")
        skinLabelFont = QFont('Arial')
        skinLabelFont.setPointSize(30)
        skinLabel.setFont(skinLabelFont)

        # SKIN EDIT
        skinEdit = QLineEdit()
        skinEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        skinEdit.setFixedWidth(300)
        skinEdit.setFixedHeight(30)

        # HAIR LABEL
        hairLabel = QLabel("Hair: ")
        hairLabelFont = QFont('Arial')
        hairLabelFont.setPointSize(30)
        hairLabel.setFont(hairLabelFont)

        # HAIR EDIT
        hairEdit = QLineEdit()
        hairEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        hairEdit.setFixedWidth(300)
        hairEdit.setFixedHeight(30)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(lambda: goBackToEquipmentWindowFromPhysicalWindow(physicalWindow, equipmentWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(
            lambda: goToCharacterAppearanceWindowFromPhysicalWindow(physicalWindow, characterAppearanceWindow))

        # ADDING WIDGETS TO THE SKILLS2 LAYOUT
        physicalLayout.addWidget(physicalTitle)
        physicalLayout.addWidget(ageLabel)
        physicalLayout.addWidget(ageEdit)
        physicalLayout.addWidget(heightLabel)
        physicalLayout.addWidget(heightEdit)
        physicalLayout.addWidget(weightLabel)
        physicalLayout.addWidget(weightEdit)
        physicalLayout.addWidget(eyesLabel)
        physicalLayout.addWidget(eyesEdit)
        physicalLayout.addWidget(skinLabel)
        physicalLayout.addWidget(skinEdit)
        physicalLayout.addWidget(hairLabel)
        physicalLayout.addWidget(hairEdit)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        physicalWindow.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO SKILLS LAYOUT
        physicalLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        physicalWindow.setLayout(physicalLayout)

        # CHARACTER APPEARANCE SECTION

        # INITIALIZING LAYOUTS
        characterAppearanceLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        characterAppearanceLayout.setAlignment(layoutAlignment)

        # TITLE OF THE INTERFACE
        characterAppearanceTitle = QLabel("Character Appearance: ")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        characterAppearanceTitle.setFont(font)
        alignment = Qt.AlignHCenter
        characterAppearanceTitle.setAlignment(alignment)

        # CHARACTER APPEARANCE EDIT
        characterAppearanceEdit = QTextEdit()
        characterAppearanceEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        characterAppearanceEdit.setFixedWidth(1000)
        characterAppearanceEdit.setFixedHeight(900)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(
            lambda: goBackToPhysicalWindowFromCharacterAppearanceWindow(characterAppearanceWindow, physicalWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(
            lambda: goToBackstoryWindowFromCharacterAppearanceWindow(characterAppearanceWindow, backstoryWindow))

        # ADDING WIDGETS TO THE MAIN LAYOUT
        characterAppearanceLayout.addWidget(characterAppearanceTitle)

        # ADDING WIDGETS TO HORIZONTAL LAYOUT
        horizontalLayout.addWidget(characterAppearanceEdit)

        # ADDING HORIZONTAL LAYOUT TO MAIN LAYOUT
        characterAppearanceLayout.addLayout(horizontalLayout)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        characterAppearanceWindow.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO MAIN LAYOUT
        characterAppearanceLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        characterAppearanceWindow.setLayout(characterAppearanceLayout)

        # BACKSTORY SECTION

        # INITIALIZING LAYOUTS
        backstoryLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        backstoryLayout.setAlignment(layoutAlignment)

        # POSITIONING HORIZONTAL LAYOUT
        horizontalLayoutAligment = Qt.AlignTop
        horizontalLayout.setAlignment(horizontalLayoutAligment)

        # TITLE OF THE INTERFACE
        backstoryTitle = QLabel("Character Backstory: ")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        backstoryTitle.setFont(font)
        alignment = Qt.AlignHCenter
        backstoryTitle.setAlignment(alignment)

        # CHARACTER BACKSTORY QTEXTEDIT
        backstoryEdit = QTextEdit()
        backstoryEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        backstoryEdit.setFixedWidth(1000)
        backstoryEdit.setFixedHeight(900)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(
            lambda: goBackToCharacterAppearanceWindowFromBackstoryWindow(backstoryWindow, characterAppearanceWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(lambda: goToAlliesWindowFromBackstoryWindow(backstoryWindow, alliesWindow))

        # ADDING WIDGETS TO THE MAIN LAYOUT
        backstoryLayout.addWidget(backstoryTitle)

        # ADDING WIDGETS TO HORIZONTAL LAYOUT
        horizontalLayout.addWidget(backstoryEdit)

        # ADDING HORIZONTAL LAYOUT TO MAIN LAYOUT
        backstoryLayout.addLayout(horizontalLayout)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        backstoryWindow.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO MAIN LAYOUT
        backstoryLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        backstoryWindow.setLayout(backstoryLayout)

        # ALLIES SECTION

        # INITIALIZING LAYOUTS
        alliesLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        alliesLayout.setAlignment(layoutAlignment)

        # TITLE OF THE INTERFACE
        alliesTitle = QLabel("Allies and Organizations: ")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        alliesTitle.setFont(font)
        alignment = Qt.AlignHCenter
        alliesTitle.setAlignment(alignment)

        # ALLIES EDIT
        alliesEdit = QTextEdit()
        alliesEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        alliesEdit.setFixedWidth(1000)
        alliesEdit.setFixedHeight(900)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(lambda: goBackToBackstoryWindowFromAlliesWindow(alliesWindow, backstoryWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(lambda: goToSymbolWindowFromAlliesWindow(alliesWindow, symbolWindow))

        # ADDING WIDGETS TO THE MAIN LAYOUT
        alliesLayout.addWidget(alliesTitle)

        # ADDING WIDGETS TO HORIZONTAL LAYOUT
        horizontalLayout.addWidget(alliesEdit)

        # ADDING HORIZONTAL LAYOUT TO MAIN LAYOUT
        alliesLayout.addLayout(horizontalLayout)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        alliesWindow.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO MAIN LAYOUT
        alliesLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        alliesWindow.setLayout(alliesLayout)

        # SYMBOL SECTION

        # INITIALIZING LAYOUTS
        symbolLayout = QVBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        symbolLayout.setAlignment(layoutAlignment)

        # TITLE OF THE INTERFACE
        symbolTitle = QLabel("Symbol ")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        symbolTitle.setFont(font)
        alignment = Qt.AlignHCenter
        symbolTitle.setAlignment(alignment)

        # SYMBOL NAME LABEL
        symbolNameLabel = QLabel("Name: ")
        symbolNameLabelFont = QFont('Arial')
        symbolNameLabelFont.setPointSize(30)
        symbolNameLabel.setFont(symbolNameLabelFont)

        # SYMBOL EDIT
        symbolEdit = QLineEdit()
        symbolEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        symbolEdit.setFixedWidth(300)
        symbolEdit.setFixedHeight(30)

        # AGE LABEL
        ageLabel = QLabel("Age: ")
        ageLabelFont = QFont('Arial')
        ageLabelFont.setPointSize(30)
        ageLabel.setFont(ageLabelFont)

        # AGE EDIT
        ageEdit = QLineEdit()
        ageEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        ageEdit.setFixedWidth(300)
        ageEdit.setFixedHeight(30)

        # SYMBOL DESCRIPTION LABEL
        symbolDescriptionLabel = QLabel("Symbol Description: ")
        symbolDescriptionLabelFont = QFont('Arial')
        symbolDescriptionLabelFont.setPointSize(30)
        symbolDescriptionLabel.setFont(symbolDescriptionLabelFont)

        # SYMBOL DESCRIPTION EDIT
        symbolDescriptionEdit = QLineEdit()
        symbolDescriptionEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        symbolDescriptionEdit.setFixedWidth(500)
        symbolDescriptionEdit.setFixedHeight(200)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(lambda: goBackToAlliesWindowFromSymbolWindow(symbolWindow, alliesWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(
            lambda: goToAdditionalFeaturesWindowFromSymbolWindow(symbolWindow, additionalFeaturesWindow))

        # ADDING WIDGETS TO THE MAIN LAYOUT
        symbolLayout.addWidget(symbolTitle)
        symbolLayout.addWidget(symbolNameLabel)
        symbolLayout.addWidget(symbolEdit)
        symbolLayout.addWidget(symbolDescriptionLabel)
        symbolLayout.addWidget(symbolDescriptionEdit)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        symbolWindow.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO MAIN LAYOUT
        symbolLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        symbolWindow.setLayout(symbolLayout)

        # ADDITIONAL FEATURES SECTION

        # INITIALIZING LAYOUTS
        additionalFeaturesLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        additionalFeaturesLayout.setAlignment(layoutAlignment)

        # TITLE OF THE INTERFACE
        additionalFeaturesTitle = QLabel("Character Additional Features and Traits: ")
        font = QFont('Arial')
        font.setPointSize(40)
        font.setBold(True)
        additionalFeaturesTitle.setFont(font)
        alignment = Qt.AlignHCenter
        additionalFeaturesTitle.setAlignment(alignment)

        # CHARACTER ADDITIONAL FEATURES EDIT
        additionalFeaturesEdit = QTextEdit()
        additionalFeaturesEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        additionalFeaturesEdit.setFixedWidth(1000)
        additionalFeaturesEdit.setFixedHeight(900)
        additionalFeaturesEdit.setAlignment(Qt.AlignTop)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(
            lambda: goBackToSymbolWindowFromAdditionalFeaturesWindow(additionalFeaturesWindow, symbolWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(
            lambda: goToTreasureWindowFromAdditionalFeaturesWindow(additionalFeaturesWindow, treasureWindow))

        # ADDING WIDGETS TO THE MAIN LAYOUT
        additionalFeaturesLayout.addWidget(additionalFeaturesTitle)

        # ADDING WIDGETS TO HORIZONTAL LAYOUT
        horizontalLayout.addWidget(additionalFeaturesEdit)

        # ADDING HORIZONTAL LAYOUT TO MAIN LAYOUT
        additionalFeaturesLayout.addLayout(horizontalLayout)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        additionalFeaturesWindow.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO MAIN LAYOUT
        additionalFeaturesLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        additionalFeaturesWindow.setLayout(additionalFeaturesLayout)

        # TREASURE SECTION

        # INITIALIZING LAYOUTS
        treasureLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        treasureLayout.setAlignment(layoutAlignment)

        # TITLE OF THE INTERFACE
        treasureTitle = QLabel("Treasure: ")
        font = QFont('Arial')
        font.setPointSize(40)
        font.setBold(True)
        treasureTitle.setFont(font)
        alignment = Qt.AlignHCenter
        treasureTitle.setAlignment(alignment)

        # TREASURE EDIT
        treasureEdit = QTextEdit()
        treasureEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        treasureEdit.setFixedWidth(1000)
        treasureEdit.setFixedHeight(900)
        treasureEdit.setAlignment(Qt.AlignTop)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(
            lambda: goBackToAdditionalFeaturesWindowFromTreasureWindow(treasureWindow, additionalFeaturesWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(lambda: goToSpellWindowFromTreasureWindow(treasureWindow, spellWindow))

        # ADDING WIDGETS TO THE MAIN LAYOUT
        treasureLayout.addWidget(treasureTitle)

        # ADDING WIDGETS TO HORIZONTAL LAYOUT
        horizontalLayout.addWidget(treasureEdit)

        # ADDING HORIZONTAL LAYOUT TO MAIN LAYOUT
        treasureLayout.addLayout(horizontalLayout)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        treasureWindow.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO MAIN LAYOUT
        treasureLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        treasureWindow.setLayout(treasureLayout)

        # SPELL SECTION

        # INITIALIZING LAYOUTS
        spellLayout = QVBoxLayout()
        buttonsLayout = QHBoxLayout()

        # TITLE OF THE LOGIN INTERFACE
        spellTitle = QLabel("Spellcasting ")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        spellTitle.setFont(font)
        alignment = Qt.AlignHCenter
        spellTitle.setAlignment(alignment)

        # SPELLCASTING CLASS LABEL
        spellcastingClassLabel = QLabel("Spellcasting Class: ")
        spellcastingClassLabelFont = QFont('Arial')
        spellcastingClassLabelFont.setPointSize(30)
        spellcastingClassLabel.setFont(spellcastingClassLabelFont)

        # SPELLCASTING CLASS EDIT
        spellcastingClassEdit = QLineEdit()
        spellcastingClassEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        spellcastingClassEdit.setFixedWidth(300)
        spellcastingClassEdit.setFixedHeight(30)

        # SPELLCASTING ABILITY LABEL
        spellcastingAbilityLabel = QLabel("Spellcasting Ability: ")
        spellcastingAbilityLabelFont = QFont('Arial')
        spellcastingAbilityLabelFont.setPointSize(30)
        spellcastingAbilityLabel.setFont(spellcastingAbilityLabelFont)

        # SPELLCASTING ABILITY EDIT
        spellcastingAbilityEdit = QLineEdit()
        spellcastingAbilityEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        spellcastingAbilityEdit.setFixedWidth(300)
        spellcastingAbilityEdit.setFixedHeight(30)

        # SPELL SAVE DC LABEL
        spellSaveDcLabel = QLabel("Spell Save DC: ")
        spellSaveDcLabelFont = QFont('Arial')
        spellSaveDcLabelFont.setPointSize(30)
        spellSaveDcLabel.setFont(spellSaveDcLabelFont)

        # SPELL SAVE DC EDIT
        spellSaveDcEdit = QLineEdit()
        spellSaveDcEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        spellSaveDcEdit.setFixedWidth(300)
        spellSaveDcEdit.setFixedHeight(30)

        # SPELL ATTACK BONUS LABEL
        spellAttackBonusLabel = QLabel("Spell Attack Bonus: ")
        spellAttackBonusLabelFont = QFont('Arial')
        spellAttackBonusLabelFont.setPointSize(30)
        spellAttackBonusLabel.setFont(spellAttackBonusLabelFont)

        # SPELL ATTACK BONUS EDIT
        spellAttackBonusEdit = QLineEdit()
        spellAttackBonusEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        spellAttackBonusEdit.setFixedWidth(300)
        spellAttackBonusEdit.setFixedHeight(30)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(lambda: goBackToTreasureWindowFromSpellWindow(spellWindow, treasureWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(lambda: goToCantripsWindowFromSpellWindow(spellWindow, cantripsWindow))

        # ADDING WIDGETS TO THE LAYOUT
        spellLayout.addWidget(spellTitle)
        spellLayout.addWidget(spellcastingClassLabel)
        spellLayout.addWidget(spellcastingClassEdit)
        spellLayout.addWidget(spellcastingAbilityLabel)
        spellLayout.addWidget(spellcastingAbilityEdit)
        spellLayout.addWidget(spellSaveDcLabel)
        spellLayout.addWidget(spellSaveDcEdit)
        spellLayout.addWidget(spellAttackBonusLabel)
        spellLayout.addWidget(spellAttackBonusEdit)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        spellWindow.setStyleSheet("background-color: #D2B48C")

        # CENTERING THE LAYOUT
        layoutAlignment = Qt.AlignCenter
        spellLayout.setAlignment(layoutAlignment)

        # ATTACHING CHARACTER CREATION LAYOUT TO BUTTONS LAYOUT
        spellLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        spellWindow.setLayout(spellLayout)

        # CANTRIPS SECTION

        # INITIALIZING LAYOUTS
        cantripsLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        buttonsLayout = QHBoxLayout()

        # CENTERING THE MAIN LAYOUT
        layoutAlignment = Qt.AlignCenter
        cantripsLayout.setAlignment(layoutAlignment)

        # TITLE OF THE INTERFACE
        cantripsTitle = QLabel("Cantrips: ")
        font = QFont('Arial')
        font.setPointSize(40)
        font.setBold(True)
        cantripsTitle.setFont(font)
        alignment = Qt.AlignHCenter
        cantripsTitle.setAlignment(alignment)

        # CHARACTER APPEARANCE EDIT
        cantripsEdit = QTextEdit()
        cantripsEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        cantripsEdit.setFixedWidth(1000)
        cantripsEdit.setFixedHeight(900)
        cantripsEdit.setAlignment(Qt.AlignTop)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(lambda: goBackToSpellWindowFromCantripsWindow(cantripsWindow, spellWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Next")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)
        nextButton.clicked.connect(lambda: goToSpellListWindowFromCantripsWindow(cantripsWindow, spellListWindow))

        # ADDING WIDGETS TO THE MAIN LAYOUT
        cantripsLayout.addWidget(cantripsTitle)

        # ADDING WIDGETS TO HORIZONTAL LAYOUT
        horizontalLayout.addWidget(cantripsEdit)

        # ADDING HORIZONTAL LAYOUT TO MAIN LAYOUT
        cantripsLayout.addLayout(horizontalLayout)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        cantripsWindow.setStyleSheet("background-color: #D2B48C")

        # ATTACHING BUTTONS LAYOUT TO MAIN LAYOUT
        cantripsLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        cantripsWindow.setLayout(cantripsLayout)

        # SPELL LIST SECTION

        # INITIALIZING LAYOUTS
        spellListLayout = QVBoxLayout()
        verticalLayout1 = QVBoxLayout()
        verticalLayout2 = QVBoxLayout()
        verticalLayout3 = QVBoxLayout()
        horizontalLayout = QHBoxLayout()
        verticalLayout4 = QVBoxLayout()
        buttonsLayout = QHBoxLayout()

        # TITLE OF THE INTERFACE
        spellListTitle = QLabel("Spell List: ")
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        spellListTitle.setFont(font)
        alignment = Qt.AlignHCenter
        spellListTitle.setAlignment(alignment)

        # SLOTS TOTAL LABEL
        slotsTotalLabel = QLabel("Slots Total:")
        slotsTotalLabelFont = QFont('Arial')
        slotsTotalLabelFont.setPointSize(30)
        slotsTotalLabel.setFont(slotsTotalLabelFont)

        # TEXTBOX1 LAYOUT1
        textBox1Layout1 = QLineEdit()
        textBox1Layout1.setStyleSheet("background-color: #FFFFFF; color: black;")
        textBox1Layout1.setFixedWidth(300)
        textBox1Layout1.setFixedHeight(30)

        # SPELL LEVEL LABEL
        spellLevelLabel = QLabel("Spell Level:")
        spellLevelLabelFont = QFont('Arial')
        spellLevelLabelFont.setPointSize(30)
        spellLevelLabel.setFont(spellLevelLabelFont)

        # TEXTBOX1 LAYOUT2
        textBox1Layout2 = QLineEdit()
        textBox1Layout2.setStyleSheet("background-color: #FFFFFF; color: black;")
        textBox1Layout2.setFixedWidth(300)
        textBox1Layout2.setFixedHeight(30)

        # SLOTS EXTENDED LABEL
        slotsExpendedLabel = QLabel("Slots Expended: ")
        slotsExpendedLabelFont = QFont('Arial')
        slotsExpendedLabelFont.setPointSize(30)
        slotsExpendedLabel.setFont(slotsExpendedLabelFont)

        # TEXTBOX1 LAYOUT3
        textBox1Layout3 = QLineEdit()
        textBox1Layout3.setStyleSheet("background-color: #FFFFFF; color: black;")
        textBox1Layout3.setFixedWidth(300)
        textBox1Layout3.setFixedHeight(30)

        # TOTAL HIT DICE LABEL
        totalHitLabel = QLabel("Total Hit Dice: ")
        totalHitLabelFont = QFont('Arial')
        totalHitLabelFont.setPointSize(30)
        totalHitLabel.setFont(totalHitLabelFont)

        # TOTAL HIT LABEL EDIT
        totalHitLabelEdit = QLineEdit()
        totalHitLabelEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        totalHitLabelEdit.setFixedWidth(300)
        totalHitLabelEdit.setFixedHeight(30)

        # ATTACKS AND SPELLCASTING LABEL
        attacksAndSpellcastingLabel = QLabel("Attacks and Spellcasting: ")
        attacksAndSpellcastingLabelFont = QFont('Arial')
        attacksAndSpellcastingLabelFont.setPointSize(30)
        attacksAndSpellcastingLabel.setFont(attacksAndSpellcastingLabelFont)

        # ATTACKS AND SPELLCASTING EDIT
        attacksAndSpellcastingEdit = QLineEdit()
        attacksAndSpellcastingEdit.setStyleSheet("background-color: #FFFFFF; color: black;")
        attacksAndSpellcastingEdit.setFixedWidth(300)
        attacksAndSpellcastingEdit.setFixedHeight(30)

        # SPELL NAME OF SPELL LIST LABEL
        spellNameOfSpellListLabel = QLabel("Name the known Spells: ")
        spellNameOfSpellListLabelFont = QFont('Arial')
        spellNameOfSpellListLabelFont.setPointSize(30)
        spellNameOfSpellListLabel.setFont(spellLevelLabelFont)

        # LIST TEXTBOX 1
        listTextbox1 = QLineEdit()
        listTextbox1.setStyleSheet("background-color: #FFFFFF; color: black;")
        listTextbox1.setFixedWidth(300)
        listTextbox1.setFixedHeight(30)

        # LIST TEXTBOX 2
        listTextbox2 = QLineEdit()
        listTextbox2.setStyleSheet("background-color: #FFFFFF; color: black;")
        listTextbox2.setFixedWidth(300)
        listTextbox2.setFixedHeight(30)

        # LIST TEXTBOX 3
        listTextbox3 = QLineEdit()
        listTextbox3.setStyleSheet("background-color: #FFFFFF; color: black;")
        listTextbox3.setFixedWidth(300)
        listTextbox3.setFixedHeight(30)

        # LIST TEXTBOX 3
        listTextbox3 = QLineEdit()
        listTextbox3.setStyleSheet("background-color: #FFFFFF; color: black;")
        listTextbox3.setFixedWidth(300)
        listTextbox3.setFixedHeight(30)

        # LIST TEXTBOX 4
        listTextbox4 = QLineEdit()
        listTextbox4.setStyleSheet("background-color: #FFFFFF; color: black;")
        listTextbox4.setFixedWidth(300)
        listTextbox4.setFixedHeight(30)

        # LIST TEXTBOX 5
        listTextbox5 = QLineEdit()
        listTextbox5.setStyleSheet("background-color: #FFFFFF; color: black;")
        listTextbox5.setFixedWidth(300)
        listTextbox5.setFixedHeight(30)

        # BACK BUTTON
        backButton = QPushButton("Back")
        backButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        backButton.setFixedWidth(300)
        backButton.setFixedHeight(30)
        backButton.clicked.connect(lambda: goBackToCantripsWindowFromSpellListWindow(spellListWindow, cantripsWindow))

        # NEXT BUTTON
        nextButton = QPushButton("Confirm")
        nextButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        nextButton.setFixedWidth(300)
        nextButton.setFixedHeight(30)

        # ADDING WIDGETS TO SPELL LIST LAYOUT
        spellListLayout.addWidget(spellListTitle)

        # ADDING WIDGETS TO VERTICAL LAYOUT 1
        verticalLayout1.addWidget(spellLevelLabel)
        verticalLayout1.addWidget(textBox1Layout1)

        # ADDING WIDGETS TO VERTICAL LAYOUT 2
        verticalLayout2.addWidget(slotsTotalLabel)
        verticalLayout2.addWidget(textBox1Layout2)

        # ADDING WIDGETS TO VERTICAL LAYOUT 3
        verticalLayout3.addWidget(slotsExpendedLabel)
        verticalLayout3.addWidget(textBox1Layout3)

        # ADDING WIDGETS TO VERTICAL LAYOUT 4
        verticalLayout4.addWidget(spellNameOfSpellListLabel)
        verticalLayout4.addWidget(listTextbox1)
        verticalLayout4.addWidget(listTextbox2)
        verticalLayout4.addWidget(listTextbox3)
        verticalLayout4.addWidget(listTextbox4)
        verticalLayout4.addWidget(listTextbox5)

        # ADDING WIDGETS TO BUTTONS LAYOUT
        buttonsLayout.addWidget(backButton)
        buttonsLayout.addWidget(nextButton)

        # COLORING THE WINDOW BACKGROUND
        spellListWindow.setStyleSheet("background-color: #D2B48C")

        # CENTERING THE LAYOUT
        layoutAlignment = Qt.AlignCenter
        spellListLayout.setAlignment(layoutAlignment)

        # ATTACHING LAYOUTS TO HORIZONTAL LAYOUT
        horizontalLayout.addLayout(verticalLayout1)
        horizontalLayout.addLayout(verticalLayout2)
        horizontalLayout.addLayout(verticalLayout3)

        # ATTACHING LAYOUTS TO SPELL LIST LAYOUT
        spellListLayout.addLayout(horizontalLayout)
        spellListLayout.addLayout(verticalLayout4)
        spellListLayout.addLayout(buttonsLayout)

        # ATTACHING THE LAYOUT TO THE WINDOW
        spellListWindow.setLayout(spellListLayout)

        # REGISTER SECTION

        registrationLayout = QVBoxLayout()

        # TITLE OF THE REGISTER INTERFACE
        registrationTitle = QLabel('D&D')
        registrationFont = QFont('Arial')
        registrationFont.setPointSize(60)
        registrationFont.setBold(True)
        registrationTitle.setFont(registrationFont)
        alignment = Qt.AlignHCenter
        registrationTitle.setAlignment(alignment)

        # USERNAME
        username_label = QLabel("Username:")
        username_edit = QLineEdit()
        username_edit.setStyleSheet("background-color: #FFFFFF; color: black;")
        username_edit.setFixedWidth(434)
        username_edit.setFixedHeight(30)
        usernameFont = QFont('Arial')
        usernameFont.setPointSize(30)
        username_label.setFont(usernameFont)

        # EMAIL
        email_label = QLabel('Email:')
        email_edit = QLineEdit()
        email_edit.setStyleSheet("background-color: #FFFFFF; color: black;")
        email_edit.setFixedWidth(434)
        email_edit.setFixedHeight(30)
        email_labelFont = QFont('Arial')
        email_labelFont.setPointSize(30)
        email_label.setFont(email_labelFont)

        # PASSWORD
        password_label = QLabel("Password:")
        password_edit = QLineEdit()
        password_edit.setStyleSheet("background-color: #FFFFFF; color: black;")
        password_edit.setFixedWidth(434)
        password_edit.setFixedHeight(30)
        passwordFont = QFont('Arial')
        passwordFont.setPointSize(30)
        password_label.setFont(passwordFont)

        # PASSWORD CONFIRMATION
        password_confirmation_label = QLabel('Confirm Password:')
        password_confirmation_edit = QLineEdit()
        password_confirmation_edit.setStyleSheet("background-color: #FFFFFF; color: black;")
        password_confirmation_edit.setFixedWidth(434)
        password_confirmation_edit.setFixedHeight(30)
        password_confirmation_labelFont = QFont('Arial')
        password_confirmation_labelFont.setPointSize(30)
        password_confirmation_label.setFont(password_confirmation_labelFont)

        # ALREADY REGISTERED BUTTON
        alreadyRegisteredButton = QPushButton("Already Registered? Click Here to Login")
        alreadyRegisteredButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        alreadyRegisteredButton.clicked.connect(
            lambda: goBackToLoginWindowFromRegistrationWindow(registrationWindow, loginWindow))

        # REGISTER BUTTON
        registrationButton = QPushButton('Register')
        registrationButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        registrationButton.clicked.connect(
            lambda: goToMenuWindowFromRegistrationWindow(registrationWindow, self.menuWindow))

        # ADDING WIDGETS TO THE LAYOUT
        registrationLayout.addWidget(registrationTitle)
        registrationLayout.addWidget(username_label)
        registrationLayout.addWidget(username_edit)
        #registrationLayout.addWidget(email_label)
        #registrationLayout.addWidget(email_edit)
        registrationLayout.addWidget(password_label)
        registrationLayout.addWidget(password_edit)
        registrationLayout.addWidget(password_confirmation_label)
        registrationLayout.addWidget(password_confirmation_edit)
        registrationLayout.addWidget(alreadyRegisteredButton)
        registrationLayout.addWidget(registrationButton)

        # COLORING THE WINDOW BACKGROUND
        registrationWindow.setStyleSheet("background-color: #D2B48C")

        # CENTERING THE LAYOUT
        layoutAlignment = Qt.AlignCenter
        registrationLayout.setAlignment(layoutAlignment)

        # ATTACHING THE LAYOUT TO THE WINDOW
        registrationWindow.setLayout(registrationLayout)

        # LOGIN SECTION

        loginLayout = QVBoxLayout()

        # TITLE OF THE LOGIN INTERFACE
        loginTitle = QLabel('D&D')
        font = QFont('Arial')
        font.setPointSize(60)
        font.setBold(True)
        loginTitle.setFont(font)
        alignment = Qt.AlignHCenter
        loginTitle.setAlignment(alignment)

        # USERNAME
        username_label = QLabel("Username:")
        username_login_edit = QLineEdit()
        username_login_edit.setStyleSheet("background-color: #FFFFFF; color: black;")
        username_login_edit.setFixedWidth(300)
        username_login_edit.setFixedHeight(30)
        usernameFont = QFont('Arial')
        usernameFont.setPointSize(30)
        username_label.setFont(usernameFont)

        # PASSWORD
        password_label = QLabel("Password:")
        password_login_edit = QLineEdit()
        password_login_edit.setStyleSheet("background-color: #FFFFFF; color: black;")
        password_login_edit.setFixedWidth(300)
        password_login_edit.setFixedHeight(30)
        passwordFont = QFont('Arial')
        passwordFont.setPointSize(30)
        password_label.setFont(passwordFont)

        # NOT REGISTERED BUTTON
        notRegisteredButton = QPushButton("Not Registered? Click Here")
        notRegisteredButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        notRegisteredButton.clicked.connect(
            lambda: goToRegistrationWindowFromLoginWindow(loginWindow, registrationWindow))

        # LOGIN BUTTON
        loginButton = QPushButton("Login")
        loginButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        loginButton.clicked.connect(lambda: goToMenu(loginWindow, self.menuWindow))

        loginExitButton = QPushButton("Exit")
        loginExitButton.setStyleSheet("background-color: #FFFFFF; color: black;")
        loginExitButton.clicked.connect(exitFromMenuWindow)

        # ADDING WIDGETS TO THE LAYOUT
        loginLayout.addWidget(loginTitle)
        loginLayout.addWidget(username_label)
        loginLayout.addWidget(username_login_edit)
        loginLayout.addWidget(password_label)
        loginLayout.addWidget(password_login_edit)
        loginLayout.addWidget(notRegisteredButton)
        loginLayout.addWidget(loginButton)
        loginLayout.addWidget(loginExitButton)

        # COLORING THE WINDOW BACKGROUND
        loginWindow.setStyleSheet("background-color: #D2B48C")

        # CENTERING THE LAYOUT
        layoutAlignment = Qt.AlignCenter
        loginLayout.setAlignment(layoutAlignment)

        # ATTACHING THE LAYOUT TO THE WINDOW
        loginWindow.setLayout(loginLayout)

        # EXECUTING THE PROGRAM
        loginWindow.show()

if __name__ == '__main__':
    app = QApplication([])
    entryWindow = Entry()
    app.exec()
