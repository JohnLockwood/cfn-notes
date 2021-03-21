.PHONY: build run debug_make

env := development
app := api
# Doesn't work yet:
POSTGRES_PASSWORD := $(shell aws ssm get-parameter --name /api/development/db/password --with-decryption | jq -r ".Parameter.Value")

run: build
	@ # echo Running...
	export POSTGRES_PASSWORD
	docker-compose up

build:
	export POSTGRES_PASSWORD
	docker-compose build

debug_make:
	echo Using environment $(env)
	echo Unsecurely printing password: $(POSTGRES_PASSWORD)
