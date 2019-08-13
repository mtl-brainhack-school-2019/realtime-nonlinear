#!/usr/bin/env python

import sys
from EEGsynth import preprocessing, spectral, plotspectral, plotsignal, historycontrol, postprocessing

inipath = '/home/stephen/PycharmProjects/eegsynth/module/inputcontrol/'

patch = []
patch.append(preprocessing(inifile=inipath + 'preprocessing.ini'))
patch.append(spectral(inifile=inipath + 'spectral.ini'))
patch.append(plotspectral(inifile=inipath + 'plotspectral.ini'))
patch.append(plotsignal())  # this is using only the defaults
patch.append(historycontrol(inifile=inipath + 'historycontrol.ini'))
patch.append(postprocessing(inifile=inipath + 'postprocessing.ini'))

for module in patch:
  module.setVerbosity(2)                        # overrule whatever is specified in the ini
  module.setRedis(host='localhost', port=6379)  # overrule whatever is specified in the ini
  module.setErrorHandler(sys.exit)              # stop the whole patch, an alternative could be to restart the module

if __name__ == "__main__":
  for module in patch:
    module.begin()
