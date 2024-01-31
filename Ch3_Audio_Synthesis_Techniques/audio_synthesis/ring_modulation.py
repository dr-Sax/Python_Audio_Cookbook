from pyo import *

s = Server().boot()

mod = Sine(freq=500)
# Input() allows realtime mic audio input to be played with.
car = Sine(freq=1000)
# rm = Sig(car*mod, mul=.2).out() # single left speaker output
rm = Mix(car*mod, voices=2, mul=.2).out() # allows sounds to be sent to LR speakers

sp = Spectrum(rm)
sc = Scope(rm)

s.gui(locals()) 