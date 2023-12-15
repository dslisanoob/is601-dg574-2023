from MyCalc import MyCalc
import pytest

calc = MyCalc()

# Test cases for MyCalc class methods
# Dhruv Gargi - dg574 - 10th Nov 2023

def test_many_add():
    # Test addition for various inputs
    data = [
        {"a": "2", "b": "2", "r": "4"},
        {"a": "4", "b": "4", "r": "8"},
        {"a": "1", "b": "1", "r": "2"}
    ]
    for d in data:
        assert calc.add(d["a"], d["b"]) == int(d["r"])

def test_many_sub():
    # Test subtraction for different input pairs
    data = [
        {"a": "3", "b": "2", "r": "1"},
        {"a": "5", "b": "3", "r": "2"},
        {"a": "10", "b": "2", "r": "8"}
    ]
    for d in data:
        assert calc.sub(d["a"], d["b"]) == int(d["r"])

def test_many_mult():
    # Test multiplication for various cases
    data = [
        {"a": "3", "b": "2", "r": "6"},
        {"a": "5", "b": "3", "r": "15"},
        {"a": "10", "b": "2", "r": "20"}
    ]
    for d in data:
        assert calc.mult(d["a"], d["b"]) == int(d["r"])

def test_many_div():
    # Test division for a range of inputs
    data = [
        {"a": "10", "b": "2", "r": "5"},
        {"a": "9", "b": "3", "r": "3"},
        {"a": "15", "b": "3", "r": "5"}
    ]
    for d in data:
        assert calc.div(d["a"], d["b"]) == int(d["r"])
# Dhruv Gargi - dg574 - 10th Nov 2023
@pytest.fixture
def my_calc_ans_add():
    # Fixture for testing addition using the 'ans' attribute
    calc.ans = "3"
    return [
        {"a": "ans", "b": "2", "r": "5"},
        {"a": "ans", "b": "4", "r": "9"},
        {"a": "ans", "b": "1", "r": "10"},
        {"a": "ans", "b": "1", "negative": True, "r": "1"}
    ]
# Dhruv Gargi - dg574 - 10th Nov 2023
def test_data_ans_add(my_calc_ans_add):
    # Test addition using the 'ans' attribute
    for d in my_calc_ans_add:
        if "negative" in d and d["negative"]:
            assert calc.add(d["a"], d["b"]) != int(d["r"])
        else:
            assert calc.add(d["a"], d["b"]) == int(d["r"])

@pytest.fixture
def my_calc_ans_sub():
    # Fixture for testing subtraction with 'ans'
    calc.ans = "20"
    return [
        {"a": "ans", "b": "5", "r": "15"},
        {"a": "ans", "b": "4", "r": "11"},
        {"a": "ans", "b": "1", "r": "10"},
        {"a": "ans", "b": "1", "negative": True, "r": "1"}
    ]

def test_data_ans_sub(my_calc_ans_sub):
    # Test subtraction using 'ans'
    for d in my_calc_ans_sub:
        if "negative" in d and d["negative"]:
            assert calc.sub(d["a"], d["b"]) != int(d["r"])
        else:
            assert calc.sub(d["a"], d["b"]) == int(d["r"])

@pytest.fixture
def my_calc_ans_mult():
    # Fixture for testing multiplication using 'ans'
    calc.ans = "5"
    return [
        {"a": "ans", "b": "5", "r": "25"},
        {"a": "ans", "b": "4", "r": "100"},
        {"a": "ans", "b": "1", "r": "100"},
        {"a": "ans", "b": "1", "negative": True, "r": "1"}
    ]
# Dhruv Gargi - dg574 - 10th Nov 2023
def test_data_ans_mult(my_calc_ans_mult):
    # Test multiplication with 'ans'
    for d in my_calc_ans_mult:
        if "negative" in d and d["negative"]:
            assert calc.mult(d["a"], d["b"]) != int(d["r"])
        else:
            assert calc.mult(d["a"], d["b"]) == int(d["r"])

@pytest.fixture
def my_calc_ans_div():
    # Fixture for testing division with 'ans'
    calc.ans = "20"
    return [
        {"a": "ans", "b": "2", "r": "10"},
        {"a": "ans", "b": "5", "r": "2"},
        {"a": "ans", "b": "1", "r": "2"},
        {"a": "ans", "b": "1", "negative": True, "r": "1"}
    ]
# Dhruv Gargi - dg574 - 10th Nov 2023
def test_data_ans_div(my_calc_ans_div):
    # Test division using 'ans'
    for d in my_calc_ans_div:
        if "negative" in d and d["negative"]:
            assert calc.div(d["a"], d["b"]) != int(d["r"])
        else:
            assert calc.div(d["a"], d["b"]) == int(d["r"])
