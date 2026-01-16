def chunk_story(text, min_words=120, max_words=220):
    paragraphs = text.split("\n\n")
    chunks, current = [], []
    count = 0

    for p in paragraphs:
        words = len(p.split())
        current.append(p)
        count += words

        if min_words <= count <= max_words:
            chunks.append("\n".join(current))
            current, count = [], 0

    return chunks
