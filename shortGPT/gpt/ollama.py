import json
import requests


def ollama_generate(base_url: str, model: str, prompt: str, options: dict = {},
    system: str = None, stream: bool = False, raw=False) -> dict:
    url = f"{base_url}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "options": options,
        "stream": stream,
        "raw": raw,
        **({"system": system} if system else {}),
    }
    http_resp = requests.post(url, data=json.dumps(payload))
    return http_resp.json()
