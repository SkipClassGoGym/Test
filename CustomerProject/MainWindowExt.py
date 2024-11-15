import functools
from urllib.request import localhost

from PyQt6.QtWidgets import QPushButton

from CustomerProject.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.customer=[]
    def datasimulation(self):
        self.customer.append({"Ma":"Cus1", "Ten":"Obama", "Age":"59", "LoaiKH":"VIP"})
        self.customer.append({"Ma": "Cus2", "Ten": "Cẩm Đào", "Age": "50", "LoaiKH": "Normal"})
        self.customer.append({"Ma": "Cus3", "Ten": "Trump", "Age": "78", "LoaiKH": "VIP"})
        self.customer.append({"Ma": "Cus4", "Ten": "Putin", "Age": "67", "LoaiKH": "VIP"})
        self.customer.append({"Ma": "Cus5", "Ten": "Kim Jon Un", "Age": "45", "LoaiKH": "Normal"})
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()
    def showCustomerIntoUI(self):
        for customer in self.customer:
            ma=customer["Ma"]
            ten = customer["Ten"]
            tuoi = customer["Age"]
            loaiKH = customer["LoaiKH"]
            buttonCustomer=QPushButton()
            infor = f"Mã = {ma}, Tên = {ten}, Tuổi = {tuoi}"
            buttonCustomer.setText(infor)
            if loaiKH == "VIP":
                style = "background-color:pink; font size:15pt"
            else:
                style = "background-color:yellow; font size:15pt"
            buttonCustomer.setStyleSheet(style)
            self.verticalLayoutCustomer.addWidget(buttonCustomer)
            buttonCustomer.clicked.connect(functools.partial(self.show_detail,customer))
    def show_detail(self,customer):
        ma = customer["Ma"]
        ten = customer["Ten"]
        tuoi = customer["Age"]
        loaiKH = customer["LoaiKH"]
        self.lineEditMa.setText(ma)
        self.lineEditTen.setText(ten)
        self.lineEditTuoi.setText(tuoi)
        if loaiKH == "VIP":
            self.radioButtonVIP.setChecked(True)
            self.radioButtonPhoThong.setChecked(False)
        else:
            self.radioButtonVIP.setChecked(False)
            self.radioButtonPhoThong.setChecked(True)