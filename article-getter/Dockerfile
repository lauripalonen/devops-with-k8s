FROM curlimages/curl:latest

WORKDIR /app
COPY --chmod=755 getter.sh /app/getter.sh

ENTRYPOINT ["/app/getter.sh"]