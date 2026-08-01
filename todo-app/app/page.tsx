import styles from "./page.module.css";
import Image from "next/image";

export default async function Home() {
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
      </main>
    </div>
  );
}
