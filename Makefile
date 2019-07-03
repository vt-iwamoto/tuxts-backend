build:
	docker build -t tuxts-backend .

run:
	docker run --rm -it -v $(CURDIR):/tuxts-backend -p 8000:8000 tuxts-backend

sh:
	docker run --rm -it -v $(CURDIR):/tuxts-backend -p 8000:8000 tuxts-backend sh
