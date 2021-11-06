# -*- coding:utf8 -*-
from PyQt4 import QtCore, QtGui, uic
import sys
formclass, baseclass = uic.loadUiType("1.ui")


class MyForm(baseclass, formclass):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.go.clicked.connect(self.cl)

    def cl(self):
        self.x1 = int(self.in1.text())
        self.x2 = int(self.in2.text())
        self.txt.setText(u"结果：" + str(self.x1 / self.x2) + u"\n" + u"余数：" + str(self.x1 % self.x2))


app = QtGui.QApplication(sys.argv)
myapp = MyForm()
myapp.show()
app.exec_()
