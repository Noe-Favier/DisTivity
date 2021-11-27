from PyQt5 import QtWidgets
import sys

class InputBox():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

    def getText(self,text):
        """
            open a text box and return the input
        """
        input, done = QtWidgets.QInputDialog.getText(None, 'Input Dialog', text)
        if done:
            return input
              
if __name__ == "__main__":
    ib = InputBox()
    print(ib.getText("Enter a title"))
