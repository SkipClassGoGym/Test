from PyQt6.QtWidgets import QApplication, QMainWindow

from MyMultiplycationTableExt import MyMultiplycationTableExt

#Create QApplication instance
app=QApplication([]) #Copy

#Create QMainWindow instance
qMainWindow=QMainWindow() #Copy

#Create MyQMainWindowExt instance
myWindow=MyMultiplycationTableExt() #Chinh lai ten ext minh
#call setupUi method for MyQMainWindowExt
myWindow.setupUi(qMainWindow) #Copy

#call methods for Signal and slots processing
#call show method to show Window
qMainWindow.show() #Copy
#start Event loop
app.exec() #Copy