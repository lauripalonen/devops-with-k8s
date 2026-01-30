# log-output

**Version 1.11. notes**:
- Three apps ([log-output server](./server), [log-output string-generator](./string-generator) and [ping-pong](../ping-pong)) now use a shared persistent volume 
- relevant updates:
  - [log-output/manifests/deployment.yaml](./manifests/deployment.yaml) has a persistent volume claimed
  - [pingpong/manifests/deployment.yaml](../pingpong/manifests/deployment.yaml) has a persistent volume claimed
  - [log-output/persistent_volume](./persistent_volume) has files for configuring the persistent volume

This directory contains two apps: string-generator and server. The file sharing between the two apps requires K8s deployment.

## string-generator

- creates a logs.txt file
- generates a random string on startup
- writes the string with current timestamp to the logs.txt file every 5 seconds

## server

- reads logs.txt file
- reads pongs.txt
- serves the files contents in port 8000

## Instructions

Have a kubernetes cluster running, and apply the deployment running `kubectl apply -f manifests` (this needs to be run for the [./persistent_volume](./persistent_volume) as well). The logs should be then visible at localhost:8081.
