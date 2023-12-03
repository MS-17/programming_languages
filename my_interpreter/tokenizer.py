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


	def get_tokens(self):
		tokens = []
		for char in self._text:

			# print(f"Current character: {char}")
			if char.isdigit():
				tokens.append(Token(TokenType.INTEGER, char))
			elif char == "+":
				tokens.append(Token(TokenType.PLUS, char))
			elif char == "-":
				tokens.append(Token(TokenType.MINUS, char))

		
		return tokens


	def __str__(self):
		return f"{self._text}"



