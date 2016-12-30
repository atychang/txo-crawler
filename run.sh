#!/bin/bash

source .env/bin/activate

python taiex.py >>log.txt 2>&1
python option.py >>log.txt 2>&1
python rawdata.py >>log.txt 2>&1

deactivate
