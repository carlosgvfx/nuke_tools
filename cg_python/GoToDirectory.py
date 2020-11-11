# Max van Leeuwen - maxvanleeuwen.com
# GoToDirectory - 1.2
#
# Opens the directory of the path that is currently in the clipboard - except if nodes with a fileKnob are selected, in which case the file paths of the selected nodes will be opened.



import os
import nuke
import subprocess
import sys



GoToDirectoryMessage = '[GoToDirectory] '



def get_clipboard_text():

	text = ""

	# get clipboard text
	try:
		from PySide2 import QtWidgets
	except:
		from PySide import QtGui as QtWidgets

	text = QtWidgets.QApplication.clipboard().text()
	
	# return clipboard text
	return text



def openFolderFromString(folder):

	# for easy string manipulation, make sure all slashes are forward ('/')
	folder = folder.replace('\\', '/')

	# create a new variable for the path to open
	foundFolderPath = folder

	# check if the path is a directory
	if not os.path.isdir(foundFolderPath):

		# only try to find a working parent path 5 times
		attempts = 0
		folderFound = False
		while (attempts < 5) and (not folderFound):

			# try the parent of the previous folder
			foundFolderPath = os.path.dirname(foundFolderPath)

			if os.path.isdir(foundFolderPath):

				# it works!
				folderFound = True

			else:

				# this folder does not exist
				attempts += 1


	# check if the result is a folder
	if os.path.isdir(foundFolderPath):

		# reverse the backslashes on Windows
		if sys.platform == 'win32':
			BackslashfixPluginsdir = foundFolderPath.replace("/", "\\")

			# and open the path in windows explorer
			os.startfile(BackslashfixPluginsdir)

		else:

			# open for Mac or Linux
			opener ="open" if sys.platform == "darwin" else "xdg-open"
			subprocess.call([opener, foundFolderPath])

	else:
		
		print (GoToDirectoryMessage + "Not a valid path - checked up to 5 parent directories:\n" + GoToDirectoryMessage + folder)



def GoToDirectory():

	# bool to open dir from a node or from clipboard
	fromNode = False

	# if nodes are selected
	if len(nuke.selectedNodes()) > 0:

		# for each selected node
		for n in nuke.selectedNodes():

			# check if the selected knobs are file paths (of any kind - Read, DeepRead, ReadGeo, etc.)
			for k in n.knobs():
				if n[k].Class() == 'File_Knob':

					# get its value
					v = n[k].getValue()

					# open folder
					openFolderFromString(v.replace('/', '\\'))

					# set bool
					fromNode = True
				

	# if no knob paths were opened
	if not fromNode:

		# open the folder from the string returned by get_clipboard_text()
		openFolderFromString(get_clipboard_text())


# autostart (if not imported)
if __name__ == "__main__":
	GoToDirectory()