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
		# self._accumulator = None
		self._current_pos = 0


	# def _is_number(self, char):
	# 	return char.isdigit()


	# get the whole number
	def _move_forward(self):
		res = []
		while self._text[self._current_pos] != " " and self._current_pos + 1 != len(self._text):
			print("Loop", self._text, self._text[self._current_pos])
			if self._text[self._current_pos].isdigit() or self._text[self._current_pos] == ".":
				res.append(self._text[self._current_pos])
			self._current_pos += 1
			print(self._current_pos)
		return "".join(res)


	def get_tokens(self):
		tokens = []
		# for char in self._text:
		while self._current_pos != len(self._text):
			# print(f"Current character: {char}")
			char = self._text[self._current_pos]
			if char.isdigit():
				# move forward until encounter a space or \t or \n
				# I need an accumulator that will store a number as a string to then convert it to the Token 
				number = self._move_forward()
				tokens.append(Token(TokenType.INTEGER, number))
				continue
			elif char == "+":
				tokens.append(Token(TokenType.PLUS, char))
			elif char == "-":
				tokens.append(Token(TokenType.MINUS, char))
			self._current_pos += 1

		# make 45  +6 work (45 is now divided)
		# add floats

		return tokens


	def __str__(self):
		return f"{self._text}"



