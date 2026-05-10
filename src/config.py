from os import getenv
from uuid import uuid4

MODEL_MAPPING = {
    'qwen3.5-0.8b': 'qwen3.5-0.8b-claude-4.6-opus-reasoning-distilled',
    'gemma-4-e2b': 'gemma-4-e2b-it'
}

MODEL = getenv('MODEL', default=MODEL_MAPPING['gemma-4-e2b'])
BASE_URL = getenv('BASE_URL', default='http://localhost:1234/v1')
LOGGING_LEVEL = getenv('LOGGING_LEVEL', default='INFO')

RUN_ID = str(uuid4())
API_KEY = 'fake'

from src.utils import load_system_prompt
SYSTEM_PROMPT = load_system_prompt()
