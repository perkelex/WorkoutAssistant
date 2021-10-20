from PySide6 import QtCore, QtWidgets, QtGui
import sys
import time

class WorkoutAssistant(QtWidgets.QWidget):
    class Decoratos(object):
        @staticmethod
        def stopTimers(func):
            def inner(self, *args, **kwargs):
                if self.countdownTimer.isActive():
                    self.countdownTimer.stop()
                if self.triggerTimer.isActive():
                    self.triggerTimer.stop()

                func(self, *args, **kwargs)
            return inner

    def __init__(self) -> None:
        super().__init__()
        self.counter = 0

        self.restButton = QtWidgets.QPushButton("1:30")
        # self.restButton.setSizePolicy(
        #     QtGui.QSizePolicy.Preferred,
        #     QtGui.QSizePolicy.Expanding)

        self.countdownTimer = QtCore.QTimer()
        self.countdownTimer.setInterval(1000)
        self.countdownTimer.timeout.connect(self.countdown)

        self.triggerTimer = QtCore.QTimer()
        self.triggerTimer.timeout.connect(self.discoParty)
        self.triggerTimer.setSingleShot(True)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.restButton)

        self.restButton.clicked.connect(self.restOnClick)

    @Decoratos.stopTimers
    def restOnClick(self):
        self.counter = 90
        self.countdownTimer.start()

    @Decoratos.stopTimers
    def regularPlusOnClick(self):
        pass

    @Decoratos.stopTimers
    def slothOnClick(self):
        pass

    def discoParty(self):
        pass

    def countdown(self):
        if self.counter > 0:
            self.counter -= 1
        self.restButton.setText(f"{time.strftime('%#M:%S', time.gmtime(self.counter))}")
        # self.restButton.setText(f"{self.counter}")

    # def updateButtonText(self, button):
    #     button.setText(f"{self.counter}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(['--style', 'Fusion'])

    widget = WorkoutAssistant()
    widget.setWindowTitle("Workout Assistant")
    widget.resize(300, 200)
    widget.show()

    sys.exit(app.exec())