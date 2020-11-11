import nuke

def reloadRead():
    for a in nuke.allNodes():
        if a.Class()=='Read':
            a['reload'].execute()