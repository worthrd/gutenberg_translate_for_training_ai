from pathlib import Path
import json
from app.celery_app import celery_app
from app.pipeline.translator import adapt_to_turkish_child_story

OUTPUT_DIR = Path("/app/output")

@celery_app.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=15,
    retry_kwargs={"max_retries": 5},
)
def process_chunk(self, chunk: str, chunk_id: int):
    print("TASK STARTED:", chunk_id)
    tr_story = adapt_to_turkish_child_story(chunk)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    row = {
        "messages": [
            {"role": "system", "content": "Sen küçük çocuklar için güvenli, neşeli ve öğretici hikayeler anlatan bir hikaye anlatıcısısın."},
            {"role": "user", "content": "Bu hikayeyi anlatır mısın?"},
            {"role": "assistant", "content": tr_story},
        ]
    }

    out_file = OUTPUT_DIR / f"chunk_{chunk_id}.json"
    out_file.write_text(json.dumps(row, ensure_ascii=False), encoding="utf-8")

    return "OK"
