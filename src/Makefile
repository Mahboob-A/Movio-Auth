
# ### Docker management commands 
 
docker-up: 
	docker compose -p movio_auth_prod -f production.yml up --build -d --remove-orphans

docker-down: 
	docker compose -p movio_auth_prod -f production.yml down

docker-down-v: 
	docker compose -p movio_auth_prod -f production.yml down -v

docker-logs: 
	docker compose -p movio_auth_prod -f production.yml logs 

docker-logs-movio: 
	docker compose -p movio_auth_prod -f production.yml logs movio_auth_api

docker-restart-movio: 
	docker compose -p movio_auth_prod -f production.yml restart movio_auth_api

docker-restart-nginx:
	docker compose -p movio_auth_prod -f production.yml restart nginx

docker-exec-movio: 
	docker compose -p movio_auth_prod -f production.yml exec movio_auth_api /bin/bash 

docker-check-deploy:
	docker compose -p movio_auth_prod -f production.yml run --rm movio_auth_api python manage.py check --deploy 

# ## 


# ### Docker Volume and Postgres Database 

docker-exec-postgres: 
	docker compose -p movio_auth_prod -f production.yml exec postgres /bin/bash 

movio-database: 
	docker compose -p movio_auth_prod -f production.yml exec postgres psql --username="$(POSTGRES_USER)" --dbname="$(POSTGRES_DB)" 

# ## 



# ### Services logs commands 

docker-logs-postgres: 
	docker compose -p movio_auth_prod -f production.yml logs postgres

# ## 



# ### Django Commands

makemigrations: 
	docker compose -p movio_auth_prod -f production.yml run --rm movio_auth_api python manage.py makemigrations

migrate: 
	docker compose -p movio_auth_prod -f production.yml run --rm movio_auth_api python manage.py migrate

collectstatic: 
	docker compose -p movio_auth_prod -f production.yml run --rm movio_auth_api python manage.py collectstatic --no-input --clear 

superuser: 
	docker compose -p movio_auth_prod -f production.yml run --rm movio_auth_api python manage.py createsuperuser 

# ## 
