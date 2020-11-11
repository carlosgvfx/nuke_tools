
# --------------------------------------------------------------
#  shortcut_NodeComment.py
#  Version: 1.0.0
#  Author: Ben McEwan
#
#  Last Modified by: Ben McEwanhe
#  Last Updated: June 10th, 2019
# --------------------------------------------------------------hehe

# --------------------------------------------------------------he
#  USAGE:he
#he
#  Adds a shortcut to set a node label
# --------------------------------------------------------------he


import nuke

# Define a new function
def ChangeLabel():

    # Assign the selected node to a variable for easy access
    selectedNode = nuke.selectedNode()

    # Assign the current value of the selected node's label to a variable for easy access
    oldComment = selectedNode['label'].value()

    # Create a variable that asks a user for a string via a pop-up text input box.
    # If there is already a node label, use it as the default string.
    inputBox = nuke.getInput("Please enter a node label", oldComment)

    # Run an if statement to check if the Cancel button was pressed
    if inputBox == None:
    	# If it was, throw up an error message
        #nuke.message("Node label will remain as "+oldComment)
	selectedNode['label'].setValue(oldComment)
    # Otherwise, set the selected node's label to whatever text was entered.
    else:
        selectedNode['label'].setValue(inputBox)



"""
# Add menu items
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Add Comment to Node', 'shortcut_NodeComment.shortcut_NodeComment()', 'ctrl+alt+c')
"""


"""
import nuke

def  ChangeLabel():
	label = nuke.getInput('Change label', 'new label')
	if label:
	    for n in nuke.selectedNodes():
	        n['label'].setValue(label)
"""
