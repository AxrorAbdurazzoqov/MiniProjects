from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QRadioButton, QListWidget
from PyQt5.QtGui import QIcon

import json

from words import List
from add_dict import Add_CLS

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Dictionary")
        self.setWindowIcon(QIcon("img.png"))
        
        self.vbox_main = QVBoxLayout()
        self.search_hbox = QHBoxLayout()
        
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("⌕‍")
        self.search_edit.setStyleSheet("font-size: 18px")
        
        self.eng_btn = QRadioButton()
        self.eng_btn.setText("eng")
        self.eng_btn.clicked.connect(lambda: self.search_edit.setPlaceholderText("Enter the word"))
        
        self.uzb_btn = QRadioButton()
        self.uzb_btn.setText("uzb")
        self.uzb_btn.clicked.connect(lambda: self.search_edit.setPlaceholderText("So'z kiriting"))
        
        self.search_hbox.addWidget(self.search_edit)
        self.search_hbox.addWidget(self.eng_btn)
        self.search_hbox.addWidget(self.uzb_btn)
        self.vbox_main.addLayout(self.search_hbox)
        
        self.words_wdg = QListWidget()
        self.vbox_main.addWidget(self.words_wdg)
        
        self.hbox_btn = QHBoxLayout()
        self.search_btn = QPushButton("search")
        self.search_btn.clicked.connect(self.SEARCH)
        self.listOfWords_btn = QPushButton("list of words")
        self.listOfWords_btn.clicked.connect(self.SHOW_WORDS)
        self.add_btn = QPushButton("add word")
        self.add_btn.clicked.connect(self.ADD_WORD)
        self.hbox_btn.addWidget(self.search_btn)
        self.hbox_btn.addWidget(self.listOfWords_btn)
        self.hbox_btn.addWidget(self.add_btn)
        self.vbox_main.addLayout(self.hbox_btn)
        
        self.setLayout(self.vbox_main)
           
    def SEARCH(self):
        self.words_wdg.clear()
        if not self.search_edit.text():
            self.words_wdg.addItems(["Empty field", "Ma'lumot taqdim etilmadi"])
            self.words_wdg.setStyleSheet("color: red")
        else:
            word = self.search_edit.text().lower()
            with open("data.json", 'r') as file:
                try:
                    data = json.load(file)
                    if self.eng_btn.isChecked():
                        self.words_wdg.addItem(data[word])
                        self.words_wdg.setStyleSheet("font-size: 20px")
                    elif self.uzb_btn.isChecked():
                        for key, value in data.items():
                            if value == word:
                                self.words_wdg.addItem(key)
                                self.words_wdg.setStyleSheet("font-size: 20px")
                                
                except:
                    self.words_wdg.addItem("Not found")
    
    def SHOW_WORDS(self):
        self.LIST = List()
        self.LIST.show()
    
    def ADD_WORD(self):
        self.add_cls = Add_CLS()
        self.add_cls.show()
        
