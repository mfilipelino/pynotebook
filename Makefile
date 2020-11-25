enviroment: venv
	virtualenv venv -p python3.8

init:
	virtualenv venv -p python3.8
	pip install -r requirements.txt

test:
	py.test tests

.PHONY: init test
