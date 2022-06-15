# _*_ codnig: utf-8 _*_
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
# 背景部件
from widgets.background import Background
# 自定义控件
from widgets.lable import TitleLable
from widgets.lable import TemperatureLable
from widgets.lable import WeatherLable
from widgets.lable import CompanyLable
from widgets.lable import WeatherImageLable
from widgets.lable import WindDirectionLable
from widgets.lable import AirQualityLable
from widgets.lable import RelativeHumidityLable
from widgets.button import LockButton
from widgets.tray import TrayIcon
# 定时器
from core import Timer
# 全局热键
from core import Hotkey
# 坐标读写
from tools import CoorOper

'''
    {'code': 0,
     'data': {'today_air_quality': '120',
              'today_relative_humidity': '65%',
              'today_temperature': '7',
              'today_weather': '阴',
              'today_wind_direction': '东北风',
              'today_wind_direction_level': '3级'},
     'msg': 'success'}
'''

class WeatherUI(QtWidgets.QDialog):
    # 鼠标状态
    _Mouse_Flag = False
    # 相对坐标
    _Relative_Pos = None
    # 锁定状态
    _Move_Flag = True
    # 需变化的标签功能集
    _Lable_Func_Set = {}
    def __init__(self, parent=None):
        super(WeatherUI, self).__init__(parent)

        self.tray_icon = None
        self.lock_button = None
        self.title_lable = None
        self.temperature_lable = None
        self.company_lable = None
        self.weather_lable = None
        self.weather_image_lable = None
        self.air_quality_lable = None
        self.relative_humidity_lable =None
        self.wind_direction_lable = None
        self.timer = None
        self.hot_key = None

        self.initUI()
        self.initQss()


    def initUI(self) -> None:
        '''初始化UI'''
        # 窗口透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 背景
        self.setLayout(Background())
        # 无边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SplashScreen)
        # 添加部件
        self.addWidgets()
        # 窗口大小
        self.setFixedSize(250, 350)
        # 应用状态
        self.initAppStatus()
        # 展示
        self.show()


    def initQss(self) -> None:
        '''初始化Qss样式'''
        with open("./qss/style.qss", "r") as fp:
            self.setStyleSheet(fp.read())


    def initAppStatus(self) -> None:
        '''初始化应用状态'''
        info = CoorOper.read()
        if info is None:
            return
        # 设置应用坐标
        self.move(info[0])
        # 锁定状态
        if info[-1] == True:
            # 可移动
            self.lock_button.downIcon()
            self._Move_Flag = True
        else:
            # 不可移动
            self.lock_button.upQIcon()
            self._Move_Flag = False


    def addWidgets(self) -> None:
        '''添加部件'''
        # 图片图标
        self.tray_icon = TrayIcon(self)
        # 按钮锁
        self.lock_button = LockButton(self)
        # 动作
        self.lock_button.clicked.connect(self.locking)
        # 标题
        self.title_lable = TitleLable(self)
        self._Lable_Func_Set["title_lable"] = self.title_lable.setText
        # 当前温度
        self.temperature_lable = TemperatureLable(self)
        self._Lable_Func_Set["temperature_lable"] = self.temperature_lable.setText
        # 单位
        self.company_lable = CompanyLable(self)
        # 天气文本
        self.weather_lable = WeatherLable(self)
        self._Lable_Func_Set["weather_lable"] = self.weather_lable.setText
        # 天气图片
        self.weather_image_lable = WeatherImageLable(self)
        self._Lable_Func_Set["weather_image_lable"] = self.weather_image_lable.setImage
        # 空气质量
        self.air_quality_lable = AirQualityLable(self)
        self._Lable_Func_Set["air_quality_lable"] = self.air_quality_lable.setText
        # 相对湿度
        self.relative_humidity_lable = RelativeHumidityLable(self)
        self._Lable_Func_Set["relative_humidity_lable"] = self.relative_humidity_lable.setText
        # 风向、风级
        self.wind_direction_lable = WindDirectionLable(self)
        self._Lable_Func_Set["wind_direction_lable"] = self.wind_direction_lable.setText
        # 计数器
        self.timer = Timer(self._Lable_Func_Set)
        # 热键
        self.hot_key = Hotkey(self)
        self.hot_key.start()


    def locking(self) -> None:
        '''锁定窗口不可移动'''
        if self._Move_Flag == True:
            # 不可移动
            self.lock_button.upQIcon()
            self._Move_Flag = False
        else:
            # 可移动
            self.lock_button.downIcon()
            self._Move_Flag = True


    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        '''鼠标移动事件'''
        if Qt.LeftButton and self._Mouse_Flag and self._Move_Flag:
            self.move(a0.globalPos() - self._Relative_Pos)
            a0.accept()


    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        '''鼠标点击事件'''
        if a0.button() == Qt.LeftButton:
            self._Mouse_Flag = True
            # 获得相对坐标
            self._Relative_Pos = a0.globalPos() - self.pos()
            a0.accept()
            self.setCursor(QtGui.QCursor(Qt.ArrowCursor))


    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        '''鼠标松开事件'''
        self._Mouse_Flag = False
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))


    def quit(self) -> None:
        '''退出'''
        # 记录相应的坐标, 和窗口锁定状态
        CoorOper.save([self.pos(), self._Move_Flag])
        # 关闭功能
        Hotkey.stop(int(self.hot_key.currentThreadId()))
        self.timer.stop()
        self.tray_icon.setVisible(False)
        QtWidgets.qApp.quit()
        sys.exit()


    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        '''按钮按下事件'''
        # ESC关闭应用
        if a0.key() == Qt.Key_Escape:
            self.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    weatherUi = WeatherUI()
    sys.exit(app.exec_())

