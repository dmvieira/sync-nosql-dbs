# Top:-level Makefile for sync nosql dbs.
# Restart apps, test code and start vagrant.

ROOT_DIR = $(abspath ./)
export ROOT_DIR


.PHONY: all restart vagrant test

# If you call make it just make sure that vagrant is running, 
# install new pip requirements and test code.
all:
	$(MAKE) up -C vagrant
	$(MAKE) pip -C vagrant
	$(MAKE) restart -C vagrant
	$(MAKE) test -C vagrant

# Restarts all services for running app
restart:
	$(MAKE) restart -C vagrant

# Run tests for pep8 and app
# TODO make tests for app
test:
	@echo 'Checking for pep8'
	@find $(ROOT_DIR) -name "*.py" | xargs pep8

# Starts vagrant with server configured
vagrant:
	$(MAKE) run -C vagrant
