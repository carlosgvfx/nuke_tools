######################################################################################
# Lig import Lineup Nuke Setup
# v01
# Pierre Gobilliard
# 07/2020
######################################################################################

import nuke
import os

def importLigthingNukeSetup():

    show = os.environ.get('SHOW', '')
    sequence = os.environ.get('SHOT', '').split('_')[0]
    shot = os.environ.get('SHOT', '').split('_')[1]
    sequenceShot =  os.environ.get('SHOT', '')
    vpFolder = "/rdo/shows/"+show + "/" + sequence + "/" + shot + "/cg/nuke/lig/"
    extentions = 'nk'
    vpFiles = []
    
    
    ExistVpFolder =  os.path.exists(vpFolder)

    if ExistVpFolder :
        for f in os.listdir(vpFolder):
            if f.endswith(extentions):
                fs = os.path.splitext(f)[0]
                if fs.startswith(sequenceShot + '_lig_v'):
                    if fs.find('_lig_'):
                        vpFiles.append(f)
        vpFiles = sorted(vpFiles)

        vpSelect = (vpFolder + (vpFiles[len(vpFiles)-1]))
        print vpSelect
        #nuke.scriptSource(vpSelect)
        nuke.nodePaste(vpSelect)
        message = 'imported ligthing set up from : '+ vpFiles[len(vpFiles)-1]
        nuke.message(message )



"""
def importLigthingNukeSetup():

    import os
    show = os.environ.get('SHOW', '')
    sequence = os.environ.get('SHOT', '').split('_')[0]
    shot = os.environ.get('SHOT', '').split('_')[1]
    sequenceShot =  os.environ.get('SHOT', '')
    vpFolder = "/rdo/shows/"+show + "/" + sequence + "/" + shot + "/cg/nuke/lig/"
    extentions = 'nk'
    ligFiles = []
    
    
    ExistLigFolder =  os.path.exists(ligFolder)

    if ExistLigFolder :
        for f in os.listdir(ligFolder):
            if f.endswith(extentions):
                fs = os.path.splitext(f)[0]
                if fs.startswith(sequenceShot + '_lig_v'):
                    if fs.find('_lig_'):
                        ligFiles.append(f)
        ligFiles = sorted(ligFiles)

        ligSelect = (ligFolder + (ligFiles[len(ligFiles)-1]))
        print ligSelect
        #nuke.scriptSource(ligSelect)
        nuke.nodePaste(ligSelect)
        message = 'imported linup from : '+ ligFiles[len(ligFiles)-1]
        nuke.message(message )


#importLigthingNukeSetup()
"""
