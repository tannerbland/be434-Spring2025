.PHONY: test pdf clean

pdf:
	asciidoctor-pdf README.adoc

test:
	pytest -xv test.py csvfilter.py
	flake8 csvfilter.py
	pylint csvfilter.py

clean:
	rm -rf __pycache__
