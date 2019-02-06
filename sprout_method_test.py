from sprout_method import lines_to_print

def test_lines_to_print():
    o_words = [('hello', 5), ('world', 10)]
    lines = lines_to_print(0, o_words)

    assert lines == ['hello:  5', 'world: 10'], lines

test_lines_to_print()
