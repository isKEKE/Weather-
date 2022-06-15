# _*_ coding: utf-8 _*_
from PyQt5 import QtCore
from .modules import HotKeyThread

class Hotkey(QtCore.QThread):
    '''全局热键'''
    _Flag = True
    def __init__(self, parent=None):
        super(Hotkey, self).__init__(parent)
        self._parent = parent
        self.hotkey_thread = None


    def showWindow(self) -> None:
        self._parent.showNormal()
        self._parent.activateWindow()


    def run(self) -> None:
        '''运行'''
        self.hotkey_thread = HotKeyThread(self.showWindow)
        self.hotkey_thread.start()
        self.hotkey_thread.join()


    def stop(self) -> None:
        self.hotkey_thread.stop()



