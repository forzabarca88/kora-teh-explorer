from src.utils import load_system_prompt


#MODEL = 'unsloth/qwen3.5-4b'
MODEL = 'qwen3.5-0.8b-claude-4.6-opus-reasoning-distilled'
#BASE_URL = 'http://192.168.0.40:1234/v1'
BASE_URL = 'http://192.168.0.5:1234/v1'
API_KEY = 'fake'
LOGGING_LEVEL = 'WARNING'
SYSTEM_PROMPT = load_system_prompt()
