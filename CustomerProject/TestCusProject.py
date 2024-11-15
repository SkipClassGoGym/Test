from PyQt6.QtWidgets import QApplication, QMainWindow

from CustomerProject.MainWindowExt import MainWindowExt

app = QApplication([])
mainwindow = QMainWindow()
myui=MainWindowExt()
myui.setupUi(mainwindow)

myui.datasimulation()
myui.showCustomerIntoUI()

myui.showWindow()
app.exec()