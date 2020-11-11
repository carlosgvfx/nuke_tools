import nuke

def postStampOn():
    for r in nuke.allNodes('Read'):
	r.knob('postage_stamp').setValue(1)
    for n in nuke.selectedNodes():
	n.knob('postage_stamp').setValue(1)

def postStampOff():
    for r in nuke.allNodes('Read'):
	r.knob('postage_stamp').setValue(0)
    for n in nuke.selectedNodes():
	n.knob('postage_stamp').setValue(0)
