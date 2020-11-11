mergeMenu = nuke.menu('Nodes').findItem('Merge/Merges')
mergeMenu.addCommand('stencil','nuke.createNode('Merge','operation stencil bbox B'))