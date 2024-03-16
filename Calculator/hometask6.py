from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("img_calculator.png"))
        self.setGeometry(800, 250, 335, 500)
        
        # ******************************************** #
        
        # 1 - qator --> 0, ., =
        self.b0 = QPushButton('       0        ', self)
        self.b0.setStyleSheet("font-size: 30px")
        self.b0.move(10, 450)
        self.b0.clicked.connect(lambda: self.set_label('0'))
        
        self.dot = QPushButton('.', self)
        self.dot.setStyleSheet("font-size: 30px")
        self.dot.move(170, 450)
        self.dot.clicked.connect(lambda: self.set_dot())
        
        self.equal = QPushButton('=', self)
        self.equal.setStyleSheet("font-size: 30px; background-color: #4CC4FC")
        self.equal.move(250, 450)
        self.equal.clicked.connect(self.get_result)
        
        # 2 - qator --> 1, 2, 3, +
        self.b1 = QPushButton('1', self)
        self.b1.setStyleSheet("font-size: 30px")
        self.b1.move(10, 400)
        self.b1.clicked.connect(lambda: self.set_label('1'))
        
        self.b2 = QPushButton('2', self)
        self.b2.setStyleSheet("font-size: 30px")
        self.b2.move(90, 400)
        self.b2.clicked.connect(lambda: self.set_label('2'))
        
        self.b3 = QPushButton('3', self)
        self.b3.setStyleSheet("font-size: 30px")
        self.b3.move(170, 400)
        self.b3.clicked.connect(lambda: self.set_label('3'))
        
        self.plus = QPushButton('+', self)
        self.plus.setStyleSheet("font-size: 30px")
        self.plus.move(250, 400)
        self.plus.clicked.connect(lambda: self.set_operator('+'))
        
        # 3 - qator --> 4, 5, 6, -
        self.b4 = QPushButton('4', self)
        self.b4.setStyleSheet("font-size: 30px")
        self.b4.move(10, 350)
        self.b4.clicked.connect(lambda: self.set_label('4'))
        
        self.b5 = QPushButton('5', self)
        self.b5.setStyleSheet("font-size: 30px")
        self.b5.move(90, 350)
        self.b5.clicked.connect(lambda: self.set_label('5'))
        
        self.b6 = QPushButton('6', self)
        self.b6.setStyleSheet("font-size: 30px")
        self.b6.move(170, 350)
        self.b6.clicked.connect(lambda: self.set_label('6'))
        
        self.minus = QPushButton('-', self)
        self.minus.setStyleSheet("font-size: 30px")
        self.minus.move(250, 350)
        self.minus.clicked.connect(lambda: self.set_operator('-'))
        
        # 4 - qator --> 7, 8, 9, ×
        self.b7 = QPushButton('7', self)
        self.b7.setStyleSheet("font-size: 30px")
        self.b7.move(10, 300)
        self.b7.clicked.connect(lambda: self.set_label('7'))
        
        self.b8 = QPushButton('8', self)
        self.b8.setStyleSheet("font-size: 30px")
        self.b8.move(90, 300)
        self.b8.clicked.connect(lambda: self.set_label('8'))
        
        self.b9 = QPushButton('9', self)
        self.b9.setStyleSheet("font-size: 30px")
        self.b9.move(170, 300)
        self.b9.clicked.connect(lambda: self.set_label('9'))
        
        self.multiply = QPushButton('×', self)
        self.multiply.setStyleSheet("font-size: 30px")
        self.multiply.move(250, 300)
        self.multiply.clicked.connect(lambda: self.set_operator('×'))
        
        # 4 - qator --> ¹⁄x, x², √x, ÷
        self.division = QPushButton('÷', self)
        self.division.setStyleSheet("font-size: 30px")
        self.division.move(250, 250)
        self.division.clicked.connect(lambda: self.set_operator('÷'))
        
        self.square = QPushButton('√x', self)
        self.square.setStyleSheet("font-size: 30px")
        self.square.move(170, 250)
        self.square.clicked.connect(self.get_square)
        
        self.pow2 = QPushButton('x²', self)
        self.pow2.setStyleSheet("font-size: 30px")
        self.pow2.move(90, 250)
        self.pow2.clicked.connect(self.get_pow2)
        
        self.btn = QPushButton('¹⁄x', self)
        self.btn.setStyleSheet("font-size: 30px")
        self.btn.move(10, 250)
        self.btn.clicked.connect(lambda: 1/int(self.label.text()))
        self.btn.clicked.connect(self.get_btn)
        
        # 5 - qator --> %, CE, C, ⌫
        self.modulus = QPushButton('%', self)
        self.modulus.setStyleSheet("font-size: 30px")
        self.modulus.move(10, 200)
        self.modulus.clicked.connect(self.get_modulus)
        
        # dastur oynasini butunlay tozalaydi
        self.CE = QPushButton('CE', self)
        self.CE.setStyleSheet("font-size: 30px")
        self.CE.move(90, 200)
        self.CE.clicked.connect(self.set_CE)
        
        # foydalanuvchi kiritgan oynani tozalaydi
        self.C = QPushButton('C', self)
        self.C.setStyleSheet("font-size: 30px")
        self.C.move(170, 200)
        self.C.clicked.connect(self.set_C)
        
        self.clear = QPushButton('⌫', self)
        self.clear.setStyleSheet("font-size: 30px")
        self.clear.move(250, 200)
        self.clear.clicked.connect(self.set_clear)

        # ******************************************** #
        
        self.label = QLabel('0', self)
        self.label.setStyleSheet("font-size: 50px")
        self.label.move(10, 125)  
        
        self.operator = QLabel('', self)
        self.operator.setStyleSheet("font-size: 20px")
        self.operator.move(0, 100)
        
        self.label2 = QLabel("", self)
        self.label2.setStyleSheet("font-size: 40px")
        self.label2.move(10, 50)
        
        
    def set_label(self, digit):
        if len(self.label.text()) <= 10:
            if len(self.label.text())==1 and self.label.text() == '0':
                self.label.setText(digit)
                self.label.adjustSize()
            else: 
                self.label != '0'
                self.label.setText(self.label.text()+digit)
                self.label.adjustSize()
        
    def set_CE(self):
        self.label.setText('0')
        self.label.adjustSize()
        
    
    def set_C(self):
        self.label.setText('0')
        self.label.adjustSize()
        
        self.operator.setText('')
        self.operator.adjustSize()
        
        self.label2.setText('')
        self.label2.adjustSize()
        
    
    def set_clear(self):
        if len(self.label.text())<=1 or self.label.text()=="0 bo'linmaydi":
            self.set_CE()
        else:
            self.label.setText(self.label.text()[:-1])
            self.label.adjustSize()
    
    def set_operator(self, opr):
        self.operator.setText(opr)
        self.operator.adjustSize()
        self.label2.setText(self.label.text())
        self.label2.adjustSize()
        
        self.label.setText('0')
        self.label.adjustSize()
    
    def get_result(self):
        if len(self.label.text()) and len(self.operator.text()) and len(self.label2.text()):
            opr = {'+': '+', '-': '-', '×': '*', '÷': '/'}
            
            try:
                result = eval(f"{self.label2.text()}{opr[self.operator.text()]}{self.label.text()}")
                self.label.setText(str(round(result, 9)))
                self.label.adjustSize()
                
                self.label2.setText('')
                self.operator.setText('')
            except ZeroDivisionError:
                self.label.setText("0 bo'linmaydi")
                self.label.adjustSize()
    
    
    def set_dot(self):
        if '.' not in self.label.text():
            self.label.setText(self.label.text()+'.')
            self.label.adjustSize()
    
    def get_square(self):
        result = float((self.label.text()))**(1/2)
        self.label.setText(str(round(result, 5)))
        self.label.adjustSize()
    
    def get_btn(self):
        result = 1/int(self.label.text())
        self.label.setText(str(round(result, 5)))
        self.label.adjustSize()
    
    def get_pow2(self):
        result = int(self.label.text())**2
        self.label.setText(str(round(result, 5)))
        self.label.adjustSize()
    
    def get_modulus(self):
        result = int(self.label.text())/100
        self.label.setText(str(round(result, 5)))
        self.label.adjustSize()
        


app = QApplication([])
win = Calculator()

win.show()
app.exec_()