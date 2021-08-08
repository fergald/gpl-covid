#! /bin/bash -xe

for f in $(ls code/models/alt_growth_rates/???_adm?-*.do); do
    code/statab.sh do "$f"
done
