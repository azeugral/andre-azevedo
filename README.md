# Andre Azevedo · Tattoo

Site de apresentação do tatuador Andre Azevedo ([@andreazevedotattoo](https://www.instagram.com/andreazevedotattoo/)), Capão Bonito, SP.
Fineline delicado e realismo preto e branco, desde 2020.

Prévia: https://azeugral.github.io/andre-azevedo/ (com `noindex` até ter domínio).

## Identidade v4 (06/10): layout padrão, simétrico

A v3 (trilho lateral, nome em pé, faixas assimétricas) foi rejeitada: "ficou tudo torto". Voltamos ao modelo padrão.

- **Fontes do LRGZ:** Unbounded nos títulos, IBM Plex Sans no texto e JetBrains Mono nos rótulos e botões.
- **Paleta de luxo**, com a estrutura das referências: uma âncora escura, um metal e um neutro, poucas cores.
  - ônix `#0b0b0a` (fundo);
  - oxblood `#5c1a1b` → `#45120f` (seções de destaque: Estilos e a chamada final);
  - ouro `#c9a96e` (botões, rótulos e detalhes);
  - marfim `#efe9df` (texto).
- **Logo ΛΛ:** um A em fio + um A cheio + um ponto dourado (`assets/img/logo.svg`, `favicon.svg`).
- **Layout:**
  - nav no topo com o logo à esquerda, os links no centro e o botão "Pedir orçamento" à direita; menu em gaveta no celular;
  - abertura em duas colunas iguais;
  - seções com título centralizado e grades regulares;
  - estilos em dois cartões iguais, sobre em duas colunas e passos em três cartões.
- **Botões:** retos, em ouro sólido ou com contorno. Ao passar o mouse, o marfim sobe por baixo. Fotos em moldura de fio dourado.
- **Pendentes:** "a preencher" com um losango dourado.

## Estrutura

| Arquivo | O que é |
|---|---|
| `index.html` | Abertura, trabalhos recentes, estilos, sobre, como agendar e chamada |
| `trabalhos.html` | Os 63 trabalhos, com filtro Fineline/Realismo (`?estilo=`) e lightbox |
| `orcamento.html` | Monta a mensagem, copia o texto e abre a DM (ou o WhatsApp, se configurado) |
| `assets/js/site.js` | `CONFIG` (Instagram, TikTok, WhatsApp) e o comportamento do site |
| `assets/js/obras.js` | Gerado. Não editar à mão |

## Fluxo

```bash
python tools/processar.py      # fotos de ../_ref/zip -> assets/obras + obras.js
python tools/montar_paginas.py # tools/paginas/*.html -> páginas da raiz (V = cache)
```

- **Lista de fotos:** fica em `OBRAS`, dentro de `tools/processar.py`, com o estilo, a legenda e um recorte opcional.
- **Repetidas removidas** (a segunda foto do par ficou):
  - leão na mão (16/17)
  - "cont;nue" (5/32)
  - besouro (35/66)
  - olho na pirâmide (43/67)
  - medusa (68/54)
  - lobo (29/60)
  - onça de corações (15/2)
  - pug Oliver (11/12)
- **Marcas d'água cortadas:** TikTok no carneiro e CapCut no fluido.
- **Prévia de link:** `og-andre.jpg` é gerada a partir de `tools/og.html` (1200×630).

## CONFIRMAR

Os itens pendentes aparecem no site como "a preencher" (Sobre, Como agendar e rodapé):

- [ ] **WhatsApp:** sem número, o orçamento vai para a DM do Instagram. Preencher `CONFIG.whatsapp`.
- [ ] **Endereço do estúdio** em Capão Bonito.
- [ ] **Horários** de atendimento.
- [ ] **Valores e sinal** (em Como agendar) e cuidados pós-tattoo, se ele quiser.
- [ ] **Classificação dos estilos:** algumas peças ficam entre os dois (ornamental, mandala, fluido em blackwork). Revisar com ele.
- [ ] **Foto 28** (bastidor de camiseta amarela): ficou fora porque não deu para confirmar se é ele.
- [ ] **TikTok:** o Beacons aponta para @andreazevedotattoo, mas o vídeo do carneiro tem a marca @tattooandre. Confirmar qual vale.
- [ ] **Adega Realledo** (ele é sócio, está na bio): ficou fora do site. Perguntar se ele quer citar.
- [ ] **Domínio:** trocar `BASE` em `tools/montar_paginas.py` e o `<base>` do 404, e tirar o `noindex`.

---

Site por [L R G Z](https://lrgz.com.br)
