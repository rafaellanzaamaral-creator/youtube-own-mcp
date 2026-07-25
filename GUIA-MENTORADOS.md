# Guia do Mentorado — YouTube Own MCP

Olá! Este guia é bem simples para você conectar o MCP no **seu** canal do YouTube.

Você vai conseguir:
- Atualizar tags / palavras-chave
- Mudar título e descrição
- Fazer upload de legendas (SRT ou VTT)

Tudo só no **seu** canal. Ninguém mais tem acesso.

---

## O que você precisa (só uma vez)

1. Conta Google (a mesma do seu canal YouTube)
2. Python instalado no computador
3. 10-15 minutos

---

## Passo 1 — Clonar o projeto

Abra o terminal e rode:

```bash
git clone https://github.com/rafaellanzaamaral-creator/youtube-own-mcp.git
cd youtube-own-mcp
python -m venv venv
source venv/bin/activate   # no Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Passo 2 — Criar as credenciais no Google (a parte mais importante)

1. Acesse: https://console.cloud.google.com/
2. Crie um **projeto novo** (pode chamar de "YouTube MCP")
3. Vá em **APIs e Serviços → Biblioteca**
4. Procure e **ative** a **YouTube Data API v3**
5. Vá em **Credenciais → + Criar credenciais → ID do cliente OAuth**
6. Tipo de aplicativo: **Aplicativo para computador**
7. Baixe o arquivo JSON
8. Renomeie para `client_secret.json` e coloque na pasta do projeto (raiz)

**Importante:** Na Tela de consentimento OAuth, adicione seu e-mail como **Usuário de teste**.

---

## Passo 3 — Autenticar (só uma vez)

No terminal (ainda dentro da pasta do projeto):

```bash
python -m src.auth
```

Vai abrir o navegador. Faça login com a conta **do seu canal YouTube** e autorize.

Pronto! O token fica salvo só no seu computador.

---

## Passo 4 — Rodar e conectar

```bash
python -m src.server
```

Para usar no Grok ou ChatGPT:
1. Abra outro terminal e rode um tunnel:
   ```bash
   npx localtunnel --port 8000
   # ou cloudflared tunnel --url http://localhost:8000
   ```
2. Copie a URL HTTPS que aparecer
3. No Grok: grok.com/connectors → New Connector → Custom → cole a URL
4. No ChatGPT: Settings → Apps/Connectors → Developer Mode → crie connector e cole a URL

---

## Pronto!

Agora é só pedir no chat:

- “Liste meus vídeos”
- “Atualize as tags do vídeo XXX para [tag1, tag2, tag3]”
- “Faça upload desta legenda SRT no vídeo YYY”

Se der qualquer erro, mande print para o mentor.

Boa criação!
