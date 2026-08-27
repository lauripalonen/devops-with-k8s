"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";

const TODO_URL = process.env.TODO_SERVICE_URL;

export async function addTodo(formData: FormData) {
  try {
    const todo = formData.get("todo");

    if (!todo || typeof todo !== "string") {
      console.error("Invalid todo item");
      return;
    }

    if (!TODO_URL) {
      console.error("TODO_SERVICE_URL is not defined");
      return;
    }

    const response = await fetch(`${TODO_URL}/todos`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ todo }),
    });

    if (!response.ok) {
      console.error("Failed to create todo:", response.statusText);
    }

    console.log("todo backend response:", response);
    revalidatePath("/");
  } catch (error) {
    console.error("Error adding todo:", error);
  }
}

export async function getTodos() {
  try {
    if (!TODO_URL) {
      console.error("TODO_SERVICE_URL is not defined");
      return { error: "TODO_SERVICE_URL is not defined", todos: [] };
    }

    const response = await fetch(`${TODO_URL}/todos`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      console.error("Failed to fetch todos:", response.statusText);
      return { error: "Failed to fetch todos", todos: [] };
    }

    const todos = await response.json();
    return { todos };
  } catch (error) {
    console.error("Error fetching todos:", error);
    return { error: "An unexpected error occurred", todos: [] };
  }
}
