// Observatory Core Architecture: Navigation, Mega Menu, Mobile Drawer, and Realtime Telemetry
function toggleObservatoryMegaMenu(event) {
    if (event) {
        event.stopPropagation();
        event.preventDefault();
    }
    const menu = document.getElementById('observatory-mega-menu');
    if (!menu) return;
    const isHidden = menu.classList.contains('hidden');
    if (isHidden) {
        menu.classList.remove('hidden');
        menu.classList.add('flex', 'flex-col');
    } else {
        menu.classList.add('hidden');
        menu.classList.remove('flex', 'flex-col');
    }
}

function closeObservatoryMegaMenu() {
    const menu = document.getElementById('observatory-mega-menu');
    if (menu) {
        menu.classList.add('hidden');
        menu.classList.remove('flex', 'flex-col');
    }
}

document.addEventListener('click', function(e) {
    const wrapper = document.getElementById('observatory-nav-dropdown-wrapper');
    const floatBtn = document.getElementById('floating-menu-btn');
    if (wrapper && !wrapper.contains(e.target) && (!floatBtn || !floatBtn.contains(e.target))) {
        closeObservatoryMegaMenu();
    }
});

function toggleMobileDrawer() {
    const drawer = document.getElementById('mobile-drawer');
    const overlay = document.getElementById('mobile-drawer-overlay');
    if (!drawer || !overlay) return;
    
    if (overlay.classList.contains('hidden')) {
        overlay.classList.remove('hidden');
        drawer.classList.remove('-translate-x-full', 'rtl:translate-x-full');
    } else {
        overlay.classList.add('hidden');
        drawer.classList.add('-translate-x-full', 'rtl:translate-x-full');
    }
}

// Realtime Telemetry & Pulse Engine
(function() {
  const STATS_API = 'https://mrhermes.ir/api/autoplaza_stats.php';

  function getSessionId() {
    let sid = localStorage.getItem('apz_visitor_sid');
    if (!sid) {
      sid = 'apz_' + Math.random().toString(36).substring(2, 11) + '_' + Date.now().toString(36);
      localStorage.setItem('apz_visitor_sid', sid);
    }
    return sid;
  }

  function toPersianDigits(n) {
    if (n === undefined || n === null || isNaN(n)) return '۰';
    return Number(n).toLocaleString('fa-IR');
  }

  function applyStats(data) {
    if (!data || !data.success) return;

    const online = data.online || 0;
    const onlineText = toPersianDigits(online);
    ['stat-online-users', 'live-header-users', 'float-online-users'].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.textContent = onlineText;
    });

    const todayViews = toPersianDigits(data.today?.views);
    const todayVisitors = toPersianDigits(data.today?.visitors);
    const todayViewsEl = document.getElementById('stat-today-views');
    const todayVisitorsEl = document.getElementById('stat-today-visitors');
    const floatTodayEl = document.getElementById('float-today-views');
    if (todayViewsEl) todayViewsEl.textContent = todayViews;
    if (todayVisitorsEl) todayVisitorsEl.textContent = todayVisitors;
    if (floatTodayEl) floatTodayEl.textContent = todayViews;

    const yestViews = toPersianDigits(data.yesterday?.views);
    const yestVisitors = toPersianDigits(data.yesterday?.visitors);
    const yestViewsEl = document.getElementById('stat-yesterday-views');
    const yestVisitorsEl = document.getElementById('stat-yesterday-visitors');
    if (yestViewsEl) yestViewsEl.textContent = yestViews;
    if (yestVisitorsEl) yestVisitorsEl.textContent = yestVisitors;

    const totalViews = toPersianDigits(data.total?.views);
    const totalVisitors = toPersianDigits(data.total?.visitors);
    const totalViewsEl = document.getElementById('stat-total-views');
    const totalVisitorsEl = document.getElementById('stat-total-visitors');
    if (totalViewsEl) totalViewsEl.textContent = totalViews;
    if (totalVisitorsEl) totalVisitorsEl.textContent = totalVisitors;
  }

  const sid = getSessionId();
  const page = window.location.pathname + window.location.hash;

  fetch(`${STATS_API}?action=hit&sid=${encodeURIComponent(sid)}&page=${encodeURIComponent(page)}`)
    .then(res => res.json())
    .then(applyStats)
    .catch(err => console.log('Analytics pulse:', err));

  setInterval(() => {
    fetch(`${STATS_API}?action=heartbeat&sid=${encodeURIComponent(sid)}&page=${encodeURIComponent(window.location.pathname + window.location.hash)}`)
      .then(res => res.json())
      .then(applyStats)
      .catch(() => {});
  }, 25000);
})();
