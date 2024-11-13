from Ui.MyMultiplycationTable import Ui_MainWindow

from PyQt6 import QtCore, QtGui, QtWidgets

class MyMultiplycationTableExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton_DrawTable.clicked.connect(self.draw_table)

        # Tạo một QScrollArea và thiết lập nó để hiển thị Result QLabel
        self.scrollArea = QtWidgets.QScrollArea(self.MainWindow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setGeometry(70, 180, 481, 201)  # Kích thước và vị trí của QScrollArea
        self.Result.setParent(None)  # Loại bỏ Result khỏi parent cũ trước khi thêm vào scroll area
        self.scrollArea.setWidget(self.Result)
        self.Result.setStyleSheet("color: black; background-color: rgb(255, 255, 127);")  # Thiết lập màu chữ đen và giữ màu nền

    def draw_table(self):
        # Lấy giá trị từ QLineEdit
        try:
            n1 = int(self.lineEdit_N1.text())
            n2 = int(self.lineEdit_N2.text())
        except ValueError:
            self.Result.setText("Vui lòng nhập số hợp lệ cho N1 và N2!")
            return

        start = min(n1, n2)
        end = max(n1, n2)

        result_text = ""
        for i in range(1, 10):  # Lặp qua các số từ 1 đến 10
            for num in range(start, end + 1):
                result_text += f"{num} x {i} = {num * i}\t"  # Thêm kết quả vào cùng một dòng
            result_text += "\n"  # Xuống dòng sau mỗi hàng

        # Hiển thị kết quả
        self.Result.setText(result_text)



