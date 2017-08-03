#! /bin/bash

minikube start

git clone https://github.com/alexellis/faas-netes

curl -sSL cli.get-faas.com | sudo sh

kubectl apply -f faas-netes/faas.yml,faas-netes/monitoring.yml,./time2code-server-k8s.yml

kubectl get pods > .pod_running

while [ $(awk '/gateway/ {print $3}' .pod_running) != "Running" ] || [ $(awk '/faas-netesd/ {print $3}' .pod_running) != "Running" ] || [ $(awk '/prometheus/ {print $3}' .pod_running) != "Running" ] || [ $(awk '/alertmanager/ {print $3}' .pod_running) != "Running" ]; do
    echo "waiting for faas to start"
    sleep 1
    kubectl get pods > .pod_running
done

rm .pod_running

sed "s/localhost/$(minikube ip)/" time2code-faas-cli-functions.yml > .time2code-faas-cli-minikube.yml

faas-cli -action deploy -f .time2code-faas-cli-minikube.yml

echo "Now, navigate to http://$(minikube ip):31114 in your favorite browser, and HAPPY CODING!!!"
