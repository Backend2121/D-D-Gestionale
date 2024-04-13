class Message:
    def __init__(self, sender: str, text: str, receiver: str = None) -> None:
        self.sender = sender
        self.text = text
        self.receiver = receiver
