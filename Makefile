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
DOCKER_RUN = docker run -p 8000:8000 -it --env-file .env $(APPLICATION_NAME)


env:
	@$(eval SHELL:=/bin/bash)
	@cp .env.sample .env
	@echo "BOT_TOKEN=your_key" >> .env

run:
	python3 -m word_lexord_bot

%::
	echo $(MESSAGE)
