from shortGPT.gpt import gpt_utils
import os

def translateContent(content, language):
    chat, system = gpt_utils.load_local_yaml_prompt('prompt_templates/ollama_translate_content.yaml') \
        if os.getenv("USE_OLLAMA", "1") == "1" \
        else gpt_utils.load_local_yaml_prompt('prompt_templates/translate_content_gpt3.yaml')
    if language == "arabic":
        language =="arabic, and make the translated text two third of the length of the original."
    system = system.replace("<<LANGUAGE>>", language)
    chat = chat.replace("<<CONTENT>>", content)
    result = gpt_utils.gpt3Turbo_completion(chat_prompt=chat, system=system, temp=1)
    return result