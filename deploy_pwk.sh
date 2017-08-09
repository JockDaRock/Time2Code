#!/bin/sh

yum update -y && yum install -y git

kubeadm init --apiserver-advertise-address $(hostname -i) && \
kubectl apply -n kube-system -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"

cd /root/
git clone https://github.com/alexellis/faas-netes.git \
 && cd faas-netes && kubectl apply -f faas.yml,rbac.yml,monitoring.yml

cd /root/
curl -sSL cli.get-faas.com | sh
git clone https://github.com/JockDaRock/Time2Code.git \
&& cd Time2Code && git checkout dev
faas-cli -action deploy -f ~/Time2Code/time2code-faas-cli-functions.yml
