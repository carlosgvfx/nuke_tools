def smMerge(nodeType):
    import nuke
    a = nuke.selectedNodes()
    al = []
    for node in a:
        al.append(node['xpos'].value())
        al.sort()
        al.reverse()


    amm =  len(al)
    new = [None]*amm
    p = 0
    while p< amm:   
        a = nuke.selectedNodes()
        for one in a:
            pos = one['xpos'].value()
            if pos == al[p]:
                new.insert(p,one)
        #print new[:amm]
        p+=1

    q=1
    merges = []
    for node in new[:amm]: 
        if q==1:
            followed = node
            q+=1
        else:
            if nodeType== "MergeGeo":
                follower = nuke.nodes.MergeGeo()
                #merges.append(follower)
            if nodeType== "MergeMat":
                follower = nuke.nodes.MergeMat()
                #merges.append(follower)
            if nodeType== "DeepMerge":
                follower = nuke.nodes.DeepMerge()
                #merges.append(follower)
            if nodeType== "Merge2":
                follower = nuke.nodes.Merge2()
                #merges.append(follower)
            follower.setInput(0,followed)
            follower.setInput(1,node)
            followed = follower
            merges.append(follower)
    for node in nuke.allNodes():
        node.setSelected(False)
    for node in merges:
        node.setSelected(True)


def mergeThis():
    import nuke 
    try: 
        if 'shadow_override' in nuke.selectedNode().knobs() or 'Camera' in nuke.selectedNode().Class() or 'render_mode' in nuke.selectedNode().knobs() or 'Light' in nuke.selectedNode().Class() or 'DisplaceGeo' in nuke.selectedNode().Class() or 'Axis' in nuke.selectedNode().Class():
            if len(nuke.selectedNodes())==1:
                return nuke.createNode( "MergeGeo")
            else:
                smMerge("MergeGeo")

        elif 'MergeMat' in nuke.selectedNode().Class() or 'project_on' in nuke.selectedNode().knobs() or 'Mat' in nuke.selectedNode()['name'].value(): 
             if len(nuke.selectedNodes())==1:
                return nuke.createNode( "MergeMat")
             else:
                smMerge("MergeMat")
        elif 'Deep' in nuke.selectedNode().Class() and "DeepHoldout" not in nuke.selectedNode()['name'].value() and "DeepToImage" not in nuke.selectedNode()['name'].value(): 
             if len(nuke.selectedNodes())==1:
                return nuke.createNode( "DeepMerge")
             else:
                smMerge("DeepMerge")
        else: 
            raise ValueError 
    except: 
         if len(nuke.selectedNodes())<=1:
            return nuke.createNode( "Merge2")

         else:
            smMerge("Merge2")



