from algorithms.dynamic_programming.array.steps import can_bounce

RUNWAY = [True, False, True, True, True, False, True, True, False, True, True]


def test_cant_bounce_out_of_bounds():
    assert not can_bounce(runway=RUNWAY, initspeed=2, initstart=10)


def test_cant_bounce_from_spike():
    assert not can_bounce(runway=RUNWAY, initspeed=0, initstart=1)


def test_impossible():
    assert not can_bounce(runway=RUNWAY, initspeed=4, initstart=3)


def test_possible():
    assert can_bounce(runway=RUNWAY, initspeed=5, initstart=0)
