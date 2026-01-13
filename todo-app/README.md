# Todo app

For now, this app only has a single server that responds with given PORT number, if given.

## Instructions
Ensure you have a `.env` file with `PORT` defined.

For just running the container, run `docker run palolaur/todo-app`.

For deploying, run `kubectl create deployment todo-app --image=palolaur/todo-app`

For checking that the server responsed with the port number, run `kubectl logs -f todo-app-<pod-id>`
