import employee_info as feet

def test_get_empl_by_age_range():
    result = []
    result = feet.get_employees_by_age_range(23,30)
    expected_results = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}]
    assert (result == expected_results)

def test_calc_ave_salary():
    result = []
    result = feet.calculate_average_salary()

    assert (result == 60166.67)

def test_get_empl_by_dept():
    result = []
    result = feet.get_employees_by_dept("Engineering")
    expected_result = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000}, {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert (result == expected_result)