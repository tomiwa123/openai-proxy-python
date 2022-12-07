import json
import requests

import openai_proxy
from openai_proxy.utils import token_estimator


def authenticate():
    if openai_proxy.username == "" or openai_proxy.username is None \
            or openai_proxy.course_id == "" or openai_proxy.course_id is None \
            or openai_proxy.access_key == "" or openai_proxy.access_key is None \
            or openai_proxy.access_token == "" or openai_proxy.access_token is None:
        return "Please set your username, courseId, accessKey, and accessToken"
    return False


class Completion:
    @staticmethod
    def create(prompt,
               engine="babbage",
               temperature=0.7,
               max_tokens=200,
               top_p=1,
               frequency_penalty=0,
               presence_penalty=0,
               stop=[],
               n=1
               ):
        error = authenticate()
        if error:
            return error

        body = {
            "username": openai_proxy.username,
            "courseId": openai_proxy.course_id,
            "accessKey": openai_proxy.access_key,
            "accessToken": openai_proxy.access_token,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "engine": engine,
            "temperature": temperature,
            "top_p": top_p,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty,
            "stop": stop,
            "n": n
        }
        r = requests.post('http://openai-proxy.herokuapp.com/b/request/openai', json=body)
        response = json.loads(r.text)
        if response['status'] == 'success':
            return response['response']
        else:
            return response['error']

    @staticmethod
    def price(prompt,
              engine="babbage",
              max_tokens=200,
              n=1
              ):

        body = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "engine": engine,
            "n": n
        }

        return {
            "status": "success",
            "price": token_estimator.price_calculator(body)
        }
