DOCKER_IMAGE_NAME := opt_meth_img
DOCKER_CONTAINER_NAME := opt_meth

all: test build run

test:
	python3 -m test -v

build:
	docker build -t $(DOCKER_IMAGE_NAME) .

run:
	docker run --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME)

clean:
	docker container rm $(DOCKER_CONTAINER_NAME)
	docker image rm $(DOCKER_IMAGE_NAME)
