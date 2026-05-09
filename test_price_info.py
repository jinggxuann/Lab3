import price_info as jip

def test_total_cost():
    result = jip.total_cost_shopping()
    assert (result == 46.75)

def test_cost_of_fruit():
    result = []
    result = jip.cost_of_fruits('apple',2)

    assert (result == 2.40)