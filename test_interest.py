from interest import simInt

def test_interest_pos():
    assert simInt(20000,8,12) == 19200
def test_interest_zer():
    assert simInt(10000,7,0) == 0