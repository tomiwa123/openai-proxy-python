import openai_proxy

if __name__ == "__main__":
    # openai_proxy.username = "kairos"
    # openai_proxy.course_id = "8000"
    # openai_proxy.access_key = "O6rbLM3-yYcwS5GaWZEghA"
    # openai_proxy.access_token = "4q-_apNm72sGENVtYtcCXAnC7jEGnIUZfylHbEAEdFQ"
    # openai_proxy.api_key = "sk-h0pSnheoN1vl4mfrc0RuT3Blbk3J356L2MQdU1c9mZc6pwef"
    
    # response = openai_proxy.Completion.price(
    #     engine="text-davinci-003",
    #     prompt="What can you say about the Aztec Empire. Thousands of years",
    #     max_tokens=200,
    #     n=2,
    # )
    #
    # print(response['price'])

    # response = openai_proxy.Completion.create(
    #     engine="text-davinci-003",
    #     prompt="What can you say about the Aztec Empire. Thousands of years",
    #     temperature=0.7,
    #     max_tokens=200,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0,
    #     stop=["###", '\n'],
    #     n=2
    # )
    #
    # print(response['choices'][0]['text'])
    # print(response['price'])

    # response = openai_proxy.Embedding.create(
    #     phrases=[
    #         "This is the first phrase",
    #         "This is the second slightly longer phrase",
    #         "This is the third phrase",
    #     ]
    # )
    # print(response)
    # print(response['price'])

    # response = openai_proxy.ChatCompletion.create(
    #     messages=[
    #         {
    #             "role": "system",
    #             "content": "You are a polite but sarcastic chat bot"
    #         },
    #         {
    #             "role": "user",
    #             "content": "What can you say about the Aztec Empire. Thousands of years"
    #         }],
    #     model="gpt-3.5-turbo",
    # )
    # print(response)
    # print(response['price'])

    # response = openai_proxy.Image.create(
    #     prompt="What can you say about the Aztec Empire. Thousands of years",
    #     n=2,
    #     size="1024x1024",
    # )
    # print(response)
    # print(response['price'])

    # print(openai_proxy.engines[:5])
