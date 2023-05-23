exe: dist/main

dist/main: main.py
	pyinstaller -F -w main.py

run: main.py
	python3 main.py

test:
	pytest test.py

.PHONY: exe run test