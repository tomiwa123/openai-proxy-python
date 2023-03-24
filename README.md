# Openai_proxy
A proxy for OpenAI requests.
Primarily for AI students at UPenn to track their spending on GPT-3 requests.
Available for anyone to get the estimate and actual cost of a request 

Price estimates in this package are based on the [OpenAI API docs](https://beta.openai.com/docs/api-reference/completions/create) and [pricing page](https://beta.openai.com/pricing) 
They are also designed to estimate the highest possible cost of requests before they are sent. 
Actual request costs will always, assuming no bugs, be lower than the estimates.

A frontend GUI is available [here](https://openai-proxy-client.herokuapp.com/)

## Installation
Install the python package using pip
```angular2html
pip install --upgrade openai_proxy
```

## Setup
Setup as follows in your development environment or server (not frontend, otherwise you may get a "CORS Error")
```
import openai_proxy

openai_proxy.username = "koawood"
openai_proxy.course_id = "8000"
openai_proxy.access_key  = "O6rbLM3-yYcwS5GaWZEghA"
openai_proxy.access_token = "4q-_apNm72sGENVtYtcCXAnC7jEGnIUZfylHbEAEdFQ"
```


### Check Completion Price
This request accepts the following parameters corresponding to the OpenAI API's request parameters:
See the [OpenAI API docs](https://beta.openai.com/docs/api-reference/completions/create) for more details
<br /> Note that this request does not require the credentials in the setup.
- prompt: the prompt to be sent to OpenAI's GPT-3 [_required_]
- engine: the GPT-3 engine to be used for the request
- max_tokens: the maximum number of tokens to be generated in the completion

Example:
```
response = openai_proxy.Completion.price(
    engine="davinci",
    prompt="What can you say about the Aztec Empire. Thousands of years",
    max_tokens=200,
    n=2,
)

response['price']
```
Returns a response object  with a price field. 
Note that the Embedding and ChatCompletion classes also have price functions to estimate without sending a request.

### Send Completion Request to OpenAI
This request accepts the following parameters corresponding to the OpenAI API's request parameters.
See the [OpenAI API docs](https://beta.openai.com/docs/api-reference/completions/create) for more details
<br /> Note that this request requires the credentials in the setup.
- prompt: the prompt to be sent to OpenAI's GPT-3 [_required_]
- engine: the GPT-3 engine to be used for the request
- max_tokens: the maximum number of tokens to be generated in the completion
- temperature: controls randomness. Lower temperature, lower randomness
- top_p: controls diversity. 1.0 means no diversity, 0.0 means maximum diversity
- frequency_penalty: controls frequency of words in the completion. high penalty, less repetition
- presence_penalty: controls probability of words in the completion. high penalty, newer topics
- stop: a list of tokens to stop the completion on
- n: the number of completions to generate
- best_of: the number of completions to generate and evaluate server side before returning only the best

Example:
```
response = openai_proxy.Completion.create(
    engine="davinci",
    prompt="What can you say about the Aztec Empire. Thousands of years",
    temperature=0.7,
    max_tokens=200,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["###", '\n'],
    n=2
)

response['choices'][0]['text']
response['price']
```
Returns the Openai response object along with a price field.


### Send Embedding Request to OpenAI
This request accepts the following parameters corresponding to the OpenAI API's request parameters.
See the [OpenAI API docs](https://beta.openai.com/docs/api-reference/embeddings/create) for more details
<br /> Note that this request requires the credentials in the setup.
- phrases: the list of phrases to be sent to OpenAI's embedding model [_required_]
- engine: defaults to text-embedding-ada-002 (the cheapest model)

Example:
```
response = openai_proxy.Embedding.create(
        phrases=["What can you say about the Aztec Empire. Thousands of years"]
    )
    
print(response)
print(response['price'])
```
Returns the Openai response object along with a price field. 


### Send ChatCompletion Request to OpenAI
This request accepts the following parameters corresponding to the OpenAI API's request parameters.
See the [OpenAI API docs](https://platform.openai.com/docs/guides/chat/introduction) for more details
<br /> Note that this request requires the credentials in the setup.
- messages: the list of phrases to be sent to OpenAI's embedding model [_required_]
- engine: defaults to gpt-3.5-turbo (the cheapest model)

Example:
```
response = openai_proxy.ChatCompletion.create(
        messages=[
            {
                "role": "system",
                "content": "You are a polite but sarcastic chat bot"
            },
            {
                "role": "user",
                "content": "What can you say about the Aztec Empire. Thousands of years"
            }]
    )
    print(response)
    print(response['price'])
```
Returns the Openai response object along with a price field. 

Note that the Embedding and ChatCompletion classes also have price functions to estimate without sending a request.

Please reach out with any questions or suggestions
<br /> Ayotomiwa, tomiwa@wharton.upenn.edu