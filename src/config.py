from src.utils import load_system_prompt
from os import getenv

MODEL_MAPPING = {
    'qwen3.5-0.8b': 'qwen3.5-0.8b-claude-4.6-opus-reasoning-distilled',
    'gemma-4-e2b': 'gemma-4-e2b-it'
}

MODEL = getenv('MODEL', default=MODEL_MAPPING['qwen3.5-0.8b'])
BASE_URL = getenv('BASE_URL', default='http://192.168.0.5:1234/v1')
LOGGING_LEVEL = getenv('LOGGING_LEVEL', default='INFO')

API_KEY = 'fake'
SYSTEM_PROMPT = load_system_prompt()
