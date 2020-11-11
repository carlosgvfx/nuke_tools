######################################################################################
# Dailie Sourcer
# v01.1
#  didn't managed to select Approved versions only yet
######################################################################################

import nuke
import rdo_shotgun_workflows
import os
def dailieSourcer():
    


 
    deptList = ['LineUp','Layout','Anim','Lighting','FX','Crowd','CFX','ENV','Asset','Comp','Cmm','BMM']
    deptListTraduced = ['IO','Layout','Anim','Lighting','FX','Crowd','CFX','ENV','Asset','Comp','Cmm','BMM']
    statList = ['Approved',"All_status"]
    statListALL = ['cmpt', 'apr', 'supr', 'fxsupr', 'rev' ]
    statListApproved = ['cmpt', 'apr']
    versionNumber = ['Last_version', '3_Last', 'All_versions']
    i = 1


    settingsList = ['hold','loop','bounce','black']
    panel = nuke.Panel('Dailie Sourcer')
    panel.addEnumerationPulldown('department', ' '.join( deptList ))
    # panel.addEnumerationPulldown('Status', ' '.join( statList ))    
    panel.addEnumerationPulldown('import', ' '.join( versionNumber ))
    panel.show()

    if panel.value('department') :
        selDepartment = panel.value('department')
        if selDepartment == "LineUp" :
            selDepartment = 'IO'

        selStatus = panel.value('Status')
        if selStatus == 'Approved' :
            getStatus = statListApproved
        else :
            getStatus = statListALL

        selImport = panel.value('import')
        if selImport == 'Last_version' :
            getImport = 1
        elif selImport == '3_Last' :
            getImport = 3
        else :
            getImport = 999

        show = os.environ.get('SHOW', '')
        sequence = os.environ.get('SHOT', '').split('_')[0]
        shot = os.environ.get('SHOT')

        INVALID_SHOT_STATUS = ['omt', 'awd']
        sg = rdo_shotgun_workflows.connect('colorTools',
                                               'c39acf0b480e8d744ea06ddb5ed97caf320e325931cc79fefb629c42c7e5279f')

        fields = ['sg_first_frame', 'sg_last_frame', 'sg_path_to_frames', 'entity.Shot.code',
                  'entity.Shot.sg_status_list', 'sg_status_list', 'sg_department', 'entity.Shot.tags',
                  'entity.Shot.sg_shot_grouping']

        sgStatus = ['sg_status_list', 'is_not', 'na']

        versions = sg.find('Version',
                           [['project.Project.code', 'is', show],
                            ['entity.Shot.code', 'starts_with', shot],
                            ['entity.Shot.sg_status_list', 'not_in', INVALID_SHOT_STATUS],
                            ['sg_department', 'in', selDepartment],
                            sgStatus],
                           fields,
                           [{'field_name': 'entity', 'direction': 'asc'},
                            {'field_name': 'created_at', 'direction': 'desc'},
                            {'field_name': 'sg_department', 'direction': 'desc'}])

        for v in versions:
            
            if i <= getImport :
                i = i + 1
                readLineup = nuke.createNode('Read', ('file {0} first {1} last {2} on_error black before hold after hold'
                                                   ).format(v['sg_path_to_frames'].replace('@', '\#'),
                                                            v['sg_first_frame'],
                                                            v['sg_last_frame']),
                                          inpanel=False)



#dailieSourcer()

