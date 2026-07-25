# YouTube Own Channel MCP

MCP server **limpo, auditável e 100% seu** para gerenciar o seu canal do YouTube:
- Atualizar tags / palavras-chave
- Título e descrição
- Upload de legendas (SRT / VTT)

**Repo:** https://github.com/rafaellanzaamaral-creator/youtube-own-mcp

## Para Mentorados

Veja o guia simples e passo a passo:
**[GUIA-MENTORADOS.md](GUIA-MENTORADOS.md)**

## Para o dono do repositório / avançado

### Setup rápido

1. Clone o repo
2. Coloque seu `client_secret.json` na raiz
3. `python -m src.auth`
4. `python -m src.server`
5. Use tunnel + connector no Grok / ChatGPT / Claude

### Tools disponíveis

- `update_video_metadata_tool`
- `upload_caption_tool`
- `list_captions_tool`
- `list_my_videos_tool`
- `get_video_tool`
- `get_channel_info_tool`

### Segurança

- Cada pessoa autentica com a própria conta
- Tokens ficam só no computador de cada um
- Nunca compartilhe `client_secret.json` ou `token.json`

Licença MIT.
