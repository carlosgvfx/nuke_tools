import nuke
import nukescripts
import re

def toggleTrackerTRS():
    n = nuke.thisNode()
    
    if n.Class() == 'Tracker4':
        k = n['tracks']
        items = re.findall('{ [0-9, ]*}', k.toScript())[0]
        tracks = int(items.split(' ')[-2])
        
        p = nukescripts.panels.PythonPanel('TRS')

        p.setTooltip('Select the boxes to enable TRS respectively')
        
        t = nuke.Boolean_Knob('t', 'T')
        r = nuke.Boolean_Knob('r', 'R')
        s = nuke.Boolean_Knob('s', 'S')

        # set values of first Track
        t.setValue(k.getValue(6))
        r.setValue(k.getValue(7))
        s.setValue(k.getValue(8))

        p.addKnob(t)
        p.addKnob(r)
        p.addKnob(s)

        ret = p.showModalDialog()

        if ret == 1:
            # T
            for i in range(0, tracks):
                k.setValue(p.knobs()['t'].value(), 31*i+6)

            #R
            for i in range(0, tracks):
                k.setValue(p.knobs()['r'].value(), 31*i+7)

            #S
            for i in range(0, tracks):
                k.setValue(p.knobs()['s'].value(), 31*i+8)

    else:
        nuke.message('This is a Tracker4 feature, please select a Tracker.')