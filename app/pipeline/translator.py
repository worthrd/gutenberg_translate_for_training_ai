import os
from openai import AzureOpenAI
from app.pipeline.prompt import SYSTEM_PROMPT, build_prompt

client = AzureOpenAI(
    api_key=os.environ["AZURE_API_KEY"],
    azure_endpoint=os.environ["AZURE_ENDPOINT"],
    api_version=os.environ["AZURE_API_VERSION"],
)

def adapt_to_turkish_child_story(english_text: str) -> str:
    prompt = build_prompt(english_text)

    res = client.chat.completions.create(
        model=os.environ["AZURE_DEPLOYMENT"],
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        top_p=0.9,
    )

    return res.choices[0].message.content.strip()
