test:
	python -m pytest --cov=. --cov-report=term-missing -s

app:
	python script.py
