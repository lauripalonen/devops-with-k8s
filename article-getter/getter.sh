#!/bin/sh
set -e

if [ -z "$API_URL" ]; then
  echo "Error: API_URL environment variable is not set."
  exit 1
fi

WIKI_URL=$(curl -sI -A "WikiTodoCron/1.0" "https://en.wikipedia.org/wiki/Special:Random" \
  | grep -i "^location:" \
  | awk '{print $2}' \
  | tr -d '\r\n')

if [ -z "$WIKI_URL" ]; then
  echo "Error: Failed to retrieve wiki url."
  exit 1
fi

echo "Fetched random article: $WIKI_URL"

curl -sS -f -X POST "$API_URL" \
  -H "Content-Type: application/json" \
  -d "{\"todo\": \"read $WIKI_URL\"}"

echo "Successfully created todo."