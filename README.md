🤖 Simple Local AI Chatbot

Um chatbot inteligente com interface web rodando 100% localmente.

Este projeto foi construído para integrar um modelo de Inteligência Artificial moderno (Causal LLM) em um servidor back-end local, permitindo conversar com a IA através de uma página web no navegador, sem depender de APIs pagas ou serviços na nuvem.

🚀 Funcionalidades

Interface Web: Chat fluido com HTML, CSS e JavaScript.

Processamento Local: Privacidade total, o modelo roda direto na máquina.

Memória de Contexto: O bot lembra das últimas mensagens para manter uma conversa natural usando Chat Templates.

LLM Moderno: Utiliza o modelo SmolLM2-360M-Instruct via Hugging Face.

🛠️ Tecnologias Utilizadas

Back-end: Python, Flask, Flask-CORS

IA & Machine Learning: PyTorch, Transformers (Hugging Face)

Front-end: HTML, CSS, JavaScript Vanilla

⚙️ Como rodar o projeto na sua máquina

Siga os passos abaixo no seu terminal para rodar o chatbot:

1. Clone o repositório

git clone https://github.com/IamLucasLimaDev/simple_chatbot.git
cd simple_chatbot


2. Crie e ative um ambiente virtual (Recomendado)

python3 -m venv my_env
source my_env/bin/activate  # No Windows use: my_env\Scripts\activate


3. Instale as dependências

pip install -r requirements.txt


4. Inicie o servidor

python3 app.py


5. Acesse no navegador
Abra o seu navegador favorito e acesse: http://127.0.0.1:5000

Desenvolvido por Lucas Lima. 💡