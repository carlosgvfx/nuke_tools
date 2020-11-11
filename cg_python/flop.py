import nuke

def flopNodes():
    nodes = nuke.selectedNodes()

    maxX = max( [ n.xpos()+n.screenWidth()/2  for n in nodes ])
    minX = min( [ n.xpos()+n.screenWidth()/2  for n in nodes ])
    centreX = (maxX - minX)/2 + minX

    for n in nodes :
        n.setXpos( (centreX + (centreX-(n.xpos()+n.screenWidth()/2 )))-n.screenWidth()/2 )

def flipNodes():
    nodes = nuke.selectedNodes()

    maxY = max( [ n.ypos()+n.screenHeight()/2  for n in nodes ])
    minY = min( [ n.ypos()+n.screenHeight()/2  for n in nodes ])
    centreY = (maxY - minY)/2 + minY

    for n in nodes :
        n.setYpos( (centreY + (centreY-(n.ypos()+n.screenHeight()/2 )))-n.screenHeight()/2 )


def rotateNodes():
    nodes = nuke.selectedNodes()
    
    maxX = max( [ n.xpos()+n.screenWidth()/2  for n in nodes ])
    minX = min( [ n.xpos()+n.screenWidth()/2  for n in nodes ])
    centreX = (maxX - minX)/2 + minX
    
    maxY = max( [ n.ypos()+n.screenHeight()/2  for n in nodes ])
    minY = min( [ n.ypos()+n.screenHeight()/2  for n in nodes ])
    centreY = (maxY - minY)/2 + minY
    
    for r in nodes :
        rpx = r.xpos()  + r.screenWidth()/2
        rpy = r.ypos()  + r.screenHeight()/2
        r.setXpos( centreX - rpy  + centreY - r.screenWidth()/2 )
        r.setYpos( centreY + rpx  - centreX - r.screenHeight()/2 )
    
    bdnodes = nuke.selectedNodes('BackdropNode')
    for bd in bdnodes :
        bdposX = bd.xpos()
        bdposY = bd.ypos()
        bdsizeX = bd.knob('bdwidth').getValue()
        bdsizeY = bd.knob('bdheight').getValue()
        centreX = bdposX + bdsizeX/2
        centreY = bdposY + bdsizeY/2
        
        bd.setXpos( centreX - bdsizeY /2)
        bd.setYpos( centreY - bdsizeX /2)
        bd.knob('bdwidth').setValue(bdsizeY)
        bd.knob('bdheight').setValue(bdsizeX)