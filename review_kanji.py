import csv
import sys
class Kanji:
    def __init__(self,row):
        self.kanji = row[0]
        self.id = row[2]
        self.meaning = row[4]
        self.on_reading = row[6]
        self.kun_reading = row[7]
    def __str__(self):
        return f'Kanji: {self.kanji}, Id:{self.id} Meaning: {self.meaning}, On-reading: {self.on_reading}, Kun-reading: {self.kun_reading}'
def get_kanji_list(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        kanji_list_raw = list(reader)[1:]
        kanji_list = []
        for kanji in kanji_list_raw:
            _kanji = Kanji(kanji)
            kanji_list.append( _kanji)
    return kanji_list
"""
This function will shuffle the kanji list and return the list of kanji to review.
"""
def shuffle_kanji_list(kanji_list,min,max):
    import random
    review_list = kanji_list[min-1:max]
    return random.sample(review_list,len(review_list))
"""
This function will start the review of the kanji.
It will show the kanji, meaning, on-reading and kun-reading.
Press any key to proceed to the next kanji.
Press "x" to save the kanji for next review.
Returns the list of kanji to save for next review if any.
"""
def start_review(kanji_list):
    print('Kani review starting...')
    print('To proceed to the next kanji, press any key. Press x to save it for next review')
    kanji_next = []
    for kanji in review_list:
        print('--------------------------------')
        print(kanji.kanji)
        is_next = input()
        if is_next == 'x':
            kanji_next.append(kanji.id)
        print(kanji)
    return kanji_next
"""
Driver code
"""
if __name__ == '__main__':
    file_name = 'heisig-kanjis.csv'
    args = sys.argv
    kanji_list = get_kanji_list(file_name)
    # Custom file mode
    if args[1] == '-f' and args[2]:
        file_name = args[2]
        review_list = []
        with open(file_name,'r') as f:
            lines = f.readlines()
        f.close()
        for line in lines:
            kanji = kanji_list[int(line)-1]
            review_list.append(kanji)
        review_list = shuffle_kanji_list(review_list,1,len(review_list))
    # Standard mode
    else:
        min = input('Enter the starting kanji id: ')
        max = input('Enter the ending kanji id: ')
        while not min.isdigit() or not max.isdigit() or int(min) > int(max):
            print('Please enter a number')
            min = input('Enter the starting kanji id: ')
            max = input('Enter the ending kanji id: ')
        min = int(min)
        max = int(max)
        review_list = shuffle_kanji_list(kanji_list,min,max)
    kanji_next = start_review(review_list)
    if kanji_next:
        file_to_save = input('Enter the file name to save the kanji for next review: ')
        with open(file_to_save,'w') as f:
            for kanji in kanji_next:
                f.write(f'{kanji}\n')
    