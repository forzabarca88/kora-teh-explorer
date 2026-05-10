from src.utils import load_system_prompt

MODEL_MAPPING = {
    'qwen3.5-0.8b': 'qwen3.5-0.8b-claude-4.6-opus-reasoning-distilled',
    'gemma-4-e2b': 'gemma-4-e2b-it'
}

MODEL = MODEL_MAPPING['qwen3.5-0.8b']
BASE_URL = 'http://192.168.0.5:1234/v1'
API_KEY = 'fake'
LOGGING_LEVEL = 'WARNING'
SYSTEM_PROMPT = load_system_prompt()
