from src.config import MODEL, BASE_URL, API_KEY, LOGGING_LEVEL, SYSTEM_PROMPT, RUN_ID
from src.utils import (
    get_current_timestamp, create_new_observations_post, read_memory_file, write_memory_file
)
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper

# Set up logging with both console and rotating file handler
logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)

# Create logs directory if it doesn't exist
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(LOGGING_LEVEL)

# Rotating file handler
file_handler = RotatingFileHandler(
    log_dir / "kora.log",
    maxBytes=10485760,  # 10MB
    backupCount=5
)
file_handler.setLevel(LOGGING_LEVEL)

# Formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


@tool
def read_memory():
    '''
    Retrieve Kora's core memories.
    '''
    return read_memory_file()


@tool
def replace_memory(content: str):
    '''
    Update Kora's core memories with new information.
    '''
    write_memory_file(content, run_id=RUN_ID)


@tool
def search_web(query: str) -> str:
    '''
    Search the web for the latest information and return the results.
    '''
    search = DuckDuckGoSearchAPIWrapper( max_results=10)
    logger.info(f"Searching web for: {query}")
    return search.run(query)


@tool
def create_blog_post(markdown_content: str):
    '''
    Create a blog post about your latest obervations and insights.
    '''
    create_new_observations_post(
        content=markdown_content, model_name=MODEL, run_id=RUN_ID
    )


def run_agent():
    model = ChatOpenAI(model=MODEL, base_url=BASE_URL, api_key=API_KEY)
    agent = create_agent(
        model=model,
        tools=[search_web, create_blog_post, read_memory, replace_memory],
        system_prompt=SYSTEM_PROMPT
    )
    for token, metadata in agent.stream(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        f"The current time is {get_current_timestamp()}. "
                        "Assume your identity as Kora and make sure to search the web and create a blog post."
                        "Examine your memories and update them if your latest observations seem important for your study."
                    )
                }
            ]
        },
        stream_mode='messages'
    ):
        if hasattr(token, 'content') and token.content:
            print(token.content, end='', flush=True)

