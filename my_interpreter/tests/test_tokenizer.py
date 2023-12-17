import pytest
from Interpreter.tokenizer import Tokenizer


class TestTokenizer():
	def test_move_forward(self):
		s = "4444"
		assert s == Tokenizer(s)._move_forward()


