import pytest
from lib.diary import Diary
from lib.diary_entry import DiaryEntry

# given a DiaryEntry, adds the diary entry to the entries list
# returns a list of instances of DiaryEntry

"""
Given three DiaryEntrys 
The three entries are visible in the list
"""

def test_add_and_list_three_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry('Title 1', 'Contents 1')
    entry_2 = DiaryEntry('Second title', 'Second set of content')
    entry_3 = DiaryEntry('Title 3', 'Third set of content')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.all() == [entry_1, entry_2, entry_3]


