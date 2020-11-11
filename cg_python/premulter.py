import nuke

def  Premulter():
	myPremult = nuke.createNode('Unpremult') 
	myPremult ['channels'].setValue('all')
	#myPremult = nuke.createNode('NoOp')
	#myPremult ['label'].setValue('grading')   
	myPremult = nuke.createNode('Premult')
