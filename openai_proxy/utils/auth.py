import openai_proxy

from enum import Enum


# def an enum with a public, private and error field
class AuthStatus(str, Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
    ERROR = "ERROR"


def authenticate():
    # TODO: Authorize public users
    if openai_proxy.api_key is not None and openai_proxy.api_key != "":
        return AuthStatus.PUBLIC
    if openai_proxy.username is not None and openai_proxy.username != "" \
            and openai_proxy.course_id is not None and openai_proxy.course_id != "" \
            and openai_proxy.access_key is not None and openai_proxy.access_key != "" \
            and openai_proxy.access_token is not None and openai_proxy.access_token != "":
        return AuthStatus.PRIVATE
    return AuthStatus.ERROR
