from pyo import *

s = Server().boot()

bal = SigTo(.75) # linear interpolation between previous and current value

samp = SfPlayer(SNDS_PATH + '/transparent.aif',loop=True,mul=.4)
verb = Freeverb(samp, size=[.79,.8], damp=.9, bal=bal).out()

def restore_verb():

    bal.setTime(5)
    bal.setValue(.75)
    
ca = CallAfter(restore_verb, time=1)  # delay calling a function without stalling program
ca.stop()

def reset_verb():  # clears the memory of reverberation

    verb.reset()

bal.setTime(0)  # dry
bal.setValue(0)  # dry
ca.play()
s.gui(locals())