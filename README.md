# Andre Azevedo · Tattoo

Site de apresentação do tatuador Andre Azevedo ([@andreazevedotattoo](https://www.instagram.com/andreazevedotattoo/)), Capão Bonito, SP.
Fineline delicado e realismo preto e branco, desde 2020.

Prévia: https://azeugral.github.io/andre-azevedo/ (com `noindex` até ter domínio).

## Identidade v5 (06/10): logo do cliente + topo no modelo DAC

- **Logo oficial** (enviado pelo usuário): o original em `_ref/cliente/logo-andre-original.webp` já vem com fundo transparente. Recortado em `assets/img/logo-andre-1200.webp` e `-640.webp`.
- **Topo como na DAC Art Ink:**
  - logo centralizado (400 px na home, 260 px nas internas via `body.interna`);
  - barra de menu fixa logo abaixo: Início · Trabalhos · Sobre · Orçamento;
  - hero de texto centralizado abaixo do menu.
- **Rodapé centralizado:** logo, frase, 3 colunas (Páginas, Redes, Estúdio), aviso 18+ e assinatura.
- **Fonte do logo:** Rye (a mais próxima no Google Fonts, western/vitoriana com esporões) em títulos, menu, rótulos e botões. IBM Plex Sans no texto corrido.
- **Cores:**
  - ônix `#0b0b0a`;
  - oxblood `#5c1a1b` (seções de destaque e o brilho atrás do logo);
  - ouro areia `#ecc590` (tirado do próprio logo, `#f2cb96`);
  - marfim `#efe9df`.
- **Favicon:** "A" dourado em Rye dentro de um anel duplo, com a estrela de 4 pontas do logo.
  - O fundo é transparente, com o mesmo contorno escuro fino do logo, para ler em aba clara e escura.
  - A fonte está em `tools/logo/favicon.html`: renderizar a 800 px sobre preto, converter o preto em alfa e reduzir.
  - O `icone-180` (apple-touch) mantém o fundo ônix, porque o iOS não aceita transparência.
- **Texto:** "André" com acento, como no logo. O @ do Instagram segue sem acento.

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
