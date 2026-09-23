from flask import Flask, request, render_template
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)
CORS(app)

model_name = "HuggingFaceTB/SmolLM2-360M-Instruct"
print("Carregando o modelo SmolLM2. Aguarde...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.unk_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cpu",
    torch_dtype=torch.float32
)

# Inicializa o histórico de mensagens com o papel do sistema
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Give short and concise answers in 2-3 lines."
    }
]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    global messages # Permite atualizar o histórico global
    
    data = request.get_json()
    input_text = data["prompt"]

    # Adiciona a mensagem do usuário ao histórico
    messages.append({"role": "user", "content": input_text})

    # Mantém apenas a regra do sistema e as últimas 10 interações
    messages = [messages[0]] + messages[-10:]

    # Aplica o template de chat moderno
    tokenized = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt",
        return_dict=True,
        max_length=512
    )

    # Gera a resposta
    with torch.inference_mode():
        outputs = model.generate(
            tokenized["input_ids"],
            attention_mask=tokenized["attention_mask"],
            max_new_tokens=60,
            temperature=0.5,
            top_p=0.8,
            do_sample=True,
            repetition_penalty=1.3,
            no_repeat_ngram_size=3,
            pad_token_id=tokenizer.pad_token_id
        )

    # Decodifica apenas a parte nova gerada pelo bot
    response = tokenizer.decode(
        outputs[0][tokenized["input_ids"].shape[-1]:],
        skip_special_tokens=True
    )

    # Salva a resposta no histórico
    messages.append({"role": "assistant", "content": response})

    return response

if __name__ == '__main__':
    app.run()