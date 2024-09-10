import csv
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
def shuffle_kanji_list(kanji_list,min,max):
    import random
    review_list = kanji_list[min-1:max]
    return random.sample(review_list,len(review_list))
def start_review(kanji_list):
    # review_list = kanji_list[min-1:max]
    print('Kani review starting...')
    print('To proceed to the next kanji, press any key')
    for kanji in review_list:
        print('--------------------------------')
        print(kanji.kanji)
        # remove the below line to show the meaning
        input()
        print(kanji)
if __name__ == '__main__':
    # read csv file
    file_name = 'heisig-kanjis.csv'
    kanji_list = get_kanji_list(file_name)
    
    # min = input('Enter the starting kanji id: ')
    # max = input('Enter the ending kanji id: ')
    # while not min.isdigit() or not max.isdigit() or int(min) > int(max):
    #     print('Please enter a number')
    #     min = input('Enter the starting kanji id: ')
    #     max = input('Enter the ending kanji id: ')
    # min = int(min)
    # max = int(max)
    # shuffle
    min = 1
    max = 10
    import random
    print(type(kanji_list))
    l = review_list = shuffle_kanji_list(kanji_list,min,max)
    for i in l:
        print(i)
    
    
    
    # review_list = shuffle_kanji_list(kanji_list,min,max)
    # start_review(review_list)