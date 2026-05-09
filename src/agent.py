from src.config import MODEL, BASE_URL, API_KEY, LOGGING_LEVEL, SYSTEM_PROMPT
from src.utils import (
    get_current_timestamp, create_new_observations_post, read_memory_file, write_memory_file
)
import logging
from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI
from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper

logging.basicConfig(level=LOGGING_LEVEL)
logger = logging.getLogger(__name__)


def read_memory():
    '''
    Retrieve Kora's core memories.
    '''
    return read_memory_file()


def replace_memory(content: str):
    '''
    Update Kora's core memories with new information.
    '''
    write_memory_file(content)


def search_web(query: str) -> str:
    '''
    Search the web for the latest information and return the results.
    '''
    search = DuckDuckGoSearchAPIWrapper( max_results=10)
    logger.info(f"Searching web for: {query}")
    return search.run(query)


def create_blog_post(markdown_content: str):
    '''
    Create a blog post about your latest obervations and insights.
    '''
    create_new_observations_post(
        content=markdown_content, model_name=MODEL
    )


def run_agent():
    model = ChatOpenAI(model=MODEL, base_url=BASE_URL, api_key=API_KEY)
    agent = create_deep_agent(
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
        print(token.content, end='', flush=True)
