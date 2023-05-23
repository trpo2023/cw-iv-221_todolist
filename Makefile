exe: dist/main

dist/main: main.py
	pyinstaller -F -w main.py

run: main.py
	python3 main.py

test:
	pytest -s test.py

clean:
	rm -f история.txt невыполненное.txt ID.txt

.PHONY: exe run test clean