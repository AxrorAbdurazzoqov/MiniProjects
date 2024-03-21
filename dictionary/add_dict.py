from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

import json

class Add_CLS(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("add word")

        self.v_main_lay = QVBoxLayout()
        self.v_edit_lay = QVBoxLayout()
        self.h_btn_edit_lay = QHBoxLayout()

        self.eng_edit = QLineEdit()
        self.eng_edit.setPlaceholderText("ENG...")

        self.uz_edit = QLineEdit()
        self.uz_edit.setPlaceholderText("UZ...")

        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.OK)

        self.menu_btn = QPushButton("MENU")
        self.menu_btn.clicked.connect(self.hide)

        self.lbl = QLabel()

        self.v_edit_lay.addWidget(self.eng_edit)
        self.v_edit_lay.addWidget(self.uz_edit)

        self.h_btn_edit_lay.addWidget(self.btn)
        self.h_btn_edit_lay.addLayout(self.v_edit_lay)

        self.v_main_lay.addLayout(self.h_btn_edit_lay)
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addWidget(self.menu_btn)

        self.setLayout(self.v_main_lay)

    def OK(self):
        a = self.eng_edit.text()
        b = self.uz_edit.text()
            
        data = None
        with open('data.json') as file:
            data = json.load(file)
            
        if len(a) and len(b) and a != ' ' and b != ' ':
            if data.get(a):
                self.lbl.setStyleSheet("background-color:yellow;font-size:20px")
                self.lbl.setText("This word already exists")
            else:
                with open("data.json", "w") as file:
                    data[a] = b
                    json.dump(data, file, indent=2, sort_keys=True)
                    self.lbl.setStyleSheet("background-color:lightgreen;font-size:20px")
                    self.lbl.setText("Successfully ✅")
        else:
            self.lbl.setStyleSheet("background-color:red;font-size:20px")
            self.lbl.setText("Fields are empty ⁉️")
        self.lbl.adjustSize()
        self.eng_edit.clear()
        self.uz_edit.clear()