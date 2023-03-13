import openai_proxy

if __name__ == "__main__":
    openai_proxy.username = "kairos"
    openai_proxy.course_id = "8000"
    openai_proxy.access_key = "O6rbLM3-yYcwS5GaWZEghA"
    openai_proxy.access_token = "4q-_apNm72sGENVtYtcCXAnC7jEGnIUZfylHbEAEdFQ"

    # Completion means GPT-3 requests as opposed to
    # dall-e requests
    
    # response = openai_proxy.Completion.price(
    #     engine="text-davinci-003",
    #     prompt="What can you say about the Aztec Empire. Thousands of years",
    #     max_tokens=200,
    #     n=2,
    # )
    #
    # print(response['price'])

    # response = openai_proxy.Completion.create(
    #     engine="davinci",
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

    # response = openai_proxy.Price.training(
    #     filename="lecture-22-dialogue-systems-and-chatbots-summarizer-output.jsonl",
    #     engine="babbage",
    # )
    #
    # print(response['price'])
    #
    # response = openai_proxy.Price.training(
    #     prompt="What can you say about the Aztec Empire. Thousands of years",
    #     engine="davinci",
    # )
    #
    # print(response['price'])
    #
    # # a function that gets the standard deviation from a list of numbers
    # def get_standard_deviation(numbers):
    #     # get the mean
    #     mean = sum(numbers) / len(numbers)
    #     # get the variance
    #     variance = sum([pow(x - mean, 2) for x in numbers]) / len(numbers)
    #     # get the standard deviation
    #     return pow(variance, 0.5)

    # response = openai_proxy.Embedding.create(
    #     phrases=["What can you say about the Aztec Empire. Thousands of years"]
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
    #         }]
    # )
    # print(response)
    # print(response['price'])

    print(openai_proxy.engines[:5])
