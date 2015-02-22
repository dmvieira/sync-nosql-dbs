# Makefile for varant starts and vagrant commands.

.PHONY: all run up restart pip test

# If you call make it just calls make run
all:
	$(MAKE) run;

# Destroy vagrant machine and runs again. Needs reload because of
# some configuration
run:
	@echo 'Remaking vagrant box...';
	vagrant destroy -f;
	$(MAKE) up;
	vagrant reload;

# Make vagrant up to start working
up:
	vagrant up;

# Restart all services: elasticsearch, cassandra and python daemon
# TODO make this feature
restart:
	@echo 'Restarting services...';

# Install pip requirements for new requirements
pip:
	@echo 'Installing pip requirements...';
	vagrant exec pip install -r requirements.txt;

# Test code and pep8 in vagrant
test:
	vagrant exec make test;
