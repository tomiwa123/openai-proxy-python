import json

from openai_proxy.utils import token_estimator


def get_training_data(filename):
    with open(filename, 'r') as json_file:
        json_list = list(json_file)

    data = ""
    for json_str in json_list:
        result = json.loads(json_str)
        data += result['prompt'] + "\n"
        data += result['completion'] + "\n"

    return data


class Price:
    @staticmethod
    def training(filename=None,
                 prompt=None,
                 engine="babbage",
                 ):
        if filename:
            if not filename.endswith(".jsonl"):
                return {
                    'status': 'error',
                    'error': 'Please provide a .jsonl file'
                }
            else:
                data = get_training_data(filename)
        elif prompt:
            data = prompt
        else:
            return {
                'status': 'error',
                'error': 'Please provide a .jsonl file or prompt'
            }

        if not engine.endswith("-finetuned-training"):
            engine = f"{engine}-finetuned-training"

        body = {
            "prompt": data,
            "engine": engine,
        }

        return {
            'status': 'success',
            "price": token_estimator.price_calculator(body)
        }
