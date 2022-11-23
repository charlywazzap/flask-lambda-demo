import pytest


@pytest.mark.parametrize(
    "test_cases",
    [
        (1, 1, 2),
    ],
)
def test_sum(test_cases):
    a, b, expected = test_cases
    res = a + b
    assert res == expected
