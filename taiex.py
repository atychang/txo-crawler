import datetime
import pandas as pd

import database


class Taiex():
    def __init__(self):
        self._url = ("http://www.twse.com.tw/ch/trading/indices/"
                     "MI_5MINS_HIST/MI_5MINS_HIST.php?myear={}&mmon={}")
        self._db = database.Database()

    @property
    def date_recorded(self):
        sql = "SELECT `date` FROM `config` WHERE `table`='taiex'"
        self._date_recorded = self._db.query_from_mysql(sql)[0][0]
        return self._date_recorded

    @date_recorded.setter
    def date_recorded(self, date_recorded):
        sql = "UPDATE `config` SET `date`='{}' WHERE `table`='{}'"
        self._db.update_mysql(sql.format(date_recorded, 'taiex'))
        self._date_recorded = date_recorded

    def crawler(self):
        today = datetime.datetime.today()
        mdate = self.date_recorded

        while mdate <= today:
            # in minguo calendar
            myear = str(int(mdate.year) - 1911)
            mmon = str(mdate.month).zfill(2)
            self.parse_page(myear, mmon, today)
            self.date_recorded += datetime.timedelta(1)
            mdate = self.date_recorded

    def parse_page(self, myear, mmon, today):
        table = pd.read_html(self._url.format(myear, mmon))
        table = table[-1]
        table = table.drop(table.columns[0:2], axis=0)

        for index, row in table.iterrows():
            trade_date = row[0].split('/')
            trade_date = '-'.join((str(int(trade_date[0]) + 1911),
                                  trade_date[1],
                                  trade_date[2]))
            trade_date = datetime.datetime.strptime(trade_date, "%Y-%m-%d")
            price_open = row[1]
            price_high = row[2]
            price_low = row[3]
            price_close = row[4]

            if trade_date <= today and self.date_recorded <= trade_date:
                sql = "INSERT INTO `taiex` VALUES (%s, %s, %s, %s, %s)"
                self._db.insert_into_mysql(sql, (trade_date, price_open,
                                                 price_high, price_low,
                                                 price_close))
                sql = "INSERT INTO `trading_days` VALUES (null, %s)"
                self._db.insert_into_mysql(sql, (trade_date))

                self.date_recorded = trade_date
                print(trade_date)

taiex = Taiex()
taiex.crawler()
