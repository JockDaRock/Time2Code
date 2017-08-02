#! /bin/bash

minikube start

git clone https://github.com/alexellis/faas-netes

curl -sSL cli.get-faas.com | sudo sh

kubectl apply -f faas-netes/faas.yml,faas-netes/monitoring.yml,./time2code-server-k8s.yml

sed "s/localhost/$(minikube ip)/" time2code-faas-cli-functions.yml > .time2code-faas-cli-minikube.yml

faas-cli -action deploy -f .time2code-faas-cli-minikube.yml

echo "Now, navigate to http://$(minikube ip):31114 in your favorite browser, and HAPPY CODING!!!"
