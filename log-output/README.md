# log-output

**Version 1.14. notes**:

- [log-output server](./server) and [ping-pong](../ping-pong) no more share a persistent volume.
- [log-output server](./server) fetches the pong count through HTTP request to `http://pingpong-svc:2345/pings`.

## string-generator

- creates a logs.txt file
- generates a random string on startup
- writes the string with current timestamp to the logs.txt file every 5 seconds

## server

- reads logs.txt file
- fetches pong count from `http://pingpong-svc:2345/pings`
- serves the random string and pong count in port 8000

## Instructions

Have a kubernetes cluster running, and apply the deployment running `kubectl apply -f manifests` (this needs to be run for the [./persistent_volume](./persistent_volume) as well). The application expects the [ping-pong](../ping-pong) application to be running as well.

Once both applications are deployed, use port-forward for accessing the application on your local browser;

`kubectl port-forward log-output-<pod-id> 8082:8000`

`kubectl port-forward ping-pong-<pod-id> 8083:8000`

Now you can call the ping-pong API at localhost:8083/pingpong. You should now see in localhost:8082 the random string and ping / pong count that is incremented by a GET to the `/pingpong` API.
