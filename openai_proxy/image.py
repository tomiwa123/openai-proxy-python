import json
import requests

import openai
import openai_proxy
from openai_proxy.utils import token_estimator, auth


class Image:
    @staticmethod
    def create(prompt,
               n=1,
               size="1024x1024"
               ):
        authentication = auth.authenticate()
        if authentication == auth.AuthStatus.ERROR:
            return "Please set your username, courseId, accessKey, and accessToken or just your OpenAI API key"

        params = {
            "prompt": prompt,
            "n": n,
            "size": size
        }

        if authentication == auth.AuthStatus.PUBLIC:
            openai.api_key = openai_proxy.api_key
            response = openai.Image.create(**params)
            response["price"] = token_estimator.price_calculator_image(params)
            return response

        params["username"] = openai_proxy.username
        params["courseId"] = openai_proxy.course_id
        params["accessKey"] = openai_proxy.access_key
        params["accessToken"] = openai_proxy.access_token
        r = requests.post('http://openai-proxy.herokuapp.com/b/request/openai/image', json=params)
        response = json.loads(r.text)
        if response['status'] == 'success':
            return response['response']
        else:
            return response

    @staticmethod
    def price(prompt,
              n=1,
              size="1024x1024"
              ):

        body = {
            "prompt": prompt,
            "n": n,
            "size": size
        }

        return {
            "status": "success",
            "price": token_estimator.price_calculator_image(body)
        }
