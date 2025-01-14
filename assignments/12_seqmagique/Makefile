.PHONY: test

data:
	wget ftp://ftp.imicrobe.us/projects/26/samples/578/CAM_SMPL_GS108.fa.gz

test:
	python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --pylint-rcfile=../pylintrc --mypy seqmagique.py tests/test.py

