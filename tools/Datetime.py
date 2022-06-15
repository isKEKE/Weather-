# _*_ config: utf-8 _*_
import time

class Datetime(object):
    _Month_Str = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    @staticmethod
    def now() -> str:
        return time.strftime("{} %d,%Y", time.localtime()).format(
            Datetime._Month_Str.get(time.localtime().tm_mon)
        )

if __name__ == "__main__":
    print(Datetime.now())