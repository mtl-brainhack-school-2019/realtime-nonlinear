from mne.io import read_raw_fif
from brainpipe.feature import power
import numpy as np
import neurokit
import time
import matplotlib.pyplot as plt
import neurokit
# 1.
# Fetch time series data from any file whatsoever
# Must be at least 30 seconds at 250Hz

raw = read_raw_fif('/home/hyruuk/GitHub/eegsynth/datafiles/SA04_01_preprocessed.fif.gz', preload=True)
raw_rs = raw.copy().resample(250)
sf = raw_rs.info['sfreq']

data = np.asarray(raw_rs.get_data()[1:3,7500:15000])


# 2.
# Compute hilbert using brainpipe
f = [ [2, 4], [4, 8], [8, 12], [12, 30], [30, 60] ]
npts = data.shape[1]
print(data.shape)
power_obj = power(sf, npts, f=f, baseline=None, norm=None, method='hilbert', window=None, width=None, step=None, split=None, time=None)
start = time.time()
power_vals = power_obj.get(data.T)
stop = time.time()
print(stop-start)
print(power_vals[0].shape)
print(power_vals[1])
print('Done')

powow = power_vals[0].squeeze()

dtp = powow[2,:,0]
t = np.arange(0,len(dtp),1)
plt.plot(t, dtp)
plt.show()

start = time.time()
comp = neurokit.complexity(dtp)
stop = time.time()
print("duration of computation :")
print(stop-start)
print(comp)

# 3.
# Compute complexity using neurokit
