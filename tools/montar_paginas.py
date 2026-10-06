"""Monta as páginas da raiz a partir de tools/paginas/*.html (cabeçalho e rodapé comuns).
Troque V para furar o cache de CSS/JS."""
import os, re, glob
V = '3'
AQUI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(AQUI)
BASE = 'https://azeugral.github.io/andre-azevedo/'  # CONFIRMAR: trocar quando houver domínio

HEAD = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0e0e0d">
<meta property="og:type" content="website">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{base}og-andre.jpg">
<meta property="og:locale" content="pt_BR">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" href="assets/img/icone-512.png" type="image/png">
<link rel="apple-touch-icon" href="assets/img/icone-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Host+Grotesk:wght@300..600&display=swap">
<link rel="stylesheet" href="assets/css/site.css?v={v}">
</head>
<body>
<a class="sr" href="#conteudo">Pular para o conteúdo</a>
<header class="topo">
  <div class="wrap">
    <a class="marca" href="./" aria-label="Andre Azevedo, início"><span class="mono" aria-hidden="true">AA</span><b>Andre Azevedo</b></a>
    <nav class="menu" aria-label="Principal">{menu}</nav>
    <button class="abrir" type="button" aria-expanded="false" aria-controls="gaveta" aria-label="Menu"><i></i><i></i></button>
  </div>
</header>
<nav class="gaveta" id="gaveta" aria-label="Menu do celular">{menu}<span class="rot">Capão Bonito · SP · desde 2020</span></nav>
<div class="progresso" aria-hidden="true"><i></i></div>
<main id="conteudo">
'''

FOOT = '''</main>
<footer class="rodape">
  <div class="wrap">
    <div class="colunas">
      <div>
        <a class="marca" href="./"><span class="mono" aria-hidden="true">AA</span><b>Andre Azevedo</b></a>
        <p class="aviso18" style="margin-top:24px"><b>18+</b>Não atendemos menores de idade.</p>
      </div>
      <div><h4>Site</h4><ul><li><a href="./">Início</a></li><li><a href="trabalhos.html">Trabalhos</a></li><li><a href="orcamento.html">Orçamento</a></li></ul></div>
      <div><h4>Redes</h4><ul><li><a href="https://www.instagram.com/andreazevedotattoo/" target="_blank" rel="noopener">Instagram</a></li><li><a href="https://www.tiktok.com/@andreazevedotattoo" target="_blank" rel="noopener">TikTok</a></li><li>WhatsApp: <em class="a-preencher">a preencher</em></li></ul></div>
      <div><h4>Estúdio</h4><ul><li>Capão Bonito, SP</li><li>Endereço: <em class="a-preencher">a preencher</em></li><li>Horários: <em class="a-preencher">a preencher</em></li></ul></div>
    </div>
    <div class="base"><span>Fineline e realismo P&amp;B · desde 2020</span><span>Site por <a href="https://lrgz.com.br" target="_blank" rel="noopener">L R G Z</a></span></div>
  </div>
</footer>
{extra}<script src="assets/js/obras.js?v={v}"></script>
<script src="assets/js/site.js?v={v}"></script>
</body>
</html>
'''

LB = '''<div class="lb" role="dialog" aria-modal="true" aria-label="Foto ampliada" aria-hidden="true">
  <div class="lb-topo"><span class="rot" data-cont></span><button type="button" data-fechar>Fechar</button></div>
  <div class="lb-palco"><img alt=""></div>
  <div class="lb-base"><button type="button" data-ant aria-label="Anterior">&larr;</button><span class="rot" data-leg></span><button type="button" data-prox aria-label="Próxima">&rarr;</button></div>
</div>
'''

SETA = '<svg viewBox="0 0 18 18" aria-hidden="true"><path d="M2 9h13M10 4l5 5-5 5"/></svg>'

MENU = [('./', 'Início'), ('trabalhos.html', 'Trabalhos'), ('index.html#sobre', 'Sobre'), ('orcamento.html', 'Orçamento')]

for f in glob.glob(os.path.join(AQUI, 'paginas', '*.html')):
    nome = os.path.basename(f)
    txt = open(f, encoding='utf-8').read()
    meta = dict(re.findall(r'<!--\s*(\w+):\s*(.*?)\s*-->', txt.split('\n---\n')[0]))
    corpo = txt.split('\n---\n', 1)[1].replace('<!--seta-->', SETA)
    atual = {'index.html': './', '404.html': None}.get(nome, nome)
    menu = ''.join(f'<a href="{h}"' + (' aria-current="page"' if h == atual else '') + f'>{t}</a>' for h, t in MENU)
    html = HEAD.format(titulo=meta['titulo'], desc=meta['desc'], base=BASE, v=V, menu=menu) + corpo + \
        FOOT.format(v=V, extra=LB if meta.get('lightbox') == 'sim' else '')
    if nome == '404.html':
        html = html.replace('<head>', '<head>\n<base href="/andre-azevedo/">', 1)
    open(os.path.join(SITE, nome), 'w', encoding='utf-8', newline='\n').write(html)
    print('ok', nome)
