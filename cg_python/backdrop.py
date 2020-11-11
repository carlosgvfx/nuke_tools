
import nuke
import random

def CreateBackD() :
    nodes = nuke.selectedNodes()
    amount = len(nodes)
    if amount ==0:       return  

    lowX= min( [ n.xpos() for n in nodes ] )
    highX= max( [ n.xpos() for n in nodes ] )
    lowY= min( [ n.ypos() for n in nodes ] )
    highY= max( [ n.ypos() for n in nodes ] )

    backD=nuke.createNode('BackdropNode')
    backD.knob('bdwidth').setValue(highX-lowX+120)
    backD.knob('bdheight').setValue(highY-lowY+140)
    backD.setXpos(lowX-20)
    backD.setYpos(lowY-100)
    backD.knob('note_font_size').setValue(62)
    backD.knob("tile_color").setValue( 306+ int(random.random()*400)*10000000 )
    
#   (0x2d2d2dff)
#( 306+ int(random.random()*400)*10000000 )

def GrowBackD():
  nodes=nuke.selectedNodes('BackdropNode')
  for sel in nodes:
    selw=sel.knob('bdwidth').getValue()
    selh=sel.knob('bdheight').getValue()
    selxp=sel.xpos()
    selyp=sel.ypos()
  
    sel.knob('bdwidth').setValue(selw+20)
    sel.knob('bdheight').setValue(selh+20)
    sel.setXpos(selxp-10)
    sel.setYpos(selyp-10)

def ShrinkBackD():
  nodes=nuke.selectedNodes('BackdropNode')
  for sel in nodes:
    selw=sel.knob('bdwidth').getValue()
    selh=sel.knob('bdheight').getValue()
    selxp=sel.xpos()
    selyp=sel.ypos()
  
    sel.knob('bdwidth').setValue(selw-20)
    sel.knob('bdheight').setValue(selh-20)
    sel.setXpos(selxp+10)
    sel.setYpos(selyp+10)

def GrowBdropUp():
  sel=nuke.selectedNodes('BackdropNode')
  for nodes in sel:
    selbh=nodes.knob('bdheight').getValue()
    nodes.knob('bdheight').setValue(selbh+20)
    selby=nodes.ypos()
    nodes.setYpos(selby-20)

def GrowBdropDown():
  sel=nuke.selectedNodes('BackdropNode')
  for nodes in sel:
    selbh=nodes.knob('bdheight').getValue()
    nodes.knob('bdheight').setValue(selbh+20)

def GrowBdropRight():
  sel=nuke.selectedNodes('BackdropNode')
  for nodes in sel:
    selbw=nodes.knob('bdwidth').getValue()
    nodes.knob('bdwidth').setValue(selbw+20)

def GrowBdropLeft():
  sel=nuke.selectedNodes('BackdropNode')
  for nodes in sel:
    selbw=nodes.knob('bdwidth').getValue()
    nodes.knob('bdwidth').setValue(selbw+20)
    selbx=nodes.xpos()
    nodes.setXpos(selbx-20)
 
def ShrinkBdropUp():
  sel=nuke.selectedNodes('BackdropNode')
  for nodes in sel:
    selbh=nodes.knob('bdheight').getValue()
    nodes.knob('bdheight').setValue(selbh-20)
    selby=nodes.ypos()
    nodes.setYpos(selby+20)

def ShrinkBdropDown():
  sel=nuke.selectedNodes('BackdropNode')
  for nodes in sel:
    selbh=nodes.knob('bdheight').getValue()
    nodes.knob('bdheight').setValue(selbh-20)

def ShrinkBdropRight():
  sel=nuke.selectedNodes('BackdropNode')
  for nodes in sel:
    selbw=nodes.knob('bdwidth').getValue()
    nodes.knob('bdwidth').setValue(selbw-20)

def ShrinkBdropLeft():
  sel=nuke.selectedNodes('BackdropNode')
  for nodes in sel:
    selbw=nodes.knob('bdwidth').getValue()
    nodes.knob('bdwidth').setValue(selbw-20)
    selbx=nodes.xpos()
    nodes.setXpos(selbx+20)
