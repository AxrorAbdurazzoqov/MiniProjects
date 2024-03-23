from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

import json

class InfoWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.show()
        
        self.vmain_box = QVBoxLayout()
        self.edit1 = QLineEdit()
        self.edit1.setPlaceholderText("Karta raqamini kiriting...")
        
        self.edit2 = QLineEdit()
        self.edit2.setPlaceholderText("Karta parolini kiriting...")
        
        self.check_btn = QPushButton("Tekshirish")
        self.check_btn.clicked.connect(self.CHECK)
        
        self.vmain_box.addWidget(self.edit1)
        self.vmain_box.addWidget(self.edit2)
        self.vmain_box.addWidget(self.check_btn)
        
        self.setLayout(self.vmain_box)
    
    def CHECK(self):
        card_number = self.edit1.text()
        password = self.edit2.text()
        with open("data.json") as file:
            data = json.load(file)
            if data.get(card_number):
                if data[card_number]["password"] == password:
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Information)
                    info = data[card_number]
                    self.msg.setText(f"""{info["name"]}
{card_number}
{info["password"]}""")
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
            