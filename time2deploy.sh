#!/bin/sh

echo "Deploying Time2Code on FaaS"
docker stack deploy time2code --compose-file time2code-swarm-deploy.yml