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
                [sg.Button('Go'),sg.Button('Custom list') ,sg.Button('Exit')]]
    custom_list_layout_column = [[sg.Text('Enter file name')],
                                [sg.Input(key='-FILE-')],
                                [sg.Button('Go'), sg.Button('Standard list'),sg.Button('Exit')]]
    

    show_kanji_layout_column = [[sg.Text('Kanji:',key='-KANJI-',font=('Helvetica', FONT_SIZE))],
                                [sg.Text('Meaning:',key='-MEANING-',font=('Helvetica', FONT_SIZE),visible=True)],
                                [sg.Text('On-reading:',key='-ON-',font=('Helvetica', FONT_SIZE),visible=True)],
                                [sg.Text('Kun-reading:',key='-KUN-',font=('Helvetica', FONT_SIZE),visible=True)],
                                [sg.Button('Next')]]

    starting_layout = [[sg.VPush()],
              [sg.Push(), sg.Column(starting_layout_column,element_justification='c',key='-L1-'),sg.Column(custom_list_layout_column,visible=False,key='-L2-'),sg.Push()],
              [sg.VPush()]]
    show_kanji_layout  = [
        [sg.VPush()],
        [sg.Push(),sg.Column(show_kanji_layout_column,element_justification='c'),sg.Push()],
        [sg.VPush()],
    ]

    window = sg.Window('Window Title', starting_layout, size=(500,300))
    layout=1
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Custom list':
            window['-L1-'].update(visible=False)
            window['-L2-'].update(visible=True)
            layout = 2
        if event == 'Standard list':
            window['-L1-'].update(visible=True)
            window['-L2-'].update(visible=False)
            layout = 1
        if layout == 1 and event == 'Go':
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
            window.close()
            break
        if layout == 2 and event == 'Go':
            # TODO: leggere il file, salvarsi i numeri e creare la review list con solo i numeri salvati
            pass

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
        if len(review_list) != 0:
            window['-KANJI-'].update(f'Kanji:{review_list[0].kanji} ')
        else:
            window.close()
        if event == 'Next':
            if not new_kanji:
                window['-MEANING-'].update(f'Meaning: {review_list[0].meaning}',visible=True)
                window['-ON-'].update(f'On-reading: {review_list[0].on_reading}',visible=True)
                window['-KUN-'].update(f'Kun-reading: {review_list[0].kun_reading}',visible=True)
                window['-KANJI-'].update(f'Kanji:{review_list[0].kanji} ')
                review_list.pop(0)
                new_kanji = True
                
                # break
            else:
                if len(review_list) == 0:
                    window.close()
                    break
                window['-MEANING-'].update(visible=False)
                window['-ON-'].update(visible=False)
                window['-KUN-'].update(visible=False)
                window['-KANJI-'].update(f'Kanji:{review_list[0].kanji} ')
                new_kanji = False
            # FIXME: fix the last kanji 
            

        


    window.close()


if __name__ == '__main__':
    main()