from transformers import GPT2TokenizerFast


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

    return {
        "prompt": prompt,
        "engine": engine,
        "max_tokens": max_tokens,
        "n": n,
    }


def price_calculator(args):
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

    price_per_token = {
        'ada': 0.0004 / 1000,
        'babbage': 0.0005 / 1000,
        'curie': 0.002 / 1000,
        'davinci': 0.02 / 1000,
        'ada-finetuned': 0.0016 / 1000,
        'babbage-finetuned': 0.0024 / 1000,
        'curie-finetuned': 0.0120 / 1000,
        'davinci-finetuned': 0.1200 / 1000,
        'ada-finetuned-training': 0.0004 / 1000,
        'babbage-finetuned-training': 0.0006 / 1000,
        'curie-finetuned-training': 0.0030 / 1000,
        'davinci-finetuned-training': 0.0300 / 1000,
        'ada-embedding': 0.0040 / 1000,
        'babbage-embedding': 0.0050 / 1000,
        'curie-embedding': 0.0200 / 1000,
        'davinci-embedding': 0.2000 / 1000,
    }

    engine_max_tokens = {
        'ada': 2048,
        'babbage': 2048,
        'curie': 2048,
        'davinci': 4000,
        'ada-finetuned': 2048,
        'babbage-finetuned': 2048,
        'curie-finetuned': 2048,
        'davinci-finetuned': 4000,
        'ada-finetuned-training': 2048,
        'babbage-finetuned-training': 2048,
        'curie-finetuned-training': 2048,
        'davinci-finetuned-training': 4000,
        'ada-embedding': 2048,
        'babbage-embedding': 2048,
        'curie-embedding': 2048,
        'davinci-embedding': 4000,
    }

    token_len = token_counter(prompt)
    price_per_completion = min((token_len + int(max_tokens)), engine_max_tokens[engine]) * price_per_token[engine]

    if engine in ['ada', 'babbage', 'curie', 'davinci', 'ada-finetuned', 'babbage-finetuned', 'curie-finetuned',
                  'davinci-finetuned']:
        price = price_per_completion * n
    else:
        price = price_per_completion * 1

    return round(price, 10)