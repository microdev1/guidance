import guidance

from guidance import assistant, gen, models, user, chat, system, select
from transformers import AutoTokenizer

llm = models.Ollama(
    "llama3.2:1b",
    echo=False,
    chat_template=chat.auto_chat_template(
        AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B-Instruct")
    ),
)

# with system():
#     llm += "Your are an helpful assistant."

# with user():
#     llm += ""

# with assistant():
#     llm += "It's none of your " + select(["business", "concern"]) + "."

# print(llm)


@guidance
def add(lm, input1, input2):
    print("add", input1, input2)
    lm += f" = {float(input1) + float(input2)}"
    return lm


@guidance
def subtract(lm, input1, input2):
    print("subtract", input1, input2)
    lm += f" = {float(input1) - float(input2)}"
    return lm


@guidance
def multiply(lm, input1, input2):
    print("multiply", input1, input2)
    lm += f" = {float(input1) * float(input2)}"
    return lm


@guidance
def divide(lm, input1, input2):
    print("divide", input1, input2)
    lm += f" = {float(input1) / float(input2)}"
    return lm

lm = llm + '''\
1 + 1 * 2 = add(1, multiply(1, 2)) = 3
3 / 4 - 5 = subtract(divide(3, 4), 5) = -4.25
'''
lm += gen(max_tokens=15, tools=[add, subtract, multiply, divide])

print(lm)
