from src.calculator import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
    assert add(-1.5, 1.5) == 0.0
    assert add(0.0, 0.0) == 0.0
    assert add(1.5, -2.5) == -1.0
    assert add(-1.5, 2.5) == 1.0
    assert add(0.0, 0.0) == 0.0
    assert add(1.5, -2.5) == -1.0

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    assert subtract(1.5, 2.5) == -1.0
    assert subtract(-1.5, 1.5) == -3.0
    assert subtract(0.0, 0.0) == 0.0
    assert subtract(1.5, -2.5) == 4.0
    assert subtract(-1.5, 2.5) == -4.0
    assert subtract(0.0, 0.0) == 0.0
    assert subtract(1.5, -2.5) == 4.0
    assert subtract(-1.5, 2.5) == -4.0
    assert subtract(0.0, 0.0) == 0.0

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0
    assert multiply(1.5, 2.5) == 3.75
    assert multiply(-1.5, 1.5) == -2.25
    assert multiply(0.0, 0.0) == 0.0
    assert multiply(1.5, -2.5) == -3.75
    assert multiply(-1.5, 2.5) == -3.75
    assert multiply(0.0, 0.0) == 0.0
    assert multiply(1.5, -2.5) == -3.75
def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(-1, 1) == -1
    assert divide(0, 0) == "Error: division by zero"
    assert divide(1.5, 2.5) == 0.6
    assert divide(-1.5, 1.5) == -1.0
    assert divide(0.0, 0.0) == "Error: division by zero"
    assert divide(1.5, -2.5) == -0.6
    assert divide(-1.5, 2.5) == -0.6
    assert divide(0.0, 0.0) == "Error: division by zero"
    assert divide(1.5, -2.5) == -0.6