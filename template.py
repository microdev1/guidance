from transformers import AutoTokenizer

qwen = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B")
llama = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B-Instruct")


def template(tokenizer):
    return tokenizer.apply_chat_template(
        [{"role": "assistant", "content": "You are an expert at this."}],
        tokenize=False,
    )


print("Qwen:")
print(template(qwen))
print()
print("Llama:")
print(template(llama))

# from guidance.chat import auto_chat_template

# qwen = auto_chat_template(qwen)
# llama = auto_chat_template(llama)

# print("Qwen:")
# print(json.dumps(qwen._role_dict, indent=4))
# print()
# print("Llama:")
# print(json.dumps(llama._role_dict, indent=4))

# print(
#     llama.get_role_start("system"), "AAAA", llama.get_role_end("system"),
#     llama.get_role_start("user"), "BBBB", llama.get_role_end("user"),
#     llama.get_role_start("assistant"), "CCCC", llama.get_role_end("assistant"),
#     sep=""
# )
# print("---")

# from guidance.chat import Llama3ChatTemplate

# llama = Llama3ChatTemplate()
