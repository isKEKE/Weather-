# _*_ coding: utf-8 _*_
from PyQt5 import QtCore
from config import UPDATE_TIME
from tools import Datetime
from .modules import Request

class Timer(QtCore.QTimer):
    '''计时器'''
    def __init__(self, lableFuncSet:dict, parent=None):
        super(Timer, self).__init__(parent)
        self.lableFuncSet = lableFuncSet
        self.initTimer()


    def initTimer(self) -> None:
        '''初始化计时器'''
        self.start(UPDATE_TIME)
        # 开始更新信息
        self.updateWeather()
        # 绑定槽函数
        self.timeout.connect(self.updateWeather)


    def updateWeather(self) -> None:
        '''行为'''
        try:
            datas = Request.datas()
        except Exception:
            return
        
        if datas is None:
            return
        # 标题
        self.lableFuncSet["title_lable"](f"{Datetime.now()} Current Weather")
        # 当前温度
        self.lableFuncSet["temperature_lable"](datas.get("today_temperature"))
        # 当前天气
        self.lableFuncSet["weather_lable"](datas.get("today_weather"))
        # 天气图片
        self.lableFuncSet["weather_image_lable"](
            f"./img/{datas.get('today_weather')}.png")
        # 空气质量
        self.lableFuncSet["air_quality_lable"](
            f'''空气质量\t{datas.get("today_air_quality")}''')
        # 相对湿度
        self.lableFuncSet["relative_humidity_lable"](
            f'''相对湿度\t{datas.get(f"today_relative_humidity")}''')
        # 风向、风级
        self.lableFuncSet["wind_direction_lable"](
            f'''{datas.get("today_wind_direction")}\t{datas.get("today_wind_direction_level")}'''
        )



