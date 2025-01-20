import pytest
from HW_interview import check_balance_brackets

@pytest.mark.parametrize(
    'brackets, expected',
    (
        ("(((([{}]))))", "Сбалансированно"),
        ("[([])((([[[]]])))]{()}", "Сбалансированно"),
        ("{{[()]}}", "Сбалансированно"),
        ("}{}", "Неcбалансированно"),
        ("{{[(])]}}", "Неcбалансированно"),
        ("[[{())}]", "Неcбалансированно")
    )
)
def test_check_balance_brackets(brackets, expected):
    result = check_balance_brackets(brackets)
    assert result == expected

