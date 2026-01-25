# To Do app

A base for single page To Do application.

## Instructions

For just running the container, run `docker run palolaur/todo-app`.

You can also use `docker compose build` and `docker compose up` for running the container. In [docker-compose.yaml](./docker-compose.yaml) you can define the PORT environment variable as desired.

For deploying, run `kubectl create deployment todo-app --image=palolaur/todo-app`

For checking that the server responsed with the port number, run `kubectl logs -f todo-app-<pod-id>`

In deployment manifest, the PORT env is set as **3002**. After deploying, you can run `kubectl port-forward todo-app-<pod-id> 3000:3002` to forward the container port 3002 to your port 3000.
