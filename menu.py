# --------------------------------------------------------------
#  menu.py
#  Version: 1.0.0
#  Last Updated: August 8th, 2020
# --------------------------------------------------------------

# --------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------


import nuke
import nukescripts
import sys
import os


# --------------------------------------------------------------
#  PYTHON TEST ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import dailieSourcer

CG=nuke.menu('Nuke').addMenu('python_test')
CG.addCommand('python/dailieSourcer','dailieSourcer.dailieSourcer()')

import importLigthingNukeSetup
CG.addCommand('python/import Ligthing Script','importLigthingNukeSetup.importLigthingNukeSetup()')

import importLineup
CG.addCommand('python/Lineup','importLineup.importLineup()')





# --------------------------------------------------------------
#  PYTHON SCRIPTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------


import reloadRead
import GoToDirectory

#import shuffle
import shuffleShortcuts
import copyPremult
import premulter

import flop
import alignNodes
import ChangeLabel
import rotoOutput

import autoChangeKnobs
import backdrop
import StickyNoter
import postStampControl
import dopeSheetControl
import MultiPaste
import connectMultipleMask
import connectMultiple

import killViewers
import viewer
import GPU_OnOff 

import myTransform
import myMerge
import merge_transforms_v2
#('Transform/mergeTransforms', 'merge_transforms_v2.start()')

import stamps
import KnobScripter

import channel_hotbox
nuke.menu("Nuke").findItem("Edit").addCommand("HotBox", 'channel_hotbox.start()', "`")

import versionToLatest
nuke.menu( 'Nuke' ).addCommand( 'Edit/Node/Filename/Version to Latest (Reads only)' , versionToLatest.versionToLatest)


import sb_distributeObjects
sb_tools = nuke.toolbar("Nodes").addMenu( "sb_Tools", icon = "sb_tools.png" )
sb_tools.addCommand('Python/sb DistributeObjects', 'sb_distributeObjects.sb_distributeObjects()')


#shortcuteditor
try:
    import shortcuteditor
    shortcuteditor.nuke_setup()
except Exception:
    import traceback
    traceback.print_exc()


#Closed nodes properties
def close():
    [node.hideControlPanel() 
for node in nuke.allNodes()]

nuke.menu( 'Nodes' ).addCommand( 'close', 'close()' , 'shift+d')

"""
def MultiPaste():
    selected = nuke.selectedNodes()
    for eachNode in selected:
        n = nuke.toNode(str(eachNode.name()))
"""


#FrameHold to set current frame
"""
def customFrameHold():
    n = nuke.thisNode()
    n.addKnob(nuke.PyScript_Knob('setFrame', "Set to Current Frame", "{nuke.thisNode()['first_frame'].setValue(nuke.frame())}"))

nuke.addOnCreate(customFrameHold, nodeClass="FrameHold")
"""
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')


#Adjust icon size
def iconSizeIncrement ( amount = 20 ):
    preferences = nuke.toNode('preferences')
    currentIconSize = preferences ['icon_size_base'].value()
    preferences['icon_size_base'].setValue(currentIconSize + amount)

def iconSizeDecrement ( amount = 20 ):
    preferences = nuke.toNode('preferences')
    currentIconSize = preferences ['icon_size_base'].value()
    preferences['icon_size_base'].setValue(currentIconSize - amount)





mergeMenu = nuke.menu('Nodes').findItem('Merge/Merges')
mergeMenu.addCommand('Difference','nuke.createNode("Merge2", "operation difference")')
mergeMenu.addCommand('Disjoint Over','nuke.createNode("Merge2", "operation disjoint-over")')
mergeMenu.addCommand('Divide','nuke.createNode("Merge2", "operation divide")')
mergeMenu.addCommand('From','nuke.createNode("Merge2", "operation from")')
mergeMenu.addCommand('Geometric','nuke.createNode("Merge2", "operation geometric")')
mergeMenu.addCommand('Mask','nuke.createNode("Merge2", "operation mask")')
mergeMenu.addCommand('Minus','nuke.createNode("Merge2", "operation minus")')
mergeMenu.addCommand('Stencil','nuke.createNode("Merge2", "operation stencil bbox B")')
mergeMenu.addCommand('Under','nuke.createNode("Merge2", "operation under")')




# --------------------------------------------------------------
#  KNOB DEFAULT ::::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

#knobDefault
#Viewer
nuke.knobDefault('Viewer.hide_input','True')
nuke.knobDefault('Viewer.note_font_size','66')
nuke.knobDefault('Viewer.tile_color','0x7fff00ff')
nuke.knobDefault('views_colours','True')

#Dot
nuke.knobDefault('Dot.tile_color','0xff')

#ClipType.no_clip
nuke.knobDefault('cliptype','no_clip')

#Shutteroffset.centre
nuke.knobDefault('shutteroffset','centred')

#DeepRead.black_outside
nuke.knobDefault("DeepRead.black_outside","false")

#DRAW
#Bezier
tb = nuke.toolbar("Nodes")
tb.addCommand("Draw/Bezier","nuke.createNode(\"Bezier\")", icon="Bezier.png", )


#Bezier.linear
nuke.knobDefault("Bezier.linear","true") 
#Roto.rgba
nuke.knobDefault("Roto.output","rgba")
nuke.knobDefault("Roto.cliptype","none")


#Rotopaint.opacity
nuke.knobDefault("RotoPaint.toolbox", "brush {{brush ltt 0} {clone ltt 0}}")
nuke.knobDefault("RotoPaint.toolbox", "brush {{brush opc .1} {clone opc .1}}")
nuke.knobDefault("RotoPaint.cliptype","none")
#def rpFilterSet():
#    n = nuke.thisNode()
#    n['source_filter'].setValue('0')
#nuke.addKnobChanged(rpFilterSet, nodeClass='RotoPaint')
#nuke.knobDefault("RotoPaint.cliptype","none")

#Constant.rgba
nuke.knobDefault('Constant.channels','rgba')
nuke.knobDefault('Constant.color','{1}')

#CHANNEL
#Shuffel.valueIN
nuke.knobDefault('Shuffle.label','[value in]')
#Remove.keep.rgba
nuke.knobDefault('Remove.operation','keep')
nuke.knobDefault('Remove.channels','rgba')

#COLOR
#Add.channels
nuke.knobDefault('Add.channels','rgba')
#Multiply.rgba
nuke.knobDefault('Multiply.channels','rgba')
#Gamma.channels
nuke.knobDefault('Gamma.channels','rgba')
#ColorMatrix.matrix
nuke.knobDefault('ColorMatrix.matrix','{1 0 0} {0 1 0} {0 0 1}')
#Clamp.rgba
nuke.knobDefault('Clamp.channels','rgba')
#Invert.rgba
nuke.knobDefault('Invert.channels','rgba')
#Colorspace.label
nuke.knobDefault('Colorspace.label', '[value colorspace_in] >> [value colorspace_out]')

#FILTER
#Blur.alpha
nuke.knobDefault("Blur.channels","rgba")
nuke.knobDefault("Blur.size","2")
nuke.knobDefault('Blur.label', 'size:[value size]')
#BumpBoss.rgba
nuke.knobDefault("BumpBoss.channels","rgba")
#Convolve.alpha
nuke.knobDefault("Convolve.channels","rgba")
#Defocus.alpha
nuke.knobDefault("Defocus.channels","rgba")
nuke.knobDefault('Defocus.label', 'Size: [value defocus]')
#DegrainSimple.alpha
nuke.knobDefault("DegrainSimple.channels","rgb")
#DirBlurWrapper.rgba
nuke.knobDefault('DirBlurWrapper.channels','rgba')
#EdgeBlur.alpha
nuke.knobDefault("EdgeBlur.channels","rgba")
#EdgeDetect.alpha
nuke.knobDefault("EdgeDetect.channels","alpha")
#Emboss.alpha
nuke.knobDefault("Emboss.channels","rgba")
#Dilate.alpha
nuke.knobDefault('Dilate.channels','alpha')
#GodRays.rgba
nuke.knobDefault('GodRays.channels','rgba')
#Laplacian.rgba
nuke.knobDefault('Laplacian.channels','rgba')
#Sharpen.rgba
nuke.knobDefault('Sharpen.channels','rgba')
#Soften.rgba
nuke.knobDefault('Soften.channels','rgba')
#VectorBlur.rgba+uv.motion
nuke.knobDefault('VectorBlur.channels','rgba')
nuke.knobDefault('VectorBlur.uv','motion')
#ZDefocus.rgba
nuke.knobDefault('ZDefocus2.channels','rgba')
#ZSlice.rgba
nuke.knobDefault('ZSlice.channels','rgba')

#MERGE
#Keymix.rgba
nuke.knobDefault('Keymix.channels','rgba')
#LayerContactSheet.showLayerNames
nuke.knobDefault('LayerContactSheet.showLayerNames','true')
#Dissolve.rgba+value
nuke.knobDefault('Dissolve.channels','rgba')
nuke.knobDefault('Dissolve.label', 'input:[value which]')
#Switch.input
nuke.knobDefault('Switch.label', 'input:[value which]')
#Blend.rgba
nuke.knobDefault('Blend.channels','rgba')

#Transform
#TransformMasked
nuke.knobDefault('TransformMasked.channels','rgba')
nuke.knobDefault('TransformMasked.label','transfmask')
#Tracker.label
from toggleTracker4TRS import toggleTrackerTRS
animM = nuke.menu('Animation')
animM.addCommand('toggleTRS', 'toggleTrackerTRS()')
nuke.knobDefault('Tracker4.label', '[value transform] / ref:[value reference_frame]')
nuke.knobDefault('Tracker3.label', '[value transform] / ref:[value reference_frame]')
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')
#TVIscale.rgba
nuke.knobDefault('TVIscale.channels','rgba')
#GridWarp.rgba
nuke.knobDefault('GridWarp3.channels','rgba')
#SplineWarp.rgba
nuke.knobDefault('SplineWarp3.channels','rgba')
#STMap.rgba
nuke.knobDefault('STMap.channels','rgba')

#3D
#ScanlineRender.overscan
nuke.knobDefault('ScanlineRender.overscan','50')

#Project3D.crop
nuke.knobDefault('Project3D2.crop','False')

#Deep
#DeepColorCorrect.limit_z
nuke.knobDefault('DeepColorCorrect.limit_z','true')


#SET DEFAULT VIEWER LUT
#nuke.knobDefault('viewerProcess','rec709')
#Root.format
#nuke.knobDefault("Root.format", "HD")


nuke.menu('Nuke').findItem('Edit/Node/Filename/Show').setShortcut('alt+q')

nuke.menu('Nuke').addCommand('Viewer/Overlay',"nuke.menu('Viewer').findItem('Overlay').invoke()",'q')





# --------------------------------------------------------------
#  CUSTOM MENUS ::::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

#CG_Menu
CG=nuke.menu('Nuke').addMenu('CGuillen')
CG.addCommand('Image/Reload Read','reloadRead.reloadRead()','shift+alt+r')
CG.addCommand('Image/Go To Directory', "GoToDirectory.GoToDirectory()", "shift+r")
CG.addCommand('Image/Autocrop','nukescripts.autocrop()')


from nuke_align_motion import controller
CG.addCommand("Edit/Node/Motion Align", 'controller.start()', "f4")
	
CG.addCommand('Edit/Node/Move/Flop','flop.flopNodes()','Ctrl+shift+y')
CG.addCommand('Edit/Node/Move/Flip','flop.flipNodes()','Ctrl+shift+t')
CG.addCommand('Edit/Node/Move/Rotate','flop.rotateNodes()','Ctrl+shift+r')
CG.addCommand('Edit/Node/Move/AlignX', 'alignNodes.alignNodes( nuke.selectedNodes(), direction="y" )', 'alt+x')
CG.addCommand('Edit/Node/Move/AlignY', 'alignNodes.alignNodes( nuke.selectedNodes(), direction="x" )', 'alt+y')

CG.addCommand('Edit/Node/MultiPaste', 'MultiPaste.MultiPaste()', "shift+alt+v")
CG.addCommand('Edit/Node/connectMultipleMask', 'connectMultipleMask.connectMultipleMask()', 'shift+alt+y')
CG.addCommand('Edit/Node/connectMultiple', 'connectMultiple.connectMultiple()', 'shift+y')

CG.addCommand('Viewer/IconSize/iconSizeincrement' , 'iconSizeIncrement()','ctrl+shift+alt+o')
CG.addCommand('Viewer/IconSize/iconSizeDecrement' , 'iconSizeDecrement()','ctrl+shift+alt+i') 
CG.addCommand('Viewer/killViewers','killViewers.killViewers()')

CG.addCommand('Viewer/Set Input 1','viewer.createDot1()','shift+1')
CG.addCommand('Viewer/Set Input 2','viewer.createDot2()','shift+2')
CG.addCommand('Viewer/Set Input 3','viewer.createDot3()','shift+3')
CG.addCommand('Viewer/Set Input 4','viewer.createDot4()','shift+4')
CG.addCommand('Viewer/Reset Viewer','viewer.resetViewer()','shift+v')
CG.addCommand('Viewer/Remove Viewer','viewer.removeViewer()','shift+alt+d')

CG.addCommand('Change Value/Auto-Change Knobs', 'autoChangeKnobs.autoChangeKnobs()')
CG.addCommand('Change Value/rotoOutput', 'rotoOutput.rotoOutput()')

CG.addCommand('Other/Backdrop/BackDrop','backdrop.CreateBackD()','u', icon='Backdrop.png' )
CG.addCommand('Other/Backdrop/GrowBackDrop','backdrop.GrowBackD()','Shift+h', icon='Backdrop.png' )
CG.addCommand('Other/Backdrop/ShrinkBackDrop','backdrop.ShrinkBackD()','Ctrl+Shift+h', icon='Backdrop.png' )
CG.addCommand('Other/Backdrop/GrowBackdropUp','backdrop.GrowBdropUp()','Shift+up', icon='Backdrop.png' )
CG.addCommand('Other/Backdrop/GrowBackdropDown','backdrop.GrowBdropDown()','Shift+down', icon='Backdrop.png' )
CG.addCommand('Other/Backdrop/GrowBackdropRight','backdrop.GrowBdropRight()','Shift+right', icon='Backdrop.png' )
CG.addCommand('Other/Backdrop/GrowBackdropLeft','backdrop.GrowBdropLeft()','Shift+left', icon='Backdrop.png' )
CG.addCommand('Other/Backdrop/ShrinkBackdropUp','backdrop.ShrinkBdropUp()','Shift+ctrl+up', icon='Backdrop.png' )
CG.addCommand('Other/Backdrop/ShrinkBackdropDown','backdrop.ShrinkBdropDown()','Shift+ctrl+down', icon='Backdrop.png' )
CG.addCommand('Other/Backdrop/ShrinkBackdropRight','backdrop.ShrinkBdropRight()','Shift+ctrl+right', icon='Backdrop.png' )
CG.addCommand('Other/Backdrop/ShrinkBackdropLeft','backdrop.ShrinkBdropLeft()','Shift+ctrl+left', icon='Backdrop.png' )

CG.addCommand('Other/postStampControl/postStampOn','postStampControl.postStampOn()',icon='PostageStamp.png')
CG.addCommand('Other/postStampControl/postStampOff','postStampControl.postStampOff()',icon='PostageStamp.png')

CG.addCommand('Other/dopeSheetControl/dopeSheetOff','dopeSheetControl.dopeSheetOff()')


CG.addCommand('Other/GPU_disabler/EnableGPUAcceleration', 'GPU_OnOff.enableGPUAcceleration()')
CG.addCommand('Other/GPU_disabler/DisableGPUAcceleration', 'GPU_OnOff.disableGPUAcceleration()')

CG.addCommand('Other/StickyNote','StickyNoter.StickyNote()','alt+n', icon='StickyNote.png')

CG.addCommand('Other/changeLabel','ChangeLabel.ChangeLabel()','f5')




# --------------------------------------------------------------
#  MY TOOLS ::::::::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------


#CG_TOOLS
cgToolBar = nuke.menu("Nodes").addMenu("CG_Tools", icon = "cgicon_v01.png")

cgToolBar.addCommand("Time/Frame", 'nuke.createNode("Frame")')

"""
cgToolBar.addCommand("Channel/ID_Shuffle", 'nuke.createNode("ID_Shuffle")')
cgToolBar.addCommand('Channel/Shuffle/ShuffleRed','shuffle.ShuffleRed()')
cgToolBar.addCommand('Channel/Shuffle/ShuffleGreen','shuffle.ShuffleGreen()')
cgToolBar.addCommand('Channel/Shuffle/ShuffleBlue','shuffle.ShuffleBlue()')
cgToolBar.addCommand('Channel/Shuffle/ShuffleAlpha','shuffle.ShuffleAlpha()')
"""
cgToolBar.addCommand('Channel/copyPremult','copyPremult.copyPremult()','ctrl+alt+k')


cgToolBar.addCommand("Color/despillToColor", 'nuke.createNode("despillToColor")')
cgToolBar.addCommand("Color/ml_color_transfer", 'nuke.createNode("ml_color_transfer")')
cgToolBar.addCommand("Color/ColorSampler", 'nuke.createNode("ColorSampler")', icon = "ColorSampler.png")
cgToolBar.addCommand("Color/RealBlackSoftClip", 'nuke.createNode("RealBlackSoftClip")')
cgToolBar.addCommand('Color/SuperWhiteRollOff','nuke.createNode("SuperWhiteRollOff")')
cgToolBar.addCommand('Color/OCIO_WB_ANALYZER','nuke.createNode("OCIO_WB_ANALYZER")')
cgToolBar.addCommand('Color/OCIO_WB_READ','nuke.createNode("OCIO_WB_READ")')

cgToolBar.addCommand("Keyer/AdditiveKeyer", 'nuke.createNode("AdditiveKeyer")')
cgToolBar.addCommand("Keyer/KeyChew", 'nuke.createNode("KeyChew")')
cgToolBar.addCommand("Keyer/TX_HueKeyer", 'nuke.createNode("TX_HueKeyer")')

cgToolBar.addCommand("Filter/RealHeatDistortion", 'nuke.createNode("RealHeatDistortion")')
cgToolBar.addCommand("Filter/DirMotionBlur", 'nuke.createNode("DirMotionBlur")')
cgToolBar.addCommand("Filter/ColorDilatePF", 'nuke.createNode("ColorDilatePF")')
cgToolBar.addCommand("Filter/Edge", 'nuke.createNode("Edge")')
cgToolBar.addCommand("Filter/GaussianEdgeExtend", 'nuke.createNode("GaussianEdgeExtend")')
cgToolBar.addCommand("Filter/PushPixel", 'nuke.createNode("PushPixel")')
cgToolBar.addCommand("Filter/LightWarpExp", 'nuke.createNode("LightWarpExp")')
cgToolBar.addCommand('Filter/ExponentialGlow','nuke.createNode("ExponentialGlow")')
cgToolBar.addCommand('Filter/ExponentialGlow1_1','nuke.createNode("ExponentialGlow1_1")')
cgToolBar.addCommand('Filter/Murk','nuke.createNode("Murk")')
cgToolBar.addCommand('Filter/Haze','nuke.createNode("Haze")')
cgToolBar.addCommand('Filter/apChroma','nuke.createNode("apChroma")')
cgToolBar.addCommand('Filter/nanInfCleaner','nuke.createNode("nanInfCleaner")')

cgToolBar.addCommand('Transform/mergeTransforms', 'merge_transforms_v2.start()')
cgToolBar.addCommand('Transform/smartTransform', 'myTransform.transformThis()', 't')
cgToolBar.addCommand("Transform/Crop_Padding", 'nuke.createNode("Crop_Padding")')
cgToolBar.addCommand("Transform/Offset", 'nuke.createNode("Offset")')
cgToolBar.addCommand("Transform/Distort", 'nuke.createNode("Distort")')
cgToolBar.addCommand("Transform/Morph_Dissolve", 'nuke.createNode("Morph_Dissolve")')

cgToolBar.addCommand('Merge/smartMerge', 'myMerge.mergeThis()', 'm')
cgToolBar.addCommand('Merge/Premulter','premulter.Premulter()','alt+a')

cgToolBar.addCommand("N/NReflection", 'nuke.createNode("NReflection")')
cgToolBar.addCommand("N/NRelight", 'nuke.createNode("NRelight")')
cgToolBar.addCommand("N/PositionPicker", 'nuke.createNode("PositionPicker")')
cgToolBar.addCommand("N/P_rotation", 'nuke.createNode("P_rotation")')
cgToolBar.addCommand("N/P_slicer", 'nuke.createNode("P_slicer")')
cgToolBar.addCommand("N/P_percentage", 'nuke.createNode("P_percentage")')

cgToolBar.addCommand("Deep/DeepFromImageBlender", 'nuke.createNode("DeepFromImageBlender")')
cgToolBar.addCommand("Deep/DeepKeyerDepth", 'nuke.createNode("DeepKeyerDepth")')
cgToolBar.addCommand("Deep/DeepedgeSmoother", 'nuke.createNode("DeepedgeSmoother")')
cgToolBar.addCommand("Deep/DeepCropSoft", 'nuke.createNode("DeepCropSoft")')

cgToolBar.addCommand('3D/CardtoTrack','CardtoTrack.corn3D()',icon="Camera.png")
cgToolBar.addCommand('3D/Axis My','Axis_My.Axis_My()',icon = "Axis.png")
cgToolBar.addCommand('3D/SnapAndMove','nuke.createNode("SnapAndMove")')

cgToolBar.addCommand("Other/ContactSheet_Comp", 'nuke.createNode("ContactSheet_Comp")')
cgToolBar.addCommand("Other/TechChecker", 'nuke.createNode("TechChecker")')
cgToolBar.addCommand("Other/WaveMaker", 'nuke.createNode("WaveMaker")')
import RandomTile
cgToolBar.addCommand('Other/Random Tile', 'RandomTile.randomTile()',icon='RandomTile.png')
cgToolBar.addCommand("Other/V_Multilabel", 'nuke.createNode("V_Multilabel")')
cgToolBar.addCommand("Other/Python_and_TCL", 'nuke.createNode("Python_and_TCL")')


#GONZO TOOLS
cgToolBar = nuke.menu("Nodes").addMenu("CG_Tools/Gonzo_Tools", icon = "gonzoicon25.png")
cgToolBar.addCommand("Filters/FineEdgeDetect", 'nuke.createNode("FineEdgeDetect")')
cgToolBar.addCommand("Filters/AngleEdgeDetect", 'nuke.createNode("AngleEdgeDetect")')
cgToolBar.addCommand("Filters/ChannelReBuild", 'nuke.createNode("ChannelReBuild")')
cgToolBar.addCommand("Keyers/ScreenXchange", 'nuke.createNode("ScreenXchange")')
cgToolBar.addCommand("CC/EdgeHammer", 'nuke.createNode("EdgeHammer")')
cgToolBar.addCommand("CC/Matchtone", 'nuke.createNode("Matchtone")')
cgToolBar.addCommand("Showreel/Breakdowner", 'nuke.createNode("Breakdowner")')
cgToolBar.addCommand("CC/WrappersDelight", 'nuke.createNode("WrappersDelight")')
cgToolBar.addCommand("Filters/Sharpenner", 'nuke.createNode("Sharpenner")')
cgToolBar.addCommand("3d/Image_Plane", 'nuke.createNode("ImagePlane")')
cgToolBar.addCommand("AOV/AOV_Tweak", 'nuke.createNode("AOV_Tweak")')




#3D_Objects

toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("CG_Tools/3D Object v1.1", icon = os.path.join(Object3D_path, "icon/3D_Object.png"))



#BASIC OBJECTS low
m.addCommand('Basic Geometry/Low Res/cube', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/low/cube_low.nk") + "\")", icon=os.path.join(Object3D_path, "icon/cube.png"))
m.addCommand('Basic Geometry/Low Res/cylinder', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/low/cylinder_low.nk") + "\")", icon=os.path.join(Object3D_path, "icon/cylinder.png"))
m.addCommand('Basic Geometry/Low Res/cone', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/low/cone_low.nk") + "\")", icon=os.path.join(Object3D_path, "icon/cone.png"))
m.addCommand('Basic Geometry/Low Res/pype', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/low/pype_low.nk") + "\")", icon=os.path.join(Object3D_path, "icon/pype.png"))
m.addCommand('Basic Geometry/Low Res/torus', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/low/torus_low.nk") + "\")", icon=os.path.join(Object3D_path, "icon/torus.png"))
m.addCommand('Basic Geometry/Low Res/pyramid 3sides', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/low/pyramid_3sides_low.nk") + "\")", icon=os.path.join(Object3D_path, "icon/pyramid.png"))
m.addCommand('Basic Geometry/Low Res/pyramid 4sides', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/low/pyramid_4sides_low.nk") + "\")", icon=os.path.join(Object3D_path, "icon/pyramid.png"))
m.addCommand('Basic Geometry/Low Res/pyramid 5sides', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/low/pyramid_5sides_low.nk") + "\")", icon=os.path.join(Object3D_path, "icon/pyramid.png"))



#BASIC OBJECTS high
m.addCommand('Basic Geometry/High Res/cube', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/high/cube.nk") + "\")", icon=os.path.join(Object3D_path, "icon/cube.png"))
m.addCommand('Basic Geometry/High Res/cylinder', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/high/cylinder.nk") + "\")", icon=os.path.join(Object3D_path, "icon/cylinder.png"))
m.addCommand('Basic Geometry/High Res/cone', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/high/cone.nk") + "\")", icon=os.path.join(Object3D_path, "icon/cone.png"))
m.addCommand('Basic Geometry/High Res/pype', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/high/pype.nk") + "\")", icon=os.path.join(Object3D_path, "icon/pype.png"))
m.addCommand('Basic Geometry/High Res/torus', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/high/torus.nk") + "\")", icon=os.path.join(Object3D_path, "icon/torus.png"))
m.addCommand('Basic Geometry/High Res/pyramid 3sides', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/high/pyramid_3sides.nk") + "\")", icon=os.path.join(Object3D_path, "icon/pyramid.png"))
m.addCommand('Basic Geometry/High Res/pyramid 4sides', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/high/pyramid_4sides.nk") + "\")", icon=os.path.join(Object3D_path, "icon/pyramid.png"))
m.addCommand('Basic Geometry/High Res/pyramid 5sides', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Basic/high/pyramid_5sides.nk") + "\")", icon=os.path.join(Object3D_path, "icon/pyramid.png"))



#TEST GEOMETRY
m.addCommand('Test Geometry/buddha', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestGeometry/buddha.nk") + "\")", icon=os.path.join(Object3D_path, "icon/buddha.png"))
#m.addCommand('Test Geometry/buddha_low', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestGeometry/buddha_low.nk") + "\")", icon=os.path.join(Object3D_path, "icon/buddha.png"))

m.addCommand('Test Geometry/dragon', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestGeometry/dragon.nk") + "\")", icon=os.path.join(Object3D_path, "icon/dragon.png"))
#m.addCommand('Test Geometry/dragon_low', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestGeometry/dragon_low.nk") + "\")", icon=os.path.join(Object3D_path, "icon/dragon.png"))

m.addCommand('Test Geometry/human head', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestGeometry/human_head.nk") + "\")", icon=os.path.join(Object3D_path, "icon/human_head.png"))

m.addCommand('Test Geometry/teapot', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestGeometry/teapot.nk") + "\")", icon=os.path.join(Object3D_path, "icon/teapot.png"))
m.addCommand('Test Geometry/teapot_low', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestGeometry/teapot_low.nk") + "\")", icon=os.path.join(Object3D_path, "icon/teapot.png"))

m.addCommand('Test Geometry/monkey', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestGeometry/monkey.nk") + "\")", icon=os.path.join(Object3D_path, "icon/monkey.png"))

m.addCommand('Test Geometry/pig head', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestGeometry/pig_head.nk") + "\")", icon=os.path.join(Object3D_path, "icon/pig_head.png"))

m.addCommand('Test Geometry/rubber toy', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestGeometry/rubber_toy.nk") + "\")", icon=os.path.join(Object3D_path, "icon/rubber_toy.png"))

m.addCommand('Test Geometry/shaderBall', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestGeometry/shaderBall.nk") + "\")", icon=os.path.join(Object3D_path, "icon/shaderBall.png"))

#DEEP SCENE
m.addCommand('Test Deep/deepScene', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestDeep/deepScene.nk") + "\")", icon=os.path.join(Object3D_path, "icon/deepScene.jpg"))

#AOV SCENE
m.addCommand('Test AOVs/RenderAOV', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestAOV/renderAOV.nk") + "\")", icon=os.path.join(Object3D_path, "icon/render.png"))
m.addCommand('Test AOVs/SceneAOV', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestAOV/sceneAOV.nk") + "\")", icon=os.path.join(Object3D_path, "icon/aov.png"))

#TEST IMAGES
m.addCommand('Test Images/Kodak Digital LAD', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestImages/kodak.nk") + "\")", icon=os.path.join(Object3D_path, "icon/kodak.jpg"))
m.addCommand('Test Images/Green Screen', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestImages/greenScreen.nk") + "\")", icon=os.path.join(Object3D_path, "icon/green_screen.jpg"))
m.addCommand('Test Images/Green Screen Hair', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestImages/greenScreen_hair.nk") + "\")", icon=os.path.join(Object3D_path, "icon/green_screen_hair.jpg"))
m.addCommand('Test Images/Blue Screen', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestImages/blueScreen.nk") + "\")", icon=os.path.join(Object3D_path, "icon/blue_screen.jpg"))
m.addCommand('Test Images/Blue Screen Hair', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestImages/blueScreen_hair.nk") + "\")", icon=os.path.join(Object3D_path, "icon/blue_screen_hair.jpg"))


#TOOLS
m.addCommand('Tool/Background 3D', "nuke.createNode(\"" + os.path.join(Object3D_path + "/Tool/background3D") + "\")", icon=os.path.join(Object3D_path, "icon/wireframe.png"))
m.addCommand('Tool/UV Render', "nuke.createNode(\"" + os.path.join(Object3D_path + "/Tool/UVRender") + "\")", icon=os.path.join(Object3D_path, "icon/UV_cube.png"))
m.addCommand('Tool/Card 360', "nuke.createNode(\"" + os.path.join(Object3D_path + "/Tool/Card360") + "\")", icon=os.path.join(Object3D_path, "icon/card360.png"))
m.addCommand('Tool/DeepThickness', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Tool/DeepThickness.nk") + "\")")
m.addCommand('Tool/Coordinates', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Tool/coordinates.nk") + "\")", icon=os.path.join(Object3D_path, "icon/coordinates.jpg"))
m.addCommand('Tool/C4x4', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Tool/C4x4.nk") + "\")", icon=os.path.join(Object3D_path, "icon/coordinates.jpg"))


#TEXTURE
m.addCommand('Texture/CheckerBoard UV', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Texture/CheckerBoard_UV.nk") + "\")", icon=os.path.join(Object3D_path, "icon/UV_mapper.jpg"))
m.addCommand('Texture/UV Map', "nuke.createNode(\"" + os.path.join(Object3D_path + "/Texture/UVMap") + "\")", icon=os.path.join(Object3D_path, "icon/UVMap.png"))
m.addCommand('Texture/Coordinates img', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/Texture/coordinates_img.nk") + "\")", icon=os.path.join(Object3D_path, "icon/coordinates.jpg"))



m.addSeparator()


#INFO
m.addCommand('Info e Tutorial', "nuke.tcl('start', 'http://www.andreageremia.it/tutorial_3dobject.html')", icon = os.path.join(Object3D_path, "icon/question_mark.png"))




"""
weta stacker menu

__import__('wetaStackerMenu', fromlist=['createMenu']).createMenu()
"""
