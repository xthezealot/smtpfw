run:
	docker run -it --rm --name my-running-script -v "$(PWD)":/usr/src/myapp -w /usr/src/myapp -p 8025:8025 python:3.4 python main.py
