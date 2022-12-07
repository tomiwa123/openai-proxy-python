# Openai_proxy
A proxy for OpenAI requests.
Primarily for AI students at UPenn to track their spending on GTP-3 requests.
Available for anyone to get the estimate and actual cost of a request 

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


### Send Request to OpenAI
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

### Check Request Price
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

Please reach out with any questions or suggestions
<br /> Ayotomiwa, tomiwa@wharton.upenn.edu