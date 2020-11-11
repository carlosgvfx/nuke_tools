import nuke
isAutoChangeKnobs = False

def autoChangeKnobs():
    global isAutoChangeKnobs
    DAGcolor = nuke.toNode('preferences').knob('DAGBackColor');
    
    if isAutoChangeKnobs:
        nuke.removeKnobChanged(_autoChangeKnobs)
        #nuke.tcl('puts','Auto-Change Knobs: Off')
        DAGcolor.setValue(DAGcolor.value() - 0x10000000)
    
    else:
        nuke.addKnobChanged(_autoChangeKnobs)
        #nuke.tcl('puts','Auto-Change Knobs: On')
        DAGcolor.setValue(DAGcolor.value() + 0x10000000)
        
    isAutoChangeKnobs = not isAutoChangeKnobs

    return isAutoChangeKnobs


def autoChangeKnobsEnable(Enable):
    global isAutoChangeKnobs
    if (isAutoChangeKnobs == Enable):
        return isAutoChangeKnobs
    return autoChangeKnobs()


def _autoChangeKnobs():
  selNodes = nuke.selectedNodes()
  if not selNodes:
    return
  checkExpression = True

  for n in selNodes:
    if nuke.thisNode() == n:
      continue
    try:
      if nuke.thisKnob().name() == 'xpos' or nuke.thisKnob().name() == 'ypos' or nuke.thisKnob().name() == 'selected' or nuke.thisKnob().name() == 'name':
        continue
      if checkExpression and nuke.thisKnob().hasExpression():
        expr = nuke.thisKnob().toScript(0,None)
        if expr.find(nuke.thisKnob().name())<0:
          n.knob(nuke.thisKnob().name()).fromScript(expr)
      else:
        n.knob(nuke.thisKnob().name()).setValue(nuke.thisKnob().value())
    except:
      pass
