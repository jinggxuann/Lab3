import Lab2.bmi as bmi

def test_bmi_normal_weight():
    weight = 46
    height = 1.52
    result = bmi.calculate_bmi(height, weight)
    assert (result == 0)

def test_bmi_over_weight():
    weight = 67
    height = 1.57
    result = bmi.calculate_bmi(height, weight)
    assert (result == 1)

def test_bmi_under_weight():
    weight = 35
    height = 1.47
    result = bmi.calculate_bmi(height, weight)
    assert (result == -1)

