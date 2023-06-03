ifeq ($(shell test -e '.env' && echo -n yes),yes)
	include .env
endif


args := $(wordlist 2, 100, $(MAKECMDGOALS))
ifndef args
MESSAGE = "No such command (or you pass two or many targets to ). List of possible commands: make help"
else
MESSAGE = "Done"
endif


APPLICATION_NAME = word_lexord_bot
DOCKER_RUN = docker run -p 443:443 -it --env-file .env $(APPLICATION_NAME)


env:
	@$(eval SHELL:=/bin/bash)
	@cp .env.sample .env
	@echo "BOT_TOKEN=your_key" >> .env

run:
	python3 -m word_lexord_bot

up:
	docker compose -f docker-compose.yml up -d --remove-orphans

build:
	docker compose -f docker-compose.yml up -d --remove-orphans --build

down:
	docker compose down

lint:
	flake8 word_lexord_bot

%::
	echo $(MESSAGE)
