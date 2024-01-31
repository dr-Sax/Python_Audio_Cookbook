from pyo import *

s = Server().boot()

fm = FM(carrier=800,ratio=0.25,index=0.75,mul=.2).mix(2).out()

sp = Spectrum(fm, size=4096)

s.gui(locals())