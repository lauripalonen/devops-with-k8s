import styles from "./page.module.css";
import Image from "next/image";
import { addTodo, getTodos } from "./actions";

export default async function Home() {
  const { todos, error } = await getTodos();

  if (error) {
    console.error(error);
  }

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <div>
          <h1>To Do app</h1>
          <Image
            src="/api/images/random.jpg"
            alt="Random image"
            width={200}
            height={200}
            unoptimized
          />
        </div>
        <div>
          <form className={styles.formSection} action={addTodo}>
            <label htmlFor="new-todo">
              Enter a new todo (max 140 characters):
            </label>
            <div className={styles.formRow}>
              <input
                id="new-todo"
                name="todo"
                type="text"
                placeholder="Fetch groceries"
                maxLength={140}
                className={styles.input}
              />
              <button type="submit">Send</button>
            </div>
          </form>
          <h2>Todos</h2>
          <ul>
            {todos.map((todo: string, index: number) => (
              <li key={index}>{todo}</li>
            ))}
          </ul>
        </div>
      </main>
    </div>
  );
}
