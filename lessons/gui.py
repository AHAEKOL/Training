# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
  
  
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.counter = 0
        self.counter2 = 0
        
        # setting title
        self.setWindowTitle("Python")
  
        # setting geometry
        self.setGeometry(100, 100, 600, 400)
  
        # creating a push button
        self.button = QPushButton("CLICK", self)
  
        # setting geometry of button
        self.button.setGeometry(200, 150, 100, 30)
  
        # adding action to a button
        self.button.clicked.connect(self.clickme)
  
        # changing the text of button
        self.button.setText("Over-write")
       
        # timer creation and setup
        self.timer = QTimer(self)
        self.timer.setInterval(1000);
        self.timer.timeout.connect(self.timeouthandler)
        self.timer.start()
  
        # showing all the widgets
        self.show()
  
    # action method
    def clickme(self):
        self.counter += 1
        self.button.setText(f"Ahoj {self.counter}")
        # printing pressed
        print("pressed")


    def timeouthandler(self):
        self.counter2 += 1
        self.setWindowTitle(f'Python {self.counter2}')
 
 
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())
