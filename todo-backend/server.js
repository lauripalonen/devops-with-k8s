import express from "express";
const app = express();
app.use(express.json());
const todos = [];
app.get("/", (req, res) => {
    res.send("<h1>Hello, Express.js Server!</h1>");
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
// Set up the server to listen on port 3000
const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
//# sourceMappingURL=server.js.map