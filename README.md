# Andre Azevedo · Tattoo

Site de apresentação do tatuador Andre Azevedo ([@andreazevedotattoo](https://www.instagram.com/andreazevedotattoo/)), Capão Bonito, SP.
Fineline delicado e realismo preto e branco, desde 2020.

Prévia: https://azeugral.github.io/andre-azevedo/ (com `noindex` até ter domínio).

## Identidade: preto minimalista + vermelhão (v2, 06/10)

A v1 (régua de diluição, Bodoni) foi trocada a pedido: o traço fino e os botões com sombra davam cara de IA.

- **Cores:** base preta `#0e0e0d`, texto osso `#ecebe7` e cinzas `#9a9893` / `#6c6a66`. Uma cor extra, o vermelhão `#d6402b`, que vem da camiseta da foto dele. Uma seção clara (Como agendar) dá respiro.
- **Fonte:** Host Grotesk (300 nos títulos, 400/500 no texto), uma família só. O arquivo está em `_ref/fontes`.
- **Marca e favicon:** monograma "AA" num quadrado vermelho.
- **Botão:** duas células, rótulo e seta. Ao passar o mouse, o osso sobe por baixo do rótulo e a seta atravessa a célula. A versão em contorno (`.btn.linha`) é para a ação secundária. Sem sombra e sem canto arredondado.
- **Assinatura:** cantos de decalque em vermelho nas fotos (`.decalque`), que lembram as marcas de alinhamento do stencil. Na abertura, a foto colorida sobe revelada e os cantos entram depois.
- **Progresso:** um fio vermelho no topo da tela.
- **Pendentes:** campos sem informação aparecem como "a preencher" (`.a-preencher`, com um quadradinho vermelho).

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
