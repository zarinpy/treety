import pytest
from main import sortExpressions


@pytest.mark.parametrize("expressions, expected", [
    (["x = a * y", "y = x * 5"], ["cyclic_dependency"]),
    (["x = y + 6", "y = 7 * 4", "z = ( x * y )"],
     ["y = 7 * 4", "x = y + 6", "z = ( x * y )"]),
    (["x = y * z", "y = z + 5", "z = 10"],
     ["z = 10", "y = z + 5", "x = y * z"]),
    (["x = y + z", "y = z * 2", "z = 3"], ["z = 3", "y = z * 2", "x = y + z"]),
    (["x = y + z", "y = z * 2", "z = x"], ["cyclic_dependency"]),
    (["x = y * z", "y = z + 6", "z = ( x * y )"], ["cyclic_dependency"]),
    (["x = y * z", "y = z + 5", "z = 10"],
     ["z = 10", "y = z + 5", "x = y * z"]),
    (["x = y + z", "y = z * 2", "z = 3"], ["z = 3", "y = z * 2", "x = y + z"])
])
def test_sortExpressions(expressions, expected):
    assert sortExpressions(expressions) == expected
