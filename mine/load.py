from jinja2 import Environment, FileSystemLoader, StrictUndefined

env = Environment(loader=FileSystemLoader("guidance/templates"), undefined=StrictUndefined)
template = env.get_template("llama3.jinja")

context = {
    "messages": [
        {"role": "system", "content": "AAAA"},
        {"role": "user", "content": "BBBB"},
        {"role": "assistant", "content": "CCCC"},
    ],
    "bos_token": "",
    "add_generation_prompt": False,
}
print(template.render(context))
