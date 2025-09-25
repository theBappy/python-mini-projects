import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())
