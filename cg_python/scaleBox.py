# -*- coding: utf-8 -*-
'''
this script is based on Frank Rueters "scaleNodes v1.3". I just wrapped the UI/Sliders around it to make ot work
interactively. The original script can be found here:
http://www.nukepedia.com/python/nodegraph/scalenodes

falk hofmann, 03/2017
'''

#from PySide import QtGui
#from PySide import QtCore
import nuke

try:
    # Prefer Qt.py when available
    from Qt import QtCore, QtGui, QtWidgets, Qt
except ImportError:
    try:
        # PySide2 for default Nuke 11
        from PySide2 import QtCore, QtGui, QtWidgets
        from PySide2.QtCore import Qt
    except ImportError:
        # Or PySide for Nuke 10
        from PySide import QtCore, QtGui, QtGui as QtWidgets
        from PySide.QtCore import Qt


class SlidersGroup(QtGui.QWidgets):
    '''
    subclass to create a set of slider and label
    '''
    valueChanged = QtCore.Signal(int)

    def __init__(self, parent, direction):
        super(SlidersGroup, self).__init__(parent=parent)
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.slider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.slider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.slider.setTickInterval(20)
        self.slider.setSingleStep(20)
        self.slider.setValue(50)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.label = QtGui.QLabel(direction)
        self.label.setStyleSheet("color: #C26828; font: 30px")
        sliders_layout = QtGui.QHBoxLayout()
        sliders_layout.addWidget(self.label)
        sliders_layout.addWidget(self.slider)
        self.setLayout(sliders_layout)
        self.slider.valueChanged.connect(lambda: self.parent().value_changed(direction, self.slider.value()))


class ScaleBox(QtGui.QWidgets):
    '''
    main UI class
    '''
    orig_state = None
    x_mod = None
    y_mod = None

    def __init__(self):
        super(ScaleBox, self).__init__()
        self.setup_ui()
        self.save_orig_state()

    def setup_ui(self):
        '''
        setting up the user interface
        :return: None
        '''
        width = 600
        height = 120
        self.setMinimumSize(width, height)
        point = QtGui.QCursor.pos() - QtCore.QPoint(width / 2, height / 2)
        self.move(point)
        self.setWindowTitle('ScaleBox')
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.slider_x = SlidersGroup(self, 'X')
        self.slider_y = SlidersGroup(self, 'Y')
        sliders_layout = QtGui.QVBoxLayout()
        sliders_layout.addWidget(self.slider_x)
        sliders_layout.addWidget(self.slider_y)
        self.setLayout(sliders_layout)
        self.installEventFilter(self)

    def save_orig_state(self):
        '''
        store original position as dict in global var
        :return: None
        '''
        if not self.orig_state:
            state_dict = {}
            for node in nuke.selectedNodes():
                state_dict[node] = [node.xpos(), node.ypos()]
            self.orig_state = state_dict

    def value_changed(self, direction, value):
        '''
        connected to valueChanged Signal from Sliders
        :param direction: 'X' or'Y' as string
        :param value: scalefactor
        :return: None
        '''
        nvalue = (((value - 1.0) * 3) / 99.0)
        if direction == 'X':
            self.x_mod = nvalue
            scale_nodes(self.orig_state, nvalue, self.y_mod)
        else:
            self.y_mod = nvalue
            scale_nodes(self.orig_state, self.x_mod, nvalue)

    def leaveEvent(self, event):
        self.cancel()

    def cancel(self):
        self.close()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.cancel()


def scale_nodes(orig_state, x_scale, y_scale):
    '''
    this function was originally written by Frank Rueter and modified to make it work with sliders
    :param orig_state: selected nodes position as dict[node]: [xpos, ypos]
    :param x_scale: horizontal scalefactor
    :param y_scale: vertical scalefactor
    :return: None
    '''
    def get_side_nodes(bd):
        '''return a given backdrop node's "side nodes" (left, right, top andbottom most nodes) as a dictionary including the nodes and the respective DAG coordinates'''
        orig_sel = nuke.selectedNodes()
        [n.setSelected(False) for n in orig_sel]

        bd.selectNodes()
        bd_nodes = nuke.selectedNodes()
        [n.setSelected(False) for n in bd_nodes]  # DESELECT BACKDROP NODES
        [n.setSelected(True) for n in orig_sel]  # RESTORE ORIGINAL SELECTION
        if not bd_nodes:
            return []

        left_node = right_node = bottom_node = top_node = bd_nodes[0]  # START WITH RANDOM NODE
        for n in bd_nodes:
            if n.xpos() < left_node.xpos():
                left_node = n
            if n.xpos() > right_node.xpos():
                right_node = n
            if n.ypos() < top_node.ypos():
                top_node = n
            if n.ypos() > bottom_node.ypos():
                bottom_node = n

        return dict(left=[left_node, nuke.math.Vector2(left_node.xpos(), left_node.ypos())],
                    right=[right_node, nuke.math.Vector2(right_node.xpos(), right_node.ypos())],
                    top=[top_node, nuke.math.Vector2(top_node.xpos(), top_node.ypos())],
                    bottom=[bottom_node, nuke.math.Vector2(bottom_node.xpos(), bottom_node.ypos())])

    # COLLECT SIDE NODES AND COORDINATES FOR BACKDROPS
    backdrops = {}
    for bd in nuke.allNodes('BackdropNode'):
        backdrops[bd] = get_side_nodes(bd)

    # MOVE NODES FROM CENTRE OUTWARD
    nodes = [n for n in nuke.selectedNodes() if n.Class() != 'BackdropNode']
    amount = len(nodes)
    if amount == 0:    return

    all_x = 0
    all_y = 0
    for n in nodes:
        all_x += n.xpos()
        all_y += n.ypos()

    centre_x = all_x / amount
    centre_y = all_y / amount

    if not x_scale:
        x_scale = 1
    if not y_scale:
        y_scale = 1

    for n in nodes:
        n.setXpos(int(centre_x + (orig_state[n][0] - centre_x) * x_scale))
        n.setYpos(int(centre_y + (orig_state[n][1] - centre_y) * y_scale))

    # ADJUST BACKDROP NODES
    for bd, bdSides in backdrops.iteritems():
        left_delta = bdSides['left'][0].xpos() - bdSides['left'][1].x
        top_delta = bdSides['top'][0].ypos() - bdSides['top'][1].y
        right_delta = bdSides['right'][0].xpos() - bdSides['right'][1].x
        bottom_delta = bdSides['bottom'][0].ypos() - bdSides['bottom'][1].y

        bd.setXpos(int(bd.xpos() + left_delta))
        bd.setYpos(int(bd.ypos() + top_delta))

        bd['bdwidth'].setValue(int(bd['bdwidth'].value() - left_delta + right_delta))
        bd['bdheight'].setValue(int(bd['bdheight'].value() - top_delta + bottom_delta))


new_box = None


def start():
    '''
    start up function from inside nuke
    :return:
    '''
    global new_box
    new_box = ScaleBox()
    new_box.show()
