from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QButtonGroup,QRadioButton,QPushButton

app = QApplication([])
window = QWidget()
window.setWindowTitle('Моё первое приложение!')
window.resize(600,350)
v_line = QVBoxLayout()
bnt1 = QRadioButton('1')
bnt2 = QRadioButton('2')
bnt3 = QRadioButton('3')
bnt4 = QPushButton('Проверить')
bnt1.setChecked(True)
button = QButtonGroup()
button.addButton(bnt1,id = 1)
button.addButton(bnt2,id = 2)
button.addButton(bnt3,id = 3)
v_line.addWidget(bnt1)
v_line.addWidget(bnt2)
v_line.addWidget(bnt3)
v_line.addWidget(bnt4,alignment = Qt.AlignCenter)
text = QLabel()
v_line.addWidget(text,alignment = Qt.AlignCenter)
def check():
    text.setText('Выбранная кнопка:'+ str(button.checkedId()))
bnt4.clicked.connect(check)


    
    






window.setLayout(v_line)

window.show()
app.exec_()



