from transformers import GPT2TokenizerFast
from openai_proxy.utils.constants import price_per_token, engine_max_tokens, get_price_per_token, get_engine_max_tokens


def token_counter(prompt):
    # counts tokens given input text
    #
    # input: text
    # output: length of tokens
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    token_len = len(tokenizer(prompt)['input_ids'])

    return token_len


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

    token_len = token_counter(prompt)
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


def price_calculator_chat(messages):
    cost = 0
    if 'total_tokens' in messages:
        cost = messages['total_tokens'] * get_price_per_token('gpt-3.5-turbo')
        return round(cost, 10)

    for message in messages:
        token_len = token_counter(message["content"])
        cost += token_len * get_price_per_token('gpt-3.5-turbo')
    return round(cost, 10)


def price_calculator_embedding(phrases):
    cost = 0
    for phrase in phrases:
        token_len = token_counter(phrase)
        cost += token_len * get_price_per_token('text-embedding-ada-002')
    return round(cost, 10)
