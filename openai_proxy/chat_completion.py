import json
import requests

import openai_proxy
from openai_proxy.utils import token_estimator


def authenticate():
    # TODO: Authorize public users
    if openai_proxy.username == "" or openai_proxy.username is None \
            or openai_proxy.course_id == "" or openai_proxy.course_id is None \
            or openai_proxy.access_key == "" or openai_proxy.access_key is None \
            or openai_proxy.access_token == "" or openai_proxy.access_token is None:
        return "Please set your username, courseId, accessKey, and accessToken"
    return False


class ChatCompletion:
    @staticmethod
    def create(messages=[]):
        error = authenticate()
        if error:
            return error

        body = {
            "username": openai_proxy.username,
            "courseId": openai_proxy.course_id,
            "accessKey": openai_proxy.access_key,
            "accessToken": openai_proxy.access_token,
            "messages": messages
        }
        r = requests.post('http://openai-proxy.herokuapp.com/b/request/openai/chat', json=body)
        response = json.loads(r.text)
        if response['status'] == 'success':
            return response['response']
        else:
            return response

    @staticmethod
    def price(messages=[]):

        return {
            "status": "success",
            "price": token_estimator.price_calculator_chat(messages)
        }
