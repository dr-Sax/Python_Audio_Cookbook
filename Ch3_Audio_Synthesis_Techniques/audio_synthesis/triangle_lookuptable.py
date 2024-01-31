from pyo import *

s = Server().boot()

tritab = TriangleTable(order=40).normalize()
lookup = Osc(table=tritab, interp=2, freq=200, mul=.2).out()

sc = Scope(lookup, gain=1)

s.gui(locals())