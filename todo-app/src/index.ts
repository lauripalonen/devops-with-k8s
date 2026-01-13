import { createServer } from "node:http";

const port = process.env.PORT;

const server = createServer((req, res) => {});

server.listen(port, () => {
  if (!port) {
    throw new Error("PORT environment variable not defined");
  }

  console.log(`Server started in port ${port}`);
});
