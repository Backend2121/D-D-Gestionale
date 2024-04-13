import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from Classes.Adventure import Adventure
import jsonpickle
from Classes.Entity import Entity
from Utils import *
from Utils import validateName, nameExists


class NPCs(QWidget):

    def delete(self) -> None:
        if self.selected is not None:
            for npc in self.adventure.entities:
                if npc == self.selected:
                    cnf = confirmDialogue()
                    if cnf.exec():
                        self.adventure.entities.remove(npc)
                        self.npcList.takeItem(self.npcList.currentRow())
                        if os.path.isfile(f"{os.getcwd()}\\DB\\NPCs\\{npc.name}.json"):
                            os.remove(f"{os.getcwd()}\\DB\\NPCs\\{npc.name}.json")
                        self.adventure.save()
                        break

    def createNew(self) -> None:
        # Check if the Npc the user wants to create already exists in the adventure's NPCsList
        for npcPresent in self.adventure.entities:
            if npcPresent.entityType == "NPC":
                if not nameExists(self.npcNameLineEdit.text(), npcPresent.name):
                    return
        if not validateName(self.npcNameLineEdit.text()):
            return
        npc = Entity(entityType="NPC")
        # Set all the parameters to the new ones
        npc.name = self.npcNameLineEdit.text()
        npc.alignment = self.npcAlignmentLineEdit.text()
        npc.size = self.npcSizeLineEdit.text()
        npc.profilePic = self.npcProfilePicLineEdit.text()
        # This solution allows the use of multiple : but they get removed
        attacksDict = {}
        line: str
        for line in self.npcAttacksTextEdit.toPlainText().splitlines():
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
        npc.attacks = attacksDict
        equipDict = {}
        line: str
        for line in self.npcEquipTextEdit.toPlainText().splitlines():
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
        npc.equip = equipDict

        skillsDict = {}
        line: str
        for line in self.npcSkillsTextEdit.toPlainText().splitlines():
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
        npc.skills = skillsDict

        extrasDict = {}
        line: str
        for line in self.npcExtrasTextEdit.toPlainText().splitlines():
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
        npc.extras = extrasDict

        try:
            npc.hp = int(self.npcHpLineEdit.text())
            npc.maxHp = int(self.npcHpLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Hp is invalid!")
            return
        try:
            npc.armorClass = int(self.npcACLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Armor class is invalid!")
            return
        try:
            npc.speed = int(self.npcSpeedLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Speed is invalid!")
            return
        try:
            npc.strength = int(self.npcStrengthLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Strength is invalid!")
            return
        try:
            npc.dexterity = int(self.npcDexterityLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Dexterity is invalid!")
            return
        try:
            npc.constitution = int(self.npcConstitutionLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Constitution is invalid!")
            return
        try:
            npc.intelligence = int(self.npcIntelligenceLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Intelligence is invalid!")
            return
        try:
            npc.wisdom = int(self.npcWisdomLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Wisdom is invalid!")
            return
        try:
            npc.charisma = int(self.npcCharismaLineEdit.text())
        except ValueError:
            sendAlert("Invalid number", "Charisma is invalid!")
            return
        self.adventure.NPCs.append(npc)
        item = QListWidgetItem(npc.name)
        item.setData(Qt.UserRole + 1, npc)
        self.npcList.addItem(item)
        npc.save()

    def save(self) -> None:
        npc: Entity = self.selected
        oldName = npc.name
        if npc is not None:
            if validateName(self.npcNameLineEdit.text()):
                # Set all the parameters to the new ones
                npc.name = self.npcNameLineEdit.text()
                npc.alignment = self.npcAlignmentLineEdit.text()
                npc.size = self.npcSizeLineEdit.text()
                npc.profilePic = self.npcProfilePicLineEdit.text()
                # This solution allows the use of multiple : but they get removed
                attacksDict = {}
                line: str
                for line in self.npcAttacksTextEdit.toPlainText().splitlines():
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
                npc.attacks = attacksDict
                equipDict = {}
                line: str
                for line in self.npcEquipTextEdit.toPlainText().splitlines():
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
                npc.equip = equipDict

                skillsDict = {}
                line: str
                for line in self.npcSkillsTextEdit.toPlainText().splitlines():
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
                npc.skills = skillsDict

                extrasDict = {}
                line: str
                for line in self.npcExtrasTextEdit.toPlainText().splitlines():
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
                npc.extras = extrasDict

                try:
                    npc.hp = int(self.npcHpLineEdit.text())
                    npc.maxHp = int(self.npcHpLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Hp is invalid!")
                    return
                try:
                    npc.armorClass = int(self.npcACLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Armor class is invalid!")
                    return
                try:
                    npc.speed = int(self.npcSpeedLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Speed is invalid!")
                    return
                try:
                    npc.strength = int(self.npcStrengthLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Strength is invalid!")
                    return
                try:
                    npc.dexterity = int(self.npcDexterityLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Dexterity is invalid!")
                    return
                try:
                    npc.constitution = int(self.npcConstitutionLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Constitution is invalid!")
                    return
                try:
                    npc.intelligence = int(self.npcIntelligenceLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Intelligence is invalid!")
                    return
                try:
                    npc.wisdom = int(self.npcWisdomLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Wisdom is invalid!")
                    return
                try:
                    npc.charisma = int(self.npcCharismaLineEdit.text())
                except ValueError:
                    sendAlert("Invalid number", "Charisma is invalid!")
                    return

                # Remove old .json file
                try:
                    if oldName != npc.name:
                        os.remove(f"{os.getcwd()}\\DB\\NPCs\\{oldName}.json")
                except FileNotFoundError:
                    pass
                # Create new .json file
                npc.save()
                # Update UI and self.adventure data
                for k, i in enumerate(self.adventure.entities):
                    if i.name == npc.name:
                        self.adventure.entities[k] = npc
                        self.npcList.item(self.npcList.currentRow()).setText(npc.name)
                        self.npcList.item(self.npcList.currentRow()).setData(Qt.UserRole + 1, npc)

    def __init__(self, adv: Adventure) -> None:
        """NPCs tab"""
        super().__init__()
        self.adventure = adv
        self.selected = None
        self.npcList = QListWidget()

        self.npcSizeLineEdit = QLineEdit()
        self.npcAlignmentLineEdit = QLineEdit()
        self.npcNameLineEdit = QLineEdit()
        self.npcProfilePicLineEdit = QLineEdit()
        self.npcAttacksTextEdit = QTextEdit()
        self.npcEquipTextEdit = QTextEdit()
        self.npcSkillsTextEdit = QTextEdit()
        self.npcExtrasTextEdit = QTextEdit()

        self.npcHpLineEdit = QLineEdit()
        self.npcACLineEdit = QLineEdit()
        self.npcSpeedLineEdit = QLineEdit()
        self.npcStrengthLineEdit = QLineEdit()
        self.npcDexterityLineEdit = QLineEdit()
        self.npcConstitutionLineEdit = QLineEdit()
        self.npcIntelligenceLineEdit = QLineEdit()
        self.npcWisdomLineEdit = QLineEdit()
        self.npcCharismaLineEdit = QLineEdit()

        self.initNPCs()

    def getNPCInfo(self, item):
        self.selected = item.data(Qt.UserRole + 1)
        for npc in self.adventure.entities:
            if npc.entityType == "NPC":
                if npc.name == self.selected.name:
                    # Populate info on the right
                    self.npcProfilePicLineEdit.setText(npc.profilePic)
                    self.npcNameLineEdit.setText(npc.name)
                    self.npcSizeLineEdit.setText(npc.size)
                    self.npcAlignmentLineEdit.setText(npc.alignment)

                    attackString = ""
                    self.npcAttacksTextEdit.setText(attackString)
                    if npc.attacks is not None:
                        for k in npc.attacks:
                            attackString += f"{k}:{npc.attacks[k]}\n"
                        self.npcAttacksTextEdit.setText(attackString)

                    skillsString = ""
                    self.npcSkillsTextEdit.setText(skillsString)
                    if npc.skills is not None:
                        for k in npc.skills:
                            skillsString += f"{k}:{npc.skills[k]}\n"
                    self.npcSkillsTextEdit.setText(skillsString)

                    equipString = ""
                    self.npcEquipTextEdit.setText(equipString)
                    if npc.equip is not None:
                        for k in npc.equip:
                            equipString += f"{k}:{npc.equip[k]}\n"
                    self.npcEquipTextEdit.setText(equipString)

                    extrasString = ""
                    self.npcEquipTextEdit.setText(extrasString)
                    if npc.extras is not None:
                        for k in npc.equip:
                            extrasString += f"{k}:{npc.extras[k]}\n"
                    self.npcExtrasTextEdit.setText(extrasString)

                    if str(npc.maxHp) != "None":
                        self.npcHpLineEdit.setText(str(npc.maxHp))
                    else:
                        self.npcHpLineEdit.setText(str(0))

                    if str(npc.armorClass) != "None":
                        self.npcACLineEdit.setText(str(npc.armorClass))
                    else:
                        self.npcACLineEdit.setText(str(0))

                    if str(npc.speed) != "None":
                        self.npcSpeedLineEdit.setText(str(npc.speed))
                    else:
                        self.npcSpeedLineEdit.setText(str(0))

                    if str(npc.strength) != "None":
                        self.npcStrengthLineEdit.setText(str(npc.strength))
                    else:
                        self.npcStrengthLineEdit.setText(str(0))

                    if str(npc.dexterity) != "None":
                        self.npcDexterityLineEdit.setText(str(npc.dexterity))
                    else:
                        self.npcDexterityLineEdit.setText(str(0))

                    if str(npc.constitution) != "None":
                        self.npcConstitutionLineEdit.setText(str(npc.constitution))
                    else:
                        self.npcConstitutionLineEdit.setText(str(0))

                    if str(npc.intelligence) != "None":
                        self.npcIntelligenceLineEdit.setText(str(npc.intelligence))
                    else:
                        self.npcIntelligenceLineEdit.setText(str(0))

                    if str(npc.wisdom) != "None":
                        self.npcWisdomLineEdit.setText(str(npc.wisdom))
                    else:
                        self.npcWisdomLineEdit.setText(str(0))

                    if str(npc.charisma) != "None":
                        self.npcCharismaLineEdit.setText(str(npc.charisma))
                    else:
                        self.npcCharismaLineEdit.setText(str(0))

    def initNPCs(self):
        directoryExistsCreate(f"{os.getcwd()}\\DB\\")
        directoryExistsCreate(f"{os.getcwd()}\\DB\\NPCs")
        directoryExistsCreate(f"{os.getcwd()}\\DB\\NPCs\\Images")
        verticalLayout = QVBoxLayout()
        buttonsGridLayout = QGridLayout()
        horizontalLayout = QHBoxLayout()
        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addLayout(buttonsGridLayout)
        self.npcList.itemClicked.connect(self.getNPCInfo)
        npcInfo = QVBoxLayout()
        # region NPC Info
        profilePicLayout = QHBoxLayout()
        nameLayout = QHBoxLayout()
        alignmentLayout = QHBoxLayout()
        sizeLayout = QHBoxLayout()

        profilePicLabel = QLabel("Propic")
        nameLabel = QLabel("Name")
        alignmentLabel = QLabel("Alignment")
        sizeLabel = QLabel("Size")

        profilePicLayout.addWidget(profilePicLabel)
        profilePicLayout.addWidget(self.npcProfilePicLineEdit)

        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(self.npcNameLineEdit)

        alignmentLayout.addWidget(alignmentLabel)
        alignmentLayout.addWidget(self.npcAlignmentLineEdit)

        sizeLayout.addWidget(sizeLabel)
        sizeLayout.addWidget(self.npcSizeLineEdit)

        npcInfo.addLayout(profilePicLayout)
        npcInfo.addLayout(nameLayout)
        npcInfo.addLayout(alignmentLayout)
        npcInfo.addLayout(sizeLayout)
        # region Stats
        hpLayout = QHBoxLayout()
        acLayout = QHBoxLayout()
        speedLayout = QHBoxLayout()
        statsLayout = QHBoxLayout()
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
        hpLayout.addWidget(self.npcHpLineEdit)

        acLayout.addWidget(acLabel)
        acLayout.addWidget(self.npcACLineEdit)

        speedLayout.addWidget(speedLabel)
        speedLayout.addWidget(self.npcSpeedLineEdit)

        strengthLayout.addWidget(strengthLabel)
        strengthLayout.addWidget(self.npcStrengthLineEdit)

        dexterityLayout.addWidget(dexterityLabel)
        dexterityLayout.addWidget(self.npcDexterityLineEdit)

        constitutionLayout.addWidget(constitutionLabel)
        constitutionLayout.addWidget(self.npcConstitutionLineEdit)

        intelligenceLayout.addWidget(intelligenceLabel)
        intelligenceLayout.addWidget(self.npcIntelligenceLineEdit)

        wisdomLayout.addWidget(wisdomLabel)
        wisdomLayout.addWidget(self.npcWisdomLineEdit)

        charismaLayout.addWidget(charismaLabel)
        charismaLayout.addWidget(self.npcCharismaLineEdit)

        statsLayout.addLayout(hpLayout)
        statsLayout.addLayout(acLayout)
        statsLayout.addLayout(speedLayout)
        statsLayout.addLayout(strengthLayout)
        statsLayout.addLayout(dexterityLayout)
        statsLayout.addLayout(constitutionLayout)
        statsLayout.addLayout(intelligenceLayout)
        statsLayout.addLayout(wisdomLayout)
        statsLayout.addLayout(charismaLayout)
        npcInfo.addLayout(statsLayout)

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
        attacksLayout.addWidget(self.npcAttacksTextEdit)

        equipLayout.addWidget(equipLabel)
        equipLayout.addWidget(self.npcEquipTextEdit)

        skillsLayout.addWidget(skillsLabel)
        skillsLayout.addWidget(self.npcSkillsTextEdit)

        extrasLayout.addWidget(extrasLabel)
        extrasLayout.addWidget(self.npcExtrasTextEdit)

        npcInfo.addLayout(attacksLayout)
        npcInfo.addLayout(equipLayout)
        npcInfo.addLayout(skillsLayout)
        npcInfo.addLayout(extrasLayout)

        # endregion
        horizontalLayout.addWidget(self.npcList)
        horizontalLayout.addLayout(npcInfo)

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

        for npc in self.adventure.entities:
            if npc.entityType == "NPC":
                item = QListWidgetItem(npc.name)
                item.setData(Qt.UserRole + 1, npc)
                self.npcList.addItem(item)
