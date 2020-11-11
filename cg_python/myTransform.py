
def transformThis():
    import nuke  
    try: 
        if 'render_mode' in nuke.selectedNode().knobs(): 
            return nuke.createNode( 'TransformGeo' )
        elif 'Deep' in nuke.selectedNode().Class(): 
            return nuke.createNode( "DeepTransform")
        else:
            nuke.createNode( 'Transform' )   
    except: 
        return nuke.createNode( 'Transform' ) 
