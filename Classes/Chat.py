from PyQt5.QtWidgets import QWidget, QLineEdit
import jsonpickle
import os

from Classes.Message import Message


class Chat:
    def load(self, adv) -> None:
        with open(f"{os.getcwd()}\\DB\\Adventures\\{adv.name}.json", "r") as f:
            item = jsonpickle.loads(f.read())
        if item.chat != None:
            for message in item.chat.messagesList:
                if adv.owner == adv.whoami.name:
                    # If the User is the DM, load all messages
                    self.chatListWidget.addItem(f"{message.sender}: {message.text}")
                elif adv.whoami.name == message.receiver:
                    # Whisper
                    self.chatListWidget.addItem(f"{message.sender}: {message.text}")
                elif adv.whoami.name == message.sender:
                    # Whisper
                    self.chatListWidget.addItem(f"{message.sender}: {message.text}")
                elif message.receiver == None:
                    # Global message
                    self.chatListWidget.addItem(f"{message.sender}: {message.text}")
                self.messagesList.append(message)

    def sendMessage(self, user: str):
        if self.chatMessageLineEdit.text()[0] + self.chatMessageLineEdit.text()[1] == "/w":
            # This is a whisper
            # The text splitted along spaces contains in [1] the receiver
            receiver = self.chatMessageLineEdit.text().split(" ")[1]
            text = ""
            for word in self.chatMessageLineEdit.text().split()[2:]:
                text += f"{word} "
            message: Message = Message(user, text, receiver)
        else:
            message: Message = Message(user, self.chatMessageLineEdit.text())
        self.chatListWidget.addItem(f"{message.sender}: {message.text}")
        self.messagesList.append(message)
        self.chatMessageLineEdit.clear()

    def sendAutomatedMessage(self, user: str, automatedMessage: str):
        if len(self.diceList) != 0:
            message: Message = Message(user, automatedMessage)
            self.chatListWidget.addItem(f"{user}: {automatedMessage}")
            self.messagesList.append(message)

    def __init__(self, chatListWidget: QWidget, chatMessageLineEdit: QLineEdit, diceList: list,
                 messageList: list = []) -> None:
        self.chatListWidget = chatListWidget
        self.chatMessageLineEdit = chatMessageLineEdit
        self.diceList = diceList
        self.messagesList = messageList
        pass
