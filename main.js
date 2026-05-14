/* ============================================================
   HEPHZIBAH EDUTECH — Global JavaScript
   ============================================================ */

// ── Active nav link ──
(function () {
  const page = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('#site-nav .nav-links a, #site-nav .mobile-menu a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === page) {
      a.classList.add('active');
    } else if ((page === '' || page === 'index.html') && href === 'index.html') {
      a.classList.add('active');
    }
  });
})();

// ── Mobile menu ──
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobile-menu');
if (hamburger && mobileMenu) {
  hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
  });
}

// ── Nav scroll shadow ──
window.addEventListener('scroll', () => {
  const nav = document.getElementById('site-nav');
  if (nav) {
    nav.style.boxShadow = window.scrollY > 50
      ? '0 4px 30px rgba(0,0,0,0.45)'
      : 'none';
  }
}, { passive: true });

// ── Scroll reveal ──
(function () {
  const els = document.querySelectorAll('.reveal');
  if (!els.length) return;
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.1 });
  els.forEach(el => obs.observe(el));
})();
