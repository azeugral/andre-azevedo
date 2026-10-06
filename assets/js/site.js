/* Andre Azevedo — comportamento do site */
window.CONFIG = {
  instagram: 'andreazevedotattoo',
  tiktok: 'andreazevedotattoo',
  whatsapp: '' // CONFIRMAR: com número (ex.: 5515999999999) o orçamento abre o WhatsApp em vez da DM
};

(function () {
  var doc = document.documentElement;
  var reduz = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* abertura */
  requestAnimationFrame(function () { setTimeout(function () { doc.classList.add('pronto'); }, 60); });

  /* topo: fica sólido depois da abertura e some ao descer */
  var topo = document.querySelector('.topo');
  var ultimo = 0;
  var prog = document.querySelectorAll('.progresso i');
  function aoRolar() {
    var y = scrollY;
    if (topo) {
      topo.classList.toggle('solido', y > 40);
      topo.classList.toggle('some', y > 400 && y > ultimo && !document.body.classList.contains('trava'));
    }
    ultimo = y;
    if (prog.length) {
      var t = Math.max(1, document.documentElement.scrollHeight - innerHeight);
      var p = Math.min(1, y / t) * prog.length;
      prog.forEach(function (el, i) { el.style.transform = 'scaleX(' + Math.max(0, Math.min(1, p - i)) + ')'; });
    }
  }
  addEventListener('scroll', aoRolar, { passive: true });
  aoRolar();

  /* gaveta do celular */
  var abrir = document.querySelector('.abrir');
  var gaveta = document.querySelector('.gaveta');
  if (abrir && gaveta) {
    abrir.addEventListener('click', function () {
      var a = abrir.getAttribute('aria-expanded') !== 'true';
      abrir.setAttribute('aria-expanded', a);
      gaveta.classList.toggle('aberta', a);
      document.body.classList.toggle('trava', a);
      document.body.style.overflow = a ? 'hidden' : '';
    });
    gaveta.addEventListener('click', function (e) {
      if (e.target.closest('a')) { abrir.click(); }
    });
  }

  /* revelar ao rolar */
  var io = 'IntersectionObserver' in window && !reduz ? new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('vis'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -8% 0px' }) : null;
  function revelar(els) {
    els.forEach(function (el, i) {
      el.classList.add('rv');
      if (!io) { el.classList.add('vis'); return; }
      el.style.transitionDelay = (i % 4) * 70 + 'ms';
      io.observe(el);
    });
  }
  window.revelar = revelar;
  revelar(document.querySelectorAll('[data-rv]'));

  /* obras */
  var OBRAS = window.OBRAS || [];
  var NOME = { fineline: 'Fineline', realismo: 'Realismo P&B' };
  function esc(t) { return String(t).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;'); }
  function src(o, w) { return 'assets/obras/' + o.id + '-' + w + '.webp'; }
  function fig(o, i) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'obra';
    b.dataset.i = i;
    b.innerHTML = '<img src="' + src(o, 640) + '" alt="' + esc(o.d + ' — ' + NOME[o.e]) + '" loading="lazy" decoding="async" width="640" height="' + Math.round(640 / o.r) + '">' +
      '<span class="leg">' + esc(o.d) + '<small>' + esc(NOME[o.e]) + '</small></span>';
    return b;
  }

  var lista = OBRAS;
  function montar(alvo, itens) {
    alvo.innerHTML = '';
    itens.forEach(function (o) { alvo.appendChild(fig(o, OBRAS.indexOf(o))); });
    revelar(alvo.querySelectorAll('.obra'));
  }

  // amostras por estilo na home
  document.querySelectorAll('[data-amostra]').forEach(function (el) {
    var e = el.dataset.amostra;
    var ids = (el.dataset.ids || '').split(',');
    ids.forEach(function (id) {
      var o = OBRAS.filter(function (x) { return x.id === id; })[0];
      if (!o) return;
      var a = document.createElement('a');
      a.href = 'trabalhos.html?estilo=' + e;
      a.innerHTML = '<img src="' + src(o, 640) + '" alt="' + esc(o.d) + '" loading="lazy" decoding="async">';
      el.appendChild(a);
    });
  });

  var grade = document.querySelector('[data-grade]');
  if (grade) {
    var limite = +grade.dataset.limite || 0;
    var filtros = document.querySelectorAll('.filtros button');
    function aplicar(e, empurrar) {
      lista = e && e !== 'todos' ? OBRAS.filter(function (o) { return o.e === e; }) : OBRAS;
      montar(grade, limite ? lista.slice(0, limite) : lista);
      filtros.forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.f === (e || 'todos')); });
      if (empurrar && history.replaceState) {
        history.replaceState(null, '', e && e !== 'todos' ? '?estilo=' + e : location.pathname);
      }
    }
    filtros.forEach(function (b) {
      var n = b.dataset.f === 'todos' ? OBRAS.length : OBRAS.filter(function (o) { return o.e === b.dataset.f; }).length;
      var s = b.querySelector('sup'); if (s) s.textContent = n;
      b.addEventListener('click', function () { aplicar(b.dataset.f, true); });
    });
    var q = new URLSearchParams(location.search).get('estilo');
    aplicar(q === 'fineline' || q === 'realismo' ? q : 'todos');
  }

  /* lightbox */
  var lb = document.querySelector('.lb');
  if (lb) {
    var img = lb.querySelector('img');
    var leg = lb.querySelector('[data-leg]');
    var cont = lb.querySelector('[data-cont]');
    var atual = 0, origem = null;
    function mostrar(k) {
      var n = lista.length;
      atual = (k + n) % n;
      var o = lista[atual];
      img.style.opacity = 0;
      var novo = new Image();
      novo.onload = function () { img.src = novo.src; img.alt = o.d; img.style.opacity = 1; };
      novo.src = src(o, 1200);
      leg.textContent = o.d + ' · ' + NOME[o.e];
      cont.textContent = String(atual + 1).padStart(2, '0') + ' / ' + String(n).padStart(2, '0');
    }
    function abrirLb(o) {
      origem = document.activeElement;
      mostrar(lista.indexOf(o));
      lb.classList.add('aberto');
      lb.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      lb.querySelector('[data-fechar]').focus();
    }
    function fechar() {
      lb.classList.remove('aberto');
      lb.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      if (origem) origem.focus();
    }
    document.addEventListener('click', function (e) {
      var b = e.target.closest('.obra');
      if (b) abrirLb(OBRAS[+b.dataset.i]);
    });
    lb.querySelector('[data-fechar]').addEventListener('click', fechar);
    lb.querySelector('[data-ant]').addEventListener('click', function () { mostrar(atual - 1); });
    lb.querySelector('[data-prox]').addEventListener('click', function () { mostrar(atual + 1); });
    lb.querySelector('.lb-palco').addEventListener('click', function (e) { if (e.target === e.currentTarget) fechar(); });
    addEventListener('keydown', function (e) {
      if (!lb.classList.contains('aberto')) return;
      if (e.key === 'Escape') fechar();
      if (e.key === 'ArrowLeft') mostrar(atual - 1);
      if (e.key === 'ArrowRight') mostrar(atual + 1);
    });
    var x0 = null;
    lb.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 50) mostrar(atual + (dx < 0 ? 1 : -1));
      x0 = null;
    });
  }

  /* links de contato */
  function urlDM() { return 'https://ig.me/m/' + CONFIG.instagram; }
  document.querySelectorAll('[data-dm]').forEach(function (a) { a.href = urlDM(); });

  /* orçamento */
  var form = document.querySelector('[data-orcamento]');
  if (form) {
    var previa = form.querySelector('.previa');
    var ok = document.querySelector('.ok');
    function texto() {
      var f = new FormData(form);
      var l = ['Oi, Andre! Vim pelo site e queria um orçamento.', ''];
      if (f.get('nome')) l.push('Nome: ' + f.get('nome'));
      if (f.get('estilo')) l.push('Estilo: ' + f.get('estilo'));
      if (f.get('local')) l.push('Local do corpo: ' + f.get('local'));
      if (f.get('tamanho')) l.push('Tamanho aproximado: ' + f.get('tamanho') + ' cm');
      if (f.get('ideia')) { l.push(''); l.push('Ideia: ' + f.get('ideia')); }
      l.push(''); l.push('Tenho mais de 18 anos. Mando as referências aqui na conversa.');
      return l.join('\n');
    }
    function atualizar() { previa.textContent = texto(); }
    form.addEventListener('input', atualizar);
    form.addEventListener('change', atualizar);
    atualizar();
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var t = texto();
      if (CONFIG.whatsapp) {
        window.open('https://wa.me/' + CONFIG.whatsapp + '?text=' + encodeURIComponent(t), '_blank', 'noopener');
        return;
      }
      var ir = function () { window.open(urlDM(), '_blank', 'noopener'); };
      ok.classList.add('vis');
      if (navigator.clipboard) { navigator.clipboard.writeText(t).then(ir, ir); } else { ir(); }
    });
  }
})();
