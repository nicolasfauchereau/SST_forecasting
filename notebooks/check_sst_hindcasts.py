# %%
# %matplotlib inline 
from matplotlib import pyplot as plt

# %%
from datetime import date

# %%
import xarray as xr 
import pathlib

# %%
import yaml 
from yaml import SafeLoader

# %%
import pandas as pd

# %%
from seasonal_forecasting import C3S

# %%
with open('./CDS_config_operational.yaml') as f:
    dict_systems = yaml.load(f, Loader=SafeLoader)

# %%
dict_systems

# %%
dpath = '/media/nicolasf/END19101/ICU/data/CDS/operational'

dpath = pathlib.Path(dpath)

# %%
dpath = dpath.joinpath('hindcasts') 

# %%
dict_systems.keys()

# %%
smembers = []

for GCM in dict_systems.keys(): 
    
# for GCM in ['NCEP', 'JMA', 'ECCC_CanCM4i', 'ECCC_GEM5_NEMO']: 
    
    fpath = pathlib.Path('./tmp').joinpath(GCM)
    
    fpath.mkdir(parents=True, exist_ok=True)
    
    lfiles = list(dpath.joinpath(f"{GCM}/SST").glob("*.netcdf"))
    
    lfiles.sort() 
    
    ddates_members = {}

    for fname in lfiles: 

        dset = xr.open_dataset(fname) 

        dset = C3S.preprocess_GCM(dset) 
        
        fdate = f"{dset['time'].to_index().to_pydatetime()[0]:%Y-%m}"
        
        fg = dset.squeeze().sel(step=1)['sst'].plot(col='member', col_wrap=5) 
                
        fg.fig.savefig(fpath.joinpath(f'{GCM}_step1_{fdate}.png'), dpi=100, bbox_inches='tight', facecolor='w')
        
        plt.close(fg.fig)

        dsets = dset.stack(z=('lat','lon')).dropna('z') 

        dsets = dsets.dropna('member') 

        ddates_members[fdate] = len(dsets.member)
        
        dsets.close()
        
    s  = pd.Series(ddates_members)
    
    s = s.to_frame(name=GCM) 
    
    smembers.append(s) 


# %%
smembers = pd.concat(smembers, axis=1)

# %%
smembers = smembers.sort_index(ascending=False)

# %%
smembers

# %%
smembers.to_csv('./SST_hindcast_summary.csv') 

# %%
smembers.head()

# %%
smembers.tail()

# %%
