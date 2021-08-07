#! /bin/bash -xe

for npi in pck_social_distance school_closure_popw national_lockdown; do 
    code/statab.sh do ./code/models/alt_growth_rates/FRA_adm1-$npi.do
done
