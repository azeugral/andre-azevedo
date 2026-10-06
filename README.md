# Andre Azevedo · Tattoo

Site de apresentação do tatuador Andre Azevedo ([@andreazevedotattoo](https://www.instagram.com/andreazevedotattoo/)), Capão Bonito, SP.
Fineline delicado e realismo preto e branco, desde 2020.

Prévia: https://azeugral.github.io/andre-azevedo/ (com `noindex` até ter domínio).

## Identidade: régua de diluição

O realismo P&B é feito diluindo a tinta em tons de cinza, e o fineline é um traço só. O sistema visual vem daí:

- **Marca:** cinco faixas que vão do papel ao preto (`.regua`, `favicon.svg`).
- **Cores:** papel `#efeeea` e diluições `#dedcd6`, `#bdbab3`, `#8f8c86`, `#5e5c58`, com a tinta `#141413`. Não há cor de destaque.
- **Fontes:** Bodoni Moda nos títulos (haste grossa e serifa fina, o realismo e o fineline numa letra só), IBM Plex Sans no texto e IBM Plex Mono nos rótulos.
- **Movimento:** na abertura, as faixas de diluição se abrem sobre a foto e um traço fino se desenha sob o nome. A barra de progresso no rodapé da tela é a régua enchendo. A curva de easing é `cubic-bezier(.16,.84,.32,1)`.
- **Botões:** retos, com sombra dura deslocada.

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

Os itens pendentes aparecem no site com contorno tracejado (`.a-confirmar`):

- [ ] **WhatsApp:** sem número, o orçamento vai para a DM do Instagram. Preencher `CONFIG.whatsapp`.
- [ ] **Endereço do estúdio** em Capão Bonito.
- [ ] **Sinal, valores mínimos e cuidados pós-tattoo**, se ele quiser que apareçam no site.
- [ ] **Classificação dos estilos:** algumas peças ficam entre os dois (ornamental, mandala, fluido em blackwork). Revisar com ele.
- [ ] **Foto 28** (bastidor de camiseta amarela): ficou fora porque não deu para confirmar se é ele.
- [ ] **TikTok:** o Beacons aponta para @andreazevedotattoo, mas o vídeo do carneiro tem a marca @tattooandre. Confirmar qual vale.
- [ ] **Adega Realledo** (ele é sócio, está na bio): ficou fora do site. Perguntar se ele quer citar.
- [ ] **Domínio:** trocar `BASE` em `tools/montar_paginas.py` e o `<base>` do 404, e tirar o `noindex`.

---

Site por [L R G Z](https://lrgz.com.br)
