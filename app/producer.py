from pathlib import Path
from app.pipeline.gutenberg import clean_gutenberg_text
from app.pipeline.chunker import chunk_story
from app.tasks.ml_tasks import process_chunk

INPUT_DIR = Path("/app/input")
print("INPUT FILES:", list(INPUT_DIR.glob("*.txt")))

chunk_id = 0

for txt_file in INPUT_DIR.glob("*.txt"):
    print(f"📘 Kuyruğa alınıyor: {txt_file.name}")

    text = txt_file.read_text(encoding="utf-8", errors="ignore")
    clean_text = clean_gutenberg_text(text)
    chunks = chunk_story(clean_text)

    for chunk in chunks:
        process_chunk.delay(chunk, chunk_id)
        chunk_id += 1

print("✅ Tüm chunk'lar kuyruğa alındı")
