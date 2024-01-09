import pytest
from my_interpreter.Interpreter.tokenizer import Tokenizer


class TestTokenizer():
	@pytest.mark.parametrize(
		"s, res",
		[("4444", "4444"), ("4444   ", "4444"), (" 4444 ", "")]
	)
	def test_move_forward(self, s, res):
		# print("Res:", s.strip(), Tokenizer(s)._move_forward())
		assert res == Tokenizer(s)._move_forward()

	def test_move_forward_exceptions(self):
		s = "444\n"
		print("Info", Tokenizer(s)._move_forward())
		assert 0 == 0

	def test_get_tokens(self):
		pass