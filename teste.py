import json
import re

def replace_placeholders_with_defaults(model, input_data):
    def get_value_from_path(data, path):
        keys = re.split(r'\.|\[|\]\.?', path.strip('.'))
        for key in keys:
            if key.isdigit():
                key = int(key)
            if key in data:
                data = data[key]
            elif isinstance(key, int) and len(data) > key:
                data = data[key]
            else:
                return None
        return data

    def recursive_replace(model, input_data):
        if isinstance(model, dict):
            for key, value in model.items():
                if isinstance(value, dict) or isinstance(value, list):
                    recursive_replace(value, input_data)
                elif isinstance(value, str):
                    match = re.match(r'<(.+?)(?::(.+?))?>', value)
                    if match:
                        path, default = match.groups()
                        replacement_value = get_value_from_path(input_data, path)
                        if replacement_value is None and default is not None:
                            replacement_value = default
                        if replacement_value is not None:
                            model[key] = replacement_value
        elif isinstance(model, list):
            for i in range(len(model)):
                recursive_replace(model[i], input_data)
        return model

    return recursive_replace(model, input_data)

# Exemplo de modelo de entrada do agente
agent_input_model = {
    "flow_id": "<id_fluxo>",
    "step": "<step>",
    "input": {
        "messages": [
            {
                "content": "<input.messages[0].content:Você traduzirá para inglês en-US o texto enviado pelo usuário>",
                "role": "system"
            },
            {
                "content": "<input.content>",
                "role": "user"
            }
        ],
        "model": "<input.model:gpt-3.5-turbo-0301>",
        "options": {
            "stream": "<input.stream:false>"
        }
    }
}

# Exemplo de JSON de entrada recebido do usuário
user_input = {
    "id_fluxo": 3,
    "step": 1,
    "input": {
        "content": "Olá, como você está?",
        "model": "gpt-3.5-turbo-0301",
        "stream": "false",
        "messages": [
            {
                "content": "Forneça uma imagem com base na entrada do usuário",
                "role": "system"
            }
        ]
    }
}

# Substituição dos placeholders no modelo de entrada
processed_input = replace_placeholders_with_defaults(agent_input_model, user_input)
print("Processed Input:")
print(json.dumps(processed_input, indent=4, ensure_ascii=False))

# Exemplo de modelo de saída do agente
agent_output_model = {
    "translated_text": "<message.content>"
}

# Exemplo de resposta do serviço
service_response = {
    "model": "gpt-3.5-turbo-0301",
    "created_at": "2024-06-09T18:03:39.000000Z",
    "message": {
        "role": "assistant",
        "content": "Hello, how are you?"
    },
    "done": True
}

# Mapeamento e substituição dos valores na saída do agente
processed_output = replace_placeholders_with_defaults(agent_output_model, service_response)
print("Processed Output:")
print(json.dumps(processed_output, indent=4, ensure_ascii=False))
