from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel

import json

class SendMoneyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.show()
        
        self.vmain_box = QVBoxLayout()
        
        self.lbl1 = QLabel("Pul o'tqazuvchining karta raqamini kiriting: ")
        self.lbl2 = QLabel("Pul o'tqazuvchining karta raqami kodini kiriting: ")
        self.lbl3 = QLabel("Pul qabul qiluvchining karta raqamini kiriting: ")
        self.lbl4 = QLabel("Summani kiriting: ")
        
        
        self.edit1 = QLineEdit()
        self.edit1.setPlaceholderText("Karta raqamini kiriting...")
        
        self.edit2 = QLineEdit()
        self.edit2.setPlaceholderText("Karta kodini kiriting...")
        
        self.edit3 = QLineEdit()
        self.edit3.setPlaceholderText("Karta raqamini kiriting...")
        
        self.edit4 = QLineEdit()
        self.edit4.setPlaceholderText("Summani kiriting: ")
        
        self.get_money = QPushButton("Tasdiqlash")
        self.get_money.clicked.connect(self.SEND_MONEY)
    
        self.vmain_box.addWidget(self.lbl1)
        self.vmain_box.addWidget(self.edit1)
        self.vmain_box.addWidget(self.lbl2)
        self.vmain_box.addWidget(self.edit2)
        self.vmain_box.addWidget(self.lbl3)
        self.vmain_box.addWidget(self.edit3)
        self.vmain_box.addWidget(self.lbl4)
        self.vmain_box.addWidget(self.edit4)
        self.vmain_box.addWidget(self.get_money)
        
        self.setLayout(self.vmain_box)
    
    def SEND_MONEY(self):
        card_number = self.edit1.text()
        password = self.edit2.text()
        card_number2 = self.edit3.text()
        summa = int(self.edit4.text())
        with open("data.json") as file:
            data = json.load(file)
        
        if data.get(card_number):
            if data[card_number]["password"] == password:
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Information)
                
                with open("data.json", "w") as file:
                    data[card_number]["cash"] = str(int(data[card_number]["cash"]) - int(self.edit4.text()))
                    data[card_number2]["cash"] = str(int(data[card_number2]["cash"]) + int(self.edit4.text()))
                    json.dump(data, file, indent=4)
                self.msg.setText(f"""Muaffiyaqatli ✅""")
                self.msg.exec_()
            else:
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.setText("Parol notog'ri")
                self.msg.exec_()
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Ma'lumot topilmadi")
            self.msg.exec_()
            