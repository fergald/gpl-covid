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
# CHN_adm2-sim-daily.log

```
. reghdfe D_l_active_cases emergency_declaration_L* travel_ban_local_L* home_is
> olation_L* testing_regime_change_* , absorb(i.adm12_id, savefe) cluster(t) re
> sid
(dropped 1 singleton observations)
(MWFE estimator converged in 1 iterations)
warning: missing F statistic; dropped variables due to collinearity or too few 
> clusters

HDFE Linear regression                            Number of obs   =        210
Absorbing 1 HDFE group                            F(  21,     48) =          .
Statistics robust to heteroskedasticity           Prob > F        =          .
                                                  R-squared       =     0.6358
                                                  Adj R-squared   =     0.5772
                                                  Within R-sq.    =     0.5668
Number of clusters (t)       =         49         Root MSE        =     0.1154

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
emergency_~7 |   .1517481   .0385604     3.94   0.000     .0742172     .229279
emergency~14 |   .1935691   .0579755     3.34   0.002     .0770015    .3101368
emergency~21 |   .2123433   .0602446     3.52   0.001     .0912134    .3334733
emergency~28 |   .1945196   .0710119     2.74   0.009     .0517405    .3372987
emergency~70 |   .1941113   .0805285     2.41   0.020     .0321978    .3560247
travel_ban~7 |  -.1609515   .0886437    -1.82   0.076    -.3391815    .0172786
travel_ba~14 |  -.3240765   .0987217    -3.28   0.002    -.5225698   -.1255831
travel_ba~21 |  -.4416298   .1034804    -4.27   0.000    -.6496912   -.2335685
travel_ba~28 |  -.4947402   .1076496    -4.60   0.000    -.7111842   -.2782962
travel_ba~70 |  -.4750756   .1083357    -4.39   0.000    -.6928991   -.2572521
home_isola~7 |   .0066036   .0402267     0.16   0.870    -.0742776    .0874847
home_isol~14 |  -.0340397   .0372662    -0.91   0.366    -.1089685    .0408891
home_isol~21 |  -.0302388   .0459423    -0.66   0.514    -.1226121    .0621345
home_isol~28 |  -.0322852   .0530504    -0.61   0.546    -.1389503    .0743798
home_isol~70 |   -.034452   .0671319    -0.51   0.610    -.1694297    .1005256
te~18jan2020 |    .520261   .0886437     5.87   0.000      .342031     .698491
te~28jan2020 |   .2029716   .0341011     5.95   0.000     .1344067    .2715365
tes~6feb2020 |  -.0265457    .020926    -1.27   0.211    -.0686203    .0155288
tes~3feb2020 |   .0056694   .0278234     0.20   0.839    -.0502733     .061612
tes~0feb2020 |   .0218569   .0164988     1.32   0.192    -.0113162    .0550299
testin~r2020 |   .0024794   .0078978     0.31   0.755    -.0134001    .0183589
       _cons |   .3170175   .0927685     3.42   0.001     .1304939    .5035411
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
    adm12_id |         9           0           9     |
-----------------------------------------------------+

```
# CHN_adm2-sim.log

```
. reghdfe D_l_active_cases emergency_declaration_L* travel_ban_local_L* home_is
> olation_L* testing_regime_change_* , absorb(i.adm12_id, savefe) cluster(t) re
> sid
(MWFE estimator converged in 1 iterations)

HDFE Linear regression                            Number of obs   =      3,551
Absorbing 1 HDFE group                            F(  21,     48) =    1348.90
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.3641
                                                  Adj R-squared   =     0.3392
                                                  Within R-sq.    =     0.3159
Number of clusters (t)       =         49         Root MSE        =     0.1163

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
emergency_~7 |  -.1802557   .0530142    -3.40   0.001    -.2868479   -.0736635
emergency~14 |    -.34904   .0479086    -7.29   0.000    -.4453668   -.2527133
emergency~21 |  -.4091947   .0494539    -8.27   0.000    -.5086284    -.309761
emergency~28 |  -.4183063   .0507664    -8.24   0.000    -.5203791   -.3162336
emergency~70 |  -.4025073   .0527611    -7.63   0.000    -.5085905   -.2964241
travel_ban~7 |   .0360828   .0181105     1.99   0.052    -.0003308    .0724964
travel_ba~14 |    .018224   .0242832     0.75   0.457    -.0306007    .0670487
travel_ba~21 |    .000073   .0310504     0.00   0.998    -.0623581     .062504
travel_ba~28 |  -.0074037   .0382233    -0.19   0.847    -.0842568    .0694494
travel_ba~70 |  -.0231663   .0482332    -0.48   0.633    -.1201457    .0738131
home_isola~7 |  -.0550441   .0170824    -3.22   0.002    -.0893906   -.0206976
home_isol~14 |  -.0567517   .0217834    -2.61   0.012    -.1005503   -.0129532
home_isol~21 |   -.041831    .025853    -1.62   0.112     -.093812      .01015
home_isol~28 |    .024414   .0305734     0.80   0.428    -.0370579     .085886
home_isol~70 |    .094934    .040944     2.32   0.025     .0126106    .1772574
te~18jan2020 |   .3734618   .0455908     8.19   0.000     .2817954    .4651282
te~28jan2020 |   .0431452   .0328172     1.31   0.195    -.0228382    .1091285
tes~6feb2020 |  -.0348704   .0144591    -2.41   0.020    -.0639423   -.0057985
tes~3feb2020 |  -.0041118   .0025605    -1.61   0.115      -.00926    .0010364
tes~0feb2020 |   .0031199   .0026235     1.19   0.240    -.0021549    .0083947
testin~r2020 |  -.0011107   .0116184    -0.10   0.924    -.0244711    .0222497
       _cons |   .4864286   .0449904    10.81   0.000     .3959694    .5768878
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
>  testing_regime_*, absorb(i.adm1_id i.dow, savefe) cluster(t) resid  
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        270
Absorbing 2 HDFE groups                           F(   4,     22) =      34.65
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.2987
                                                  Adj R-squared   =     0.2362
                                                  Within R-sq.    =     0.2022
Number of clusters (t)       =         23         Root MSE        =     0.1315

                                     (Std. Err. adjusted for 23 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
pck_social~e |  -.2429037   .0719206    -3.38   0.003    -.3920578   -.0937496
school_clo~t |  -.0092628   .0417134    -0.22   0.826    -.0957711    .0772455
national_l~n |   .0831272   .0523789     1.59   0.127       -.0255    .1917545
testing~2020 |  -.1116384   .0205793    -5.42   0.000    -.1543171   -.0689596
       _cons |   .3345041   .0216868    15.42   0.000     .2895285    .3794797
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        13           0          13     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# FRA_adm1-national_lockdown-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases national_lockdown, absorb(i.adm1_id i.dow, sa
> vefe) cluster(t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        212
Absorbing 2 HDFE groups                           F(   1,     24) =       2.67
Statistics robust to heteroskedasticity           Prob > F        =     0.1155
                                                  R-squared       =     0.1600
                                                  Adj R-squared   =     0.0769
                                                  Within R-sq.    =     0.0194
Number of clusters (t)       =         25         Root MSE        =     0.3075

                                     (Std. Err. adjusted for 25 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
national_l~n |  -.1256324   .0769221    -1.63   0.115    -.2843918     .033127
       _cons |    .275134   .0540203     5.09   0.000     .1636417    .3866264
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        13           0          13     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# FRA_adm1-national_lockdown-sim.log

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
# FRA_adm1-pck_social_distance-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases pck_social_distance, absorb(i.adm1_id i.dow, 
> savefe) cluster(t) resid  
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        212
Absorbing 2 HDFE groups                           F(   1,     24) =       2.98
Statistics robust to heteroskedasticity           Prob > F        =     0.0972
                                                  R-squared       =     0.1618
                                                  Adj R-squared   =     0.0788
                                                  Within R-sq.    =     0.0215
Number of clusters (t)       =         25         Root MSE        =     0.3072

                                     (Std. Err. adjusted for 25 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
pck_social~e |  -.1369634   .0793442    -1.73   0.097    -.3007217     .026795
       _cons |   .3099953   .0692699     4.48   0.000     .1670294    .4529613
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        13           0          13     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# FRA_adm1-pck_social_distance-sim.log

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
# FRA_adm1-school_closure_popw-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases school_closure_popw, absorb(i.adm1_id i.dow, 
> savefe) cluster(t) resid  
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        212
Absorbing 2 HDFE groups                           F(   1,     24) =       2.30
Statistics robust to heteroskedasticity           Prob > F        =     0.1425
                                                  R-squared       =     0.1541
                                                  Adj R-squared   =     0.0704
                                                  Within R-sq.    =     0.0126
Number of clusters (t)       =         25         Root MSE        =     0.3086

                                     (Std. Err. adjusted for 25 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
school_clo~t |  -.0937354   .0618185    -1.52   0.143    -.2213225    .0338517
       _cons |   .2790701    .057775     4.83   0.000     .1598284    .3983119
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        13           0          13     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# FRA_adm1-school_closure_popw-sim.log

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
# FRA_adm1-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases pck_social_distance school_closure_popw natio
> nal_lockdown ///
>  testing_regime_*, absorb(i.adm1_id i.dow, savefe) cluster(t) resid  
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        212
Absorbing 2 HDFE groups                           F(   4,     24) =       1.01
Statistics robust to heteroskedasticity           Prob > F        =     0.4229
                                                  R-squared       =     0.1751
                                                  Adj R-squared   =     0.0790
                                                  Within R-sq.    =     0.0370
Number of clusters (t)       =         25         Root MSE        =     0.3071

                                     (Std. Err. adjusted for 25 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
pck_social~e |  -.1992382    .138935    -1.43   0.164    -.4859859    .0875095
school_clo~t |   .0115511    .078155     0.15   0.884    -.1497529     .172855
national_l~n |     .03817   .1497673     0.25   0.801    -.2709345    .3472744
testing~2020 |  -.1998911   .1385368    -1.44   0.162    -.4858169    .0860347
       _cons |    .338338   .0758842     4.46   0.000     .1817207    .4949553
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
# IRN_adm1-p_1-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_1, absorb(i.adm1_id i.dow, savefe) cluster(
> date) resid
(dropped 1 singleton observations)
(MWFE estimator converged in 5 iterations)

HDFE Linear regression                            Number of obs   =        327
Absorbing 2 HDFE groups                           F(   1,     21) =       2.83
Statistics robust to heteroskedasticity           Prob > F        =     0.1074
                                                  R-squared       =     0.2033
                                                  Adj R-squared   =     0.1136
                                                  Within R-sq.    =     0.0003
Number of clusters (date)    =         22         Root MSE        =     0.1432

                                  (Std. Err. adjusted for 22 clusters in date)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.0466999   .0277687    -1.68   0.107     -.104448    .0110482
       _cons |   .2033423   .0260852     7.80   0.000     .1490951    .2575895
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        27           0          27     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# IRN_adm1-p_1-sim.log

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
# IRN_adm1-p_2-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_2, absorb(i.adm1_id i.dow, savefe) cluster(
> date) resid
(dropped 1 singleton observations)
(MWFE estimator converged in 5 iterations)

HDFE Linear regression                            Number of obs   =        327
Absorbing 2 HDFE groups                           F(   1,     21) =       2.91
Statistics robust to heteroskedasticity           Prob > F        =     0.1030
                                                  R-squared       =     0.2093
                                                  Adj R-squared   =     0.1202
                                                  Within R-sq.    =     0.0078
Number of clusters (date)    =         22         Root MSE        =     0.1427

                                  (Std. Err. adjusted for 22 clusters in date)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_2 |   .0308588   .0181036     1.70   0.103    -.0067896    .0685073
       _cons |   .1447022   .0152363     9.50   0.000     .1130166    .1763877
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        27           0          27     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# IRN_adm1-p_2-sim.log

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
# IRN_adm1-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_* testing_regime_*, absorb(i.adm1_id i.dow,
>  savefe) cluster(date) resid
(dropped 1 singleton observations)
(MWFE estimator converged in 5 iterations)

HDFE Linear regression                            Number of obs   =        327
Absorbing 2 HDFE groups                           F(   3,     21) =       1.33
Statistics robust to heteroskedasticity           Prob > F        =     0.2898
                                                  R-squared       =     0.2101
                                                  Adj R-squared   =     0.1151
                                                  Within R-sq.    =     0.0088
Number of clusters (date)    =         22         Root MSE        =     0.1431

                                  (Std. Err. adjusted for 22 clusters in date)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |   -.083891   .0422976    -1.98   0.061    -.1718535    .0040716
         p_2 |   .0321363   .0187661     1.71   0.102      -.00689    .0711625
testing~2020 |   .0061647   .0091452     0.67   0.508    -.0128537    .0251831
       _cons |   .2085812   .0262735     7.94   0.000     .1539425    .2632198
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        27           0          27     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# IRN_adm1-sim.log

```
. reghdfe D_l_cum_confirmed_cases p_* testing_regime_*, absorb(i.adm1_id i.dow,
>  savefe) cluster(date) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        583
Absorbing 2 HDFE groups                           F(   3,     21) =      76.36
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.7255
                                                  Adj R-squared   =     0.7058
                                                  Within R-sq.    =     0.4628
Number of clusters (date)    =         22         Root MSE        =     0.0264

                                  (Std. Err. adjusted for 22 clusters in date)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.1116594   .0136009    -8.21   0.000     -.139944   -.0833748
         p_2 |  -.0346092   .0040523    -8.54   0.000    -.0430364   -.0261819
testing~2020 |   .0104432    .005772     1.81   0.085    -.0015603    .0224466
       _cons |    .278562    .010331    26.96   0.000     .2570775    .3000466
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
# ITA_adm2-p1-sim-daily.log

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
# ITA_adm2-p1-sim.log

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
# ITA_adm2-p2-sim-daily.log

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
# ITA_adm2-p2-sim.log

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
# ITA_adm2-p3-sim-daily.log

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
# ITA_adm2-p3-sim.log

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
# ITA_adm2-p4-sim-daily.log

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
# ITA_adm2-p4-sim.log

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
# ITA_adm2-p5-sim-daily.log

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
# ITA_adm2-p5-sim.log

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
# ITA_adm2-p6-sim-daily.log

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
# ITA_adm2-p6-sim.log

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
# ITA_adm2-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_*, absorb(i.adm2_id i.dow, savefe) cluster(
> t) resid
(dropped 2 singleton observations)
(MWFE estimator converged in 5 iterations)

HDFE Linear regression                            Number of obs   =        635
Absorbing 2 HDFE groups                           F(   6,     38) =       0.83
Statistics robust to heteroskedasticity           Prob > F        =     0.5510
                                                  R-squared       =     0.2651
                                                  Adj R-squared   =     0.2049
                                                  Within R-sq.    =     0.0157
Number of clusters (t)       =         39         Root MSE        =     0.1697

                                     (Std. Err. adjusted for 39 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |   .2799898   .2061527     1.36   0.182    -.1373445    .6973241
         p_2 |  -.0300517   .0660587    -0.45   0.652    -.1637807    .1036772
         p_3 |   .3534646   .3388117     1.04   0.303    -.3324238    1.039353
         p_4 |  -.1180159   .0824476    -1.43   0.160    -.2849223    .0488906
         p_5 |  -.3651571   .2879996    -1.27   0.213    -.9481817    .2178676
         p_6 |   .0931595   .0805801     1.16   0.255    -.0699664    .2562854
       _cons |   .0294057   .0142201     2.07   0.046     .0006186    .0581929
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm2_id |        37           0          37     |
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
# KOR_adm1-p_1-sim-daily.log

```
. reghdfe D_l_active_cases p_1, absorb(i.adm1_id i.dow, savefe) cluster(t) resi
> d
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        102
Absorbing 2 HDFE groups                           F(   1,     31) =       0.85
Statistics robust to heteroskedasticity           Prob > F        =     0.3648
                                                  R-squared       =     0.1231
                                                  Adj R-squared   =     0.0267
                                                  Within R-sq.    =     0.0132
Number of clusters (t)       =         32         Root MSE        =     0.0359

                                     (Std. Err. adjusted for 32 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.0309282   .0336252    -0.92   0.365    -.0995072    .0376508
       _cons |   .0480766    .027971     1.72   0.096    -.0089707    .1051238
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |         4           0           4     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-p_1-sim.log

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
# KOR_adm1-p_2-sim-daily.log

```
. reghdfe D_l_active_cases p_2, absorb(i.adm1_id i.dow, savefe) cluster(t) resi
> d
note: p_2 is probably collinear with the fixed effects (all partialled-out valu
> es are close to zero; tol = 1.0e-09)
(MWFE estimator converged in 4 iterations)
note: p_2 omitted because of collinearity
(748 missing values generated)

HDFE Linear regression                            Number of obs   =        102
Absorbing 2 HDFE groups                           F(   0,     31) =          .
Statistics robust to heteroskedasticity           Prob > F        =          .
                                                  R-squared       =     0.1113
                                                  Adj R-squared   =     0.0244
                                                  Within R-sq.    =     0.0000
Number of clusters (t)       =         32         Root MSE        =     0.0360

                                     (Std. Err. adjusted for 32 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_2 |          0  (omitted)
       _cons |   .0233643    .003557     6.57   0.000     .0161098    .0306188
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |         4           0           4     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-p_2-sim.log

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
# KOR_adm1-p_3-sim-daily.log

```
. reghdfe D_l_active_cases p_3, absorb(i.adm1_id i.dow, savefe) cluster(t) resi
> d
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        102
Absorbing 2 HDFE groups                           F(   1,     31) =       0.13
Statistics robust to heteroskedasticity           Prob > F        =     0.7163
                                                  R-squared       =     0.1127
                                                  Adj R-squared   =     0.0152
                                                  Within R-sq.    =     0.0015
Number of clusters (t)       =         32         Root MSE        =     0.0361

                                     (Std. Err. adjusted for 32 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_3 |   .0042379   .0115564     0.37   0.716    -.0193315    .0278073
       _cons |   .0215362   .0058939     3.65   0.001     .0095155    .0335569
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |         4           0           4     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-p_3-sim.log

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
# KOR_adm1-p_4-sim-daily.log

```
. reghdfe D_l_active_cases p_4, absorb(i.adm1_id i.dow, savefe) cluster(t) resi
> d
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        102
Absorbing 2 HDFE groups                           F(   1,     31) =       0.92
Statistics robust to heteroskedasticity           Prob > F        =     0.3461
                                                  R-squared       =     0.1188
                                                  Adj R-squared   =     0.0220
                                                  Within R-sq.    =     0.0085
Number of clusters (t)       =         32         Root MSE        =     0.0360

                                     (Std. Err. adjusted for 32 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_4 |  -.0098479   .0102924    -0.96   0.346    -.0308394    .0111437
       _cons |   .0267435   .0059312     4.51   0.000     .0146467    .0388402
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |         4           0           4     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-p_4-sim.log

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
# KOR_adm1-sim-daily.log

```
. reghdfe D_l_active_cases p_* testing_regime_change_*, absorb(i.adm1_id i.dow,
>  savefe) cluster(t) resid
note: p_2 is probably collinear with the fixed effects (all partialled-out valu
> es are close to zero; tol = 1.0e-09)
(MWFE estimator converged in 4 iterations)
note: p_2 omitted because of collinearity
note: testing_regime_change_20feb2020 omitted because of collinearity
note: testing_regime_change_29feb2020 omitted because of collinearity

HDFE Linear regression                            Number of obs   =        102
Absorbing 2 HDFE groups                           F(   5,     31) =       4.82
Statistics robust to heteroskedasticity           Prob > F        =     0.0022
                                                  R-squared       =     0.2187
                                                  Adj R-squared   =     0.0930
                                                  Within R-sq.    =     0.1209
Number of clusters (t)       =         32         Root MSE        =     0.0347

                                     (Std. Err. adjusted for 32 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.1587704    .087737    -1.81   0.080    -.3377112    .0201704
         p_2 |          0  (omitted)
         p_3 |   .0645794   .0341917     1.89   0.068     -.005155    .1343139
         p_4 |  -.0062971   .0135075    -0.47   0.644    -.0338458    .0212515
tes~0feb2020 |          0  (omitted)
tes~9feb2020 |          0  (omitted)
tes~2mar2020 |   -.013108     .01417    -0.93   0.362     -.042008    .0157919
tes~7mar2020 |  -.0277023   .0061199    -4.53   0.000    -.0401839   -.0152207
       _cons |   .1261283   .0593339     2.13   0.042     .0051161    .2471406
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |         4           0           4     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# KOR_adm1-sim.log

```
. reghdfe D_l_active_cases p_* testing_regime_change_*, absorb(i.adm1_id i.dow,
>  savefe) cluster(t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        706
Absorbing 2 HDFE groups                           F(   8,     48) =      37.86
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.2480
                                                  Adj R-squared   =     0.2146
                                                  Within R-sq.    =     0.1932
Number of clusters (t)       =         49         Root MSE        =     0.1601

                                     (Std. Err. adjusted for 49 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_active~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |  -.1440465    .033358    -4.32   0.000    -.2111172   -.0769758
         p_2 |   -.357495   .0567462    -6.30   0.000    -.4715909   -.2433992
         p_3 |   .0758065   .0280079     2.71   0.009     .0194928    .1321201
         p_4 |   .0477061   .0132649     3.60   0.001     .0210352     .074377
tes~0feb2020 |  -.2697992    .036592    -7.37   0.000    -.3433724    -.196226
tes~9feb2020 |   .0604647   .0183124     3.30   0.002     .0236452    .0972842
tes~2mar2020 |  -.0340091   .0163392    -2.08   0.043    -.0668612    -.001157
tes~7mar2020 |  -.0468114    .022731    -2.06   0.045    -.0925151   -.0011077
       _cons |    .398162   .0275806    14.44   0.000     .3427074    .4536165
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        17           0          17     |
         dow |         7           1           6     |
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
# USA_adm1-p10-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_10, absorb(i.adm1_id i.dow, savefe) cluster
> (t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        638
Absorbing 2 HDFE groups                           F(   1,     33) =       0.08
Statistics robust to heteroskedasticity           Prob > F        =     0.7737
                                                  R-squared       =     0.5647
                                                  Adj R-squared   =     0.5285
                                                  Within R-sq.    =     0.0002
Number of clusters (t)       =         34         Root MSE        =     0.0211

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
        p_10 |   .0007093    .002447     0.29   0.774    -.0042691    .0056878
       _cons |    .095187   .0018236    52.20   0.000     .0914769     .098897
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        43           0          43     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p10-sim.log

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
# USA_adm1-p11-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_11, absorb(i.adm1_id i.dow, savefe) cluster
> (t) resid
(MWFE estimator converged in 5 iterations)

HDFE Linear regression                            Number of obs   =        638
Absorbing 2 HDFE groups                           F(   1,     33) =       0.14
Statistics robust to heteroskedasticity           Prob > F        =     0.7136
                                                  R-squared       =     0.5647
                                                  Adj R-squared   =     0.5285
                                                  Within R-sq.    =     0.0001
Number of clusters (t)       =         34         Root MSE        =     0.0211

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
        p_11 |  -.0008669   .0023419    -0.37   0.714    -.0056315    .0038978
       _cons |   .0963543   .0023041    41.82   0.000     .0916666    .1010421
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        43           0          43     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p11-sim.log

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
# USA_adm1-p1-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_1, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        638
Absorbing 2 HDFE groups                           F(   1,     33) =       0.35
Statistics robust to heteroskedasticity           Prob > F        =     0.5588
                                                  R-squared       =     0.5649
                                                  Adj R-squared   =     0.5286
                                                  Within R-sq.    =     0.0005
Number of clusters (t)       =         34         Root MSE        =     0.0211

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |   .0018411    .003117     0.59   0.559    -.0045004    .0081827
       _cons |   .0941192   .0027025    34.83   0.000      .088621    .0996174
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        43           0          43     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p1-sim.log

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
# USA_adm1-p2-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_2, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 5 iterations)

HDFE Linear regression                            Number of obs   =        638
Absorbing 2 HDFE groups                           F(   1,     33) =       0.02
Statistics robust to heteroskedasticity           Prob > F        =     0.9006
                                                  R-squared       =     0.5647
                                                  Adj R-squared   =     0.5284
                                                  Within R-sq.    =     0.0000
Number of clusters (t)       =         34         Root MSE        =     0.0211

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_2 |  -.0007752   .0061599    -0.13   0.901    -.0133076    .0117573
       _cons |    .095843   .0023974    39.98   0.000     .0909656    .1007205
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        43           0          43     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p2-sim.log

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
# USA_adm1-p3-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_3, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        638
Absorbing 2 HDFE groups                           F(   1,     33) =       0.04
Statistics robust to heteroskedasticity           Prob > F        =     0.8407
                                                  R-squared       =     0.5647
                                                  Adj R-squared   =     0.5284
                                                  Within R-sq.    =     0.0001
Number of clusters (t)       =         34         Root MSE        =     0.0211

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_3 |   .0017317   .0085456     0.20   0.841    -.0156544    .0191178
       _cons |   .0953424   .0015227    62.61   0.000     .0922445    .0984404
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        43           0          43     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p3-sim.log

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
# USA_adm1-p4-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_4, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        638
Absorbing 2 HDFE groups                           F(   1,     33) =       0.03
Statistics robust to heteroskedasticity           Prob > F        =     0.8673
                                                  R-squared       =     0.5647
                                                  Adj R-squared   =     0.5284
                                                  Within R-sq.    =     0.0000
Number of clusters (t)       =         34         Root MSE        =     0.0211

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_4 |  -.0016583    .009846    -0.17   0.867    -.0216901    .0183736
       _cons |   .0962425   .0041446    23.22   0.000     .0878104    .1046747
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        43           0          43     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p4-sim.log

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
# USA_adm1-p5-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_5, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        638
Absorbing 2 HDFE groups                           F(   1,     33) =       0.13
Statistics robust to heteroskedasticity           Prob > F        =     0.7199
                                                  R-squared       =     0.5647
                                                  Adj R-squared   =     0.5285
                                                  Within R-sq.    =     0.0002
Number of clusters (t)       =         34         Root MSE        =     0.0211

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_5 |   .0008816   .0024376     0.36   0.720    -.0040777    .0058409
       _cons |   .0950239   .0019024    49.95   0.000     .0911533    .0988944
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        43           0          43     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p5-sim.log

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
# USA_adm1-p6-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_6, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        638
Absorbing 2 HDFE groups                           F(   1,     33) =       0.35
Statistics robust to heteroskedasticity           Prob > F        =     0.5569
                                                  R-squared       =     0.5648
                                                  Adj R-squared   =     0.5286
                                                  Within R-sq.    =     0.0003
Number of clusters (t)       =         34         Root MSE        =     0.0211

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_6 |   .0015039   .0025342     0.59   0.557     -.003652    .0066598
       _cons |   .0942769   .0023916    39.42   0.000     .0894111    .0991428
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        43           0          43     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p6-sim.log

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
# USA_adm1-p7-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_7, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        638
Absorbing 2 HDFE groups                           F(   1,     33) =       0.00
Statistics robust to heteroskedasticity           Prob > F        =     0.9441
                                                  R-squared       =     0.5647
                                                  Adj R-squared   =     0.5284
                                                  Within R-sq.    =     0.0000
Number of clusters (t)       =         34         Root MSE        =     0.0211

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_7 |  -.0002548   .0036045    -0.07   0.944    -.0075882    .0070786
       _cons |   .0956251   .0010723    89.18   0.000     .0934435    .0978067
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        43           0          43     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p7-sim.log

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
# USA_adm1-p8-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_8, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        638
Absorbing 2 HDFE groups                           F(   1,     33) =       0.05
Statistics robust to heteroskedasticity           Prob > F        =     0.8304
                                                  R-squared       =     0.5647
                                                  Adj R-squared   =     0.5284
                                                  Within R-sq.    =     0.0001
Number of clusters (t)       =         34         Root MSE        =     0.0211

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_8 |   .0005107   .0023651     0.22   0.830    -.0043011    .0053225
       _cons |   .0951987   .0019146    49.72   0.000     .0913035     .099094
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        43           0          43     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p8-sim.log

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
# USA_adm1-p9-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_9, absorb(i.adm1_id i.dow, savefe) cluster(
> t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =        638
Absorbing 2 HDFE groups                           F(   1,     33) =       0.43
Statistics robust to heteroskedasticity           Prob > F        =     0.5164
                                                  R-squared       =     0.5650
                                                  Adj R-squared   =     0.5287
                                                  Within R-sq.    =     0.0007
Number of clusters (t)       =         34         Root MSE        =     0.0211

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_9 |   .0023507   .0035837     0.66   0.516    -.0049404    .0096419
       _cons |   .0951678   .0011749    81.00   0.000     .0927773    .0975582
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        43           0          43     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-p9-sim.log

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
# USA_adm1-sim-daily.log

```
. reghdfe D_l_cum_confirmed_cases p_* testing_regime_*, absorb(i.adm1_id i.dow,
>  savefe) cluster(t) resid
(MWFE estimator converged in 5 iterations)

HDFE Linear regression                            Number of obs   =        638
Absorbing 2 HDFE groups                           F(  19,     33) =      19.82
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.5701
                                                  Adj R-squared   =     0.5196
                                                  Within R-sq.    =     0.0124
Number of clusters (t)       =         34         Root MSE        =     0.0213

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |   .0048128   .0075932     0.63   0.531    -.0106356    .0202611
         p_2 |   -.008997   .0118158    -0.76   0.452    -.0330364    .0150424
         p_3 |   .0044208   .0096017     0.46   0.648    -.0151141    .0239557
         p_4 |  -.0062269    .012288    -0.51   0.616     -.031227    .0187731
         p_5 |   .0003572   .0052929     0.07   0.947    -.0104113    .0111256
         p_6 |   .0102004   .0038977     2.62   0.013     .0022705    .0181302
         p_7 |   .0001771   .0053918     0.03   0.974    -.0107926    .0111469
         p_8 |   .0017173   .0067942     0.25   0.802    -.0121057    .0155402
         p_9 |   .0040235   .0044043     0.91   0.368    -.0049371    .0129841
        p_10 |  -.0022118   .0085794    -0.26   0.798    -.0196668    .0152431
        p_11 |  -.0112316   .0056029    -2.00   0.053    -.0226307    .0001675
testing_r~CA |   .0117541   .0041239     2.85   0.007     .0033639    .0201443
testing_r~IA |  -.0202687   .0029395    -6.90   0.000    -.0262492   -.0142882
testing_re~L |   .0093117   .0095257     0.98   0.335    -.0100684    .0286918
testing_re~J |  -.0138706   .0051439    -2.70   0.011    -.0243359   -.0034053
testing_re~H |   .0192835    .006846     2.82   0.008     .0053552    .0332118
testing_re~Z |   .0102606   .0033152     3.10   0.004     .0035158    .0170054
testing_re~D |  -.0023841   .0076959    -0.31   0.759    -.0180415    .0132733
testing_re~E |  -.0202755   .0102041    -1.99   0.055    -.0410359     .000485
       _cons |   .0971645   .0049687    19.56   0.000     .0870555    .1072735
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        43           0          43     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
# USA_adm1-sim.log

```
. reghdfe D_l_cum_confirmed_cases p_* testing_regime_*, absorb(i.adm1_id i.dow,
>  savefe) cluster(t) resid
(MWFE estimator converged in 4 iterations)

HDFE Linear regression                            Number of obs   =      1,292
Absorbing 2 HDFE groups                           F(  28,     33) =     246.64
Statistics robust to heteroskedasticity           Prob > F        =     0.0000
                                                  R-squared       =     0.6546
                                                  Adj R-squared   =     0.6306
                                                  Within R-sq.    =     0.4804
Number of clusters (t)       =         34         Root MSE        =     0.0285

                                     (Std. Err. adjusted for 34 clusters in t)
------------------------------------------------------------------------------
             |               Robust
D_l_cum_co~s |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         p_1 |   .0010349   .0048875     0.21   0.834    -.0089087    .0109785
         p_2 |   -.095937   .0115477    -8.31   0.000     -.119431   -.0724429
         p_3 |   .0003071   .0090837     0.03   0.973    -.0181738    .0187881
         p_4 |  -.0193045   .0226749    -0.85   0.401     -.065437     .026828
         p_5 |   -.021537   .0037407    -5.76   0.000    -.0291474   -.0139266
         p_6 |  -.0121019   .0030598    -3.96   0.000     -.018327   -.0058767
         p_7 |   .0061068    .006919     0.88   0.384      -.00797    .0201835
         p_8 |  -.0173672   .0032823    -5.29   0.000    -.0240451   -.0106893
         p_9 |   .0029481    .003864     0.76   0.451    -.0049133    .0108095
        p_10 |   .0180861   .0046609     3.88   0.000     .0086035    .0275688
        p_11 |  -.0129905   .0049683    -2.61   0.013    -.0230986   -.0028825
testing_re~Y |  -.0577312   .0062108    -9.30   0.000    -.0703671   -.0450952
testing_r~CA |   .0062074   .0050274     1.23   0.226     -.004021    .0164357
testing_re~C |  -.0006829   .0033537    -0.20   0.840    -.0075061    .0061404
testing_r~CT |   .0280208   .0081178     3.45   0.002      .011505    .0445367
testing_re~V |  -.0237392   .0048117    -4.93   0.000    -.0335287   -.0139498
testing_r~UT |  -.0237497   .0047425    -5.01   0.000    -.0333985   -.0141009
testing_r~IA |  -.0181337   .0125697    -1.44   0.159    -.0437069    .0074394
testing_re~N |  -.0323282   .0053423    -6.05   0.000    -.0431972   -.0214591
testing_re~L |  -.0075803   .0165679    -0.46   0.650    -.0412879    .0261273
testing_re~I |  -.0195708   .0083357    -2.35   0.025    -.0365299   -.0026117
testing_re~S |    .030344   .0058648     5.17   0.000      .018412    .0422761
testing_re~J |  -.0019964   .0048768    -0.41   0.685    -.0119183    .0079254
testing_re~H |  -.0062982   .0060789    -1.04   0.308    -.0186659    .0060695
testing_re~Z |   .0336161   .0097254     3.46   0.002     .0138297    .0534025
testing_re~D |  -.0169764   .0065856    -2.58   0.015     -.030375   -.0035778
testing_re~O |   .0026363   .0039222     0.67   0.506    -.0053434    .0106161
testing_re~E |  -.0291142    .009498    -3.07   0.004    -.0484381   -.0097904
       _cons |   .1905137   .0090042    21.16   0.000     .1721945    .2088329
------------------------------------------------------------------------------

Absorbed degrees of freedom:
-----------------------------------------------------+
 Absorbed FE | Categories  - Redundant  = Num. Coefs |
-------------+---------------------------------------|
     adm1_id |        51           0          51     |
         dow |         7           1           6     |
-----------------------------------------------------+

```
