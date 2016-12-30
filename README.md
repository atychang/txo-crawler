# txo-crawler

A cralwer for txo written in python3

### Python3 requirements (using virtualenv)
```bash
$ virtualenv --python=python3 .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

### MySQL connection config
You need create a txt file named 'connectors.cnf' and add connect information like:
```
[client]
host        = XXX.XXX.XXX.XXX
user        = username
password    = password
database    = txo
```

### Useage
```bash
# in virtualenv
(.env) $ python taiex.py
(.env) $ python option.py
(.env) $ python rawdata.py
(.env) $ deactivate
```

### Database tables
* options: 最後結算價
* rawdata: 選擇權每日交易行情
* taiex: 加權股價指數歷史資料
* trading_days: 交易日
* config: 記錄該從哪一天開始爬資料

### Config default date
* options: 2002-01-17
* rawdata: 2001-12-24
* taiex: 1999-01-05
