import PyHydro
import numpy as np
import pandas as pd

major_ver = 1
minor_ver = 11.0
edit_name = "D"
PyHydro.test_version(major_ver, minor_ver, edit_name)

# Generate some sample daily streamflow data for demonstration
# ! sample data is generated using numpy random function
np.random.seed(42)
n_days = 365
streamflow = np.random.gamma(shape=2, scale=1, size=n_days)
streamflow = streamflow * 100

station = 'Station A'
PyHydro.FDC(streamflow, title = station)


# ! sample data is generated using numpy random function
# make some sample water quality data in daily scale from 2022-1-1 to 2024-12-31
dates = pd.date_range(start='2022-01-01', end='2024-12-31', freq='D')
n_days = len(dates)
wq_data = pd.DataFrame({
    'Date': dates,
    'T-N': np.random.gamma(shape=2, scale=1, size=n_days),
    'T-P': np.random.gamma(shape=3, scale=1, size=n_days),
    'SS': np.random.gamma(shape=4, scale=1, size=n_days)
})
wq_data.set_index('Date', inplace=True)

PyHydro.boxplot(wq_data, criteria='all')
PyHydro.boxplot(wq_data, criteria='monthly')
PyHydro.boxplot(wq_data, criteria='annual')
PyHydro.boxplot(wq_data, criteria='seasonal')


# ! sample data is generated using numpy random function
# make streamflow and precip data from 2022-1-1 to 2024-12-31
dates = pd.date_range(start='2022-01-01', end='2024-12-31', freq='D')
n_days = len(dates)
sp_df = pd.DataFrame({
    'Date': dates,
    'streamflow': np.random.gamma(shape=2, scale=1, size=n_days),
    'precip': np.random.gamma(shape=3, scale=1, size=n_days)
})
sp_df.set_index('Date', inplace=True)

PyHydro.hydrograph(sp_df, title = station)




# make hundreds of sample random numbers for validation. ranged from 0 to 1000.
simlist = np.random.randint(0, 1000, size=100)
vallist = [i*np.random.uniform(0.8,1.2) for i in simlist]

PyHydro.sim_vali(simlist, vallist, title=station)