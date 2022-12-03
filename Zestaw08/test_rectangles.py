# Marlena Gryt
# Python 2022/2023
# Zd 8.1

from rectangles import *
import pytest

def test_from_points():
    assert Rectangle.from_points((Point(-1, -2), Point(1, 2))) == Rectangle(-1, -2, 1, 2)
    assert Rectangle.from_points((Point(0, 0), Point(2, 2))) == Rectangle(0, 0, 2, 2)

def test_properties():
    rect = Rectangle(-1, -2, 1, 2)
    assert rect.top == 2
    assert rect.left == -1
    assert rect.bottom == -2
    assert rect.right == 1
    assert rect.topleft == Point(-1, 2)
    assert rect.bottomleft == Point(-1, -2)
    assert rect.topright == Point(1, 2)
    assert rect.bottomright == Point(1, -2)
    assert rect.center == Point(0, 0)

if __name__ == "__main__":
    pytest.main()


# ================================================= test session starts =================================================
# platform win32 -- Python 3.9.8, pytest-7.2.0, pluggy-1.0.0
# rootdir: C:\Users\PC\desktop\Python
# plugins: anyio-3.6.1
# collected 2 items

# test_rectangles.py ..                                                                                            [100%]

# ================================================== 2 passed in 0.02s ==================================================
