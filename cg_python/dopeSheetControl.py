import nuke

def dopeSheetOff():
	for node in nuke.allNodes(recurseGroups=True):
		if node.knob('dope_sheet'):
			node['dope_sheet'].setValue(False)




#def dopeSheetOff():
#    for r in nuke.allNodes():
#	r.knob('dope_sheet').setValue(0)
#    for n in nuke.selectedNodes():
#	n.knob('dope_sheet').setValue(0)
