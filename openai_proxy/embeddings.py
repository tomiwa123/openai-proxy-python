import json
import requests

import openai
import openai_proxy
from openai_proxy.utils import token_estimator, auth


class Embedding:
    @staticmethod
    def create(phrases=[]):
        authentication = auth.authenticate()
        if authentication == auth.AuthStatus.ERROR:
            return "Please set your username, courseId, accessKey, and accessToken or just your OpenAI API key"

        if authentication == auth.AuthStatus.PUBLIC:
            openai.api_key = openai_proxy.api_key
            response = openai.Embedding.create(input=phrases, model="text-embedding-ada-002")
            response["price"] = token_estimator.price_calculator_embedding(phrases)
            return response

        body = {
            "username": openai_proxy.username,
            "courseId": openai_proxy.course_id,
            "accessKey": openai_proxy.access_key,
            "accessToken": openai_proxy.access_token,
            "phrases": phrases,
        }
        r = requests.post('http://openai-proxy.herokuapp.com/b/request/openai/embedding', json=body)
        response = json.loads(r.text)
        if response['status'] == 'success':
            return response['response']
        else:
            return response

    @staticmethod
    def price(phrases=[]):

        return {
            "status": "success",
            "price": token_estimator.price_calculator_embedding(phrases)
        }
