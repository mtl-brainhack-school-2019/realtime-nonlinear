# realtime-nonlinear
Application of non-linear metrics (eg. Granger causality, Hurst exponent, permutation/sample entropy etc..) to real-time EEG signals for neurofeedback.


Goal : Build a neurofeedback setup that outputs OSC control signals determined by complexity metrics computed in real-time on the signal streamed by a mobile EEG device (Muse 2016).


Key steps :
- [x] Stream a Muse signal to EEGsynth's FieldTrip buffer
- [ ] Watch data accumulating in the buffer and create a feature extraction module (based on e.g. PyEEG, Brainpipe and MNE)
    - [ ] Compute Hurst using pyeeg (https://github.com/forrestbao/pyeeg/blob/master/pyeeg/hurst.py)
    - [ ] Compute complexity using NeuroKit (https://github.com/neuropsychology/NeuroKit.py/blob/master/neurokit/signal/complexity.py)
- [ ] Normalize/calibrate the obtained measures to make them usable as control parameters (rescaling, baseline correction etc...)
- [ ] Continuously send the normalized features via OSC
