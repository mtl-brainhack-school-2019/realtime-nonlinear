# realtime-nonlinear
Pseudo-realtime computation of complexity features (eg. DFA, permutation/sample entropy etc...) on mobile EEG signals for ludo-aesthetic neurofeedback.

## CoCoBrainChannel

The CoCoBrainChannel is a Python + PureData project with artistic and ludic purposes that aims to provide a musical soundscape in continuous interaction with the subject's mental state. 
Because CoCoBrainChannel was developped for Muse 2014/2016 headbands, and that Interaxon discontinued support for it's SDK, using open-source community based alternatives like MuseLSL and EEGsynth has become a necessity to further develop this project.

## EEGsynth


## Complexity & the brain

Spontaneous brain activity exhibits complex dynamics [(Tozzi, Zare & Benasich, 2016)](https://www.frontiersin.org/articles/10.3389/fnhum.2016.00247/full), suggesting that self-organized criticality (SOC) is a major consequence of brain functionning (ref. Per Bak ?). It acts as a way of maintaining homeostasis through dynamical coupling with the environment (ref. Friston). Critical states are stable enough to maintain and process information while being flexible enough to let the system get entrained by external stimulations. Thus, qualifying the complex dynamics of brain signals might yield significant information about the corresponding phenomenological and cognitive states. Indeed, multiple information theoretics measures have been successfully applied to discriminate between mental states such as DFA (ref.), Hurst exponent (ref.), entropy (ref.), phi (ref.). 

To our knowledge, although one study used Higuchi's fractal dimension as a training feature for neurofeedback applications [(Qiang, Sourina & Khoa, 2010)](https://www.researchgate.net/profile/Olga_Sourina/publication/228808406_A_Fractal_Dimension_Based_Algorithm_for_Neurofeedback_Games/links/565445fc08ae4988a7b0158f/A-Fractal-Dimension-Based-Algorithm-for-Neurofeedback-Games.pdf), these well-established nonlinear measures have never been applied in the context of artistic neurofeedback.




## Goal
Goal : Build a neurofeedback setup that outputs OSC control signals determined by complexity measures computed in real-time on the signal streamed by a mobile EEG device (Muse 2016).

Because we don't hold specific hypotheses about the phenomenological and cognitive correlates of complexity measures, and because our end goal is to propose an enjoyable and transformative experience to whoever uses the setup, we adopt a passive BCI approach complemented with a manual (MIDI controler) exploration of active control opportunities given by the features.

## Key objectives
- [x] Install and run EGGsynth
  - [x] FieldTrip buffer up
  - [x] Redis database up
  - [x] Python modules up
- [x] Stream a Muse signal to EEGsynth's FieldTrip buffer
  - [x] Install and use MuseLSL (might work with BlueMuse for Windows, if you can handle the EEGsynth part) to stream Muse via LSL
  - [x] Catch LSL stream and send it to FT buffer via lsl2ft module
- [ ] Create a feature extraction module
  - [x] Compute complexity using NeuroKit (https://github.com/neuropsychology/NeuroKit.py/blob/master/neurokit/signal/complexity.py)
    - [ ] 8/12 measures return NaN, wtf is going on
    - [ ] Get an idea of how the window size influence measures robustness
  - [ ] Clean up the .py from obsolete code remaining from spectral.py
- [ ] Normalize/calibrate the obtained measures to make them usable as control parameters (rescaling, baseline correction etc...)
  - [ ] Use EEGsynth's post-processing module
- [ ] Continuously send the normalized features via OSC
  - [ ] Use EEGsynth's outputosc module
- [ ] Profit


## Secondary objectives
 - [ ] Get a pull request from EEGsynth for the complexity module.
 - [ ] Build an EEGsynth module to fluidify online machine learning classification based on spectral and complex features.
 - [ ] Build an EEGsynth module that performs peak extraction across frequency bands mapped on the MIDI controler in order to send them to PureData's dissonance curves objects.
 - [ ] Make a child's dream come true.
