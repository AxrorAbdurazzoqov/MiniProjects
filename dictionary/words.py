from PyQt5.QtWidgets import QWidget, QListWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton

import json

class List(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("words")

        self.v_main_lay = QVBoxLayout()
        self.h_lbl_lay = QHBoxLayout()

        self.eng_lbl = QLabel("English")
        self.uz_lbl = QLabel("Uzbek")

        self.lst_wdg = QListWidget()
        with open("data.json", "r") as file:
            data = json.load(file)
            for key, value in data.items():
                self.lst_wdg.addItem(f"{key} - {value}")
            
        self.menu_btn = QPushButton("MENU")
        self.menu_btn.clicked.connect(self.hide)

        self.h_lbl_lay.addWidget(self.eng_lbl)
        self.h_lbl_lay.addStretch()
        self.h_lbl_lay.addWidget(self.uz_lbl)

        self.v_main_lay.addLayout(self.h_lbl_lay)
        self.v_main_lay.addWidget(self.lst_wdg)
        self.v_main_lay.addWidget(self.menu_btn)

        self.setLayout(self.v_main_lay)