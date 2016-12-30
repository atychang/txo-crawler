import datetime
import io
import pandas as pd
import requests

import database


class Option():
    def __init__(self):
        self._url = "https://www.taifex.com.tw/chinese/5/FSPDownload.asp"
        self._data = {
            'download': '1',
            'cateId': '',
            'syear': '',
            'smonth': '',
            'eyear': '',
            'emonth': '',
            'cate': '3'
        }
        self._db = database.Database()

    @property
    def date_recorded(self):
        sql = "SELECT `date` FROM `config` WHERE `table`='options'"
        self._date_recorded = self._db.query_from_mysql(sql)[0][0]
        return self._date_recorded

    @date_recorded.setter
    def date_recorded(self, date_recorded):
        sql = "UPDATE `config` SET `date`='{}' WHERE `table`='{}'"
        self._db.update_mysql(sql.format(date_recorded, 'options'))
        self._date_recorded = date_recorded

    def crawler(self):
        today = datetime.datetime.today()
        mdate = self.date_recorded
        sql = "INSERT INTO `options` VALUES (%s, %s, %s, %s, %s)"

        while mdate <= today:
            self._data['syear'] = str(mdate.year)
            self._data['smonth'] = str(mdate.month).zfill(2)
            self._data['eyear'] = str(mdate.year)
            self._data['emonth'] = str(mdate.month).zfill(2)

            res = requests.post(self._url, data=self._data)
            content = res.content.decode('big5')
            csv = pd.read_csv(io.StringIO(content))

            trade_date = None

            for index in reversed(csv.index):
                row = tuple(csv.loc[index])
                trade_date = row[0]
                trade_date = datetime.datetime.strptime(trade_date,
                                                        "%Y/%m/%d")
                expire_month = str(row[1])
                contract_type = row[2]
                
                if contract_type != 'TXO':
                    continue
                
                contract_name = row[3]
                settlement_price = float(row[4])
                if trade_date <= today and self.date_recorded <= trade_date:
                    self._db.insert_into_mysql(sql, (trade_date,
                                                     expire_month,
                                                     contract_type,
                                                     contract_name,
                                                     settlement_price))
                    self.date_recorded = trade_date
                    print(tuple(csv.loc[index]))

            self.date_recorded += datetime.timedelta(1)
            mdate = self.date_recorded

option = Option()
option.crawler()
