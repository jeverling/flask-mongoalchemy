build: bootstrap develop test coverage

release: zip_docs
	python setup.py sdist upload
	@echo 'Released :)'

zip_docs: documentation
	cd docs/_build/html && zip -r docs.zip *
	@echo 'Docs are at docs/_build/html/docs.zip file'

bootstrap:
	pip install -r requirements.txt

develop:
	python -c 'from flaskext import mongoalchemy' 2>/dev/null || python setup.py develop

test: clean
	specloud --config=tests/nose.cfg

coverage:
	coverage html

documentation: clean
	cd docs && make html

clean:
	@echo 'Cleaning...'
	git clean -dfx
