#!/bin/sh

if ! docker -v > /dev/null
then
    echo "docker installation not found; refer to README instructions on how to install docker"
    exit
fi

docker run -d -p 6379:6379 redis/redis-stack-server:latest