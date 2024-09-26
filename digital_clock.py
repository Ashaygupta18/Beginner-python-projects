#Digital Clock
#Need to install PyQt5
#Added many comments to understand properly:)
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt

class Digitalclock(QWidget):
    def __init__(self):
        super().__init__()#to send arguments to parent we use super 
        self.time_label =  QLabel(self)#label that displays the time
        self.timer = QTimer(self)#adding timer to the clock
        self.initUI()#to call initui method

    def initUI(self):#designing layout of the clock
        self.setWindowTitle("Digital Clock")#title for window
        self.setGeometry(300,200,150,50)#where it will appear on the screen

        vbox = QVBoxLayout()#Layout manager...will arrange our widget vertically
        vbox.addWidget(self.time_label)#added our label to vbox
        self.setLayout(vbox)#to set layout

        self.time_label.setAlignment(Qt.AlignCenter)#centre align our time

        self.time_label.setStyleSheet("font-size: 75px;"#css properties
        "font-family: Ariel;"
        "color: green")#can get specific color by rgb,hex or hsl value

        self.setStyleSheet("background-color: black;")#for background color

        self.timer.timeout.connect(self.update_time)#connecting timer widget with slot of update_time
        self.timer.start(1000)#to trigger the timeout to connected timer and update time every1sec

        self.update_time()#calling update time

    def update_time(self):#method to update time
        current_time = QTime.currentTime().toString("hh:mm:ss AP")#can access current time with QTime 
        self.time_label.setText(current_time)#|____tostring is to set layout of the time (format specifiers)
        #|__to set text of the label

if __name__ == "__main__":#to run directly
    app = QApplication(sys.argv)#to create application
    clock = Digitalclock()
    clock.show()#to show the widget
    sys.exit(app.exec_())#to add mouse functions so user can interact...event loops