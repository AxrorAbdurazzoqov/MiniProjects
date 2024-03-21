from PyQt5.QtWidgets import QApplication

from search_main_window import SearchWindow

app = QApplication([])
win = SearchWindow()
win.show()
app.exec_()