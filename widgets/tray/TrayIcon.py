# _*_ coding: utf-8 _*_
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import config


class TrayIcon(QtWidgets.QSystemTrayIcon):
    '''托盘图标'''
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self._parent = self.parent()
        self.initTrayIcon()
        self.show()


    def initTrayIcon(self):
        "设计托盘的菜单，这里我实现了一个二级菜单"
        self.menu = QtWidgets.QMenu()
        self.showAct = QtWidgets.QAction("&显示")
        self.showAct.triggered.connect(self.showWindow)

        self.quitAct = QtWidgets.QAction("&退出")
        self.quitAct.triggered.connect(self._parent.quit)

        self.menu.addAction(self.showAct)
        self.menu.addAction(self.quitAct)
        # 添加菜单
        self.setContextMenu(self.menu)
        # 设置图标
        self.setIcon(QtGui.QIcon(config.LOGO_PATH))


    def showWindow(self) -> None:
        '''显示应用'''
        self._parent.showNormal()
        self._parent.activateWindow()



