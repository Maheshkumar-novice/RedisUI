.DEFAULT_GOAL := req
sources = app/*

.PHONY: install
install:
	pip install -r requirements.txt
	pre-commit install

.PHONY: format
format:
	ruff --fix --exit-non-zero-on-fix $(sources)
	ruff $(sources) -n --select I --fix --exit-non-zero-on-fix

.PHONY: lint
lint:
	ruff $(sources)
	ruff $(sources) -n --select I
.PHONY: req
req:
	pip freeze > requirements.txt
