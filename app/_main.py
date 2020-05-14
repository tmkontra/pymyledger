from PyQt5.QtWidgets import (
    QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListView, QCheckBox, QLineEdit,
    QFrame
)

from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


from model import my_profile

app = QApplication([])

def static_list():
    static = QVBoxLayout()
    slabel = QLabel("Static")
    slabel.setFont(bold)
    slabel.setMaximumHeight(20)
    static.addWidget(slabel)

    for s in my_profile.static:
        w = QHBoxLayout()
        w.addWidget(QLabel(s.name), 2)
    
        t = QLineEdit("amount")
        t.setText(str(s.amount))
        t.setAlignment(Qt.AlignCenter)
        w.addWidget(t, 2, Qt.AlignCenter)

        cb = QCheckBox("paid?")
        if s.paid:
            cb.setChecked()
        w.addWidget(cb, 1, Qt.AlignRight)

        static.addItem(w)
        hline = QFrame()
        hline.setFrameShape(QFrame.HLine)
        static.addWidget(hline)

    return static

def variable_list():
    variable = QVBoxLayout()
    vlabel = QLabel("Variable")
    vlabel.setFont(bold)
    vlabel.setMaximumHeight(20)
    variable.addWidget(vlabel)

    for s in my_profile.variable:
        w = QHBoxLayout()
        w.addWidget(QLabel(s.name), 2)

        t = QLineEdit("amount")
        t.setText(str(s.amount))
        t.setAlignment(Qt.AlignCenter)
        w.addWidget(t, 1)
        variable.addItem(w)
        hline = QFrame()
        hline.setFrameShape(QFrame.HLine)
        variable.addWidget(hline)

    return variable

window = QWidget()

columns = QHBoxLayout()

bold = QFont()
bold.setBold(True)
bold.setUnderline(True)

static = static_list()

variable = variable_list()

columns.addItem(static)
v = QFrame()
v.setFrameShape(QFrame.VLine)
columns.addWidget(v)
columns.addItem(variable)

window.setLayout(columns)
window.setWindowTitle("Account Keeper")
window.setMinimumWidth(600)
window.show()

app.exec()
