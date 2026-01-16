import re

def clean_gutenberg_text(text: str) -> str:
    start = re.search(r"\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*", text)
    end = re.search(r"\*\*\* END OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*", text)

    if start and end:
        text = text[start.end():end.start()]

    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
