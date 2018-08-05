from algorithms.string.parse.split import recursive_decode, dynamic_decode


def test_recursive_decode():
    assert 2 == recursive_decode("12")
    assert 3 == recursive_decode("226")
    assert 3 == recursive_decode("246")
    assert 5 == recursive_decode("1226")
    assert 0 == recursive_decode("011")
    assert 0 == recursive_decode("0")


def test_dynamic_decode():
    assert 2 == dynamic_decode("12")
    assert 3 == dynamic_decode("226")
    assert 3 == dynamic_decode("246")
    assert 5 == dynamic_decode("1226")
    assert 0 == dynamic_decode("011")
    assert 0 == dynamic_decode("0")