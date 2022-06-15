# _*_ coding: utf-8 _*_
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

class LockButton(QtWidgets.QPushButton):
    _width = 20
    _height = 20
    _upIcon = QtGui.QIcon()
    _downIcon = QtGui.QIcon()
    _flag = True
    def __init__(self, parent=None):
        super(LockButton, self).__init__(parent)

        self._upIcon.addPixmap(QtGui.QPixmap("./img/上锁.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._downIcon.addPixmap(QtGui.QPixmap("./img/解锁.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.initButton()


    def initButton(self) -> None:
        '''初始化按钮'''
        self.setObjectName("lock")
        # 位置、大小
        self.setGeometry(228, 3, self._width, self._height)
        # 图标
        self.downIcon()



    def upQIcon(self) -> None:
        '''上锁图标'''
        self.setIcon(self._upIcon)
        self.setIconSize(QtCore.QSize(self._width, self._height))


    def downIcon(self) -> None:
        '''解锁图标'''
        self.setIcon(self._downIcon)
        self.setIconSize(QtCore.QSize(self._width, self._height))

