from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

import json

class CheckWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.show()
        
        self.attemps = 3
        
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
        self.setFixedSize(150, 100)
    
    def CHECK(self):
        card_number = self.edit1.text()
        password = self.edit2.text()
        with open("data.json") as file:
            data = json.load(file)
            if data.get(card_number):
                if data[card_number]["password"] == password:
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Information)
                    self.msg.setText(f"""
Hisobingiz: {data[card_number]["cash"]} USZ""")
                    self.msg.exec_()
                else:
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Warning)
                    self.msg.setText("Parol notog'ri")
                    self.attemps -= 1
                    if not self.attemps:
                        with open("data.json", "w") as file:
                            data[card_number]["status"] = "False"
                            json.dump(data, file, indent=4)
                            self.msg.setText("Karta raqam bloklandi")
                    self.msg.exec_()
                    
            else:
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.setText("Ma'lumot topilmadi")
                self.msg.exec_()