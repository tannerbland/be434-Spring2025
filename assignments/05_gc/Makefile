.PHONY: test

test:
	python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --pylint-rcfile=../pylintrc --mypy cgc.py tests/test.py

seqs.fa:
	./genseq.py -n 1000
