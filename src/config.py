from os import getenv
from os.path import dirname, abspath, join
from uuid import uuid4

MODEL_MAPPING = {
    'qwen3.5-0.8b': 'unsloth/qwen3.5-0.8b',
    'gemma-4-e2b': 'unsloth/gemma-4-E2B-it-qat'
}

MODEL = getenv('MODEL', default=MODEL_MAPPING['gemma-4-e2b'])
BASE_URL = getenv('BASE_URL', default='http://localhost:1234/v1')
LOGGING_LEVEL = getenv('LOGGING_LEVEL', default='INFO')

RUN_ID = str(uuid4())
API_KEY = getenv('API_KEY', default='not used')

CODE_DIR = dirname(abspath(__file__))
DOCS_DIR = join(CODE_DIR, '..', 'docs')
MAX_CONTENT_SIZE = 100 * 1024  # 100 KB

with open(join(CODE_DIR, 'SYSTEM_PROMPT.md'), 'r', encoding='utf-8') as f:
    SYSTEM_PROMPT = f.read()
