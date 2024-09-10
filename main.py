import PySimpleGUI as sg
from review_kanji import get_kanji_list,shuffle_kanji_list,start_review
from review_kanji import Kanji
FONT_SIZE = 25
def main():
    kanji_list = get_kanji_list('heisig-kanjis.csv')
    starting_layout_column = [  [sg.Text('Enter the kanji range')],
                [sg.Text("Min", key='-OUT-')],
                [sg.Input(key='-IN-')],
                [sg.Text("Max", key='-OUT2-')],
                [sg.Input(key='-IN2-')],
                [sg.Button('Go'), sg.Button('Exit')]]

    show_kanji_layout_column = [[sg.Text('Kanji:',key='-KANJI-',font=('Helvetica', FONT_SIZE))],
                                [sg.Text('Meaning:',key='-MEANING-',font=('Helvetica', FONT_SIZE),visible=True)],
                                [sg.Text('On-reading:',key='-ON-',font=('Helvetica', FONT_SIZE),visible=True)],
                                [sg.Text('Kun-reading:',key='-KUN-',font=('Helvetica', FONT_SIZE),visible=True)],
                                [sg.Button('Next')]]

    starting_layout = [[sg.VPush()],
              [sg.Push(), sg.Column(starting_layout_column,element_justification='c'), sg.Push()],
              [sg.VPush()]]
    show_kanji_layout  = [
        [sg.VPush()],
        [sg.Push(),sg.Column(show_kanji_layout_column,element_justification='c'),sg.Push()],
        [sg.VPush()],
    ]

    window = sg.Window('Window Title', starting_layout, size=(500,300))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        
        min = values['-IN-']
        max = values['-IN2-']
        while not min.isdigit() or not max.isdigit() or int(min) > int(max):
            sg.popup('Please enter a valid number range:')
            _,values = window.read()
            min = values['-IN-']
            max = values['-IN2-']
        min = int(min)
        max = int(max)
        print(min,max)
        review_list = shuffle_kanji_list(kanji_list,min,max)
        # swap layout
        window.close()
        break
    window = sg.Window('Window Title', show_kanji_layout, size=(500,300),finalize=True)
    window['-KANJI-'].update(f'Kanji:{review_list[0].kanji} ')
    window['-MEANING-'].update(visible=False)
    window['-ON-'].update(visible=False)
    window['-KUN-'].update(visible=False)
    new_kanji = False
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        window['-KANJI-'].update(f'Kanji:{review_list[0].kanji} ')
        if event == 'Next':
            if not new_kanji:
                window['-MEANING-'].update(f'Meaning: {review_list[0].meaning}',visible=True)
                window['-ON-'].update(f'On-reading: {review_list[0].on_reading}',visible=True)
                window['-KUN-'].update(f'Kun-reading: {review_list[0].kun_reading}',visible=True)
                window['-KANJI-'].update(f'Kanji:{review_list[0].kanji} ')
                review_list.pop(0)
                new_kanji = True
            else:
                window['-MEANING-'].update(visible=False)
                window['-ON-'].update(visible=False)
                window['-KUN-'].update(visible=False)
                window['-KANJI-'].update(f'Kanji:{review_list[0].kanji} ')
                new_kanji = False

            if len(review_list) == 0:
                break

        


    window.close()


if __name__ == '__main__':
    main()