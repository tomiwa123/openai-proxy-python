import os

from openai_proxy.completion import Completion
from openai_proxy.price import Price


api_key = os.environ.get("OPENAI_API_KEY")
access_key = os.environ.get("OPENAI_PROXY_ACCESS_KEY")
access_token = os.environ.get("OPENAI_PROXY_ACCESS_TOKEN")

username = os.environ.get("OPENAI_PROXY_USERNAME")
course_id = os.environ.get("OPENAI_PROXY_COURSE_ID")

__all__ = [
    "api_key",
    "access_key",
    "access_token",
    "username",
    "course_id",
    "Completion",
    "Price",
]