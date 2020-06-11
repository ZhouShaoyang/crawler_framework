#! /bin/bash

ROOT=$(cd "$(dirname "$0")";pwd)
PYTHON="${ROOT}/venv/bin/python"
INDEX="${ROOT}/bin/index.py"
DETAIL="${ROOT}/bin/detail.py"

echo '[DETECT] - crawler'
ps -ef|grep ${PYTHON}|grep -v grep
if [ $? -eq 0 ]
then
    echo '[KILL] - old crawler'
    ps -ef|grep ${PYTHON}|grep -v grep|cut -c 9-15|xargs kill -9
    sleep 5
else
    echo '[KILL] - old crawler'
fi

echo '[START] - crawler index'
nohup ${PYTHON} ${INDEX} > /dev/null 2>&1 &
echo '[WAITING FOR SET REDIS] - 60s...'
sleep 60
echo '[START] - crawler detail'
nohup ${PYTHON} ${DETAIL} > /dev/null 2>&1 &
