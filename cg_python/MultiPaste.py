### Ernest Dios - copyConnected v1.0


import nuke
import nukescripts


def MultiPaste():
    selected = nuke.selectedNodes()
    for eachNode in selected:
        n = nuke.toNode(str(eachNode.name()))
        n.knob("selected").setValue(True)
        nuke.nodePaste("%clipboard%")


"""
import nuke

def paste_selected():

    for i in nuke.selectedNodes():
        i.setSelected(True)
        nuke.nodePaste("%clipboard%")

"""





