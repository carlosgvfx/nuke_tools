import nuke

###Version 1.0.0

def disableGPUAcceleration():
    for i in nuke.allNodes():
        if i.knob('useGPUIfAvailable'):
            i.knob('useGPUIfAvailable').setValue(0)



def enableGPUAcceleration():
    for i in nuke.allNodes():
        if i.knob('useGPUIfAvailable'):
            i.knob('useGPUIfAvailable').setValue(1)




