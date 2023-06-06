# SST hindcasts and forecasts verification, including MHWs conditions 

## pre-requesites  

### seasonal_forecasting library 

You will need to install the library 'seasonal_forecasting', this can be found at https://git.niwa.local/fauchereaun/seasonal_forecasting and can be installed with 

```
pip install -e .
```

### SST hindcast and forecast data from the C3S suite of GCMs 

The SST hindcast (1993 - 2016) and forecast (2017 - now) data needs to be downloaded and up to date, i.e. make sure you have the correct GCM <> system combo. 

for this the suite of scripts developped for the NIWA's Seasonal Climate Outlook (SCO) can be used, ask Ben and / or Tristan for use, the scripts are also on gitlab at the above URL

### Observed SST data for verification  

The dataset of choice for the SST forecasts / hindcasts is OISST, the notebook to download and / or update the global files (daily, as well as monthly calculated from the daily dataset) is `update_OISST.ipynb`

### verification of the deterministic SST hindcasts 

Deterministic SST forecasts are the MME average of the forecast SST anomalies, their verification over the hindcast period is handled by `verification_deterministic_sst.ipynb`

### verification of the probabilistic SST hindcasts for Marine Heat Waves (MHWs) conditions 

The binary forecasts for each member of each couple GCM are derived from the seasonally varying and lead-time dependent 90th percentile. If a predicted value for a gridpoint exceeds this threshold, then it is in MHWs conditions and the value is set to 1, if not it is set to 0, the probability for MHW conditions accross the C3S MME can just be calculated as the ensemble average of these binary forecasts. The notebook is `verification_probabilistic_sst_allGCMs.ipynb`.

### identification of the most recent (i.e. post 2017, forecast period for the C3S MME) MHWs around NZ, and case study / evaluation of the forecasts of these events 

See `read_forecasts_and_evaluate.ipynb`

### derive time-series for point locations in the observations, and correlate with observed SST fields as well as the C3S MME forecasts

See `read_forecasts_and_evaluate.ipynb` 

### some ancillary / utility notebooks

- `number_of_members.ipynb`: Calculate the number of members for each month, and each GCM, over the hindcast or forecast period, and saves to disk in `SST_hindcasts_summary_from_df.csv` and `SST_forecasts_summary_from_df.csv` respectively

- `ACC_variability_and_ENSO.ipynb`: Investigat the relationship between variability in the C3S MME ACC (Anomaly Correlation Coefficient) and ENSO, via correlations and composite analysis. 













