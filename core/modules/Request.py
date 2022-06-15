# _*_ coding: utf-8 _*_
import requests

class Request(object):
    _api = None
    if _api is None:
        raise AttributeError("请先填写提供数据的web服务API。")
    @staticmethod
    def datas() -> dict:
        ...


if __name__ == "__main__":
    ...
