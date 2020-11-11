import nuke


def StickyNote():
    
	sNote=nuke.createNode('StickyNote')
	sNote.knob('label').setValue('<pre>')
	sNote.knob('note_font_size').setValue(40)
	sNote.knob('tile_color').setValue(0x2d2d2dff)
	sNote.knob('note_font').setValue('SamsungImagination Bold')






