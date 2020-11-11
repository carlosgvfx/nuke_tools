
'''
@author: satheesh-R
for bugs and reports,,  mail - satheesrev@gmail.com
'''

### connect multiple nodes masks input to target node. Make sure your selecting the target node at last.
### Select the nodes need to connect and then shit+select the target node. If select with mouse drag function make sure to select the target node at last.
### Then hit the short-cut key. Bang!!!!  all your nodes mask input connected with target node.

import nuke

def connectMultipleMask():
    try:
        selNode = nuke.selectedNode()
    except ValueError: # no node selected
        pass
    selCheck = selNode.optionalInput()
    if selCheck > 0:
        for node in nuke.selectedNodes():
            min_inputs = node.minInputs()
            if min_inputs > 2:
                node.setInput(2, selNode)
            if min_inputs == 2:
                node.setInput(1, selNode)
            if min_inputs == 1:
                pass
    if selCheck == 0:
        for node in nuke.selectedNodes():
            min_inputs = node.minInputs()
            if min_inputs > 2:
                node.setInput(2, selNode)
            if min_inputs == 2:
                node.setInput(1, selNode)
            if min_inputs == 1:
                pass

