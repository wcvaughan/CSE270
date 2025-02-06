import pytest
import json
from build_sentences import (get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
                              get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures, pronouns, articles)

def test_get_seven_letter_word(monkeypatch):
    """test that a valid 7+ letter word is returned in uppercase"""
    monkeypatch.setattr('builtins.input', lambda _: 'elephant')
    result = get_seven_letter_word()
    assert result == 'ELEPHANT'
    monkeypatch.setattr('builtins.input', lambda _: 'cat')
    with pytest.raises(ValueError):
        get_seven_letter_word()

def test_parse_json_from_file(tmp_path):
    # create a temp file with test data
    test_data = {"key" : "value"}
    file_path = tmp_path / "test.json"
    with open(file_path, 'w') as temp_file:
        json.dump(test_data, temp_file)
    
    result = parse_json_from_file(file_path)
    assert result == test_data
    

def test_choose_sentence_structure():
    choice = choose_sentence_structure()
    assert choice in structures

def test_get_pronoun():
    choice = get_pronoun()
    assert choice in pronouns

def test_get_article():
    choice = get_article()
    assert choice in articles

word_list = {
"nouns": [
    "apples",
    "book"
],
"verbs": [
    "run",
    "walk"
],
"prepositions": [
    "about",
    "beyond"
],
"adjectives": [
    "happy",
    "cowardly"
],
"adverbs": [
    "quickly",
    "completely"
]
}
def test_get_word():
    nouns = word_list["nouns"]
    verbs = word_list["verbs"]
    assert get_word('A', nouns) == "apples"
    assert get_word('a', nouns) == "apples"
    assert get_word('B', nouns) == "book"
    assert get_word('R', verbs) == "run"
    assert get_word('r', verbs) == "run"
    assert get_word('W', verbs) == "walk"
    with pytest.raises(IndexError):
        get_word('1', nouns)
    with pytest.raises(IndexError):
        get_word('@', nouns)
    with pytest.raises(IndexError):
        get_word('[', nouns)
        

def test_fix_agreement():
    sentence = ["he", "will", "run"]
    fix_agreement(sentence)
    assert sentence == ["he", "will", "runs"]
    sentence = ["a", "big", "apple"]
    fix_agreement(sentence)
    assert sentence == ["an", "big", "apple"]
    sentence = ["The", "cat", "likes", "to", "run"]
    fix_agreement(sentence)
    assert sentence == ["The", "cat", "likes", "to", "runs"]
    


def test_build_sentence():
    pass    