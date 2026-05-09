from src.utils import load_system_prompt


#MODEL = 'unsloth/qwen3.5-4b'
MODEL = 'gemma-4-e4b-it'
#BASE_URL = 'http://192.168.0.40:1234/v1'
BASE_URL = 'http://127.0.0.1:1234/v1'
API_KEY = 'fake'
LOGGING_LEVEL = 'INFO'
SYSTEM_PROMPT = load_system_prompt()
