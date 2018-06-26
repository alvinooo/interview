# http://blog.refdash.com/dynamic-programming-tutorial-example/
def can_bounce(runway, initspeed, initstart=0):
    if initstart >= len(runway) or not runway[initstart]:
        return False
    if initspeed == 0:
        return runway[initstart]
    return can_bounce(runway, initspeed - 1, initstart + initspeed - 1) or \
           can_bounce(runway, initspeed, initstart + initspeed) or \
           can_bounce(runway, initspeed + 1, initstart + initspeed + 1)