#! /bin/bash -xe

rm *.log || true
./code/run_all_countries.sh
TS=$(date "+%Y%m%d-%H%M%S")
TGZ=../gpl-covid-logs-$TS.tgz
tar -zcvf "$TGZ" *.log
if [ ! -z "$1" ]; then
    scp "$TGZ" $1:
fi
