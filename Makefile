.PHONY: db build run run-api stop clean logs

db:
	echo "Starting DB container..."
	docker compose up -d migrate

build:
	echo "Building REST API image..."
	docker compose build api

run-api:
	echo "Running API container..."
	docker compose up -d api

run: db build run-api

stop:
	docker compose down

clean:
	docker compose down -v

logs:
	docker compose logs -f
