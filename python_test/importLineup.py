######################################################################################
# Import lineup
######################################################################################
import nuke
import rdo_shotgun_workflows
import os


def importLineup():

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
		            ['sg_department', 'in', 'IO'],
		            sgStatus],
		           fields,
		           [{'field_name': 'entity', 'direction': 'asc'},
		            {'field_name': 'created_at', 'direction': 'desc'},
		            {'field_name': 'sg_department', 'direction': 'desc'}])

	for v in versions:

	    readLineup = nuke.createNode('Read', ('file {0} first {1} last {2} on_error black before hold after hold'
		                               ).format(v['sg_path_to_frames'].replace('@', '\#'),
		                                        v['sg_first_frame'],
		                                        v['sg_last_frame']),
		                      inpanel=False)
