from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel

import json
from random import randint

class UnblockWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.show()
        
        self.sms_code = None
        
        self.vmain_box = QVBoxLayout()
        
        self.lbl1 = QLabel("Karta raqamini kiriting: ")
        self.lbl2 = QLabel("Karta ulangan raqamini kiriting: ")
        self.lbl3 = QLabel("Raqamga yuborilgan kodni kiriting: ")
        
        self.edit1 = QLineEdit()
        self.edit1.setPlaceholderText("Karta raqamini kiriting...")
        
        self.edit2 = QLineEdit()
        self.edit2.setPlaceholderText("Karta ulangan raqamni kiriting...")
        
        self.edit3 = QLineEdit()
        self.edit3.setPlaceholderText("Raqamga yuborilgan kiriting...")
        
        self.get_money = QPushButton("Tasdiqlash")
        self.get_money.clicked.connect(self.SEND_MONEY)
    
        self.vmain_box.addWidget(self.lbl1)
        self.vmain_box.addWidget(self.edit1)
        self.vmain_box.addWidget(self.lbl2)
        self.vmain_box.addWidget(self.edit2)
        self.vmain_box.addWidget(self.lbl3)
        self.vmain_box.addWidget(self.edit3)
        self.vmain_box.addWidget(self.get_money)
        
        self.setLayout(self.vmain_box)
    
    def SEND_MONEY(self):
        if not self.edit3.text():
            self.msg = QMessageBox()
            self.sms_code = str(randint(999, 9999))
            self.msg.setText(f"Sizning tasdiqlash kodingiz {self.sms_code}")
            self.msg.setIcon(QMessageBox.Information)
            self.get_money.setText("Blokdan chiqarish")
            self.msg.exec_()
            return
            
        card_number = self.edit1.text()
        phome_number = self.edit2.text()
        code = self.edit3.text()
        with open("data.json") as file:
            data = json.load(file)
        
        if data.get(card_number):
           
            if  self.sms_code == code:
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Information)
                with open("data.json", "w") as file:
                    data[card_number]["status"] = "True"
                    json.dump(data, file, indent=4)
                self.msg.setText(f"""Blokdan chiqarildi ✅""")
                self.msg.exec_()
            else:
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.setText("Tasdiqlash kodi notog'ri")
                self.msg.exec_()
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Ma'lumot topilmadi")
            self.msg.exec_()
            