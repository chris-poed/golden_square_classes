import math
from lib.diary_entry import DiaryEntry

class Diary:
    def __init__(self):
        self._entries_list = []

    def add(self, entry):
        self._entries_list.append(entry)

    def all(self):
        return self._entries_list

    def count_words(self):
        return sum([entry.count_words() for entry in self._entries_list])

        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.

    def reading_time(self, wpm):
        return math.ceil(self.count_words() / wpm)

        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if len(self._entries_list) == 0:
            raise ValueError('No entries found')
        reading_length = wpm * minutes 
        possible_entries_to_read = [entry for entry in self._entries_list if entry.count_words() <= reading_length]
        return max(possible_entries_to_read, key=lambda x: x.count_words())



        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass