import os
import json
import requests

from openai_proxy.completion import Completion
from openai_proxy.embeddings import Embedding
from openai_proxy.chat_completion import ChatCompletion
from openai_proxy.image import Image


api_key = os.environ.get("OPENAI_API_KEY")
access_key = os.environ.get("OPENAI_PROXY_ACCESS_KEY")
access_token = os.environ.get("OPENAI_PROXY_ACCESS_TOKEN")

username = os.environ.get("OPENAI_PROXY_USERNAME")
course_id = os.environ.get("OPENAI_PROXY_COURSE_ID")

# r = requests.get('http://openai-proxy.herokuapp.com/b/request/engines')
# response = json.loads(r.text)
#
# engines = [engine for engine in response if engine is not None]

__all__ = [
    "api_key",
    "access_key",
    "access_token",
    "username",
    "course_id",
    # "engines",
    "Completion",
    "Embedding",
    "ChatCompletion",
    "Image"
]