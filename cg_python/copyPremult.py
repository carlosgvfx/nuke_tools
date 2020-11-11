import nuke

def  copyPremult():
	nuke.createNode('Copy')     
	nuke.createNode('Premult')
