from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

import json

class GetMoneyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.show()
        
        self.attemps = 3
        
        self.vmain_box = QVBoxLayout()
        self.edit1 = QLineEdit()
        self.edit1.setPlaceholderText("Karta raqamini kiriting...")
        
        self.edit2 = QLineEdit()
        self.edit2.setPlaceholderText("Karta parolini kiriting...")
        
        self.edit3 = QLineEdit()
        self.edit3.setPlaceholderText("Kerakli mablag'ni kiriting...")
        
        self.get_money = QPushButton("Pulni olish")
        self.get_money.clicked.connect(self.GET_MONEY)
        
        self.vmain_box.addWidget(self.edit1)
        self.vmain_box.addWidget(self.edit2)
        self.vmain_box.addWidget(self.edit3)
        self.vmain_box.addWidget(self.get_money)
        
        self.setLayout(self.vmain_box)
    
    def GET_MONEY(self):
        card_number = self.edit1.text()
        password = self.edit2.text()
        with open("data.json") as file:
            data = json.load(file)
        
        if data.get(card_number):
            if data[card_number]["password"] == password and int(data[card_number]["cash"]) - int(self.edit3.text()) >= 0:
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Information)
                info = data[card_number]
                
                with open("data.json", "w") as file:
                    data[card_number]["cash"] = str(int(data[card_number]["cash"]) - int(self.edit3.text()))
                    json.dump(data, file, indent=4)
                self.msg.setText(f"""Successfully✅""")
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
