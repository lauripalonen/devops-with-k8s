# Log output
Prints out a random string every 5 seconds.

## Deployment instructions
Pre-setup: ensure kubectl and k3d are installed and a cluster is running.

1. Run `kubectl create deployment log-output --image=palolaur/log-output` to deploy.
2. Run `kubectl logs -f log-output-<pod-id>` to display the logs.
