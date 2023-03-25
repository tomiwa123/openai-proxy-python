import tiktoken
from openai_proxy.utils.constants import get_price_per_token, get_engine_max_tokens


def token_counter(prompt, model):
    # TODO: Does not properly support key "name" in chat models
    # counts tokens given input text
    #
    # input: text
    # output: length of tokens

    encoder = tiktoken.encoding_for_model(model) if model else tiktoken.get_encoding("cl100k_base")
    token_len = len(encoder.encode(prompt))

    return token_len


def get_message_padding(model):
    message_padding = 0
    if not model:
        pass
    elif model == "gpt-4":
        message_padding = 3
    elif model == "gpt-3.5-turbo":
        message_padding = 4
    return message_padding


def parse_args(args):
    prompt = args['prompt'] if 'prompt' in args else ''
    engine = args['engine'] if 'engine' in args else 'babbage'
    max_tokens = args['max_tokens'] if 'max_tokens' in args else 500
    n = args['n'] if 'n' in args else 1
    total_tokens = args['total_tokens'] if 'total_tokens' in args else None

    return {
        "prompt": prompt,
        "engine": engine,
        "max_tokens": max_tokens,
        "n": n,
        "total_tokens": total_tokens,
    }


def price_calculator_completion(args):
    # given prompt, engine and max_tokens, calculate estimated price in dollar
    #
    # input:
    #     prompt: text
    #     engine: choose between ada, babbage, curie and davinci
    #     max_tokens: parameter that sets maximum length of model response, int
    # output: estimated price in dollar
    #
    # acknowledgement: this calculation is for completion model only.
    #                 best_of option is not considered.

    p_args = parse_args(args)
    prompt = p_args['prompt']
    engine = p_args['engine']
    max_tokens = p_args['max_tokens']
    n = p_args['n']
    total_tokens = p_args['total_tokens']

    token_len = token_counter(prompt, engine)
    this_engine_max_tokens = get_engine_max_tokens(engine)
    this_price_per_token = get_price_per_token(engine)

    price_per_completion = min((token_len + int(max_tokens)), this_engine_max_tokens) * this_price_per_token

    if engine in ['ada', 'babbage', 'curie', 'davinci', 'ada-finetuned', 'babbage-finetuned', 'curie-finetuned',
                  'davinci-finetuned']:
        price = price_per_completion * n
    else:
        price = price_per_completion * 1

    # the prompt in this case is the entire training data (prompt + completion)
    if engine in ['ada-finetuned-training', 'babbage-finetuned-training', 'curie-finetuned-training',
                  'davinci-finetuned-training']:
        price = token_len * this_price_per_token

    if total_tokens:
        price = total_tokens * this_price_per_token

    return round(price, 10)


def price_calculator_chat(messages, model='gpt-3.5-turbo', has_completion=False):
    prompt_cost = 0
    completion_cost = 0

    # Post-request
    if has_completion:
        prompt_tokens = 0
        for message in messages[:-1]:
            token_len = token_counter(message["content"], model) + \
                        token_counter(message["role"], model) + \
                        get_message_padding(model)
            prompt_tokens += token_len
            prompt_cost += token_len * get_price_per_token(model + "-prompt")
        completion_tokens = token_counter(messages[-1]["content"], model) + \
                            token_counter(messages[-1]["role"], model) + \
                            get_message_padding(model)
        completion_cost += completion_tokens * \
                           get_price_per_token(model + "-completion")
        return round(prompt_cost + completion_cost, 10)

    # Pre-request estimation with max_tokens
    prompt_tokens = 0
    for message in messages:
        token_len = token_counter(message["content"], model) + \
                    token_counter(message["role"], model) + \
                    get_message_padding(model)
        prompt_tokens += token_len
        prompt_cost += token_len * get_price_per_token(model + "-prompt")
    completion_cost += (get_engine_max_tokens(model) - prompt_tokens) * \
                       get_price_per_token(model + "-completion")
    return round(prompt_cost + completion_cost, 10)


def price_calculator_embedding(phrases):
    model = 'text-embedding-ada-002'
    cost = 0
    for phrase in phrases:
        token_len = token_counter(phrase, model)
        cost += token_len * get_price_per_token(model)
    return round(cost, 10)


def price_calculator_image(args):
    n = args['n'] if 'n' in args else 1
    size = args['size'] if 'size' in args else "1024x1024"
    return round(n * get_price_per_token(size), 10)
