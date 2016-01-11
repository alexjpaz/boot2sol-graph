default: run

run: build
	python -m SimpleHTTPServer 8000

build: boot2sol
	python check.py

boot2sol:
	git clone https://github.com/masneyb/boot2sol.git

