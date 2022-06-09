install:
	poetry install
gendiff:
	poetry run gendiff 
package-install:
	poetry build
	python3 -m pip install --user dist/*.whl --force-reinstall
lint: 
	poetry run flake8 gendiff
test:
	poetry run pytest
test-coverage:
	poetry run coverage rin -m pytest
	poetry run coverage xml
