import random
import csv
import json
from logger import MyLogger


class Generator:
    def __init__(self):
        self.source = './data/data.csv'
        self.data = []
        self.mylogger = MyLogger()

    def read_csv_file(self):
        """Reads a CSV file and returns a list of lists, where each inner list contains 5 words.

        Args:
            file_path: The path to the CSV file.

        Returns:
            A list of lists, where each inner list contains 5 words.
        """
        self.mylogger.logDebug('Reading csv file...')
        with open(self.source, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if len(row) == 5:  # Ensure each row has 5 elements
                    self.data.append(row)
        
        self.mylogger.logDebug('Row Count: ' + str(len(self.data)))

   
    def getWords(self):
        if len(self.data) == 0:
            self.mylogger.logDebug('Loading Data...')
            self.read_csv_file()

        random_integer = random.randint(1, len(self.data))
        row = self.data[random_integer - 1]
        self.mylogger.logDebug('Read row ')
        self.mylogger.logDebug(row)
        cleaned_words = [word.strip().upper() for word in row]
        self.mylogger.logDebug(cleaned_words)
        return cleaned_words

    def getJumbledWords(self):
        """Rearranges each word in a list to create a new list of jumbled words.

        Args:
            word_list: A list of words to be rearranged.

        Returns:
            A new list of words, each with the same letters as the corresponding word in the input list, but in a different order.
        """

        word_list = self.getWords()
        jumbled_words = []
        for word in word_list:
            letters = list(word)
            random.shuffle(letters)
            new_word = ''.join(letters)
            while new_word == word:
                random.shuffle(letters)
                new_word = ''.join(letters)
            jumbled_words.append(new_word)
        self.mylogger.logDebug('Returning ')
        self.mylogger.logDebug(jumbled_words)

        result = list(zip(word_list, jumbled_words))
        result_json = json.dumps([{"Word":p, "jumbled_word":j} for p, j in result])
        self.mylogger.logDebug(result_json)
        self.mylogger.logDebug("returning from jumbledwords")
        return result_json
