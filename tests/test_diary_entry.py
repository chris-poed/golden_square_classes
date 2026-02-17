import pytest
from lib.diary_entry import DiaryEntry


"""
Count_words returns the correct word count
"""

def test_returns_correct_count():
    diary_entry = DiaryEntry('My Title', 'These are the contents')
    assert diary_entry.count_words() == 6

"""
Reading_time returns estimated reading time
"""

def test_estimate_200_words():
    diary_entry = DiaryEntry('My Title', """one two three four five six seven eight nine ten
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
    assert diary_entry.reading_time(200
        ) == 'Estimated reading time is 1 minute'

def test_estimate_less_than_200_words():
    diary_entry = DiaryEntry('My Title', """one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten""")
    assert diary_entry.reading_time(200) == 'Estimated reading time is less than a minute'


"""
Reading_chunk 
"""

def test_returns_string_of_300_words_to_match_reading_time_of_one_and_half_minutes():
        diary_entry = DiaryEntry('My Title', """one two three four five six seven eight nine ten
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
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten""")
        assert len(diary_entry.reading_chunk(200, 1.5)) == 300