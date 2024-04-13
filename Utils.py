import os
import uuid
from PyQt5.QtWidgets import QMessageBox, QDialog, QDialogButtonBox, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, QObject

'''
def combinePixmap(pm1: QPixmap, pm2: QPixmap) -> QPixmap:
    # Crea un QPixmap vuoto con le dimensioni della somma dei due pixmap
    combined_pixmap = QPixmap(pm1.size() + pm2.size())
    combined_pixmap.fill(Qt.transparent)

    # Crea un QPainter per disegnare sui pixmap
    painter = QPainter(combined_pixmap)

    # Disegna il primo QPixmap nella posizione (0, 0)
    painter.drawPixmap(0, 0, pm1)

    # Disegna il secondo QPixmap nella posizione (larghezza del primo pixmap, 0)
    painter.drawPixmap(pm1.width(), 0, pm2)

    # Fine del disegno
    painter.end()
    print(combined_pixmap.size())

    return combined_pixmap
'''


class confirmDialogue(QDialog):

    def reject(self):
        return super().reject()

    def accept(self):
        return super().accept()

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Confirm deletion?")

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Yes | QDialogButtonBox.No)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        valueLabel = QLabel("Are you sure?")
        self.layout.addWidget(valueLabel)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class updateMapSignalObject(QObject):
    """Used to allow access to this signal to all Classes"""
    updateMap = pyqtSignal()


def createFolderStructure() -> bool:
    basePath = os.getcwd()
    try:
        os.mkdir(f"{basePath}\\DB")
    except FileExistsError as e:
        pass
    basePath += "\\DB"
    try:
        os.mkdir(f"{basePath}\\Characters")
    except FileExistsError as e:
        pass
    try:
        os.mkdir(f"{basePath}\\NPCs")
    except FileExistsError as e:
        pass
    try:
        os.mkdir(f"{basePath}\\Adventures")
    except FileExistsError as e:
        pass
    try:
        os.mkdir(f"{basePath}\\Monsters")
    except FileExistsError as e:
        pass
    try:
        os.mkdir(f"{basePath}\\Maps")
    except FileExistsError as e:
        pass
    try:
        os.mkdir(f"{basePath}\\Items")
    except FileExistsError as e:
        pass
    try:
        os.mkdir(f"{basePath}\\Images")
    except FileExistsError as e:
        pass
    try:
        os.mkdir(f"{basePath}\\Users")
    except FileExistsError as e:
        pass
    try:
        os.mkdir(f"{basePath}\\Characters\\Images")
    except FileExistsError as e:
        pass
    try:
        os.mkdir(f"{basePath}\\Items\\Images")
    except FileExistsError as e:
        pass
    try:
        os.mkdir(f"{basePath}\\Monsters\\Images")
    except FileExistsError as e:
        pass
    try:
        os.mkdir(f"{basePath}\\NPCs\\Images")
    except FileExistsError as e:
        pass

    return True


def sendAlert(title: str, info: str, icon: QMessageBox = QMessageBox.Critical) -> None:
    """Shows the user an error MessageBox"""
    msg = QMessageBox()
    msg.setIcon(icon)
    msg.setText(info)
    msg.setWindowTitle(title)
    msg.exec_()


def validateName(text: str) -> bool:
    """Checks wether text contains any special characters -> True if the name respects this condition"""
    if not text.replace(' ', '').isalnum():
        sendAlert("Error", "The name field can't contain special symbols!")
        return False
    return True


def nameExists(new: str, current: str) -> bool:
    """If new == current returns false"""
    if new == current:
        sendAlert("Warning", "This name is already taken")
        return False
    return True


def generateID() -> int:
    """Runs only when creating a new Adventure"""
    return uuid.uuid1().int


def directoryExistsCreate(path: str) -> bool:
    if os.path.exists(path):
        return False
    else:
        os.mkdir(path)
        return True
