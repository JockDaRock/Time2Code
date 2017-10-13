#!/bin/sh

echo "Deploying Time2Code on FaaS"
curl -O https://raw.githubusercontent.com/JockDaRock/Time2Code/master/time2code-swarm-deploy.yml
docker stack deploy time2code --compose-file time2code-swarm-deploy.yml