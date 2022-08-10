install:
	poetry install
gendiff:
	poetry run gendiff
build:
	poetry build
	python3 -m pip install --user dist/*.whl --force-reinstall
lint: 
	poetry run flake8 gendiff
test:
	poetry run pytest
test-coverage:
	poetry run coverage run -m pytest
	poetry run coverage xml
