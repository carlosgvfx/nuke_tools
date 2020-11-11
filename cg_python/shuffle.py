import nuke

def  ShuffleRed():
	sr=nuke.createNode('Shuffle')     
	sr.knob('red').setValue('red')
	sr.knob('green').setValue('red')
	sr.knob('blue').setValue('red')
	sr.knob('alpha').setValue('red')
	sr.knob('name').setValue(checkNodeName('ShuffleRed'))
	sr.knob('tile_color').setValue(0xff0000ff)

def  ShuffleGreen():
	sg=nuke.createNode('Shuffle')
	sg.knob('red').setValue(2)
	sg.knob('green').setValue(2)
	sg.knob('blue').setValue(2)
	sg.knob('alpha').setValue(2)
	sg.knob('name').setValue(checkNodeName('ShuffleGreen'))
	sg.knob('tile_color').setValue(0xff00ff)

def  ShuffleBlue():
	sb=nuke.createNode('Shuffle')
	sb.knob('red').setValue(3)
	sb.knob('green').setValue(3)
	sb.knob('blue').setValue(3)
	sb.knob('alpha').setValue(3)
	sb.knob('name').setValue(checkNodeName('ShuffleBlue'))
	sb.knob('tile_color').setValue(0xffff)

def  ShuffleAlpha():
	sa=nuke.createNode('Shuffle')
	sa.knob('red').setValue(4)
	sa.knob('green').setValue(4)
	sa.knob('blue').setValue(4)
	sa.knob('alpha').setValue(4)
	sa.knob('name').setValue(checkNodeName('ShuffleAlpha'))
	sa.knob('tile_color').setValue(0xffffffff)

def  createShuffle():
	crs=nuke.createNode('Shuffle')
	crs.knob('label').setValue('[value red] > [value out]')

def checkNodeName(theName):
	#adds a number in brackets to the string if another node
	#exists with that name, otherwise just returns the string
	i = 1
	stillChecking = True
	origName = theName
	while stillChecking:
		alreadyUsed = False
		for a in nuke.allNodes():
			if (a['name'].value()==(theName)):
				alreadyUsed = True	
				break
		if alreadyUsed:
			theName = origName + ' (' + str(i) + ')'
			i = i+1	
		else:
			stillChecking=False
	
	return theName




    
