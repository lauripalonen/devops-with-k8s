import { NextResponse, NextRequest } from "next/server";

const TODO_URL = process.env.TODO_SERVICE_URL;

export async function GET() {
  if (!TODO_URL) {
    return new NextResponse("TODO_SERVICE_URL is not defined", {
      status: 500,
    });
  }

  const response = await fetch(TODO_URL, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  const todos = await response.json();

  return new NextResponse(JSON.stringify(todos), {
    status: 200,
    headers: {
      "Content-Type": "application/json",
    },
  });
}

export async function POST(req: NextRequest) {
  if (!TODO_URL) {
    return new NextResponse("TODO_SERVICE_URL is not defined", {
      status: 500,
    });
  }

  const body = await req.json();
  const { todo } = body;

  if (!todo || typeof todo !== "string") {
    return new NextResponse("Invalid todo item", {
      status: 400,
    });
  }

  const response = await fetch(TODO_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ todo }),
  });

  if (!response.ok) {
    return new NextResponse("Failed to create todo", {
      status: response.status,
    });
  }

  const result = await response.json();

  return new NextResponse(JSON.stringify(result), {
    status: 201,
    headers: {
      "Content-Type": "application/json",
    },
  });
}
