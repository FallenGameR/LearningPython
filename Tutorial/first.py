def first(l):
    return l[0] if l else None

def test_first():
    assert first([1, 2, 3]) == 2
    assert first([]) is None
