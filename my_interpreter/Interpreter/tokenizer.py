from enum import Enum, auto


class TokenType(Enum):
	PLUS = auto()
	MINUS = auto()
	INTEGER = auto()


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

		# problem: index out of range for ex 45.4 + 66 => in the end there'll be index out of range
		while self._text[self._current_pos] != " ":
			# print("Loop", self._text, self._text[self._current_pos])
			if self._text[self._current_pos].isdigit() or self._text[self._current_pos] == ".":
				res.append(self._text[self._current_pos])
			self._current_pos += 1
			# print(self._current_pos)
			if self._current_pos == len(self._text):
				break
		return "".join(res)


	def get_tokens(self):
		tokens = []
		while self._current_pos != len(self._text):
			# print(f"Current character: {char}")
			char = self._text[self._current_pos]
			if char.isdigit():
				number = self._move_forward()
				tokens.append(Token(TokenType.INTEGER, number))
				continue
			elif char == "+":
				tokens.append(Token(TokenType.PLUS, char))
			elif char == "-":
				tokens.append(Token(TokenType.MINUS, char))
			self._current_pos += 1

		return tokens


	def __str__(self):
		return f"{self._text}"



