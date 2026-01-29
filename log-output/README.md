# log-output

This directory contains two apps: string-generator and server.

> [!NOTE]
> The file sharing between the two apps requires K8s deployment.

## string-generator

- creates a logs.txt file
- generates a random string on startup
- appends the string with current timestamp to the logs.txt file every 5 seconds

## server

- reads logs.txt file
- serves the file contents in port 8000

## Instructions

Have a kubernetes cluster running, and apply the deployment running `kubectl apply -f manifests`. The logs should be then visible at localhost:8081.
