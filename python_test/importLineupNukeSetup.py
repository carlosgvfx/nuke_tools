######################################################################################
# Lig import Lineup Nuke Setup
# v01
# Pierre Gobilliard
# 07/2020
######################################################################################

def importLineupNukeSetup():

    import os
    show = os.environ.get('SHOW', '')
    sequence = os.environ.get('SHOT', '').split('_')[0]
    shot = os.environ.get('SHOT', '').split('_')[1]
    sequenceShot =  os.environ.get('SHOT', '')
    vpFolder = "/rdo/shows/"+show + "/" + sequence + "/" + shot + "/cg/nuke/vp/"
    extentions = 'nk'
    vpFiles = []
    
    
    ExistVpFolder =  os.path.exists(vpFolder)

    if ExistVpFolder :
        for f in os.listdir(vpFolder):
            if f.endswith(extentions):
                fs = os.path.splitext(f)[0]
                if fs.startswith(sequenceShot + '_vp_template_v'):
                    if fs.find('_vp_template_'):
                        vpFiles.append(f)
        vpFiles = sorted(vpFiles)

        vpSelect = (vpFolder + (vpFiles[len(vpFiles)-1]))
        print vpSelect
        #nuke.scriptSource(vpSelect)
        nuke.nodePaste(vpSelect)
        message = 'imported linup from : '+ vpFiles[len(vpFiles)-1]
        nuke.message(message )


importLineupNukeSetup()
