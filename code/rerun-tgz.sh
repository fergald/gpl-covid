#! /bin/bash -e

rm *.log || true
./code/run_all_countries.sh
tar -zcvf ../gpl-covid-logs.tgz *.log
