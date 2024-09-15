import PySimpleGUI as sg
from SpellPack import spell
import keyboard
right_menu_def=['&菜单',['&复制','&粘贴','&剪切','&全选']]
layout = [
    [sg.Text('Author: Peter Norvig')],
    [sg.Text('URL: https://norvig.com/spell-correct.html')],
    [sg.Text('请输入单词',size=(10,1)), sg.Input(key='-WORD-',enable_events=True,right_click_menu=right_menu_def)],
    [sg.Text('检查结果',size=(10,1)), sg.Input(key='-RESOULT-',right_click_menu=right_menu_def)],
    [sg.Button('清空')]
          ]

window = sg.Window('拼写检查器', layout,use_default_focus=False, finalize=True)

while True:
    event, values =window.read()
    if event == None:
        break
    word = window['-WORD-'].get()
    if event == '-WORD-':
        window['-RESOULT-'].update(spell.correction(word))
    if event == '清空':
        window['-WORD-'].update(value='')
        window['-RESOULT-'].update(value='')
    if event in ("&复制"):
        keyboard.press('Control+c')
        keyboard.release('Control+c')
    if event in ("&粘贴"):
        keyboard.press('Control+v')
        keyboard.release('Control+v')
    if event in ("&剪切"):
        keyboard.press('Control+x')
        keyboard.release('Control+x')
    if event in ("&全选"):
        keyboard.press('Control+a')
        keyboard.release('Control+a')



window.close()