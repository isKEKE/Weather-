# _*_ coding: utf-8 _*_
import os
import pickle
from PyQt5.QtCore import QPoint
from config import POS_PATH

class CoorOper(object):
    '''路径读写'''
    @staticmethod
    def read() -> [list, None]:
        # 判读路径不存在返回None
        if not  os.path.exists(POS_PATH):
            return None

        with open(POS_PATH, "rb") as fp:
            return pickle.load(fp)


    @staticmethod
    def save(info: [QPoint, bool]) -> None:
        with open(POS_PATH, "wb") as fp:
            pickle.dump(info, fp)