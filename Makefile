APP_NAME := student-api
VERSION := 4.0.0
IMAGE := $(APP_NAME):v$(VERSION)

build:
	docker build -t $(IMAGE) .

run:
	docker run -it --rm -p 5000:5000 --env-file .env $(IMAGE)

tag-latest:
	docker tag $(IMAGE) $(APP_NAME):latest

push:
	docker tag $(IMAGE) dipakrasal2009/$(APP_NAME):v$(VERSION)
	docker push dipakrasal2009/$(APP_NAME):v$(VERSION)

