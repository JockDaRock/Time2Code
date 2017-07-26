#!/bin/sh

echo "Deploying Time2Code on FaaS"
docker stack deploy func --compose-file time2code-swarm-deploy.yml