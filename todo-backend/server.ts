import express from "express";

const app = express();
const PORT = process.env.PORT ? parseInt(process.env.PORT, 10) : 3003;
const HOST = process.env.HOSTNAME || "0.0.0.0";

app.use(express.json());

const todos: string[] = [];

app.get("/", (req, res) => {
  res.send("<h1>Todo backend</h1>");
});

app.get("/todos", (req, res) => {
  res.status(200).json(todos);
});

app.post("/todos", (req, res) => {
  const { todo } = req.body;

  if (typeof todo !== "string") {
    res.status(400).send("Invalid todo item.");
    return;
  }

  todos.push(todo);

  res.status(201).json({ message: "Todo item created successfully." });
});

app.listen(PORT, HOST, () => {
  console.log(`Server is running on http://${HOST}:${PORT}`);
});
