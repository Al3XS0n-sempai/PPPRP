#!/bin/bash

eval $(minikube docker-env)

docker images

echo "Building server image with name server-image"
cd ./server
docker build -t server-image .

echo "Starting server"
kubectl apply -f server_pod.yaml

echo "------------------------"
cd ..
echo "------------------------"

echo "Building client image with name client-image"
cd ./client
docker build -t client-image .

echo "Starting client"
kubectl apply -f client_cronjob.yaml