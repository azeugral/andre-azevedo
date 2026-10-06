"""Gera assets/obras/*.webp e assets/js/obras.js a partir de _ref/zip.

Repetidas tiradas (par -> mantida): 16/17, 5/32, 35/66, 43/67, 54/68, 29/60, 2/15, 11/12.
Fora do portfólio: 20 (processo, vai no Sobre) e 28 (bastidor sem tatuagem).
"""
import glob, json, os
from PIL import Image, ImageOps

AQUI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(AQUI)
ORIG = os.path.join(SITE, '..', '_ref', 'zip', 'Andre Azevedo')
OUT = os.path.join(SITE, 'assets', 'obras')

F, R = 'fineline', 'realismo'
# índice da folha de contato -> (estilo, descrição curta, recorte opcional em frações x0,y0,x1,y1)
OBRAS = {
  0: (F, 'Raposa'), 1: (F, 'Arco e flecha'), 2: (F, 'Onça de corações'), 3: (F, 'Lettering "Loyalty"'),
  4: (F, 'Ramo floral no ombro'), 6: (R, 'Faixa com cenas'), 7: (F, 'Pegada'), 8: (R, 'Caminhão'),
  9: (F, 'Tulipa no pescoço'), 10: (R, 'Leão com flores'), 12: (R, 'Pug "Oliver"'), 13: (F, 'Sol na costela'),
  14: (R, 'Jesus'), 17: (R, 'Leão na mão'), 18: (F, 'Flor no ombro'), 19: (R, 'Zeus'),
  21: (R, 'Pantera'), 22: (R, 'Olho e ornamentos'), 23: (R, 'Carneiro', (0, 0, 1, .70)), 24: (R, 'Terço e rosa'),
  25: (R, 'Shih Tzu'), 26: (R, 'Jesus no pescoço'), 27: (R, 'Poseidon'), 30: (F, 'Lettering na nuca'),
  31: (F, 'Tattoo de amigas', (0, 0, 1, .80)), 32: (F, 'Lettering "cont;nue"'), 33: (R, 'Querubim'), 34: (F, 'Rosa'),
  36: (F, 'Símbolo no braço'), 37: (F, 'Lettering na coluna'), 38: (F, 'Mini no punho'), 39: (R, 'Tigre'),
  40: (F, 'Lettering no antebraço'), 41: (R, 'Tigre na barriga'), 42: (F, 'Ornamental'), 44: (F, 'Composição nas costas'),
  45: (R, 'Fluido na mão', (0, .08, 1, 1)), 46: (F, 'Frase na coluna'), 47: (F, 'Floral na perna'), 48: (F, 'Lírios no ombro'),
  49: (F, 'Andorinha'), 50: (F, 'Dragão nas costas'), 51: (F, 'Frase no antebraço'), 52: (F, 'Macaco'),
  53: (F, 'Fênix'), 54: (R, 'Medusa'), 55: (F, 'Mini na mão'), 56: (R, 'Polvo'),
  57: (R, 'Fechamento de braço'), 58: (R, 'Polvo no antebraço'), 59: (R, 'Tigre e rosas'), 60: (R, 'Lobo'),
  61: (F, 'Revólver e flor'), 62: (R, 'Família de leões'), 63: (F, 'Mandala na coxa'), 64: (F, 'Composição no antebraço'),
  65: (F, 'Círculo'), 66: (R, 'Besouro'), 67: (R, 'Olho na pirâmide'), 69: (F, 'Lettering "Pai"'),
  70: (F, 'Lótus ornamental'), 71: (F, 'Lettering "Serena"'), 72: (R, 'Cachorro'),
}

def salvar(im, nome, larguras=(640, 1200)):
    for w in larguras:
        c = im.copy()
        if c.width > w:
            c = c.resize((w, round(c.height * w / c.width)), Image.LANCZOS)
        c.save(os.path.join(OUT, f'{nome}-{w}.webp'), 'WEBP', quality=80, method=6)

def main():
    for f in glob.glob(os.path.join(OUT, '*.webp')):
        os.remove(f)
    fs = [f for f in sorted(glob.glob(os.path.join(ORIG, '*.jpg'))) if not os.path.basename(f).startswith('Andre')]
    lista = []
    # mais recentes primeiro (o id do arquivo do Instagram cresce com o tempo)
    for i in sorted(OBRAS, reverse=True):
        estilo, desc, *rec = OBRAS[i]
        im = ImageOps.exif_transpose(Image.open(fs[i])).convert('RGB')
        if rec:
            x0, y0, x1, y1 = rec[0]
            im = im.crop((round(x0 * im.width), round(y0 * im.height), round(x1 * im.width), round(y1 * im.height)))
        nome = f'aa-{i:02d}'
        salvar(im, nome)
        lista.append({'id': nome, 'e': estilo, 'd': desc, 'r': round(im.width / im.height, 3)})
    js = 'window.OBRAS = ' + json.dumps(lista, ensure_ascii=False, separators=(',', ':')) + ';\n'
    open(os.path.join(SITE, 'assets', 'js', 'obras.js'), 'w', encoding='utf-8').write(js)

    # foto do artista: preto e branco, como o realismo dele
    p = ImageOps.exif_transpose(Image.open(os.path.join(ORIG, 'Andre Azevedo.jpg'))).convert('L')
    p = p.crop((0, round(p.height * .05), p.width, p.height))  # tira o reflexo da luminária no topo
    p = ImageOps.autocontrast(p, cutoff=.5)
    for w in (700, 1300):
        c = p.resize((w, round(p.height * w / p.width)), Image.LANCZOS) if p.width > w else p
        c.save(os.path.join(SITE, 'assets', 'img', f'andre-{w}.webp'), 'WEBP', quality=82, method=6)
    # bastidor (20): processo do Jesus
    b = ImageOps.exif_transpose(Image.open(fs[20])).convert('RGB')
    b.save(os.path.join(SITE, 'assets', 'img', 'processo-640.webp'), 'WEBP', quality=80, method=6)
    print(len(lista), 'obras;', sum(o['e'] == F for o in lista), 'fineline')

if __name__ == '__main__':
    main()
