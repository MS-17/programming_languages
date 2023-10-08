PYTHON=python3
SOURCE="main.py"

all:run

test:
	coverage run -m pytest -v

cov: test
	coverage html

run:
	$(PYTHON) $(SOURCE)
