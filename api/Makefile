.PHONY:  build_lambda

current_dir = $(shell pwd)

build_lambda:
	rm -rf build || true
	rm -rf app/build || true
	find app -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	mkdir app/build
	mkdir build
	BUILDKIT=1 docker build app -t lambda-builder:latest -f ../tools/scripts/Dockerfile.lambda
	docker run -v $(current_dir)/app/build:/build lambda-builder
	mv app/build/*.zip build
	rm -rf app/build || true
