# realtime-nonlinear
Pseudo-realtime computation of complexity features (eg. DFA, permutation/sample entropy etc...) on mobile EEG signals for ludo-aesthetic neurofeedback.

## CoCoBrainChannel


## EEGsynth


## Complexity & the brain

Spontaneous brain activity exhibits complex dynamics [(Tozzi, Zare & Benasich, 2016)](https://www.frontiersin.org/articles/10.3389/fnhum.2016.00247/full).

Self-organized criticality (SOC) is a major consequence of brain functionning (ref. Per Bak ?). It acts as a way of maintaining homeostasis through dynamical coupling with the environment (ref. Friston). Critical states are stable enough to maintain and process information while being flexible enough to let the system get entrained by external stimulations. Thus, qualifying the complex dynamics of brain signals might yield significant information about the corresponding phenomenological and cognitive states. Indeed, multiple information theoretics measures have been successfully applied to discriminate between mental states such as DFA (ref.), Hurst exponent (ref.), entropy (ref.), phi (ref.). 

To our knowledge, even if a study used fractal dimension as a training feature for neurofeedback applications [(Qiang, Sourina & Khoa, 2010)](https://www.researchgate.net/profile/Olga_Sourina/publication/228808406_A_Fractal_Dimension_Based_Algorithm_for_Neurofeedback_Games/links/565445fc08ae4988a7b0158f/A-Fractal-Dimension-Based-Algorithm-for-Neurofeedback-Games.pdf), these well-established nonlinear measures have yet to be applied in the context of neurofeedback training.

Because we don't hold specific hypotheses about the phenomenological and cognitive correlates of these measures, and because our end goal is to propose an enjoyable and transformative experience to whoever uses the setup, we adopt a passive BCI approach complemented with a manual (MIDI controler) exploration of active control opportunities. 


## Goal
Goal : Build a neurofeedback setup that outputs OSC control signals determined by complexity metrics computed in real-time on the signal streamed by a mobile EEG device (Muse 2016).

## Secondary objectives
 - [ ] Get a pull request from EEGsynth for the complexity module.
 - [ ] Build an EEGsynth module to fluidify online machine learning classification based on spectral and complex features.
 - [ ] Make a child's dream come true.

Key steps :
- [x] Stream a Muse signal to EEGsynth's FieldTrip buffer
- [x] Watch data accumulating in the buffer and create a feature extraction module
    - [x] Compute complexity using NeuroKit (https://github.com/neuropsychology/NeuroKit.py/blob/master/neurokit/signal/complexity.py)
- [ ] Normalize/calibrate the obtained measures to make them usable as control parameters (rescaling, baseline correction etc...)
- [ ] Continuously send the normalized features via OSC
- [ ] Profit
