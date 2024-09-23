# Simple Kanji Heisig Reviewer
This is a simple program to review the Heisig Kanji book.
The review mechanism is from Kanji to Keyword. For the reverse, you can use an Anki Deck.

## How to use 
1. Install Python3
2. Install the required packages
```bash
pip install -r requirements.txt
```
3. Run the program
```bash
python3 main.py
```
4. Input the range of the Kanji you want to review(i.e. 1-100).
5. Click Next to show the meaning of the Kanji. Click Next again to show the next Kanji

### Custom review
You can also review a custom list of Kanji by creating a text file with the Kanji you want to review. Each line of the file should contain a Kanji number.
While reviewing, you can mark a kanji to later on save it to a file whose name you can specify.

### CLI Mode
You can also use the CLI mode by running the `review_kanji.py` file instead
```bash
python3 review_kanji.py
```
For the custom review, you can specify the file name as an argument
```bash
python3 review_kanji.py -f custom_kanji.txt
```

## CSV file
Thanks to https://github.com/sdcr/heisig-kanjis/tree/master for the CSV file.

