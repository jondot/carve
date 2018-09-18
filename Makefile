watch:
	poetry run ptw -- --testmon
test:
	tox
release:
	ci/release.py