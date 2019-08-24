# realtime-nonlinear

Pseudo-realtime computation of complexity features (eg. DFA, permutation/sample entropy etc...) on mobile EEG signals for ludo-aesthetic neurofeedback.

## CoCoBrainChannel

The [CoCoBrainChannel](http://antoinebellemare.com/portfolio/coco-brain-channel-ccbc/) is a Python + PureData project with artistic and ludic purposes that aims to provide a musical soundscape in continuous interaction with the subject's mental state.
It is constituted of a PureData generative music patch that receives control signals from the Muse SDK suite and Python scripts that perform online classification of brain signals. This setup gives rise to a neurofeedback experience that breaks the border between internal and external states by producing a musical soundscapes that reflect the subject's mental state.

To date, CoCoBrainChannel uses spectral features (notably the Beta/Alpha ratio, Theta band power and Delta
band power) to produce control values that are either voluntarily controllable by the subject (Beta/Alpha) or reflect global cognitive states (Theta and Delta power). Additionally, Gamma power was used to classify facial muscular activty (frowning VS relaxed, smiling VS neutral) as it picked up a lot of non-cerebral electric sources.

Because CoCoBrainChannel was developped for Muse 2014/2016 headbands, and that Interaxon discontinued support for it's SDK, __using free community based alternatives like MuseLSL and EEGsynth has become a necessity to further develop this project__.

## EEGsynth

[EEGsynth](https://github.com/eegsynth/eegsynth)
![picture with alt](https://github.com/hyruuk/eegsynth/blob/master/doc/figures/communication.jpg "EEGsynth global architecture")

## Complexity & the brain

Spontaneous brain activity exhibits complex dynamics [(Tozzi, Zare & Benasich, 2016)](https://www.frontiersin.org/articles/10.3389/fnhum.2016.00247/full), suggesting that self-organized criticality (SOC) is a major consequence of brain functionning [(Beggs & Timme, 2012)](https://www.frontiersin.org/articles/10.3389/fphys.2012.00163/full). It acts as a way of maintaining homeostasis through dynamical coupling with the environment (ref. Friston). Critical states are stable enough to maintain and process information while being flexible enough to let the system get entrained by external stimulations. Thus, qualifying the complex dynamics of brain signals might yield significant information about the corresponding phenomenological and cognitive states. Indeed, multiple information theoretics measures have been successfully applied to discriminate between mental states such as DFA ([Lee et al., 2004](https://www.sciencedirect.com/science/article/abs/pii/S1350453304001183)), Hurst exponent (ref.), sample entropy (ex. [Bruce, Bruce & Vennelaganti, 2009](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2736605/), [See & Liang, 2011](https://ieeexplore.ieee.org/abstract/document/6026802), phi (ref.).
To our knowledge however, although one study used Higuchi's fractal dimension as a training feature for neurofeedback applications [(Qiang, Sourina & Khoa, 2010)](https://www.researchgate.net/profile/Olga_Sourina/publication/228808406_A_Fractal_Dimension_Based_Algorithm_for_Neurofeedback_Games/links/565445fc08ae4988a7b0158f/A-Fractal-Dimension-Based-Algorithm-for-Neurofeedback-Games.pdf), __these well-established complexity measures have never been applied in the context of artistic neurofeedback__.




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
    - [ ] Create a Jupyter-Notebook that describes this process and presents complexity measures[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mtl-brainhack-school-2019/realtime-nonlinear/master?filepath=https%3A%2F%2Fgithub.com%2Fmtl-brainhack-school-2019%2Frealtime-nonlinear%2Fblob%2Fmaster%2Fcomplexity_offline_test.ipynb)
    - [ ] Clean up the .py from obsolete code remaining from spectral.py
- [ ] Normalize/calibrate the obtained measures to make them usable as control parameters (rescaling, baseline correction etc...)
  - [ ] Use EEGsynth's post-processing module
- [ ] Continuously send the normalized features via OSC
  - [X] Adapt outputosc to make it use python-osc instead of pyOSC
    - [X] Bonus : end up doing a pull request for it
- [ ] Profit


## Secondary objectives

- [ ] Get a pull request from EEGsynth for the complexity module.
- [ ] Build an EEGsynth module to fluidify online machine learning classification based on spectral and complex features.
- [ ] Build an EEGsynth module that performs peak extraction across frequency bands mapped on the MIDI controler in order to send them to PureData's dissonance curves objects.
- [ ] Make a child's dream come true.

## Deliverables
- [ ] A blog post/markdown file detailing every step of the process
- [ ] A working version of the CBC2.0 that can be started from a nice .sh script
  - [ ] Use Docker or something in order to have an easy-to-install suite
- [ ] Upload a video illustrating the experience of using the CBC with feedback of complexity measures
