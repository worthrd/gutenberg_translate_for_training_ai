import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.environ["AZURE_API_KEY"],
    azure_endpoint=os.environ["AZURE_ENDPOINT"],
    api_version=os.environ["AZURE_API_VERSION"],
)

def translate_story(text: str) -> str:
    res = client.chat.completions.create(
        model=os.environ["AZURE_DEPLOYMENT"],
        messages=[
            {"role": "system", "content": "Sen 5-7 yaş çocuklar için hikayeler anlatan bir Türk hikaye anlatıcısısın."},
            {"role": "user", "content": text},
        ],
        temperature=0.7,
        top_p=0.9,
    )
    return res.choices[0].message.content.strip()
