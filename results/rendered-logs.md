# CHN_adm2.log

```
. reghdfe D_l_active_cases emergency_declaration_L* travel_ban_local_L* home_is
> olation_L* testing_regime_change_* , absorb(i.adm12_id, savefe) cluster(t) re
> sid
(MWFE estimator converged in 1 iterations)

HDFE Linear regression                            Number of obs   =      3,669
Absorbing 1 HDFE group                            F(  21,     47) =    4205.85
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.5975
                                                  Adj R-squared   =     0.5821
                                                  Within R-sq.    =     0.5608
Number of clusters (t)       =         48         Root MSE        =     0.0728

                                     (Std. Err. adjusted for 48 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
emergency_~7 |  -.0115442   .0434681    -0.27   0.792    -.0989906    .0759023
emergency~14 |  -.1731809   .0456965    -3.79   0.000    -.2651104   -.0812513
emergency~21 |  -.2340776   .0465269    -5.03   0.000    -.3276776   -.1404775
emergency~28 |  -.2504335   .0467327    -5.36   0.000    -.3444477   -.1564194
emergency~70 |  -.2477916   .0473942    -5.23   0.000    -.3431364   -.1524469
travel_ban~7 |   .0150441   .0155422     0.97   0.338    -.0162227    .0463109
travel_ba~14 |  -.0091802   .0182836    -0.50   0.618    -.0459621    .0276017
travel_ba~21 |  -.0311922   .0235012    -1.33   0.191    -.0784705    .0160861
travel_ba~28 |  -.0476004   .0289415    -1.64   0.107    -.1058231    .0106224
travel_ba~70 |  -.0792491   .0381836    -2.08   0.043    -.1560645   -.0024337
home_isola~7 |  -.0290876   .0138749    -2.10   0.041    -.0570002    -.001175
home_isol~14 |  -.0212651   .0172094    -1.24   0.223     -.055886    .0133558
home_isol~21 |  -.0140919   .0213041    -0.66   0.512    -.0569502    .0287664
home_isol~28 |  -.0034785   .0266978    -0.13   0.897    -.0571876    .0502306
home_isol~70 |   .0349028   .0373555     0.93   0.355    -.0402467    .1100524
te~18jan2020 |    .487551   .0458448    10.63   0.000     .3953232    .5797787
te~28jan2020 |   .0652789   .0151059     4.32   0.000     .0348896    .0956681
tes~6feb2020 |  -.0389732   .0117854    -3.31   0.002    -.0626823   -.0152641
tes~3feb2020 |  -.0019536   .0020971    -0.93   0.356    -.0061724    .0022653
tes~0feb2020 |  -.0050039   .0019712    -2.54   0.015    -.0089695   -.0010383
testin~r2020 |  -.0058608   .0048913    -1.20   0.237    -.0157008    .0039792
       _cons |   .3094195   .0449108     6.89   0.000     .2190707    .3997684
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
    adm12_id |       115           0         115     |
-----------------------------------------------------+

```
# CHN_adm2-sim.log

```
. reghdfe D_l_active_cases emergency_declaration_L* travel_ban_local_L* home_is
> olation_L*, absorb(i.adm12_id, savefe) cluster(t) resid
(MWFE estimator converged in 1 iterations)

HDFE Linear regression                            Number of obs   =      3,551
Absorbing 1 HDFE group                            F(  15,     48) =      44.75
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.3605
                                                  Adj R-squared   =     0.3366
                                                  Within R-sq.    =     0.3120
Number of clusters (t)       =         49         Root MSE        =     0.1165

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
emergency_~7 |   -.197438   .0568653    -3.47   0.001    -.3117733   -.0831027
emergency~14 |  -.3742541   .0534466    -7.00   0.000    -.4817157   -.2667925
emergency~21 |  -.4265036   .0540383    -7.89   0.000    -.5351548   -.3178524
emergency~28 |  -.4336545   .0551667    -7.86   0.000    -.5445745   -.3227345
emergency~70 |  -.4174592   .0567301    -7.36   0.000    -.5315228   -.3033956
travel_ban~7 |   .0301714   .0179879     1.68   0.100    -.0059957    .0663386
travel_ba~14 |   .0093372   .0246053     0.38   0.706    -.0401351    .0588094
travel_ba~21 |  -.0112671      .0314    -0.36   0.721     -.074401    .0518668
travel_ba~28 |  -.0208162   .0389857    -0.53   0.596    -.0992021    .0575697
travel_ba~70 |  -.0401974   .0493188    -0.82   0.419    -.1393595    .0589646
home_isola~7 |  -.0550872   .0164499    -3.35   0.002     -.088162   -.0220124
home_isol~14 |  -.0549068   .0216976    -2.53   0.015    -.0985327    -.011281
home_isol~21 |  -.0380604    .026352    -1.44   0.155    -.0910445    .0149238
home_isol~28 |   .0296319   .0306765     0.97   0.339    -.0320473     .091311
home_isol~70 |   .1027605   .0413689     2.48   0.017     .0195828    .1859381
       _cons |   .5105748   .0507364    10.06   0.000     .4085623    .6125872
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
    adm12_id |       114           0         114     |
-----------------------------------------------------+

```
# FRA_adm1.log

```
. reghdfe D_l_cum_confirmed_cases pck_social_distance school_closure_popw natio
> nal_lockdown ///
>  , absorb(i.adm1_id i.dow, savefe) cluster(t) resid  
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        270
Absorbing 2 HDFE groups                           F(   3,     22) =      22.39
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.2845
                                                  Adj R-squared   =     0.2239
                                                  Within R-sq.    =     0.1861
Number of clusters (t)       =         23         Root MSE        =     0.1326

                                     (Std. Err. adjusted for 23 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
pck_social~e |  -.2309569   .0738442    -3.13   0.005    -.3841005   -.0778133
school_clo~t |   .0288132   .0477682     0.60   0.553    -.0702519    .1278783
national_l~n |   .0338409   .0537191     0.63   0.535    -.0775657    .1452476
       _cons |    .318286   .0236971    13.43   0.000     .2691411    .3674308
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        13           0          13     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# FRA_adm1-national_lockdown.log

```
. reghdfe D_l_cum_confirmed_cases national_lockdown, absorb(i.adm1_id i.dow, sa
> vefe) cluster(t) resid  
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        292
Absorbing 2 HDFE groups                           F(   1,     24) =      60.54
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.7665
                                                  Adj R-squared   =     0.7501
                                                  Within R-sq.    =     0.3075
Number of clusters (t)       =         25         Root MSE        =     0.0284

                                     (Std. Err. adjusted for 25 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
national_l~n |  -.0488984   .0062847    -7.78   0.000    -.0618694   -.0359274
       _cons |   .2017971   .0044219    45.64   0.000     .1926709    .2109234
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        13           0          13     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# FRA_adm1-pck_social_distance.log

```
. reghdfe D_l_cum_confirmed_cases pck_social_distance, absorb(i.adm1_id i.dow, 
> savefe) cluster(t) resid  
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        292
Absorbing 2 HDFE groups                           F(   1,     24) =     121.84
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.7818
                                                  Adj R-squared   =     0.7666
                                                  Within R-sq.    =     0.3530
Number of clusters (t)       =         25         Root MSE        =     0.0275

                                     (Std. Err. adjusted for 25 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
pck_social~e |  -.0529012   .0047925   -11.04   0.000    -.0627924   -.0430099
       _cons |   .2146431   .0040404    53.12   0.000     .2063041    .2229822
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        13           0          13     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# FRA_adm1-school_closure_popw.log

```
. reghdfe D_l_cum_confirmed_cases school_closure_popw, absorb(i.adm1_id i.dow, 
> savefe) cluster(t) resid  
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        292
Absorbing 2 HDFE groups                           F(   1,     24) =      78.65
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.7645
                                                  Adj R-squared   =     0.7480
                                                  Within R-sq.    =     0.3016
Number of clusters (t)       =         25         Root MSE        =     0.0286

                                     (Std. Err. adjusted for 25 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
school_clo~t |  -.0443824   .0050044    -8.87   0.000     -.054711   -.0340537
       _cons |   .2086796   .0046621    44.76   0.000     .1990574    .2183018
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        13           0          13     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# FRA_adm1-sim.log

```
. reghdfe D_l_cum_confirmed_cases pck_social_distance school_closure_popw natio
> nal_lockdown ///
>  testing_regime_*, absorb(i.adm1_id i.dow, savefe) cluster(t) resid  
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        292
Absorbing 2 HDFE groups                           F(   4,     24) =      32.87
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.7881
                                                  Adj R-squared   =     0.7708
                                                  Within R-sq.    =     0.3717
Number of clusters (t)       =         25         Root MSE        =     0.0272

                                     (Std. Err. adjusted for 25 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
pck_social~e |  -.0460369   .0139475    -3.30   0.003    -.0748232   -.0172506
school_clo~t |   -.011601   .0117259    -0.99   0.332    -.0358021    .0126002
national_l~n |   .0049318   .0094129     0.52   0.605    -.0144955    .0243592
testing~2020 |  -.0267931   .0081593    -3.28   0.003    -.0436332   -.0099531
       _cons |   .2165101   .0041097    52.68   0.000     .2080281    .2249921
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        13           0          13     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# FRA_adm1-sim-national_lockdown.log

```
. reghdfe D_l_cum_confirmed_cases national_lockdown, absorb(i.adm1_id i.dow, sa
> vefe) cluster(t) resid  
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        292
Absorbing 2 HDFE groups                           F(   1,     24) =      60.54
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.7665
                                                  Adj R-squared   =     0.7501
                                                  Within R-sq.    =     0.3075
Number of clusters (t)       =         25         Root MSE        =     0.0284

                                     (Std. Err. adjusted for 25 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
national_l~n |  -.0488984   .0062847    -7.78   0.000    -.0618694   -.0359274
       _cons |   .2017971   .0044219    45.64   0.000     .1926709    .2109234
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        13           0          13     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# FRA_adm1-sim-pck_social_distance.log

```
. reghdfe D_l_cum_confirmed_cases pck_social_distance, absorb(i.adm1_id i.dow, 
> savefe) cluster(t) resid  
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        292
Absorbing 2 HDFE groups                           F(   1,     24) =     121.84
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.7818
                                                  Adj R-squared   =     0.7666
                                                  Within R-sq.    =     0.3530
Number of clusters (t)       =         25         Root MSE        =     0.0275

                                     (Std. Err. adjusted for 25 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
pck_social~e |  -.0529012   .0047925   -11.04   0.000    -.0627924   -.0430099
       _cons |   .2146431   .0040404    53.12   0.000     .2063041    .2229822
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        13           0          13     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# FRA_adm1-sim-school_closure_popw.log

```
. reghdfe D_l_cum_confirmed_cases school_closure_popw, absorb(i.adm1_id i.dow, 
> savefe) cluster(t) resid  
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        292
Absorbing 2 HDFE groups                           F(   1,     24) =      78.65
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.7645
                                                  Adj R-squared   =     0.7480
                                                  Within R-sq.    =     0.3016
Number of clusters (t)       =         25         Root MSE        =     0.0286

                                     (Std. Err. adjusted for 25 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
school_clo~t |  -.0443824   .0050044    -8.87   0.000     -.054711   -.0340537
       _cons |   .2086796   .0046621    44.76   0.000     .1990574    .2183018
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        13           0          13     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# IRN_adm1.log

```
. reghdfe D_l_cum_confirmed_cases p_* testing_regime_*, absorb(i.adm1_id i.dow,
>  savefe) cluster(date) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        548
Absorbing 2 HDFE groups                           F(   3,     20) =      39.20
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.2886
                                                  Adj R-squared   =     0.2340
                                                  Within R-sq.    =     0.2412
Number of clusters (date)    =         21         Root MSE        =     0.1717

                                  (Std. Err. adjusted for 21 clusters in date)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.3338397   .0885299    -3.77   0.001    -.5185098   -.1491696
         p_2 |  -.1536023   .0329961    -4.66   0.000    -.2224309   -.0847736
testing~2020 |  -.0748997   .0955015    -0.78   0.442    -.2741124     .124313
       _cons |   .5243126   .0547953     9.57   0.000     .4100117    .6386135
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        31           0          31     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# IRN_adm1-p_1.log

```
. reghdfe D_l_cum_confirmed_cases p_1, absorb(i.adm1_id i.dow, savefe) cluster(
> date) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        583
Absorbing 2 HDFE groups                           F(   1,     21) =      81.98
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.6213
                                                  Adj R-squared   =     0.5955
                                                  Within R-sq.    =     0.2587
Number of clusters (date)    =         22         Root MSE        =     0.0310

                                  (Std. Err. adjusted for 22 clusters in date)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.1458022    .016103    -9.05   0.000    -.1792902   -.1123143
       _cons |   .2879468   .0124496    23.13   0.000     .2620564    .3138372
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        31           0          31     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# IRN_adm1-p_2.log

```
. reghdfe D_l_cum_confirmed_cases p_2, absorb(i.adm1_id i.dow, savefe) cluster(
> date) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        583
Absorbing 2 HDFE groups                           F(   1,     21) =      53.12
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.6522
                                                  Adj R-squared   =     0.6286
                                                  Within R-sq.    =     0.3193
Number of clusters (date)    =         22         Root MSE        =     0.0297

                                  (Std. Err. adjusted for 22 clusters in date)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_2 |  -.0412125   .0056543    -7.29   0.000    -.0529714   -.0294537
       _cons |   .1935692   .0054403    35.58   0.000     .1822555    .2048829
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        31           0          31     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# IRN_adm1-sim.log

```
. reghdfe D_l_cum_confirmed_cases p_*, absorb(i.adm1_id i.dow, savefe) cluster(
> date) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        583
Absorbing 2 HDFE groups                           F(   2,     21) =      97.58
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.7240
                                                  Adj R-squared   =     0.7047
                                                  Within R-sq.    =     0.4597
Number of clusters (date)    =         22         Root MSE        =     0.0265

                                  (Std. Err. adjusted for 22 clusters in date)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.1112358   .0144342    -7.71   0.000    -.1412534   -.0812182
         p_2 |  -.0338606   .0038829    -8.72   0.000    -.0419356   -.0257856
       _cons |   .2783815   .0111504    24.97   0.000     .2551929    .3015701
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        31           0          31     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# IRN_adm1-sim-p_1.log

```
. reghdfe D_l_cum_confirmed_cases p_1, absorb(i.adm1_id i.dow, savefe) cluster(
> date) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        583
Absorbing 2 HDFE groups                           F(   1,     21) =      81.98
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.6213
                                                  Adj R-squared   =     0.5955
                                                  Within R-sq.    =     0.2587
Number of clusters (date)    =         22         Root MSE        =     0.0310

                                  (Std. Err. adjusted for 22 clusters in date)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.1458022    .016103    -9.05   0.000    -.1792902   -.1123143
       _cons |   .2879468   .0124496    23.13   0.000     .2620564    .3138372
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        31           0          31     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# IRN_adm1-sim-p_2.log

```
. reghdfe D_l_cum_confirmed_cases p_2, absorb(i.adm1_id i.dow, savefe) cluster(
> date) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        583
Absorbing 2 HDFE groups                           F(   1,     21) =      53.12
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.6522
                                                  Adj R-squared   =     0.6286
                                                  Within R-sq.    =     0.3193
Number of clusters (date)    =         22         Root MSE        =     0.0297

                                  (Std. Err. adjusted for 22 clusters in date)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_2 |  -.0412125   .0056543    -7.29   0.000    -.0529714   -.0294537
       _cons |   .1935692   .0054403    35.58   0.000     .1822555    .2048829
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        31           0          31     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# ITA_adm2.log

```
. reghdfe D_l_cum_confirmed_cases p_*, absorb(i.adm2_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      2,898
Absorbing 2 HDFE groups                           F(   6,     39) =      48.64
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.2940
                                                  Adj R-squared   =     0.2640
                                                  Within R-sq.    =     0.2581
Number of clusters (t)       =         40         Root MSE        =     0.1249

                                     (Std. Err. adjusted for 40 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |    .144344    .067882     2.13   0.040     .0070398    .2816483
         p_2 |  -.1094957   .0701494    -1.56   0.127    -.2513863    .0323949
         p_3 |  -.3310829   .1372068    -2.41   0.021    -.6086098   -.0535559
         p_4 |  -.0835182   .0546016    -1.53   0.134    -.1939604    .0269241
         p_5 |  -.1212466   .0983225    -1.23   0.225    -.3201226    .0776293
         p_6 |    .047544   .0513758     0.93   0.360    -.0563733    .1514614
       _cons |    .371716   .0682814     5.44   0.000     .2336039    .5098282
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm2_id |       107           0         107     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# ITA_adm2-sim.log

```
. reghdfe D_l_cum_confirmed_cases p_*, absorb(i.adm2_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      3,143
Absorbing 2 HDFE groups                           F(   6,     39) =     107.64
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.6346
                                                  Adj R-squared   =     0.6204
                                                  Within R-sq.    =     0.6067
Number of clusters (t)       =         40         Root MSE        =     0.0307

                                     (Std. Err. adjusted for 40 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.0096929   .0157507    -0.62   0.542    -.0415517     .022166
         p_2 |   -.122784    .031839    -3.86   0.000    -.1871845   -.0583835
         p_3 |  -.0534041   .0256154    -2.08   0.044    -.1052162    -.001592
         p_4 |  -.0239565   .0119842    -2.00   0.053    -.0481969    .0002838
         p_5 |  -.0732575   .0157949    -4.64   0.000    -.1052058   -.0413092
         p_6 |   .0011367   .0108946     0.10   0.917    -.0208996     .023173
       _cons |   .3165513   .0300845    10.52   0.000     .2556996    .3774031
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm2_id |       107           0         107     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# ITA_adm2-sim-p1.log

```
. reghdfe D_l_cum_confirmed_cases p_1, absorb(i.adm2_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      2,898
Absorbing 2 HDFE groups                           F(   1,     39) =      37.13
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.1161
                                                  Adj R-squared   =     0.0803
                                                  Within R-sq.    =     0.0711
Number of clusters (t)       =         40         Root MSE        =     0.1396

                                     (Std. Err. adjusted for 40 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.2537176   .0416405    -6.09   0.000    -.3379434   -.1694917
       _cons |   .3759137   .0386674     9.72   0.000     .2977015    .4541258
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm2_id |       107           0         107     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# ITA_adm2-sim-p2.log

```
. reghdfe D_l_cum_confirmed_cases p_2, absorb(i.adm2_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      2,898
Absorbing 2 HDFE groups                           F(   1,     39) =       7.65
Statistics robust to heteroskedasticity           Prob > F        =     0.0086
                                                  R-squared       =     0.0676
                                                  Adj R-squared   =     0.0297
                                                  Within R-sq.    =     0.0201
Number of clusters (t)       =         40         Root MSE        =     0.1434

                                     (Std. Err. adjusted for 40 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_2 |  -.1998361   .0722574    -2.77   0.009    -.3459905   -.0536816
       _cons |   .3297228   .0712702     4.63   0.000     .1855653    .4738803
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm2_id |       107           0         107     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# ITA_adm2-sim-p3.log

```
. reghdfe D_l_cum_confirmed_cases p_3, absorb(i.adm2_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      2,898
Absorbing 2 HDFE groups                           F(   1,     39) =     186.43
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.2884
                                                  Adj R-squared   =     0.2595
                                                  Within R-sq.    =     0.2521
Number of clusters (t)       =         40         Root MSE        =     0.1253

                                     (Std. Err. adjusted for 40 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_3 |  -.4738772   .0347065   -13.65   0.000    -.5440777   -.4036767
       _cons |   .3086025   .0141645    21.79   0.000      .279952    .3372529
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm2_id |       107           0         107     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# ITA_adm2-sim-p4.log

```
. reghdfe D_l_cum_confirmed_cases p_4, absorb(i.adm2_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      2,898
Absorbing 2 HDFE groups                           F(   1,     39) =      67.50
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.1302
                                                  Adj R-squared   =     0.0949
                                                  Within R-sq.    =     0.0859
Number of clusters (t)       =         40         Root MSE        =     0.1385

                                     (Std. Err. adjusted for 40 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_4 |  -.1832581   .0223047    -8.22   0.000    -.2283737   -.1381426
       _cons |   .3034227   .0195489    15.52   0.000     .2638814     .342964
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm2_id |       107           0         107     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# ITA_adm2-sim-p5.log

```
. reghdfe D_l_cum_confirmed_cases p_5, absorb(i.adm2_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      2,898
Absorbing 2 HDFE groups                           F(   1,     39) =     159.25
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.2757
                                                  Adj R-squared   =     0.2463
                                                  Within R-sq.    =     0.2388
Number of clusters (t)       =         40         Root MSE        =     0.1264

                                     (Std. Err. adjusted for 40 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_5 |  -.2996527   .0237457   -12.62   0.000    -.3476829   -.2516225
       _cons |   .3753139   .0207702    18.07   0.000     .3333022    .4173256
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm2_id |       107           0         107     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# ITA_adm2-sim-p6.log

```
. reghdfe D_l_cum_confirmed_cases p_6, absorb(i.adm2_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      2,898
Absorbing 2 HDFE groups                           F(   1,     39) =     102.01
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.1726
                                                  Adj R-squared   =     0.1391
                                                  Within R-sq.    =     0.1305
Number of clusters (t)       =         40         Root MSE        =     0.1351

                                     (Std. Err. adjusted for 40 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_6 |  -.2545104   .0251992   -10.10   0.000    -.3054806   -.2035401
       _cons |   .2913951   .0159887    18.23   0.000     .2590549    .3237352
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm2_id |       107           0         107     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1.log

```
. reghdfe D_l_active_cases p_* testing_regime_change_*, absorb(i.adm1_id i.dow,
>  savefe) cluster(t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        595
Absorbing 2 HDFE groups                           F(   8,     48) =     190.65
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.2806
                                                  Adj R-squared   =     0.2423
                                                  Within R-sq.    =     0.2380
Number of clusters (t)       =         49         Root MSE        =     0.1200

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.0831519   .0376568    -2.21   0.032    -.1588659   -.0074379
         p_2 |  -.3038246   .1507523    -2.02   0.049    -.6069323   -.0007168
         p_3 |  -.1274557   .0464653    -2.74   0.009    -.2208805   -.0340309
         p_4 |     .02018   .0190416     1.06   0.295    -.0181057    .0584658
tes~0feb2020 |   .0742059   .0870075     0.85   0.398    -.1007345    .2491463
tes~9feb2020 |   .0399427   .0193272     2.07   0.044     .0010828    .0788025
tes~2mar2020 |  -.0103101   .0229372    -0.45   0.655    -.0564285    .0358083
tes~7mar2020 |  -.0387403   .0376728    -1.03   0.309    -.1144866     .037006
       _cons |   .3141452   .0934095     3.36   0.002     .1263328    .5019576
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        17           0          17     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-p_1.log

```
. reghdfe D_l_active_cases p_1, absorb(i.adm1_id i.dow, savefe) cluster(t) resi
> d
(MWFE estimator converged in 3 iterations)

HDFE Linear regression                            Number of obs   =        706
Absorbing 2 HDFE groups                           F(   1,     48) =      46.60
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.1713
                                                  Adj R-squared   =     0.1434
                                                  Within R-sq.    =     0.1109
Number of clusters (t)       =         49         Root MSE        =     0.1672

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.2033166    .029783    -6.83   0.000    -.2631992   -.1434339
       _cons |   .2185396   .0215752    10.13   0.000     .1751597    .2619195
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        17           0          17     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-p_2.log

```
. reghdfe D_l_active_cases p_2, absorb(i.adm1_id i.dow, savefe) cluster(t) resi
> d
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        706
Absorbing 2 HDFE groups                           F(   1,     48) =      62.37
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.2035
                                                  Adj R-squared   =     0.1766
                                                  Within R-sq.    =     0.1454
Number of clusters (t)       =         49         Root MSE        =     0.1639

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_2 |  -.4391511   .0556075    -7.90   0.000    -.5509574   -.3273448
       _cons |   .3846177   .0364372    10.56   0.000     .3113557    .4578797
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        17           0          17     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-p_3.log

```
. reghdfe D_l_active_cases p_3, absorb(i.adm1_id i.dow, savefe) cluster(t) resi
> d
(MWFE estimator converged in 3 iterations)

HDFE Linear regression                            Number of obs   =        706
Absorbing 2 HDFE groups                           F(   1,     48) =       0.02
Statistics robust to heteroskedasticity           Prob > F        =     0.8837
                                                  R-squared       =     0.0680
                                                  Adj R-squared   =     0.0366
                                                  Within R-sq.    =     0.0000
Number of clusters (t)       =         49         Root MSE        =     0.1773

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_3 |  -.0046645   .0317148    -0.15   0.884    -.0684313    .0591023
       _cons |   .1099857   .0102258    10.76   0.000     .0894252    .1305461
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        17           0          17     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-p_4.log

```
. reghdfe D_l_active_cases p_4, absorb(i.adm1_id i.dow, savefe) cluster(t) resi
> d
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        706
Absorbing 2 HDFE groups                           F(   1,     48) =       6.18
Statistics robust to heteroskedasticity           Prob > F        =     0.0164
                                                  R-squared       =     0.0766
                                                  Adj R-squared   =     0.0455
                                                  Within R-sq.    =     0.0092
Number of clusters (t)       =         49         Root MSE        =     0.1765

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_4 |  -.0552673   .0222236    -2.49   0.016    -.0999508   -.0105838
       _cons |   .1213262   .0133265     9.10   0.000     .0945315     .148121
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        17           0          17     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-sim.log

```
. reghdfe D_l_active_cases p_*, absorb(i.adm1_id i.dow, savefe) cluster(t) resi
> d
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        706
Absorbing 2 HDFE groups                           F(   4,     48) =      27.92
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.2340
                                                  Adj R-squared   =     0.2047
                                                  Within R-sq.    =     0.1782
Number of clusters (t)       =         49         Root MSE        =     0.1611

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.1598177   .0326565    -4.89   0.000     -.225478   -.0941574
         p_2 |  -.3005542   .0705621    -4.26   0.000    -.4424288   -.1586795
         p_3 |   .0726989   .0281114     2.59   0.013     .0161772    .1292207
         p_4 |   .0486916   .0120277     4.05   0.000     .0245082     .072875
       _cons |   .3684197   .0376389     9.79   0.000     .2927416    .4440978
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        17           0          17     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-sim-p_1.log

```
. reghdfe D_l_active_cases p_1, absorb(i.adm1_id i.dow, savefe) cluster(t) resi
> d
(MWFE estimator converged in 3 iterations)

HDFE Linear regression                            Number of obs   =        706
Absorbing 2 HDFE groups                           F(   1,     48) =      46.60
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.1713
                                                  Adj R-squared   =     0.1434
                                                  Within R-sq.    =     0.1109
Number of clusters (t)       =         49         Root MSE        =     0.1672

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.2033166    .029783    -6.83   0.000    -.2631992   -.1434339
       _cons |   .2185396   .0215752    10.13   0.000     .1751597    .2619195
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        17           0          17     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-sim-p_2.log

```
. reghdfe D_l_active_cases p_2, absorb(i.adm1_id i.dow, savefe) cluster(t) resi
> d
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        706
Absorbing 2 HDFE groups                           F(   1,     48) =      62.37
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.2035
                                                  Adj R-squared   =     0.1766
                                                  Within R-sq.    =     0.1454
Number of clusters (t)       =         49         Root MSE        =     0.1639

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_2 |  -.4391511   .0556075    -7.90   0.000    -.5509574   -.3273448
       _cons |   .3846177   .0364372    10.56   0.000     .3113557    .4578797
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        17           0          17     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-sim-p_3.log

```
. reghdfe D_l_active_cases p_3, absorb(i.adm1_id i.dow, savefe) cluster(t) resi
> d
(MWFE estimator converged in 3 iterations)

HDFE Linear regression                            Number of obs   =        706
Absorbing 2 HDFE groups                           F(   1,     48) =       0.02
Statistics robust to heteroskedasticity           Prob > F        =     0.8837
                                                  R-squared       =     0.0680
                                                  Adj R-squared   =     0.0366
                                                  Within R-sq.    =     0.0000
Number of clusters (t)       =         49         Root MSE        =     0.1773

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_3 |  -.0046645   .0317148    -0.15   0.884    -.0684313    .0591023
       _cons |   .1099857   .0102258    10.76   0.000     .0894252    .1305461
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        17           0          17     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-sim-p_4.log

```
. reghdfe D_l_active_cases p_4, absorb(i.adm1_id i.dow, savefe) cluster(t) resi
> d
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        706
Absorbing 2 HDFE groups                           F(   1,     48) =       6.18
Statistics robust to heteroskedasticity           Prob > F        =     0.0164
                                                  R-squared       =     0.0766
                                                  Adj R-squared   =     0.0455
                                                  Within R-sq.    =     0.0092
Number of clusters (t)       =         49         Root MSE        =     0.1765

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_4 |  -.0552673   .0222236    -2.49   0.016    -.0999508   -.0105838
       _cons |   .1213262   .0133265     9.10   0.000     .0945315     .148121
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        17           0          17     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# MASTER_run_all_reg.log

```
. reghdfe D_l_active_cases emergency_declaration_L* travel_ban_local_L* home_is
> olation_L* testing_regime_change_* , absorb(i.adm12_id, savefe) cluster(t) re
> sid
(MWFE estimator converged in 1 iterations)

HDFE Linear regression                            Number of obs   =      3,669
Absorbing 1 HDFE group                            F(  21,     47) =    4205.85
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.5975
                                                  Adj R-squared   =     0.5821
                                                  Within R-sq.    =     0.5608
Number of clusters (t)       =         48         Root MSE        =     0.0728

                                     (Std. Err. adjusted for 48 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
emergency_~7 |  -.0115442   .0434681    -0.27   0.792    -.0989906    .0759023
emergency~14 |  -.1731809   .0456965    -3.79   0.000    -.2651104   -.0812513
emergency~21 |  -.2340776   .0465269    -5.03   0.000    -.3276776   -.1404775
emergency~28 |  -.2504335   .0467327    -5.36   0.000    -.3444477   -.1564194
emergency~70 |  -.2477916   .0473942    -5.23   0.000    -.3431364   -.1524469
travel_ban~7 |   .0150441   .0155422     0.97   0.338    -.0162227    .0463109
travel_ba~14 |  -.0091802   .0182836    -0.50   0.618    -.0459621    .0276017
travel_ba~21 |  -.0311922   .0235012    -1.33   0.191    -.0784705    .0160861
travel_ba~28 |  -.0476004   .0289415    -1.64   0.107    -.1058231    .0106224
travel_ba~70 |  -.0792491   .0381836    -2.08   0.043    -.1560645   -.0024337
home_isola~7 |  -.0290876   .0138749    -2.10   0.041    -.0570002    -.001175
home_isol~14 |  -.0212651   .0172094    -1.24   0.223     -.055886    .0133558
home_isol~21 |  -.0140919   .0213041    -0.66   0.512    -.0569502    .0287664
home_isol~28 |  -.0034785   .0266978    -0.13   0.897    -.0571876    .0502306
home_isol~70 |   .0349028   .0373555     0.93   0.355    -.0402467    .1100524
te~18jan2020 |    .487551   .0458448    10.63   0.000     .3953232    .5797787
te~28jan2020 |   .0652789   .0151059     4.32   0.000     .0348896    .0956681
tes~6feb2020 |  -.0389732   .0117854    -3.31   0.002    -.0626823   -.0152641
tes~3feb2020 |  -.0019536   .0020971    -0.93   0.356    -.0061724    .0022653
tes~0feb2020 |  -.0050039   .0019712    -2.54   0.015    -.0089695   -.0010383
testin~r2020 |  -.0058608   .0048913    -1.20   0.237    -.0157008    .0039792
       _cons |   .3094195   .0449108     6.89   0.000     .2190707    .3997684
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
    adm12_id |       115           0         115     |
-----------------------------------------------------+

```
# USA_adm1.log

```
. reghdfe D_l_cum_confirmed_cases p_* testing_regime_*, absorb(i.adm1_id i.dow,
>  savefe) cluster(t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,238
Absorbing 2 HDFE groups                           F(  28,     33) =     564.17
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.2909
                                                  Adj R-squared   =     0.2392
                                                  Within R-sq.    =     0.2184
Number of clusters (t)       =         34         Root MSE        =     0.1285

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |   .0113248   .0352635     0.32   0.750    -.0604194    .0830689
         p_2 |  -.2458208   .0444524    -5.53   0.000    -.3362599   -.1553817
         p_3 |   -.061259   .0311536    -1.97   0.058    -.1246415    .0021234
         p_4 |  -.0265767    .086803    -0.31   0.761    -.2031788    .1500253
         p_5 |  -.0471569   .0170156    -2.77   0.009    -.0817754   -.0125384
         p_6 |   .0257595   .0306805     0.84   0.407    -.0366604    .0881794
         p_7 |  -.0083896   .0332199    -0.25   0.802    -.0759759    .0591968
         p_8 |  -.0546014   .0209646    -2.60   0.014    -.0972541   -.0119486
         p_9 |   .0075862   .0204509     0.37   0.713    -.0340215    .0491939
        p_10 |  -.0297405   .0173815    -1.71   0.096    -.0651034    .0056224
        p_11 |   .0485368   .0365211     1.33   0.193    -.0257659    .1228395
testing_re~Y |   -.137027   .0432725    -3.17   0.003    -.2250656   -.0489884
testing_r~CA |   -.020811    .023809    -0.87   0.388    -.0692508    .0276289
testing_re~C |   .1692347   .0421917     4.01   0.000      .083395    .2550744
testing_r~CT |   .1063851   .0399851     2.66   0.012     .0250349    .1877353
testing_re~V |   .2411289   .0385829     6.25   0.000     .1626315    .3196264
testing_r~UT |   -.161937   .0377304    -4.29   0.000    -.2387001   -.0851739
testing_r~IA |  -.2113128   .0242339    -8.72   0.000    -.2606171   -.1620085
testing_re~N |   .2034671   .0365539     5.57   0.000     .1290975    .2778366
testing_re~L |  -.0011465   .0270543    -0.04   0.966    -.0561888    .0538959
testing_re~I |  -.0339503    .023739    -1.43   0.162    -.0822476     .014347
testing_re~S |  -.0413613    .019992    -2.07   0.046    -.0820352   -.0006873
testing_re~J |   .0216732   .0257303     0.84   0.406    -.0306755    .0740219
testing_re~H |   .0098677   .0269526     0.37   0.717    -.0449678    .0647031
testing_re~Z |   .0465241   .0325189     1.43   0.162    -.0196362    .1126844
testing_re~D |   .0062593   .0294924     0.21   0.833    -.0537436    .0662621
testing_re~O |   -.034311   .0505336    -0.68   0.502    -.1371224    .0685005
testing_re~E |  -.0080682   .0329783    -0.24   0.808    -.0751631    .0590267
       _cons |   .2912092   .0312079     9.33   0.000     .2277163     .354702
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p10.log

```
. reghdfe D_l_cum_confirmed_cases p_10, absorb(i.adm1_id i.dow, savefe) cluster
> (t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =      66.00
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.4661
                                                  Adj R-squared   =     0.4415
                                                  Within R-sq.    =     0.1968
Number of clusters (t)       =         34         Root MSE        =     0.0350

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
        p_10 |  -.0423465   .0052124    -8.12   0.000    -.0529511   -.0317418
       _cons |   .1399811   .0043248    32.37   0.000     .1311822      .14878
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p11.log

```
. reghdfe D_l_cum_confirmed_cases p_11, absorb(i.adm1_id i.dow, savefe) cluster
> (t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =     177.55
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.5372
                                                  Adj R-squared   =     0.5159
                                                  Within R-sq.    =     0.3038
Number of clusters (t)       =         34         Root MSE        =     0.0326

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
        p_11 |  -.0619954   .0046527   -13.32   0.000    -.0714613   -.0525295
       _cons |    .177534   .0046106    38.51   0.000     .1681538    .1869142
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p1.log

```
. reghdfe D_l_cum_confirmed_cases p_1, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =     128.45
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.5463
                                                  Adj R-squared   =     0.5254
                                                  Within R-sq.    =     0.3174
Number of clusters (t)       =         34         Root MSE        =     0.0323

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.0684078   .0060359   -11.33   0.000     -.080688   -.0561277
       _cons |   .1707045   .0053699    31.79   0.000     .1597793    .1816296
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p2.log

```
. reghdfe D_l_cum_confirmed_cases p_2, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =     143.60
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.6080
                                                  Adj R-squared   =     0.5899
                                                  Within R-sq.    =     0.4103
Number of clusters (t)       =         34         Root MSE        =     0.0300

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_2 |   -.163814   .0136703   -11.98   0.000    -.1916264   -.1360017
       _cons |   .1699564   .0047122    36.07   0.000     .1603693    .1795435
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p3.log

```
. reghdfe D_l_cum_confirmed_cases p_3, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =      32.17
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.3625
                                                  Adj R-squared   =     0.3331
                                                  Within R-sq.    =     0.0409
Number of clusters (t)       =         34         Root MSE        =     0.0382

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_3 |  -.0588316   .0103733    -5.67   0.000    -.0799362   -.0377269
       _cons |    .132989   .0048772    27.27   0.000     .1230663    .1429118
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p4.log

```
. reghdfe D_l_cum_confirmed_cases p_4, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =      27.75
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.4338
                                                  Adj R-squared   =     0.4077
                                                  Within R-sq.    =     0.1482
Number of clusters (t)       =         34         Root MSE        =     0.0360

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_4 |   -.156667   .0297429    -5.27   0.000    -.2171794   -.0961546
       _cons |   .1843234   .0116409    15.83   0.000     .1606399     .208007
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p5.log

```
. reghdfe D_l_cum_confirmed_cases p_5, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =      71.50
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.4852
                                                  Adj R-squared   =     0.4614
                                                  Within R-sq.    =     0.2255
Number of clusters (t)       =         34         Root MSE        =     0.0344

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_5 |  -.0497172   .0058797    -8.46   0.000    -.0616796   -.0377548
       _cons |   .1474104   .0050367    29.27   0.000     .1371631    .1576577
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p6.log

```
. reghdfe D_l_cum_confirmed_cases p_6, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =     158.26
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.5448
                                                  Adj R-squared   =     0.5238
                                                  Within R-sq.    =     0.3152
Number of clusters (t)       =         34         Root MSE        =     0.0323

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_6 |  -.0633905   .0050389   -12.58   0.000    -.0736422   -.0531388
       _cons |   .1741249    .004301    40.48   0.000     .1653744    .1828753
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p7.log

```
. reghdfe D_l_cum_confirmed_cases p_7, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =      75.61
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.4138
                                                  Adj R-squared   =     0.3867
                                                  Within R-sq.    =     0.1181
Number of clusters (t)       =         34         Root MSE        =     0.0367

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_7 |  -.0843119    .009696    -8.70   0.000    -.1040385   -.0645853
       _cons |   .1378061   .0042999    32.05   0.000      .129058    .1465543
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p8.log

```
. reghdfe D_l_cum_confirmed_cases p_8, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =     120.90
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.5656
                                                  Adj R-squared   =     0.5455
                                                  Within R-sq.    =     0.3465
Number of clusters (t)       =         34         Root MSE        =     0.0316

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_8 |  -.0604455   .0054973   -11.00   0.000    -.0716298   -.0492612
       _cons |   .1604267   .0046211    34.72   0.000     .1510249    .1698285
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p9.log

```
. reghdfe D_l_cum_confirmed_cases p_9, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =      51.43
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.3697
                                                  Adj R-squared   =     0.3406
                                                  Within R-sq.    =     0.0518
Number of clusters (t)       =         34         Root MSE        =     0.0380

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_9 |  -.0379744   .0052954    -7.17   0.000    -.0487478   -.0272009
       _cons |   .1300369    .004275    30.42   0.000     .1213395    .1387344
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-sim.log

```
. reghdfe D_l_cum_confirmed_cases p_*, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(  11,     33) =      82.60
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.6512
                                                  Adj R-squared   =     0.6321
                                                  Within R-sq.    =     0.4752
Number of clusters (t)       =         34         Root MSE        =     0.0284

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |    .001017    .004806     0.21   0.834    -.0087609    .0107949
         p_2 |  -.0946648   .0117848    -8.03   0.000    -.1186411   -.0706884
         p_3 |   .0001436   .0089355     0.02   0.987    -.0180358    .0183229
         p_4 |  -.0197911    .022237    -0.89   0.380    -.0650327    .0254505
         p_5 |  -.0207478   .0037161    -5.58   0.000    -.0283082   -.0131874
         p_6 |  -.0122473   .0031428    -3.90   0.000    -.0186415   -.0058531
         p_7 |   .0057932   .0068363     0.85   0.403    -.0081153    .0197017
         p_8 |  -.0168408   .0033124    -5.08   0.000    -.0235799   -.0101018
         p_9 |   .0032907   .0038943     0.84   0.404    -.0046323    .0112136
        p_10 |   .0169296   .0046401     3.65   0.001     .0074893    .0263699
        p_11 |  -.0130426   .0047646    -2.74   0.010    -.0227362   -.0033491
       _cons |   .1901811   .0089679    21.21   0.000     .1719358    .2084263
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-sim-p10.log

```
. reghdfe D_l_cum_confirmed_cases p_10, absorb(i.adm1_id i.dow, savefe) cluster
> (t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =      66.00
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.4661
                                                  Adj R-squared   =     0.4415
                                                  Within R-sq.    =     0.1968
Number of clusters (t)       =         34         Root MSE        =     0.0350

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
        p_10 |  -.0423465   .0052124    -8.12   0.000    -.0529511   -.0317418
       _cons |   .1399811   .0043248    32.37   0.000     .1311822      .14878
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-sim-p11.log

```
. reghdfe D_l_cum_confirmed_cases p_11, absorb(i.adm1_id i.dow, savefe) cluster
> (t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =     177.55
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.5372
                                                  Adj R-squared   =     0.5159
                                                  Within R-sq.    =     0.3038
Number of clusters (t)       =         34         Root MSE        =     0.0326

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
        p_11 |  -.0619954   .0046527   -13.32   0.000    -.0714613   -.0525295
       _cons |    .177534   .0046106    38.51   0.000     .1681538    .1869142
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-sim-p1.log

```
. reghdfe D_l_cum_confirmed_cases p_1, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =     128.45
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.5463
                                                  Adj R-squared   =     0.5254
                                                  Within R-sq.    =     0.3174
Number of clusters (t)       =         34         Root MSE        =     0.0323

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.0684078   .0060359   -11.33   0.000     -.080688   -.0561277
       _cons |   .1707045   .0053699    31.79   0.000     .1597793    .1816296
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-sim-p2.log

```
. reghdfe D_l_cum_confirmed_cases p_2, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =     143.60
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.6080
                                                  Adj R-squared   =     0.5899
                                                  Within R-sq.    =     0.4103
Number of clusters (t)       =         34         Root MSE        =     0.0300

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_2 |   -.163814   .0136703   -11.98   0.000    -.1916264   -.1360017
       _cons |   .1699564   .0047122    36.07   0.000     .1603693    .1795435
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-sim-p3.log

```
. reghdfe D_l_cum_confirmed_cases p_3, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =      32.17
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.3625
                                                  Adj R-squared   =     0.3331
                                                  Within R-sq.    =     0.0409
Number of clusters (t)       =         34         Root MSE        =     0.0382

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_3 |  -.0588316   .0103733    -5.67   0.000    -.0799362   -.0377269
       _cons |    .132989   .0048772    27.27   0.000     .1230663    .1429118
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-sim-p4.log

```
. reghdfe D_l_cum_confirmed_cases p_4, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =      27.75
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.4338
                                                  Adj R-squared   =     0.4077
                                                  Within R-sq.    =     0.1482
Number of clusters (t)       =         34         Root MSE        =     0.0360

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_4 |   -.156667   .0297429    -5.27   0.000    -.2171794   -.0961546
       _cons |   .1843234   .0116409    15.83   0.000     .1606399     .208007
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-sim-p5.log

```
. reghdfe D_l_cum_confirmed_cases p_5, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =      71.50
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.4852
                                                  Adj R-squared   =     0.4614
                                                  Within R-sq.    =     0.2255
Number of clusters (t)       =         34         Root MSE        =     0.0344

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_5 |  -.0497172   .0058797    -8.46   0.000    -.0616796   -.0377548
       _cons |   .1474104   .0050367    29.27   0.000     .1371631    .1576577
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-sim-p6.log

```
. reghdfe D_l_cum_confirmed_cases p_6, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =     158.26
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.5448
                                                  Adj R-squared   =     0.5238
                                                  Within R-sq.    =     0.3152
Number of clusters (t)       =         34         Root MSE        =     0.0323

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_6 |  -.0633905   .0050389   -12.58   0.000    -.0736422   -.0531388
       _cons |   .1741249    .004301    40.48   0.000     .1653744    .1828753
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-sim-p7.log

```
. reghdfe D_l_cum_confirmed_cases p_7, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =      75.61
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.4138
                                                  Adj R-squared   =     0.3867
                                                  Within R-sq.    =     0.1181
Number of clusters (t)       =         34         Root MSE        =     0.0367

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_7 |  -.0843119    .009696    -8.70   0.000    -.1040385   -.0645853
       _cons |   .1378061   .0042999    32.05   0.000      .129058    .1465543
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-sim-p8.log

```
. reghdfe D_l_cum_confirmed_cases p_8, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =     120.90
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.5656
                                                  Adj R-squared   =     0.5455
                                                  Within R-sq.    =     0.3465
Number of clusters (t)       =         34         Root MSE        =     0.0316

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_8 |  -.0604455   .0054973   -11.00   0.000    -.0716298   -.0492612
       _cons |   .1604267   .0046211    34.72   0.000     .1510249    .1698285
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-sim-p9.log

```
. reghdfe D_l_cum_confirmed_cases p_9, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(   1,     33) =      51.43
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.3697
                                                  Adj R-squared   =     0.3406
                                                  Within R-sq.    =     0.0518
Number of clusters (t)       =         34         Root MSE        =     0.0380

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_9 |  -.0379744   .0052954    -7.17   0.000    -.0487478   -.0272009
       _cons |   .1300369    .004275    30.42   0.000     .1213395    .1387344
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
