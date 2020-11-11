import nuke

def createDot1():
  test=nuke.toNode('ViewerDot1')
  if test == None :
      Vdot=nuke.createNode('Dot','',False)
      Vdot.knob('name').setValue('ViewerDot1')
      Vdot.knob('label').setValue('VWR_1')
      Vdot.knob('note_font_size').setValue(80)
      Vdot.knob('note_font_color').setValue(0x2aaa00ff)
      nuke.toNode('Viewer1').setInput(0,Vdot)
  else :
      toDel=nuke.toNode('ViewerDot1')
      nuke.delete(toDel)
      Vdot=nuke.createNode('Dot','',False)
      Vdot.knob('name').setValue('ViewerDot1')
      Vdot.knob('label').setValue('VWR_1')
      Vdot.knob('note_font_size').setValue(80)
      Vdot.knob('note_font_color').setValue(0x2aaa00ff)
      nuke.toNode('Viewer1').setInput(0,Vdot)

def createDot2():
  test=nuke.toNode('ViewerDot2')
  if test == None :
      Vdot=nuke.createNode('Dot','',False)
      Vdot.knob('name').setValue('ViewerDot2')
      Vdot.knob('label').setValue('VWR_2')
      Vdot.knob('note_font_size').setValue(80)
      Vdot.knob('note_font_color').setValue(0x2aaa00ff)
      nuke.toNode('Viewer1').setInput(1,Vdot)
  else :
      toDel=nuke.toNode('ViewerDot2')
      nuke.delete(toDel)
      Vdot=nuke.createNode('Dot','',False)
      Vdot.knob('name').setValue('ViewerDot2')
      Vdot.knob('label').setValue('VWR_2')
      Vdot.knob('note_font_size').setValue(80)
      Vdot.knob('note_font_color').setValue(0x2aaa00ff)
      nuke.toNode('Viewer1').setInput(1,Vdot)

def createDot3():
  test=nuke.toNode('ViewerDot3')
  if test == None :
      Vdot=nuke.createNode('Dot','',False)
      Vdot.knob('name').setValue('ViewerDot3')
      Vdot.knob('label').setValue('VWR_3')
      Vdot.knob('note_font_size').setValue(80)
      Vdot.knob('note_font_color').setValue(0x2aaa00ff)
      nuke.toNode('Viewer1').setInput(2,Vdot)
  else :
      toDel=nuke.toNode('ViewerDot3')
      nuke.delete(toDel)
      Vdot=nuke.createNode('Dot','',False)
      Vdot.knob('name').setValue('ViewerDot3')
      Vdot.knob('label').setValue('VWR_3')
      Vdot.knob('note_font_size').setValue(80)
      Vdot.knob('note_font_color').setValue(0x2aaa00ff)
      nuke.toNode('Viewer1').setInput(2,Vdot)

def createDot4():
  test=nuke.toNode('ViewerDot4')
  if test == None :
      Vdot=nuke.createNode('Dot','',False)
      Vdot.knob('name').setValue('ViewerDot4')
      Vdot.knob('label').setValue('VWR_4')
      Vdot.knob('note_font_size').setValue(80)
      Vdot.knob('note_font_color').setValue(0x2aaa00ff)
      nuke.toNode('Viewer1').setInput(3,Vdot)
  else :
      toDel=nuke.toNode('ViewerDot4')
      nuke.delete(toDel)
      Vdot=nuke.createNode('Dot','',False)
      Vdot.knob('name').setValue('ViewerDot4')
      Vdot.knob('label').setValue('VWR_4')
      Vdot.knob('note_font_size').setValue(80)
      Vdot.knob('note_font_color').setValue(0x2aaa00ff)
      nuke.toNode('Viewer1').setInput(3,Vdot)

def resetViewer():
  Mviewer=nuke.toNode('Viewer1')
  dot1=nuke.toNode('ViewerDot1')
  dot2=nuke.toNode('ViewerDot2')
  dot3=nuke.toNode('ViewerDot3')
  dot4=nuke.toNode('ViewerDot4')
  Mviewer.setInput(3,dot4)
  Mviewer.setInput(2,dot3)
  Mviewer.setInput(1,dot2)
  Mviewer.setInput(0,dot1)


def removeViewer():
  for n in nuke.allNodes(): #from all nodes 
   if n['label'].value() == 'VWR_1':
      nuke.delete(n) #delete all...

  for n in nuke.allNodes(): #from all nodes 
   if n['label'].value() == 'VWR_2':
      nuke.delete(n) #delete all...

  for n in nuke.allNodes(): #from all nodes 
   if n['label'].value() == 'VWR_3':
      nuke.delete(n) #delete all...

  for n in nuke.allNodes(): #from all nodes 
   if n['label'].value() == 'VWR_4':
      nuke.delete(n) #delete all...
