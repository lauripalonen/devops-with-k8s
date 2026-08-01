import { NextResponse, NextRequest } from "next/server";
import { promises as fs } from "fs";

const IMG_PATH = process.env.IMAGE_STORAGE;
const EXPIRATION_TIME = 10 * 60 * 1000;

export async function GET(
  req: NextRequest,
  { params }: { params: Promise<{ filename: string }> },
) {
  const { filename } = await params;

  try {
    await fs.access(`${IMG_PATH}/${filename}`);
  } catch (error) {
    const newImage = await fetch("https://picsum.photos/200");
    const imageBuffer = await newImage.arrayBuffer();
    await fs.writeFile(`${IMG_PATH}/${filename}`, Buffer.from(imageBuffer));
  }

  const img = await fs.readFile(`${IMG_PATH}/${filename}`);

  const fileStats = await fs.stat(`${IMG_PATH}/${filename}`);
  const fileAge = Date.now() - fileStats.mtime.getTime();

  if (fileAge > EXPIRATION_TIME) {
    const newImage = await fetch("https://picsum.photos/200");
    const imageBuffer = await newImage.arrayBuffer();
    await fs.writeFile(`${IMG_PATH}/${filename}`, Buffer.from(imageBuffer));
  }

  return new NextResponse(img, {
    status: 200,
    headers: {
      "Content-Type": "image/jpeg",
    },
  });
}
