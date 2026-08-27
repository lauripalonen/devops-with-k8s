# To Do app

A base for single page To Do application. Displays a random image that changes every 10 minutes. Shows an input for adding todos, and a hardcoded list of todos. Actual functionality of adding is not yet implemented.

## Instructions

For just running the container, run `docker run palolaur/todo-app`.

You can also use `docker compose build` and `docker compose up` for running the container. In [docker-compose.yaml](./docker-compose.yaml) you can define the PORT environment variable as desired.

For deploying, run `kubectl create deployment todo-app --image=palolaur/todo-app`

For checking that the server responsed with the port number, run `kubectl logs -f todo-app-<pod-id>`

In deployment manifest, the PORT env is set as **3002**. After deploying, you can run `kubectl port-forward todo-app-<pod-id> 3000:3002` to forward the container port 3002 to your port 3000.

When running locally, a env variable `IMAGE_STORAGE` is expected, for the path for storing the image.

## Connection to todo-backend service

To Do app gets list of todo-items via [todo-backend service](../todo-backend). Also, when a new item is submitted via the form in the frontend, it gets posted to the backend. For now, the items are stored in memory of the backend.
