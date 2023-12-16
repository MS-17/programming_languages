from tokenizer import Tokenizer


if __name__ == "__main__":
	# t = Tokenizer(" 45 +  6 ")
	t = Tokenizer("44.54 + 66")
	print("Initial expression:", t)

	tokens = t.get_tokens()
	print("\nTokenization result:")
	for i in tokens:
		print(i)
