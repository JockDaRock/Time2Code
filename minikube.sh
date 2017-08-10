#! /bin/bash

git clone https://github.com/alexellis/faas-netes

curl -sSL cli.get-faas.com | sudo sh

kubectl apply -f faas-netes/faas.yml,faas-netes/monitoring.yml,./time2code-server-k8s.yml

sed "s/localhost:31112/$(minikube ip):31112/" time2code-faas-cli-functions.yml > .time2code-faas-cli-minikube.yml

echo "Load the Code execution Functions with the faas-cli and then navigate to this site http://$(minikube ip):31114 in your favorite browser."
