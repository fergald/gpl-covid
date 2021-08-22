#! /bin/bash -e

rm *.log
./code/run_simulated.sh
tar -zcvf ../gpl-covid-logs.tgz *.log
