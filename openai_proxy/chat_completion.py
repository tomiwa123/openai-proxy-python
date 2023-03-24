import json
import requests
import openai

import openai_proxy
from openai_proxy.utils import token_estimator, auth


class ChatCompletion:
    @staticmethod
    def create(messages=[], model="gpt-3.5-turbo"):
        authentication = auth.authenticate()
        if authentication == auth.AuthStatus.ERROR:
            return "Please set your username, courseId, accessKey, and accessToken or just your OpenAI API key"

        if authentication == auth.AuthStatus.PUBLIC:
            openai.api_key = openai_proxy.api_key
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages
            )
            messages.append(response["choices"][0]["message"])
            response["price"] = token_estimator.price_calculator_chat(messages, model=model, has_completion=True)
            return response

        body = {
            "username": openai_proxy.username,
            "courseId": openai_proxy.course_id,
            "accessKey": openai_proxy.access_key,
            "accessToken": openai_proxy.access_token,
            "model": model,
            "messages": messages
        }
        r = requests.post('http://openai-proxy.herokuapp.com/b/request/openai/chat', json=body)
        response = json.loads(r.text)
        if response['status'] == 'success':
            return response['response']
        else:
            return response

    @staticmethod
    def price(messages=[], model="gpt-3.5-turbo"):
        return {
            "status": "success",
            "price": token_estimator.price_calculator_chat(messages, model)
        }
