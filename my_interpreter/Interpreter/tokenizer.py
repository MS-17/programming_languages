from enum import Enum, auto


class TokenType(Enum):
	# PLUS = auto()
	# MINUS = auto()
	OPERATOR = auto()
	NUMBER = auto()


class Token():
	def __init__(self, token_type: TokenType, token: str):
		self._token_type = token_type 
		self._token = token
	
	def __str__(self):
		return f"<{self._token_type} : {self._token}>"


class Tokenizer():
	def __init__(self, text):
		self._text = text
		self._current_pos = 0


	# the goal of this function is to get the whole number
	# move forward until encounter a space
	def _move_forward(self):
		res = []
		while self._text[self._current_pos].isdigit() or self._text[self._current_pos] == ".":
			res.append(self._text[self._current_pos])
			self._current_pos += 1
			# print(self._current_pos)
			if self._current_pos == len(self._text):
				break
			# process 45. 88 situation
		return "".join(res)


	def get_tokens(self):
		tokens = []

		while self._current_pos != len(self._text):
			# print(f"Current character: {char}")
			char = self._text[self._current_pos]
			if char.isdigit():
				number = self._move_forward()
				# print(number)
				tokens.append(Token(TokenType.NUMBER, number))
				continue
			elif char in ["+", "-", "*", "/"]:
				tokens.append(Token(TokenType.OPERATOR, char))
			self._current_pos += 1

		return tokens


	def __str__(self):
		return f"{self._text}"

