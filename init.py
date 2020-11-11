# --------------------------------------------------------------
#  init.py
#  Version: 1.0.0
#  Last Updated: August 8th, 2020
# --------------------------------------------------------------

# ----- DEFINE CUSTOM FOLDER STRUCTURE -------------------------

#My tools 
nuke.pluginAddPath('./cg_gizmos')
nuke.pluginAddPath('./cg_python')
nuke.pluginAddPath('./cg_python/shuffleShortcuts')
nuke.pluginAddPath('./cg_icons')
nuke.pluginAddPath('./gonzo_gizmos')
nuke.pluginAddPath('./python_test')


#Defaul nodes setting
nuke.pluginAddPath('./default')


#3D_Objects
Object3D_path = "/mnt/users/cguillen/.nuke/Object3D_path"
nuke.pluginAddPath(Object3D_path)

