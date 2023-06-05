#!/bin/sh

# Build tests image and run tests
docker build -t kub-fastapi-test -f Dockerfile.test_backend .
docker run --rm kub-fastapi-test

# docker rmi kub-fastapi-test