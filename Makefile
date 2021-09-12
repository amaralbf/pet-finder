deps: compile-deps sync-deps

compile-deps:
	pip-compile
	pip-compile requirements-dev.in

sync-deps:
	pip-sync requirements.txt requirements-dev.txt
	pip install -e .

flask:
	FLASK_APP=app.main FLASK_ENV=development flask run
