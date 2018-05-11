# Python Flask Microservice Template

This is a cookicutter template for a python flask-based microservice.

It's a very basic project template, designed to let the developers build anythong around it. It only adds some simple helpers that I have thought useful.

- Makefile with a few commands to make easier the test process, documentation build, and manual testing.

- Sphinx prepared to autodocument your code using a `make docs`

- Unittest prepared to run all test suite with `make tests`

- `make run` to run the debug version of the code

- `docker-compose.yaml` prepared to build and run the service. It's using the version 2 of docker-compose to be able to extend the service from a extern docker-compose to be able to set-up a network of microservices.

- Docker image prepared to use with docker-compose

  - `make build` to build the docker image

  - `make docker-run` to run the dockerized service

- `make help` to get a overview of every option available in the makefile

## Extending this microservice

If you want to access the service from another docker-compose file without repeating code you just need to use this snippet:
``` yaml
version: "2"
services:
  service1:
    #Configuration

  service2:
    extends:
      file: /path/to/docker-compose.yaml
      service: name_of_service
    network:
      example

networks:
  example:
    driver: bridge
```

## Disclaimer

This template can have some failures as it's only a first version, as such any issue or feedback is welcomed and appreciated!
