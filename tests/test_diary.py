import pytest
from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
Returns the word count of all entries
"""
def test_returns_word_count_of_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry('Title 1', 'Contents 1')
    entry_2 = DiaryEntry('Second title', 'Second set of content')
    entry_3 = DiaryEntry('Title 3', 'Third set of content')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.count_words() == 16

"""
Given 200 words per minute
Returns the estimated reading time in minutes for all entries
"""
def test_returns_reading_time_for_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry('Title 1', """one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten""")
    entry_2 = DiaryEntry('Second title', """one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten""")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(200) == 2

"""
Given no diary entries
Reading time should return 0
"""

def test_reading_time_returns_0_when_no_entries():
    diary = Diary()
    assert diary.reading_time(200) == 0

"""
Given words per minute and the number of minutes the user has to read
Returns the instance of DiaryEntry that is closest to, but not over the length the user could read
"""
"""
Given three diary entries of 200 words, 100 words, and 20 words, wpm of 100, and 1 minute
Returns entry_2 chunk of 100 words
"""
def test_find_best_entry_for_reading_time():
    diary = Diary()
    entry_1 = DiaryEntry('Title 1', """one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten""")
    entry_2 = DiaryEntry('Second title', """
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten""")
    entry_3 = DiaryEntry('Third title', """one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten""")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.find_best_entry_for_reading_time(100, 1) == entry_1


def test_best_entry_for_reading_time_returns_error_if_no_entries():
    diary = Diary()
    with pytest.raises(ValueError) as error:
        diary.find_best_entry_for_reading_time(100, 1)
    assert str(error.value) == 'No entries found'
