# File: tests/test_vowel_remover.py

from lib.vowel_remover import VowelRemover

def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."

def test_if_passed_aeiou_returns_an_empty_string():
    remover = VowelRemover('aeiou')
    assert remover.remove_vowels() == ''