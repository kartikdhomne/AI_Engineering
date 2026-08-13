# . A model, stripped to its essence
# Forget chat windows and personalities for a moment. Underneath everything, a language model is one thing: a function that receives some text and hands back some text. It runs once, produces its answer, and holds on to nothing. Ask it something a second time and it has no clue it ever met you.

def stateless_reply(prompt: str) -> str:
    return f"(some llm response mimicking the model's output) {prompt}"
print(stateless_reply("Who is the PM of UK"))
(some llm response mimicking the model's output) Who is the PM of UK
print(stateless_reply("who was before him"))
(some llm response mimicking the model's output) who was before him
def stateless_chatgpt_demo(prompt: str) -> str:
    from dotenv import load_dotenv
    from openai import OpenAI

    load_dotenv()

    client = OpenAI()
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )

    return response.output_text
stateless_chatgpt_demo("Who was the PM of UK before 2020 ? ")

'Before 2020, the Prime Minister of the United Kingdom was Boris Johnson, who took office in July 2019. Before him, Theresa May served as Prime Minister from July 2016 to July 2019.'
stateless_chatgpt_demo("Who was before him ?  ")
'Could you provide more context or specify who you are referring to? That would help me give you a better answer!'