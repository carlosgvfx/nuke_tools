"""" Localise rchk versions to local raid for quick tech check.
This script must be used in a Nuke environment.

Project must be specified.
If project only, will run for all sequences and uses rchk versions per shot.
If project and sequence specified, will collect all rchk versions for that sequence. 
You may also specify the beginning of a common sequence code to collect several sequences that start_with it.
By default, will also localise the corresponding plate.

"""

import os
from datetime import datetime

import nuke
import nukescripts

import rodeo.shotgun
#import localiseThreadedRdo


def createReadsForSgVersions(sgVersions):

    previous = None
    shotCluster = []
    shot = None
    approvedStatus = []

    # loop the found versions and create a read for each
    for v in sorted(sgVersions, key=lambda k: k['entity.Shot.code']):
        # print v
        current = nuke.createNode('Read', ('file {0} first {1} last {2} on_error black before hold after hold'
                                           ).format(v['sg_path_to_frames'].replace('@', '\#'),
                                                    v['sg_first_frame'],
                                                    v['sg_last_frame']),
                                  inpanel=False)
        # identify approved version
        # identify apr plate and only append those to contact sheet connection
        # list
        if v['sg_status_list'] == 'apr':
            current['tile_color'].setValue(0xff00ff)
            approvedStatus.append(current)
        # add all comp and lig latest versions to contact sheet connection list
        elif v['sg_department'] in ['Comp', 'Lighting']:
            approvedStatus.append(current)
            # change tile colour if it has an approved client status
            # cfin/sfin/pdngblablaba
            if v['entity.Shot.sg_status_list'] not in ['ip', 'omt', 'hld', 'turn']:
                current['tile_color'].setValue(0xff00ff)
                current['label'].setValue(v['entity.Shot.sg_status_list'])

        # create a backdrop per shot cluster
        if previous:
            current['xpos'].setValue(previous['xpos'].value() + 100)
            if shot != v['entity.Shot.code']:
                current['xpos'].setValue(current['xpos'].value() + 300)
                for node in nuke.selectedNodes():
                    node.setSelected(False)
                for read in shotCluster:
                    read.setSelected(True)
                    backdrop = nukescripts.autobackdrop.autoBackdrop()
                    backdrop['label'].setValue(shot)
                shotCluster = []
            current['ypos'].setValue(previous['ypos'].value())

        shotCluster.append(current)
        shot = v['entity.Shot.code']
        previous = current

    return approvedStatus


def localiseRchkVersions(show, sequence=None, getPlates=True):
    """Will set up a nuke localise for all versions with the status rchk in the given show.

    :param show (str): show code
    :param sequence (str): optional sequence code
    :param getPlates (bool)
    Setting getPlates to True will also localise the corresponding plate
    :return: None
    """

    sg = rodeo.shotgun.connect('colorTools',
                               'c39acf0b480e8d744ea06ddb5ed97caf320e325931cc79fefb629c42c7e5279f')

    fields = ['sg_first_frame', 'sg_last_frame', 'sg_path_to_frames', 'entity.Shot.code', 'entity',
              'entity.Shot.sg_status_list', 'sg_status_list', 'sg_department']

    if sequence:
        sgVersions = sg.find('Version', [['sg_status_list', 'is', 'rchk'], ['project.Project.code', 'is', show], [
                             'entity.Shot.sg_sequence.Sequence.code', 'starts_with', sequence]], fields)
    else:
        sgVersions = sg.find('Version', [['sg_status_list', 'is', 'rchk'], [
                             'project.Project.code', 'is', show]], fields)

    createReadsForSgVersions(sgVersions)

    if getPlates:
        plateVersions = []

        for version in sgVersions:
            plateVersions.extend(sg.find('Version', [['sg_status_list', 'is', 'apr'], [
                                 'sg_department', 'is', 'Plate'], ['entity', 'is', version['entity']]], fields))

        createReadsForSgVersions(plateVersions)

    readKnobs = []

    for node in nuke.allNodes('Read'):
        readKnobs.append(node['file'])

    #localiseThreadedRdo.rdoLocaliseFile(readKnobs)


def popup():
    """Popup window UI for Nuke menu"""

    show = os.environ.get('RDO_CURRENT_SHOW', '')
    # sequence = os.environ.get('SHOT', '').split('_')[0]

    p = nuke.Panel('Localise TC to RAID settings')
    p.addSingleLineInput('Show', '%s' % show)
    p.addSingleLineInput('Sequence', '')
    p.addBooleanCheckBox('Include plates', True)
    ret = p.show()

    if not ret:
        return

    localiseRchkVersions(p.value('Show'), p.value(
        'Sequence'), p.value('Include plates'))

if __name__ == '__main__':
    localiseRchkVersions(os.environ['RDO_CURRENT_SHOW'])
