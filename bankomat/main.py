from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

from info import InfoWindow
from check import CheckWindow
from get_money import GetMoneyWindow
from send_money import SendMoneyWindow
from unblock import UnblockWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Bankomat")
        
        self.vmain_box =  QVBoxLayout()
        
        self.info_btn = QPushButton("Info")
        self.info_btn.clicked.connect(self.INFO)
        
        self.check_money_btn = QPushButton("Pulni tekshirish")
        self.check_money_btn.clicked.connect(self.CHECK)
        
        self.get_money_btn = QPushButton("Pul yechish")
        self.get_money_btn.clicked.connect(self.GET_MONEY)

        self.send_money_btn = QPushButton("Pul o'tqazish")
        self.send_money_btn.clicked.connect(self.SEND_MONEY)
        
        self.unblock_btn = QPushButton("Blockdan chiqarish")
        self.unblock_btn.clicked.connect(self.UNBLOCK)
        
        self.vmain_box.addWidget(self.info_btn)
        self.vmain_box.addWidget(self.check_money_btn)
        self.vmain_box.addWidget(self.get_money_btn)
        self.vmain_box.addWidget(self.send_money_btn)
        self.vmain_box.addWidget(self.unblock_btn)

        self.setLayout(self.vmain_box)
        
    def INFO(self):
        self.InfoWindow = InfoWindow()
    
    def CHECK(self):
        self.CheckWindow = CheckWindow()
    
    def GET_MONEY(self):
        self.GetMoney = GetMoneyWindow()
    
    def SEND_MONEY(self):
        self.SendMoney = SendMoneyWindow()
    
    def UNBLOCK(self):
        self.UnblockWindow = UnblockWindow()

app = QApplication([])
win = MainWindow()
win.show()
app.exec_()