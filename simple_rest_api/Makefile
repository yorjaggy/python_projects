# Usage:
# newrelease        # creates a new release
# initialrelease	# remove ALL binaries and objects
CONTAINER_NAME := $(shell docker ps -aqf "name=backend")
SHELL=/bin/bash

.PHONY: pullcode clean release migrate

pullcode:
	@echo "Pulling from repo"
	git pull

release:
	@echo "Deploying new volume and containers..."
	docker volume create db_data
	docker-compose build
	docker stack deploy -c docker-compose-prod.yml globant_academy
	docker ps

migrate:
	@echo "Migrating db..." $(CONTAINER_NAME)
	docker exec -it $(CONTAINER_NAME) python manage.py db init
	@echo "----------------- database initiated -----------------"
	docker exec -it $(CONTAINER_NAME) python manage.py db migrate
	@echo "----------------- database migrated -----------------"
	docker exec -it $(CONTAINER_NAME) python manage.py db upgrade
	@echo "----------------- database upgraded -----------------"
	docker exec -it $(CONTAINER_NAME) python manage.py populatedb
	@echo "----------------- database populatedb -----------------"

clean:
	@echo "Deleting stack and volume..."
	docker stack rm globant_academy
	docker rm -f $(shell docker ps -aq)
	docker volume rm db_data