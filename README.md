# Andre Azevedo · Tattoo

Site de apresentação do tatuador Andre Azevedo ([@andreazevedotattoo](https://www.instagram.com/andreazevedotattoo/)), Capão Bonito, SP.
Fineline delicado e realismo preto e branco, desde 2020.

Prévia: https://azeugral.github.io/andre-azevedo/ (com `noindex` até ter domínio).

## Identidade v3 (06/10)

Base preta, texto osso e um vermelho só, o `#d6402b` da camiseta da foto dele. Fonte Host Grotesk.

- **Logo ΛΛ** (`assets/img/logo.svg`, `favicon.svg`, ícones em `assets/img`):
  - um A em fio fino (fineline) e um A cheio (realismo), ligados na base;
  - um ponto vermelho marca onde os dois se tocam, como a ponta da agulha;
  - na abertura o logo se desenha: o fio, depois o cheio, depois o ponto;
  - os ícones PNG são gerados a partir de `tools/logo/icone.html`.
- **Navegação:**
  - no desktop, um trilho vertical à esquerda com links em pé, a barra de progresso e "Orçamento" num bloco vermelho embaixo;
  - no celular, uma doca fixa embaixo (logo, Trabalhos, Sobre e Orçamento em vermelho), sem menu hambúrguer.
- **Abertura:** o nome fica em pé na lateral, a foto colorida no centro com o botão preso no canto, e as informações à esquerda.
- **Trabalhos recentes:** uma faixa que rola de lado (arrastar, setas e contador). Os cartões se alternam em altura, e o último leva para os 63.
- **Estilos:** blocos alternados, com o título grande, a contagem em vermelho e 3 fotos em composição deslocada.
- **Sobre:** a ficha técnica fica sobre a foto.
- **Como agendar:** passos em linhas, com o título fixo ao lado.
- **Chamada final:** os botões ficam empilhados na lateral.
- **Página de trabalhos:** grade com peças em destaque (2×2) para dar ritmo.
- **Orçamento:** duas colunas, com o texto fixo de um lado e o formulário do outro.
- **Botões:** duas células, rótulo e seta. Cantos de decalque vermelhos nas fotos.
- **Pendentes:** informação que falta aparece como "a preencher" (`.a-preencher`).

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
