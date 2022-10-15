from PyQt6.QtWidgets import QMessageBox


def showPopup(text, title):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    x = msg.exec()
