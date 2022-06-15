# _*_ coding: utf-8 _*_
from .CustomLable import CustomLable


class WindDirectionLable(CustomLable):
    '''风向，风级'''
    def __init__(self, parent=None):
        super(WindDirectionLable, self).__init__(parent)


    def initLable(self) -> None:
        self.setObjectName("wind")
        self.setGeometry(70, 285, 100, 20)
        super(WindDirectionLable, self).initLable()
