# The Effect of Large-Scale Anti-Contagion Policies on the Coronavirus (COVID-19) Pandemic

This repository contains code and data necessary to replicate the findings of our paper [INSERT arXiv CITATION].

## Setup
Scripts in this repository are written in R, Python, and Stata. Note that you will need a Stata license to fully replicate the analysis. Throughout this Readme, it is assumed that you’ll execute scripts from the repo root directory. In addition, we assume that you have an environment of Python and R packages described in <environment.yml>.

To create and activate this environment using [conda](https://docs.conda.io/projects/conda/en/latest/index.html) execute :

```bash
conda env create -f environment.yml
conda activate gpl-covid
```

**Note:** RStudio is commented out of that environment, because it causes dependency clashes in a Windows environment. If you are not in Windows, and would like to use the RStudio app, feel free to uncomment it before creating the environment. Once you have activated this environment, to run some of the Python scripts, you’ll need to install the small package (1 module) that is included in this repo. Ensure you are currently located inside the repo root directory (`cd gpl-covid`), then execute

```bash
pip install -e .
```

To run one of the scripts, you will also need an API key for the US Census API, which can be obtained [here](https://api.census.gov/data/key_signup.html). You will need to save this key to `api_keys.json` in the root directory of this repo with the following format:

```json
{
    "census": "API_KEY_STRING"
}
```

Finally, to estimate the regression models, you will need several package installed in Stata. To add them, launch Stata and run:
```
ssc install reghdfe, replace
ssc install ftools, replace # the latest version of reghdfe would also require the installation of ftools
ssc install coefplot, replace
ssc install filelist, replace
```

## Data Documentation
A detailed description of the epidemiological and policy data obtained and processed for this analysis can be found [here](https://www.dropbox.com/scl/fi/8djnxhj0wqqbyzg2qhiie/SI.gdoc?dl=0&rlkey=jnjy82ov2km7vc0q1k6190esp). This is a live document that may be updated as additional data becomes available. For a version that is fixed at the time this manuscript was submitted, please see the link to our paper at the top of this README.

## Code Structure
```text
codes
├── data
│   ├── china
│   │   ├── collate_data.py
│   │   └── download_and_clean_JHU_china.R
│   ├── france
│   │   ├── download_and_clean_JHU_france.R
│   │   ├── format_infected.do
│   │   ├── format_policy.do
│   │   └── scrape_conf_cases_by_region.R
│   ├── iran
│   │   ├── download_and_clean_JHU_iran.R
│   │   ├── iran-split-interim-into-processed.py
│   │   └── iran_cleaning.R
│   ├── italy
│   │   ├── download_and_clean_JHU_italy.R
│   │   └── italy-download-cases-merge-policies.py
│   ├── korea
│   │   ├── download_and_clean_JHU_korea.R
│   │   ├── generate_KOR_interim.R
│   │   ├── korea-interim-to-processed.py
│   │   └── make_JHU_comparison_data.R
│   ├── multi_country
│   │   ├── download_6_countries_JHU.R
│   │   ├── get_JHU_country_data.R
│   │   └── get_adm_info.py
│   └── usa
│       ├── US_cleaning_school_district_closures.R
│       ├── add_testing_regimes_to_covidtrackingdotcom_data.ipynb
│       ├── check_health_data.R
│       ├── download_and_clean_JHU_usa.R
│       ├── download_latest_covidtrackingdotcom_data.py
│       ├── filter-processed-to-end-date.py
│       └── merge_policy_and_cases.py
├── models
│   ├── CHN_create_CBs.R
│   ├── CHN_generate_data_and_model_projection.R
│   ├── FRA_create_CBs.R
│   ├── FRA_generate_data_and_model_projection.R
│   ├── IRN_create_CBs.R
│   ├── IRN_generate_data_and_model_projection.R
│   ├── ITA_create_CBs.R
│   ├── ITA_generate_data_and_model_projection.R
│   ├── KOR_create_CBs.R
│   ├── KOR_generate_data_and_model_projection.R
│   ├── USA_create_CBs.R
│   ├── USA_generate_data_and_model_projection.R
│   ├── alt_growth_rates
│   │   ├── CHN_adm2.do
│   │   ├── FRA_adm1.do
│   │   ├── IRN_adm1.do
│   │   ├── ITA_adm2.do
│   │   ├── KOR_adm1.do
│   │   ├── MASTER_run_all_reg.do
│   │   └── USA_adm1.do
│   ├── get_gamma.py
│   ├── predict_felm.R
│   ├── projection_helper_functions.R
│   └── run_all_CB_simulations.R
├── plotting
│   ├── count-policies.py
│   ├── examine_lagged_relationship_between_new_deaths_recoveries_and_older_cases.R
│   ├── fig1.R
│   ├── fig2.R
│   ├── fig4_analysis.py
│   ├── figA2.py
│   └── gen_fig4.py
└── utils.py
```

## Replication Steps

There are four stages to our analysis:
1. Data collection and processing
2. Regression model estimation
3. SIR model projections
4. Figure creation

### Data collection and processing
The steps to obtain all data in <data/raw>, and then process this data into datasets that can be ingested into a regression, are described below. Note that some of the data collection was done through manual downloading of datasets and is described in as much detail as possible.

#### Manual data collection

For detailed information on the manual collection of policy, epidemiological, and population information, see the [up-to-date](https://www.dropbox.com/scl/fi/8djnxhj0wqqbyzg2qhiie/SI.gdoc?dl=0&rlkey=jnjy82ov2km7vc0q1k6190esp) version of our paper’s Appendix. A version that was frozen at the time of submission is available with the accompanying article.

Policy data for all countries was manually collected from a variety of sources and a mapping was developed from each policy to one of the variables we encode for our regression. These sources and mappings are listed in a csv or xlsx file for each country. These are:
- China: [data/raw/china/china_city_policy.xlsx](data/raw/china/china_city_policy.xlsx)
- France: [data/raw/france/france_policy_static_20200319.csv](data/raw/france/france_policy_static_20200319.csv)
- Iran: [data/raw/iran/covid_iran.xlsx](data/raw/iran/covid_iran.xlsx)
- Italy: [data/raw/italy/italy_policy_static_20200318.csv](data/raw/italy/italy_policy_static_20200318.csv)
- South Korea: [data/raw/korea/korea_policy_static_20200318.xlsx](data/raw/korea/korea_policy_static_20200318.xlsx)
- United States: [data/raw/usa/US_COVID-19_policies.csv](data/raw/usa/US_COVID-19_policies.csv)

Additional manual steps performed to collect population and/or epidemiological data, and to merge this with the above policy data, are described for each country below. Our epidemiological and policy data sources for all countries are listed [here](references/data_sources_static_20200321.xlsx), with a more frequently updated version [here](https://www.dropbox.com/scl/fi/v3o62qfrpam45ylaofekn/data_sources.gsheet?dl=0&rlkey=p3miruxmvq4cxqz7r3q7dc62t).

##### China
1. For data from January 24, 2020 onwards, we relied on [an open source GitHub project](https://github.com/BlankerL/DXY-COVID-19-Data). Download the data and save it to [data/raw/china/DXYArea.csv](data/raw/china/DXYArea.csv).
2. For data before January 24, 2020, we manually collected data, the file is in [data/raw/china/china_city_health_jan.xlsx](data/raw/china/china_city_health_jan.xlsx).
3. For city-level population data, the dataset is extracted from a compiled dataset of the 2010 Chinese City Statistical Yearbooks. We matched the city level population dataset to the city level COVID-19 epidemiology dataset. The file is in [data/raw/china/china_city_pop.csv](data/raw/china/china_city_pop.csv).

##### France
1. Download the latest file update for the number of confirmed cases per région from the [French government’s website](https://www.data.gouv.fr/en/datasets/fr-sars-cov-2/) and save it to [data/raw/france/fr-sars-cov-2-YYYYMMDD.xlsx](data/raw/france/fr-sars-cov-2-YYYYMMDD.xlsx).

##### Iran
1. Copy all of the date lines from the "New COVID-19 cases in Iran by province" table on the [Wikipedia page tracking this outbreak in Iran](https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Iran).
2. Open the excel file [data/raw/iran/covid_iran.xlsx](data/raw/iran/covid_iran.xlsx). This file contains the first step cleaning template for the cases data, as well as the information on key policy actions taken by the Iranian government. The tabs in this file are:

    a. `200314_cases_raw` :  A template into which raw data from the Wikipedia table -- see (1) -- should be pasted.

    b. `cases_cleaned--to_csv` :  A cleaned column format for the intermediate cases data. Simply extend the formulas (by copy/paste) in each row so that each row of the raw data is included. Do not change the column headings. Once all raw data has been included, save this tab to a csv file and save in [data/interim/iran/covid_iran_cases.csv](data/interim/iran/covid_iran_cases.csv).

    c. `200314_policies--to_csv` :  A list of the key policies Iran implemented to combat the coronavirus, and sources. A copy of the information in this tab is saved as [data/interim/iran/covid_iran_policies.csv](data/interim/iran/covid_iran_policies.csv). To update data with future policy changes, update this tab with the relevant information and replace the csv with a new copy of this tab.

##### South Korea
1. Download population data from [Statistics Korea](http://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B040A3&vw_cd=MT_ZTITLE&list_id=A6&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE) (a similar page in English is available [here](http://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B04005N&language=en))

    a. Click the `ITEM` tab and check the `Population` box only.

    b. Click the `By Administrative District` tab and check `1 Level Select all`.

    c. Click the `By Age Group` tab and check the `Total` box only.

    d. Click the `Time` tab and check `Monthly` and `2020.02`.

    e. Click the green `Search` button on the upper right of the window.

    f. Click the blue `Download` button under the `Search` button.

    g. Select `CSV` as `File format` and download.

    h. Open this file, remove the top two rows and the second column. Then change the header (the top row to `adm1_name, population`). Save to [data/interim/korea/KOR_population.csv](data/interim/korea/KOR_population.csv).

2. There is no automated script for constructing epidemiological variables (e.g. cumulative confirmed cases) as these were manually collected from various Korean provincial websites. Note that these provinces often report the data in different formats (e.g. pdf attachments, interactive dashboards) and usually do not have English translations. For more details on how we collected the data, please refer to the [Data Acquisition and Processing section in the appendix](https://www.dropbox.com/scl/fi/8djnxhj0wqqbyzg2qhiie/SI.gdoc?dl=0&rlkey=jnjy82ov2km7vc0q1k6190esp). 
This data is saved in [data/interim/korea/KOR_health.csv](data/interim/korea/KOR_health.csv).

#### Automated data collection and processing
Once the manual downloads are complete, execute the following scripts to download the remaining data and process the full set of input data across the six countries.

##### Multi-country
1.  `python codes/data/multi_country/get_adm_info.py`: Generates shapefiles and csvs with administrative unit names, geographies, and populations. **Note:** To run this script, you will need a U.S. Census API key. See [Setup](##Setup)
2. `Rscript codes/data/multi_country/download_6_countries_JHU.R`: Downloads 6 countries' data from the Johns Hopkins University Data underlying the dashboard [here](https://coronavirus.jhu.edu/map.html).

##### China
`python codes/data/china/collate_data.py`: Download, clean, and collate the Chinese city level dataset.

##### France
1. `Rscript codes/data/france/scrape_conf_cases_by_region.R`: R script that scrapes data on the number of confirmed cases by région in a table from the [Santé publique France website]  (https://www.santepubliquefrance.fr/maladies-et-traumatismes/maladies-et-infections-respiratoires/infection-a-coronavirus/articles/infection-au-nouveau-coronavirus-sars-cov-2-covid-19-france-et-monde). The script outputs [data/raw/france/france_confirmed_cases_by_region_yyyymmdd.csv](data/raw/france), where the date suffix is the date for the number of confirmed cases on the website, i.e. cases on yyyy-mm-dd. **Note**: Data from this site can only be downloaded in real-time. We therefore scrape this data once per day.
2. `stata -b do codes/data/france/format_infected.do`: Run in Stata to clean and format the French regional epidemiological dataset.
3. `stata -b do codes/data/france/format_policy.do`: Run in Stata to format the manually collected policy dataset and merge it with the epidemiological data.

##### Iran
1. `Rscript codes/data/iran/iran_cleaning.R`
2. `python codes/data/iran/iran-split-interim-into-processed.py`

##### Italy
`python codes/data/italy/italy-download-cases-merge-policies.py`: **Note**: You will need to have run [codes/data/multi_country/get_adm_info.py](codes/data/multi_country/get_adm_info.py) to generate [data/interim/adm](data/interim/adm) before running this.

##### South Korea

1. `Rscript codes/data/korea/generate_KOR_interim.R`: Constructs policy data and merges it with health and population data.
2. `python codes/data/korea/korea-interim-to-processed.py`: Formats this dataset.

##### United States
1. `python codes/data/usa/download_latest_covidtrackingdotcom_data.py`: Downloads testing regime data. **Note**: It seems this site has been getting high traffic and frequently fails to process requests. If this script throws an error due to that issue, try again later.
2. `jupyter nbconvert --ExecutePreprocessor.timeout=None --ExecutePreprocessor.kernel_name=python3 --execute codes/data/usa/add_testing_regimes_to_covidtrackingdotcom_data.ipynb`: Run the jupyter notebook and check that detected testing regime changes make sense, discard any false detections (it is in a notebook so you should manually check the detected changes, but you may run it directly using our choices).
3. `python codes/data/usa/merge_policy_and_cases.py`: Run the script to merge all data . This outputs [data/processed/adm1/USA_processed.csv](data/processed/adm1/USA_processed.csv).
4. `python codes/data/usa/filter-processed-to-end-date.py`: Run the script to filter [data/processed/adm1/USA_processed.csv](data/processed/adm1/USA_processed.csv) to exclude data after 3/18.
5. (optional) `Rscript codes/data/usa/check_health_data.R`: Confirm known data quality issues have been dealt with.

### Regression model estimation
Once data is obtained and processed, you can estimate regression models for each country using the following command:

`stata -b do codes/models/alt_growth_rates/MASTER_run_all_reg.do`

### SIR model projections
Once the regression coefficients have been estimated in the above models, run the following code to generate projections of active and cumulative infections using an SIR model:

1. `python codes/models/get_gamma.py`: Estimates removal rate to use in projections from data that contains both cumulative cases and active cases.
2. `Rscript codes/models/run_all_CB_simulations.R`: Generates the csv inputs for Figure 4.

### Figure creation
To generate the four figures in the paper, run the following scripts. Figure 1 only requires the data collection steps to be complete. Figures 2 and 3 require the regression step to be complete, and Figure 4 requires the projection step to be complete.

#### Figure 1

`Rscript codes/plotting/fig1.R`: Generates 12 outputs that constitute Figure 1 (`*_timeseries.pdf`, and `*_map.pdf` for each of the 6 countries).

#### Figure 2

`Rscript codes/plotting/fig2.R`: Generates 9 outputs that constitute Figure 2, in `results/figures/fig2`:
- *A1*: `Fig2_nopolicy.pdf`: Main figure for Panel A
- *A2*: `Fig2_effectsize_nopolicy.pdf`: Effect size values for Panel A
- *A3*: `Fig2_growth_nopolicy.pdf`: Effect size as percent growth values for Panel A
- *B1*: `Fig2_comb.pdf`: Main figure for Panel B 
- *B2*: `Fig2_effectsize_comb.pdf`: Effect size values for Panel B
- *B3*: `Fig2_growth_comb.pdf`: Effect size as percent growth values for Panel B
- *C1*: `Fig2_ind.pdf`: Main figure for Panel C 
- *C2*: `Fig2_effectsize_ind.pdf`: Effect size values for Panel C
- *C3*: `Fig2_growth_ind.pdf`: Effect size as percent growth values for Panel C

#### Figure 3

Figure 3 is generated by the regression estimation step (`codes/models/alt_growth_rates/MASTER_run_all_reg.do`).

#### Figure 4

Note that the outputs of [codes/plotting/fig1.R](codes/plotting/fig1.R) are required for Fig 4 as well.
1. (if not already generated) `Rscript codes/plotting/fig1.R)`: Generate the cases data
2. `python codes/plotting/gen_fig4.py`: Generate Figure 4.
3. `python codes/plotting/fig4_analysis.py`: Generate a printout of numerical results from the projections for each country.

#### Appendix Table A1

`python codes/plotting/count-policies.py`

#### Appendix Figure A1

Figure A1 is generated by the regression estimation step (`codes/models/alt_growth_rates/MASTER_run_all_reg.do`). The final output file is `figures/appendix/ALL_conf_cases_e.png`. Please note that if you're running the Stata console in Unix, .png file formats are not supported and you would need to change the final format in line 50 of `codes/models/alt_growth_rates/MASTER_run_all_reg.do` from .png to either .eps or .ps. For more information on supported file formats while using the `graph export` command on different operating systems, please click [here](https://www.stata.com/manuals13/g-2graphexport.pdf).

#### Appendix Figure A2

1. `Rscript codes/data/korea/make_JHU_comparison_data.R`: Creates [data/interim/korea/KOR_JHU_data_comparison.csv](data/interim/korea/KOR_JHU_data_comparison.csv)
2. `python codes/plotting/figA2.py`: Generates 2 outputs that constitute Figure A2 (`results/figures/appendix/figA2-1.pdf` and `results/figures/appendix/figA2-2.pdf`)