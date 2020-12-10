venv: venv
	virtualenv venv -p python3.8

init:
	virtualenv venv -p python3.8
	pip install -r requirements.txt

tests:
	pytest src/*

.PHONY: init test venv
