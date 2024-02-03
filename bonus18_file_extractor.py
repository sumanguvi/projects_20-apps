import PySimpleGUI as sg
from zip_extractor import extract_archive

label1 = sg.Text('Select archive')
input1 = sg.Input()
choose_button1 = sg.FileBrowse('choose', key='archive')

label2 = sg.Text('Select destination folder:')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('choose', key='folder')

extract_button = sg.Button('Extract')
output_label = sg.Text(key='output', text_color='green')

window = sg.Window('Archive Extractor',
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button,output_label]])

while True:
    events, values = window.read()
    print(events)
    print(values)
    sourcepath = values['archive']
    destpath = values['folder']

    extract_archive(sourcepath , destpath)
    window['output'].update(value='extraction completed')

window.close()
