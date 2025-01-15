.PHONY: test

data:
	wget ftp://ftp.imicrobe.us/projects/26/samples/578/CAM_SMPL_GS108.fa.gz

test:
	pytest -xv test.py seqmagique.py
	flake8 seqmagique.py
	pylint seqmagique.py
