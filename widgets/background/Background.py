# _*_ coding: utf-8 _*_
from PyQt5 import QtWidgets

class Background(QtWidgets.QVBoxLayout):
    '''背景'''
    def __init__(self, parent=None):
        super(Background, self).__init__(parent)
        self.initBG()


    def initBG(self) -> None:
        self.setContentsMargins(0, 0, 0, 0)
        # 透明度
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.5)
        # 背景部件
        bg = QtWidgets.QWidget()
        bg.setObjectName("bg")
        bg.setGraphicsEffect(op)
        # 添加部件
        self.addWidget(bg)