from sprout_class import WordList

def test_lines_to_print():
    o_words = [('hello', 5), ('world', 10)]
    word_list = WordList(0, o_words)
    lines = word_list.lines_to_print()

    assert lines == ['hello:  5', 'world: 10'], lines

test_lines_to_print()
