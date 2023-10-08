import builtins
import mock
import pytest
from main import prefix_to_infix, postfix_to_infix, InvalidExpressionError, main


@pytest.fixture
def operators():
    return ["+", "-", "*", "/"]


class TestPrefixToInfix:
    def test_main_input_error(self, monkeypatch):
        with mock.patch.object(builtins, 'input', lambda _: "- - 2 2"):
            assert main(1) == -1

    def test_main_returns_0(self):
        with mock.patch.object(builtins, 'input', lambda _: "- - 2 2 2"):
            assert main() == 0

    @pytest.mark.parametrize(
        "expression, expected",
        [("+ - 13 4 55", "((13-4)+55)"),
         ("+ 2 * 2 - 2 1", "(2+(2*(2-1)))"),
         ("+ + 10 20 30", "((10+20)+30)"),
         ("/ + 3 10 * + 2 3 - 3 5", "((3+10)/((2+3)*(3-5)))")]
    )
    def test_prefix_to_infix(self, expression, expected, operators):
        assert prefix_to_infix(expression, operators) == expected

    def test_is_valid_expression(self, operators):
        with pytest.raises(InvalidExpressionError):
            prefix_to_infix("- - 1 2", operators)

    @pytest.mark.parametrize(
        "expression, expected",
        [("13 4 55 + -", "(13-(4+55))"),
         ("2 2 3 + * a b c - + /", "((2*(2+3))/(a+(b-c)))")]
    )
    def test_postfix_to_infix(self, expression, expected, operators):
        assert postfix_to_infix(expression, operators) == expected
