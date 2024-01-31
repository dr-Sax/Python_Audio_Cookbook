from pyo import *

s = Server().boot()

base_freq = 100

sines = [Sine(freq=(i*base_freq), mul=(1/(i))) for i in range(1,51)] # messing with amplitude

mixer = Mixer(outs=1, chnls=2)

for i in range(50):
    mixer.addInput('additive'+ str(i), sines[i])  # dictionary key with unique keys
    mixer.setAmp('additive'+ str(i), 0, .5) # map amplitude

sig = Sig(mixer[0], mul=.5).out()

sc = Scope(sig, gain=1)
sp = Spectrum(sig)

s.gui(locals())