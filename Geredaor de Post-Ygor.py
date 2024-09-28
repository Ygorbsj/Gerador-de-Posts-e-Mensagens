import requests
import schedule
import time
from datetime import datetime

# Substitua por seu token de acesso
ACCESS_TOKEN = 'seu_token_de_acesso_aqui'
PAGE_ID = '386929114513606'
FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdPFmvaK0vpO0bxns8_xfHop9EfrMKEIZePtGtoK7qEUu8vFQ/viewform?usp=sf_link'  # Link do formulário de pesquisa

# Função para criar um post
def criar_post(mensagem):
    url = f'https://graph.facebook.com/{PAGE_ID}/feed'
    payload = {
        'message': mensagem,
        'access_token': ACCESS_TOKEN
    }
    
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print(f'Post criado com sucesso: {mensagem}')
    else:
        print(f'Falha ao criar post: {response.status_code} - {response.text}')

# Função para gerar mensagens
def gerar_mensagem():
    mensagens = [
        "Vamos cuidar do nosso bairro! Junte-se a nós na próxima reunião.",
        "O que você gostaria de ver na nossa comunidade? Deixe suas sugestões!",
        "Participe da limpeza do parque neste sábado! Sua ajuda é fundamental.",
        "Não se esqueça: o nosso próximo evento acontece na próxima semana!",
        "A segurança do nosso bairro é uma prioridade. Vamos nos unir por um Guadalupe mais seguro!",
        f"Queremos ouvir você! Por favor, participe da nossa pesquisa de satisfação: {FORM_URL}"
    ]
    return mensagens[datetime.now().day % len(mensagens)]  # Exemplo simples de seleção

# Função principal que será agendada
def postar_no_facebook():
    mensagem = gerar_mensagem()
    criar_post(mensagem)

# Agendar o post a cada 24 horas
schedule.every(24).hours.do(postar_no_facebook)

print("Gerador de posts automático iniciado. Esperando para postar...")

while True:
    schedule.run_pending()
    time.sleep(1)
