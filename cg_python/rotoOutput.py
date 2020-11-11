import nuke

def rotoOutput():
    for s in nuke.allNodes('Roto'):
        s['output'].setValue('rgba')
        s['cliptype'].setValue('none')
