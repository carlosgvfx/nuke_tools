import nuke

#t=nuke.menu("Nodes")
#u=t.addMenu("Pixelfudger", icon="PxF_Menu.png")

cgToolBar = nuke.menu("Nodes").addMenu("CG_Tools/Pixelduger", icon = "PxF_Menu.png")
 
cgToolBar.addCommand( "PxF_Bandpass", "nuke.createNode('PxF_Bandpass')", icon="PxF_Bandpass.png" ) 
cgToolBar.addCommand( "PxF_ChromaBlur", "nuke.createNode('PxF_ChromaBlur')", icon="PxF_ChromaBlur.png") 
cgToolBar.addCommand( "PxF_Distort", "nuke.createNode('PxF_Distort')", icon="PxF_Distort.png") 
cgToolBar.addCommand( "PxF_Erode", "nuke.createNode('PxF_Erode')", icon="PxF_Erode.png")
cgToolBar.addCommand( "PxF_Filler", "nuke.createNode('PxF_Filler')", icon="PxF_Filler.png") 
cgToolBar.addCommand( "PxF_Grain", "nuke.createNode('PxF_Grain')", icon="PxF_Grain.png") 
cgToolBar.addCommand( "PxF_HueSat", "nuke.createNode('PxF_HueSat')", icon="PxF_HueSat.png")  
cgToolBar.addCommand( "PxF_IDefocus", "nuke.createNode('PxF_IDefocus')", icon="PxF_IDefocus.png")
cgToolBar.addCommand( "PxF_KillSpill", "nuke.createNode('PxF_KillSpill')", icon="PxF_KillSpill.png") 
cgToolBar.addCommand( "PxF_Line", "nuke.createNode('PxF_Line')", icon="PxF_Line.png" ) 
cgToolBar.addCommand( "PxF_MergeWrap", "nuke.createNode('PxF_MergeWrap')", icon="PxF_MergeWrap.png" ) 
cgToolBar.addCommand( "PxF_ScreenClean", "nuke.createNode('PxF_ScreenClean')", icon="PxF_ScreenClean.png")
