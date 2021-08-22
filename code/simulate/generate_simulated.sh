#! /bin/bash

for c in 1/FRA 1/IRN 1/ITA 1/KOR 1/USA 2/CHN 2/ITA; do
    ./code/simulate/simulate_data.py \
	data/processed/adm${c}_processed.csv \
	> data/processed/adm${c}_simulated.csv
done
