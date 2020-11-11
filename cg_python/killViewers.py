import nuke

def killViewers():
    for v in nuke.allNodes('Viewer'):
	nuke.delete(v)
nuke.addOnScriptLoad(killViewers)








