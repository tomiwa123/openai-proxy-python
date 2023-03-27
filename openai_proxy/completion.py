import json
import requests

import openai
import openai_proxy
from openai_proxy.utils import token_estimator, auth


class Completion:
    @staticmethod
    def create(prompt,
               engine="babbage",
               temperature=0.7,
               max_tokens=200,
               top_p=1,
               frequency_penalty=0,
               presence_penalty=0,
               stop='',
               n=1
               ):
        authentication = auth.authenticate()
        if authentication == auth.AuthStatus.ERROR:
            return "Please set your username, courseId, accessKey, and accessToken or just your OpenAI API key"

        params = {
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

        if authentication == auth.AuthStatus.PUBLIC:
            openai.api_key = openai_proxy.api_key
            response = openai.Completion.create(**params)
            response["price"] = token_estimator.price_calculator_completion({
                "total_tokens": response["usage"]["total_tokens"],
                "engine": response["model"]
            })
            openai_proxy.session_price += response["price"]
            return response

        params["username"] = openai_proxy.username
        params["courseId"] = openai_proxy.course_id
        params["accessKey"] = openai_proxy.access_key
        params["accessToken"] = openai_proxy.access_token
        r = requests.post('http://openai-proxy.herokuapp.com/b/request/openai/completion', json=params)
        response = json.loads(r.text)
        if response['status'] == 'success':
            openai_proxy.session_price += response['response']["price"]
            return response['response']
        else:
            return response

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
            "price": token_estimator.price_calculator_completion(body)
        }
