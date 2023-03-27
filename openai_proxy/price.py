from openai_proxy.utils import token_estimator


class Price:
    def __init__(self):
        pass

    @staticmethod
    def from_response(response):
        if "model" not in response:
            # TODO: Image price cannot be estimated from response object
            return 0.02 * len(response["data"])
        
        model = response["model"]
        
        if "gpt" in model:
            # TODO: Support specific model names from response eg gpt-3.5-turbo-0301
            return token_estimator.price_calculator_chat_completion(response["usage"])
        elif "text-embedding" in model:
            return token_estimator.price_calculator_embedding_completion(response["usage"])
        else:
            return token_estimator.price_calculator_completion({
                "engine": model,
                "total_tokens": response["usage"]["total_tokens"],
            })


    @staticmethod
    def from_list_response(responses):
        cost = 0
        for response in responses:
            cost += Price.from_response(response)
        return cost
