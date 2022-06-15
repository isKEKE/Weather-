# _*_ coding: utf-8 _*_
import ctypes
import ctypes.wintypes
import win32con
import threading
from config import KEY_ALT
from config import KEY_D
from config import KEY_ID

user32 = ctypes.windll.user32

class HotKeyThread(threading.Thread):
    flag = True
    def __init__(self, callback=None):
        super(HotKeyThread, self).__init__()
        self.callback = callback
        # 消息盒子
        self.msg = ctypes.wintypes.MSG()

    def run(self) -> None:
        '''运行'''
        # 注册热键
        user32.RegisterHotKey(None, KEY_ID, KEY_ALT, KEY_D)

        # 消息循环
        while True:
            if HotKeyThread.flag == False:
                break

            if user32.GetMessageA(ctypes.byref(self.msg), None, 0, 0) == 0:
                continue

            if self.msg.message == win32con.WM_HOTKEY:
                if self.msg.wParam == KEY_ID:
                    # 执行
                    self.callback()

            # 该函数将虚拟键消息转换为字符消息。字符消息被寄送到调用线程的消息队列里，
            # 当下一次线程调用函数GetMessage或PeekMessage时被读出。
            user32.TranslateMessage(ctypes.byref(self.msg))
            user32.DispatchMessageA(ctypes.byref(self.msg))


    def stop(self) -> None:
        '''停止线程'''
        # 线程状态
        HotKeyThread.flag = False
        # 释放热键
        user32.UnregisterHotKey(None, KEY_ID)
        # 线程ID
        tid = ctypes.c_long(self.ident)
        # 往线程消息队列发送自定义消息
        user32.PostThreadMessageA(
            tid, win32con.WM_HOTKEY, 0, 0
        )


if __name__ == "__main__":
    hotkey = HotKeyThread()
    hotkey.start()
    while True:
        if input(">>>") == "q":
            hotkey.stop()
            break
