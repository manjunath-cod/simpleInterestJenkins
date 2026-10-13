from simple_interest import simInt

def test_simpleInt_pos():
    assert simInt(20000, 8, 12) == 19200.0

def test_simpleInt_neg():
    assert simInt(20000, 8, 12) != 1920.0

def test_simpleInt_zero():
    assert simInt(10000, 7, 0) == 0.0