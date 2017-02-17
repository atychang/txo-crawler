import datetime
import io
import pandas as pd
import requests

import database


class Rawdata():
    def __init__(self):
        self._url = "http://www.taifex.com.tw/chinese/3/3_2_3_b.asp"
        # must be fill
        # 1. DATA_DATE: 2016/07/20
        # 2. DATA_DATE1: 2016/07/25
        # 3. datestart: 2016/07/20
        # 4. dateend: 2016/07/25
        self._data = {
            'goday': '',
            'DATA_DATE': '',
            'DATA_DATE1': '',
            'DATA_DATE_Y': '',
            'DATA_DATE_M': '',
            'DATA_DATE_D': '',
            'DATA_DATE_Y1': '',
            'DATA_DATE_M1': '',
            'DATA_DATE_D1': '',
            'syear': '',
            'smonth': '',
            'sday': '',
            'syear1': '',
            'smonth1': '',
            'sday1': '',
            'datestart': '',
            'dateend': '',
            'COMMODITY_ID': 'TXO',
            'commodity_id2t': '',
            'his_year': ''
        }
        self._db = database.Database()

    @property
    def date_recorded(self):
        sql = ("SELECT `record_date` FROM `crawler_config` "
               "WHERE `table_name`='rawdata'")
        self._date_recorded = self._db.query_from_mysql(sql)[0][0]
        return self._date_recorded

    @date_recorded.setter
    def date_recorded(self, date_recorded):
        sql = ("UPDATE `crawler_config` SET `record_date`='{}' "
               "WHERE `table_name`='{}'")
        self._db.update_mysql(sql.format(date_recorded, 'rawdata'))
        self._date_recorded = date_recorded

    def crawler(self):
        today = datetime.datetime.today()
        mdate = self.date_recorded
        sql = ("INSERT INTO `rawdata` VALUES (null, %s, %s, TRIM(%s), %s, %s,"
               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        while mdate <= today:
            date = mdate.strftime("%Y/%m/%d")
            self._data['DATA_DATE'] = date
            self._data['DATA_DATE1'] = date
            self._data['datestart'] = date
            self._data['dateend'] = date
            res = requests.post(self._url, data=self._data)
            # not trade date
            try:
                content = res.content.decode('big5')
            except:
                self.date_recorded += datetime.timedelta(1)
                mdate = self.date_recorded
                continue
            csv = pd.read_csv(io.StringIO(content))
            for index, row in csv.iterrows():
                # checks if the row[-1] is a NaN
                # row[-1] is column `suspend_trading`
                if row[-1] != row[-1]:
                    row[-1] = ''
                self._db.insert_into_mysql(sql, tuple(row))
                print(tuple(row))
            self.date_recorded += datetime.timedelta(1)
            mdate = self.date_recorded


rawdata = Rawdata()
rawdata.crawler()
