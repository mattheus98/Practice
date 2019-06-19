def potato(word):
    word = "A " + word
    return word


def test_answer():
    assert potato("Hel") == "A Hel"
