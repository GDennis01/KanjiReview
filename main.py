import PySimpleGUI as sg
from review_kanji import get_kanji_list,shuffle_kanji_list,start_review
from review_kanji import Kanji
import sys
FONT_SIZE = 25
# TODO: Fix bug where layouts change position when switching between them.
def main():
    kanji_list = get_kanji_list('heisig-kanjis.csv')
    starting_layout_column = [  [sg.Text('Enter the kanji range')],
                [sg.Text("Min", key='-OUT-')],
                [sg.Input(key='-IN-')],
                [sg.Text("Max", key='-OUT2-')],
                [sg.Input(key='-IN2-')],
                [sg.Button('Go',key="Go"),sg.Button('Custom list') ,sg.Button('Exit')]]
    custom_list_layout_column = [[sg.Text('Enter file name')],
                                [sg.Input(key='-FILE-')],
                                [sg.Button('Go',key="Go2"), sg.Button('Standard list'),sg.Button('Exit')]]
    

    show_kanji_layout_column = [[sg.Text('Kanji:',key='-KANJI-',font=('Helvetica', FONT_SIZE))],
                                [sg.Text('Meaning:',key='-MEANING-',font=('Helvetica', FONT_SIZE),visible=True)],
                                [sg.Text('On-reading:',key='-ON-',font=('Helvetica', FONT_SIZE),visible=True)],
                                [sg.Text('Kun-reading:',key='-KUN-',font=('Helvetica', FONT_SIZE),visible=True)],
                                [sg.Button('Next'),sg.Button('Save for next review',key="-NEXTREVIEW-",visible=False)]]

    starting_layout = [[sg.VPush()],
              [sg.Push(), sg.Column(starting_layout_column,element_justification='c',key='-L1-'),sg.Column(custom_list_layout_column,visible=False,key='-L2-'),sg.Push()],
              [sg.VPush()]]
    show_kanji_layout  = [
        [sg.VPush()],
        [sg.Push(),sg.Column(show_kanji_layout_column,element_justification='c'),sg.Push()],
        [sg.VPush()],
    ]

    next_review_layout  = [
        [sg.Text("Enter the file name to save the next review:")],
        [sg.Input(key='-FILEREVIEW-')],
        [sg.Push(),sg.Button('Ok'),sg.Push()],
    ]

    window = sg.Window('Window Title', starting_layout, size=(500,300))
    layout=1
    while True:
        event, values = window.read()
        print(event,values)
        if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Exit0':
            sys.exit()
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
        if layout == 2 and event == 'Go2':
            file_name = values['-FILE-']
            with open(file_name,'r') as f:
                lines = f.readlines()
            f.close()
            review_list = []
            for line in lines:
                kanji = kanji_list[int(line)-1]
                review_list.append(kanji)
            review_list = shuffle_kanji_list(review_list,1,len(review_list))
            window.close()
            break

    window = sg.Window('Window Title', show_kanji_layout, size=(500,300),finalize=True)
    window['-KANJI-'].update(f'Kanji:{review_list[0].kanji} ')
    window['-MEANING-'].update(visible=False)
    window['-ON-'].update(visible=False)
    window['-KUN-'].update(visible=False)
    
    new_kanji = False
    kanji_for_next_review = []
    kanji_index = 0
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        # When in the second screen you click save for next review. It will save the kanji for next review.
        if event == '-NEXTREVIEW-':
            kanji_for_next_review.append(review_list[kanji_index-1])

        if event == 'Next' or event == '-NEXTREVIEW-':
            # When you click next the first time to show the meaning, on-reading and kun-reading
            if not new_kanji:
                window['-MEANING-'].update(f'Meaning: {review_list[kanji_index].meaning}',visible=True)
                window['-ON-'].update(f'On-reading: {review_list[kanji_index].on_reading}',visible=True)
                window['-KUN-'].update(f'Kun-reading: {review_list[kanji_index].kun_reading}',visible=True)
                window['-KANJI-'].update(f'Kanji:{review_list[kanji_index].kanji} ')
                window['-NEXTREVIEW-'].update(visible=True)
                kanji_index += 1
                new_kanji = True 
            # When you click next the second time to show the next kanji
            else:
                if len(review_list) == kanji_index:                               
                    window.close()
                    break
                window['-NEXTREVIEW-'].update(visible=False)
                window['-MEANING-'].update(visible=False)
                window['-ON-'].update(visible=False)
                window['-KUN-'].update(visible=False)
                window['-KANJI-'].update(f'Kanji:{review_list[kanji_index].kanji} ')

                new_kanji = False
    # If any kanji was saved for next review, it will ask for the file name to save them.
    if kanji_for_next_review:
        window = sg.Window('Window Title', next_review_layout, size=(500,300),finalize=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == 'Ok':
                file_name = values['-FILEREVIEW-']
                with open(file_name,'w') as f:
                    for kanji in kanji_for_next_review:
                        f.write(f'{kanji.id}\n')
                f.close()
                break          
    window.close()


if __name__ == '__main__':
    main()