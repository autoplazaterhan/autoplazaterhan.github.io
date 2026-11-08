# -*- coding: utf-8 -*-
import os
import re

workspace_dir = "/Users/ricksabchez/workspace/projects/autoplazaterhan.github.io"

# 1. Section Catalog Metadata
sections_catalog = [
    {
        "id": "posts",
        "file": "posts.html",
        "title": "پست‌ها و ریلزهای اینستاگرام",
        "subtitle": "۱۳۰ مدیا با کاور و لینک مستقیم",
        "short_title": "پست‌ها و ریلزها",
        "category_key": "social",
        "category_title": "شبکه‌های اجتماعی و افکار عمومی",
        "category_color": "cyan",
        "metric": "۱۳۰ مدیا • ۱۲.۸M ویو",
        "desc": "مجموعه مستند تمامی ویدیوها، ریلزها و پست‌های منتشرشده اینفلوئنسرها و پیج رسمی اتوپلازا با کاور ویدیویی، آمار لایک و ویو و لینک مستقیم.",
        "icon_svg": '<svg class="w-5 h-5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>',
        "extra_scripts": """
<script>
let currentPostFilter = 'all';
let currentPostView = 'cards';

function filterPosts(filterType, btn) {
    currentPostFilter = filterType;
    document.querySelectorAll('.post-filter-btn').forEach(b => {
        b.className = 'post-filter-btn px-3 py-1.5 rounded-xl text-xs font-medium text-slate-400 hover:text-white hover:bg-white/[0.05] transition whitespace-nowrap';
    });
    btn.className = 'post-filter-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-[#e85a2a]/20 text-[#e85a2a] border border-[#e85a2a]/40 whitespace-nowrap active transition';
    applyPostFilters();
}

function togglePostView(view) {
    currentPostView = view;
    const cardsView = document.getElementById('posts-cards-view');
    const tableView = document.getElementById('posts-table-view');
    const btnCards = document.getElementById('post-view-btn-cards');
    const btnTable = document.getElementById('post-view-btn-table');

    if (view === 'cards') {
        if (cardsView) cardsView.classList.remove('hidden');
        if (tableView) tableView.classList.add('hidden');
        if (btnCards) btnCards.className = 'px-3 py-1.5 rounded-lg text-xs font-bold bg-[#e85a2a]/20 text-[#e85a2a] border border-[#e85a2a]/40 transition flex items-center gap-1';
        if (btnTable) btnTable.className = 'px-3 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-white hover:bg-dark-700 transition flex items-center gap-1';
    } else {
        if (cardsView) cardsView.classList.add('hidden');
        if (tableView) tableView.classList.remove('hidden');
        if (btnTable) btnTable.className = 'px-3 py-1.5 rounded-lg text-xs font-bold bg-[#e85a2a]/20 text-[#e85a2a] border border-[#e85a2a]/40 transition flex items-center gap-1';
        if (btnCards) btnCards.className = 'px-3 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-white hover:bg-dark-700 transition flex items-center gap-1';
    }
}

function searchPosts() {
    applyPostFilters();
}

function applyPostFilters() {
    const query = (document.getElementById('posts-search-input')?.value || '').toLowerCase().trim();
    const cards = document.querySelectorAll('.post-card');
    cards.forEach(card => {
        const filters = (card.getAttribute('data-filters') || '').split(' ');
        const search = (card.getAttribute('data-search') || '').toLowerCase();
        const matchesFilter = (currentPostFilter === 'all' || filters.includes(currentPostFilter));
        const matchesQuery = (!query || search.includes(query));
        card.style.display = (matchesFilter && matchesQuery) ? 'flex' : 'none';
    });

    const rows = document.querySelectorAll('.post-table-row');
    rows.forEach(row => {
        const filters = (row.getAttribute('data-filters') || '').split(' ');
        const search = (row.getAttribute('data-search') || '').toLowerCase();
        const matchesFilter = (currentPostFilter === 'all' || filters.includes(currentPostFilter));
        const matchesQuery = (!query || search.includes(query));
        row.style.display = (matchesFilter && matchesQuery) ? '' : 'none';
    });
}
window.addEventListener('DOMContentLoaded', applyPostFilters);
</script>
"""
    },
    {
        "id": "audio-sentiment",
        "file": "audio-sentiment.html",
        "title": "واکاوی صوتی و تقابل دیدگاه‌ها",
        "subtitle": "رونویسی کلامی و تحلیل مواضع",
        "short_title": "واکاوی صوتی و کلامی",
        "category_key": "social",
        "category_title": "شبکه‌های اجتماعی و افکار عمومی",
        "category_color": "cyan",
        "metric": "رونویسی صوت • کالبدشکافی کپشن",
        "desc": "تحلیل طیف‌های تمجید، تخریب، رونویسی کلامی ویدیوهای اینستاگرام و واکاوی متنی و معنایی مواضع چهره‌های حاضر.",
        "icon_svg": '<svg class="w-5 h-5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"></path></svg>',
        "extra_scripts": ""
    },
    {
        "id": "influencers",
        "file": "influencers.html",
        "title": "دایرکتوری اینفلوئنسرها و چهره‌ها",
        "subtitle": "۵۸ پیج اینستاگرام با عکس و مشخصات",
        "short_title": "دایرکتوری اینفلوئنسرها",
        "category_key": "social",
        "category_title": "شبکه‌های اجتماعی و افکار عمومی",
        "category_color": "cyan",
        "metric": "۵۸ چهره • ۳۰M فالوور",
        "desc": "شناسنامه ۵۸ بلاگر خودرو، سبک زندگی و سلبریتی حاضر در افتتاحیه با تفکیک حوزه، تعداد دنبال‌کنندگان و نوع انتشار.",
        "icon_svg": '<svg class="w-5 h-5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>',
        "extra_scripts": """
<script>
let currentInfFilter = 'all';

function filterInfluencers(cat, btn) {
    currentInfFilter = cat;
    document.querySelectorAll('.inf-filter-btn').forEach(b => {
        b.className = 'inf-filter-btn px-3 py-1.5 rounded-xl text-xs font-medium text-slate-400 hover:text-white hover:bg-white/[0.05] transition whitespace-nowrap';
    });
    btn.className = 'inf-filter-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-[#e85a2a]/20 text-[#e85a2a] border border-[#e85a2a]/40 whitespace-nowrap active transition';
    applyInfFilters();
}

function searchInfluencers() {
    applyInfFilters();
}

function applyInfFilters() {
    const query = (document.getElementById('influencer-search')?.value || '').toLowerCase().trim();
    const cards = document.querySelectorAll('.influencer-card');
    cards.forEach(card => {
        const cat = card.getAttribute('data-cat') || '';
        const search = (card.getAttribute('data-name') || '').toLowerCase();
        const matchesFilter = (currentInfFilter === 'all' || cat === currentInfFilter);
        const matchesQuery = (!query || search.includes(query));
        card.style.display = (matchesFilter && matchesQuery) ? 'flex' : 'none';
    });
}
window.addEventListener('DOMContentLoaded', applyInfFilters);
</script>
"""
    },
    {
        "id": "critiques",
        "file": "critiques.html",
        "title": "رصدخانه توییت‌ها و شبکه X",
        "subtitle": "۱۷۵ توییت با فیلتر و سنجش احساسات",
        "short_title": "رصدخانه توییت‌ها (X)",
        "category_key": "social",
        "category_title": "شبکه‌های اجتماعی و افکار عمومی",
        "category_color": "cyan",
        "metric": "۱۷۵ توییت • ۷۹٪ نقد تند",
        "desc": "آرشیو کامل توییت‌ها و بازخوردهای شبکه X با دسته‌بندی موضوعی، سنجش احساسات، فیلتر لایک، ریتوییت و لینک مستقیم به توییت‌ها.",
        "icon_svg": '<svg class="w-5 h-5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>',
        "extra_scripts": """<script src="assets/js/twitter_observatory.js"></script>"""
    },
    {
        "id": "hashtags",
        "file": "hashtags.html",
        "title": "پایش هشتگ‌ها و خطاهای املایی",
        "subtitle": "داده‌کاوی متادیتا با باکس API",
        "short_title": "پایش هشتگ‌ها و BoxAPI",
        "category_key": "social",
        "category_title": "شبکه‌های اجتماعی و افکار عمومی",
        "category_color": "cyan",
        "metric": "پایش زنده با BoxAPI",
        "desc": "واکاوی دقیق واژگان، ترکیب‌های هشتگ رسمی و خطاهای رایج تایپی در شبکه‌های اجتماعی استخراج‌شده با اتصال مستقیم به باکس API.",
        "icon_svg": '<svg class="w-5 h-5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 20l4-16m2 16l4-16M6 9h14M4 15h14"></path></svg>',
        "extra_scripts": ""
    },
    {
        "id": "timeline",
        "file": "timeline.html",
        "title": "تایم‌لاین جامع رویدادها و وقایع",
        "subtitle": "۷۸ فاز زمانی و ۶۳ پست رسمی",
        "short_title": "تایم‌لاین رویدادها",
        "category_key": "media",
        "category_title": "رویدادها و پوشش رسانه‌ای",
        "category_color": "amber",
        "metric": "۷۸ فاز • ۶۳ پست رسمی",
        "desc": "گاه‌شمار کامل از نخستین تیزرها در تابستان ۱۴۰۵ تا مراسم افتتاحیه، موج رسانه‌ای، پیک‌های خبری و خروجی‌های پس از رویداد.",
        "icon_svg": '<svg class="w-5 h-5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>',
        "extra_scripts": """
<script>
function filterTimelineMaster(category) {
    const rows = document.querySelectorAll('.timeline-master-row');
    const buttons = document.querySelectorAll('.timeline-f-btn');
    
    buttons.forEach(btn => {
        if (btn.getAttribute('data-filter') === category) {
            btn.classList.add('bg-[#e85a2a]/20', 'text-[#e85a2a]', 'border-[#e85a2a]/40', 'active');
            btn.classList.remove('bg-dark-800', 'text-slate-400');
        } else {
            btn.classList.remove('bg-[#e85a2a]/20', 'text-[#e85a2a]', 'border-[#e85a2a]/40', 'active');
            btn.classList.add('bg-dark-800', 'text-slate-400');
        }
    });

    rows.forEach(row => {
        const cat = row.getAttribute('data-cat');
        if (category === 'all' || cat === category) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

function searchTimelineMaster() {
    const input = document.getElementById('timeline-search-input')?.value.toLowerCase().trim() || '';
    const rows = document.querySelectorAll('.timeline-master-row');
    
    rows.forEach(row => {
        const text = (row.getAttribute('data-text') || '').toLowerCase();
        if (!input || text.includes(input)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

function exportTimelineCSV() {
    fetch('data.json')
        .then(res => res.json())
        .then(data => {
            const timeline = data.unified_master_timeline_69 || data.timeline || [];
            let csv = 'Row,Date,Type,Publisher,Headline,Link\\n';
            timeline.forEach((item, idx) => {
                const row = [
                    idx + 1,
                    `"${(item.date || '').replace(/"/g, '""')}"`,
                    `"${(item.type || item.media_type || '').replace(/"/g, '""')}"`,
                    `"${(item.publisher || item.channel || '').replace(/"/g, '""')}"`,
                    `"${(item.headline || item.title || '').replace(/"/g, '""')}"`,
                    `"${(item.url || item.link || '').replace(/"/g, '""')}"`
                ].join(',');
                csv += row + '\\n';
            });
            const blob = new Blob(["\\uFEFF" + csv], { type: 'text/csv;charset=utf-8;' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'autoplaza_timeline_master.csv';
            document.body.appendChild(a);
            a.click();
            URL.revokeObjectURL(url);
        })
        .catch(err => alert('خطا در استخراج CSV: ' + err));
}
</script>
"""
    },
    {
        "id": "news",
        "file": "news.html",
        "title": "پوشش خبرگزاری‌ها و پایگاه‌های رسمی",
        "subtitle": "۳۴ رسانه رسمی همراه با لوگوی وکتور",
        "short_title": "پوشش خبرگزاری‌ها",
        "category_key": "media",
        "category_title": "رویدادها و پوشش رسانه‌ای",
        "category_color": "amber",
        "metric": "۳۴ رسانه با لوگوی رسمی",
        "desc": "فهرست مقالات، تیترها و رپرتاژهای منتشره در خبرگزاری‌های رسمی کشور با لوگوی وکتور، تاریخ انتشار و لینک مستقیم به منبع خبر.",
        "icon_svg": '<svg class="w-5 h-5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"></path></svg>',
        "extra_scripts": """
<script>
let currentNewsFilter = 'all';

function filterNews(cat, btn) {
    currentNewsFilter = cat;
    document.querySelectorAll('.news-filter-btn').forEach(b => {
        b.className = 'news-filter-btn px-3 py-1.5 rounded-xl text-xs font-medium text-slate-400 hover:text-white hover:bg-white/[0.05] transition whitespace-nowrap';
    });
    btn.className = 'news-filter-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-[#e85a2a]/20 text-[#e85a2a] border border-[#e85a2a]/40 whitespace-nowrap active transition';
    applyNewsFilters();
}

function searchNews() {
    applyNewsFilters();
}

function applyNewsFilters() {
    const query = (document.getElementById('news-search-input')?.value || '').toLowerCase().trim();
    const cards = document.querySelectorAll('.news-card');
    cards.forEach(card => {
        const cat = card.getAttribute('data-cat') || '';
        const name = (card.getAttribute('data-name') || '').toLowerCase();
        const title = (card.getAttribute('data-title') || '').toLowerCase();
        const matchesFilter = (currentNewsFilter === 'all' || cat === currentNewsFilter);
        const matchesQuery = (!query || name.includes(query) || title.includes(query));
        card.style.display = (matchesFilter && matchesQuery) ? 'flex' : 'none';
    });
}
window.addEventListener('DOMContentLoaded', applyNewsFilters);
</script>
"""
    },
    {
        "id": "broadcast",
        "file": "broadcast.html",
        "title": "پوشش رادیو، تلویزیون و مجلات خودرویی",
        "subtitle": "صداوسیما، پادکست‌ها و نشریات مکتوب",
        "short_title": "رادیو، تلویزیون و مجلات",
        "category_key": "media",
        "category_title": "رویدادها و پوشش رسانه‌ای",
        "category_color": "amber",
        "metric": "پوشش چندرسانه‌ای",
        "desc": "بررسی گزارش‌های صداوسیما، برنامه‌های خودرویی، پادکست‌ها، نشریات مکتوب و انعکاس سنتی رویداد اتوپلازا در رسانه‌ها.",
        "icon_svg": '<svg class="w-5 h-5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>',
        "extra_scripts": ""
    },
    {
        "id": "campaigns",
        "file": "campaigns.html",
        "title": "کمپین‌ها و پروموشن‌های تبلیغاتی",
        "subtitle": "تخفیف ۲۰۰ میلیون تومانی و قرعه‌کشی",
        "short_title": "کمپین‌ها و پروموشن‌ها",
        "category_key": "media",
        "category_title": "رویدادها و پوشش رسانه‌ای",
        "category_color": "amber",
        "metric": "تخفیف ۲۰۰M • قرعه‌کشی خودرو",
        "desc": "واکاوی سازوکار پروموشن‌های جذب مخاطب، بن‌های تخفیف خرید خودرو، قرعه‌کشی‌ها و تعهدات اجرایی مجتمع اتوپلازا.",
        "icon_svg": '<svg class="w-5 h-5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v13m0-13V6a2 2 0 112 2h-2zm0 0V5.5A2.5 2.5 0 109.5 8H12zm-7 4h14M5 12a2 2 0 01-2-2V7a2 2 0 012-2h14a2 2 0 012 2v3a2 2 0 01-2 2M5 12v7a2 2 0 002 2h10a2 2 0 002-2v-7"></path></svg>',
        "extra_scripts": ""
    },
    {
        "id": "ai-audit",
        "file": "ai-audit.html",
        "title": "کالبدشکافی ۱۹ ایجنت هوش مصنوعی",
        "subtitle": "ارزیابی فنی سوپراپلیکیشن اتوپلازا",
        "short_title": "کالبدشکافی ایجنت‌های AI",
        "category_key": "analysis",
        "category_title": "کالبدشکافی و پرونده‌های ویژه",
        "category_color": "emerald",
        "metric": "۱۹ ایجنت هوشمند",
        "desc": "ارزیابی فنی ۱۹ عامل هوشمند اعلام‌شده در سوپراپلیکیشن اتوپلازا، وضعیت پیاده‌سازی واقعی، ابزارها و مدل‌های هوش مصنوعی.",
        "icon_svg": '<svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"></path></svg>',
        "extra_scripts": """
<script>
function filterAgentsTable(status) {
    const rows = document.querySelectorAll('.agent-row');
    rows.forEach(row => {
        const act = row.getAttribute('data-activation') || '';
        const st = row.getAttribute('data-status') || '';
        if (status === 'all') {
            row.style.display = '';
        } else if (status === 'active' && (st.includes('فعال') || act === 'configured')) {
            row.style.display = '';
        } else if (status === 'tools_ready' && act === 'tools_ready') {
            row.style.display = '';
        } else if (status === 'not_built' && act === 'not_built') {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}
</script>
"""
    },
    {
        "id": "investigation",
        "file": "investigation.html",
        "title": "پرونده کارآگاهی و لایه‌های پنهان",
        "subtitle": "کالبدشکافی حامیان و سرمایه رویداد",
        "short_title": "پرونده کارآگاهی",
        "category_key": "analysis",
        "category_title": "کالبدشکافی و پرونده‌های ویژه",
        "category_color": "emerald",
        "metric": "کالبدشکافی پشت‌پرده",
        "desc": "بررسی ریشه‌های سرمایه، تیم اجرایی، قراردادهای حامیان مالی و لایه‌های پنهان بازیگران تبلیغاتی اتوپلازا.",
        "icon_svg": '<svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>',
        "extra_scripts": ""
    },
    {
        "id": "market-guild",
        "file": "market-guild.html",
        "title": "تحلیل صنفی، جوایز و تعارض منافع",
        "subtitle": "راستی‌آزمایی حقوقی و نمایشگاه‌داران",
        "short_title": "تحلیل صنفی و تعارض منافع",
        "category_key": "analysis",
        "category_title": "کالبدشکافی و پرونده‌های ویژه",
        "category_color": "emerald",
        "metric": "راستی‌آزمایی حقوقی",
        "desc": "واکاوی مجوزهای صنفی اتحادیه نمایشگاه‌داران خودرو، ابهامات قرعه‌کشی و نسبت میان رقابت در بازار سنتی و مدرن خودرو.",
        "icon_svg": '<svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"></path></svg>',
        "extra_scripts": ""
    },
    {
        "id": "production",
        "file": "production.html",
        "title": "تولید، ایونت و ایران نوین ونچرز",
        "subtitle": "نقش کانون ایران نوین در افتتاحیه",
        "short_title": "تولید و ایران نوین ونچرز",
        "category_key": "analysis",
        "category_title": "کالبدشکافی و پرونده‌های ویژه",
        "category_color": "emerald",
        "metric": "ایران نوین ونچرز",
        "desc": "نقش کانون ایران نوین و بازوی سرمایه‌گذاری خطرپذیر در برندینگ، سناریونویسی افتتاحیه و تامین مالی کمپین‌های تبلیغاتی.",
        "icon_svg": '<svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 4v16M17 4v16M3 8h4m10 0h4M3 12h18M3 16h4m10 0h4M4 20h16a1 1 0 001-1V5a1 1 0 00-1-1H4a1 1 0 00-1 1v14a1 1 0 001 1z"></path></svg>',
        "extra_scripts": ""
    },
    {
        "id": "platforms",
        "file": "platforms.html",
        "title": "توزیع پلتفرمی داده‌ها و سهم کانال‌ها",
        "subtitle": "سهم‌بندی تلگرام، اینستاگرام، توییتر و وب",
        "short_title": "توزیع پلتفرمی محتوا",
        "category_key": "data",
        "category_title": "اسناد، زیرساخت و آمار کلان",
        "category_color": "purple",
        "metric": "۵۷.۴٪ تلگرام • ۱۱.۶٪ اینستاگرام",
        "desc": "سهم‌بندی کانال‌های ارتباطی، نسبت رسانه‌های داخلی به خارجی و وزن انتشار محتوا در پلتفرم‌های گوناگون بر اساس سند دیتاک.",
        "icon_svg": '<svg class="w-5 h-5 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z"></path></svg>',
        "extra_scripts": """
<script>
window.addEventListener('DOMContentLoaded', () => {
    const pCtx = document.getElementById('platformPieChart');
    if (pCtx) {
        new Chart(pCtx, {
            type: 'doughnut',
            data: {
                labels: ['تلگرام (۵۷.۴٪)', 'بسترهای داخلی (۱۷.۶٪)', 'اینستاگرام (۱۱.۶٪)', 'توییتر (۸.۴٪)', 'خبرگزاری‌ها (۴.۹٪)'],
                datasets: [{
                    data: [628, 193, 127, 92, 54],
                    backgroundColor: ['#06b6d4', '#10b981', '#f59e0b', '#f43f5e', '#64748b'],
                    borderWidth: 0
                }]
            },
            options: { responsive: true, plugins: { legend: { display: false } }, cutout: '65%' }
        });
    }
});
</script>
"""
    },
    {
        "id": "specs",
        "file": "specs.html",
        "title": "مشخصات فنی، سازه، مالکان و مدیران",
        "subtitle": "۸۵٬۰۰۰ مترمربع وسعت و ۹۰ شوروم",
        "short_title": "مشخصات فنی و سازه",
        "category_key": "data",
        "category_title": "اسناد، زیرساخت و آمار کلان",
        "category_color": "purple",
        "metric": "۸۵٬۰۰۰ متر • ۹۰ شوروم",
        "desc": "شناسنامه فیزیکی، متراژ، گنجایش پارکینگ، موقعیت جغرافیایی و معرفی مدیران ارشد و سهام‌داران کلان‌پروژه اتوپلازا تهران.",
        "icon_svg": '<svg class="w-5 h-5 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>',
        "extra_scripts": ""
    },
    {
        "id": "faq",
        "file": "faq.html",
        "title": "پاسخ به سوالات کلیدی و ابهامات افکار عمومی",
        "subtitle": "۷ پرسش و پاسخ موشکافانه",
        "short_title": "سوالات افکار عمومی",
        "category_key": "data",
        "category_title": "اسناد، زیرساخت و آمار کلان",
        "category_color": "purple",
        "metric": "۷ پرسش و پاسخ کلیدی",
        "desc": "پاسخ‌های شفاف و مستند به پرسش‌های رایج پیرامون اصالت مجتمع، خرید و فروش خودرو، شایعات و مجوزهای اجرایی.",
        "icon_svg": '<svg class="w-5 h-5 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>',
        "extra_scripts": ""
    },
    {
        "id": "rawpdf",
        "file": "rawpdf.html",
        "title": "متن کامل و استناد سند رسمی دیتاک",
        "subtitle": "سامانه دستان دیتاک به همراه راستی‌آزمایی",
        "short_title": "متن کامل سند دیتاک",
        "category_key": "data",
        "category_title": "اسناد، زیرساخت و آمار کلان",
        "category_color": "purple",
        "metric": "سند رسمی PDF دیتاک",
        "desc": "متن کامل پیاده‌سازی‌شده گزارش پایش افکار عمومی سامانه دستان دیتاک به همراه راستی‌آزمایی ارقام و لینک مستقیم دانلود سند.",
        "icon_svg": '<svg class="w-5 h-5 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>',
        "extra_scripts": ""
    }
]

print("Catalog ready with", len(sections_catalog), "sections")

def generate_mega_menu_html(current_page="index.html"):
    categories = [
        ("social", "شبکه‌های اجتماعی و افکار عمومی", "text-cyan-400", "border-cyan-500/20", "bg-cyan-500/10"),
        ("media", "رویدادها و پوشش رسانه‌ای", "text-amber-400", "border-amber-500/20", "bg-amber-500/10"),
        ("analysis", "کالبدشکافی و پرونده‌های ویژه", "text-emerald-400", "border-emerald-500/20", "bg-emerald-500/10"),
        ("data", "اسناد، زیرساخت و آمار کلان", "text-purple-400", "border-purple-500/20", "bg-purple-500/10")
    ]
    
    col_htmls = []
    for cat_key, cat_title, cat_text, cat_border, cat_bg in categories:
        cat_items = [s for s in sections_catalog if s["category_key"] == cat_key]
        items_html = ""
        for s in cat_items:
            is_active = (current_page == s["file"])
            active_class = "border-[#e85a2a]/60 bg-[#e85a2a]/15 text-white shadow-sm" if is_active else "border-white/5 bg-white/[0.02] hover:bg-white/[0.06] hover:border-[#e85a2a]/40 text-white/90"
            active_badge = '<span class="w-1.5 h-1.5 rounded-full bg-[#e85a2a] animate-pulse"></span>' if is_active else ''
            
            items_html += f"""
            <a href="{s['file']}" class="group/item flex items-start gap-2.5 p-2 rounded-xl border transition-all duration-200 {active_class}">
                <div class="p-1.5 rounded-lg bg-black/40 border border-white/5 shrink-0 group-hover/item:border-[#e85a2a]/40 group-hover/item:scale-105 transition-all">
                    {s['icon_svg']}
                </div>
                <div class="flex-1 min-w-0">
                    <div class="flex items-center justify-between gap-1">
                        <span class="text-xs font-bold text-white group-hover/item:text-[#ff7b47] transition-colors truncate">{s['title']}</span>
                        {active_badge}
                    </div>
                    <span class="text-[10px] text-white/50 block font-mono mt-0.5 truncate">{s['metric']}</span>
                </div>
            </a>
            """
        
        col_htmls.append(f"""
        <div class="space-y-2">
            <div class="flex items-center gap-2 pb-1.5 border-b border-white/10">
                <span class="px-2 py-0.5 rounded-md text-[10px] font-bold border {cat_bg} {cat_text} {cat_border}">{cat_title}</span>
                <span class="text-[10px] font-mono text-white/40">({len(cat_items)} بخش)</span>
            </div>
            <div class="space-y-1">
                {items_html}
            </div>
        </div>
        """)
    
    return f"""
    <!-- Mega Menu Dropdown Panel -->
    <div id="observatory-mega-menu" class="hidden absolute top-full end-0 mt-3 w-[94vw] max-w-[1080px] rounded-2xl bg-[#08080a]/98 backdrop-blur-2xl border border-white/15 shadow-[0_25px_80px_rgba(0,0,0,0.95)] p-5 z-50 transition-all text-start">
        <div class="flex items-center justify-between gap-3 pb-3 mb-3 border-b border-white/10">
            <div class="flex items-center gap-2.5">
                <span class="w-2.5 h-2.5 rounded-full bg-[#e85a2a] animate-pulse"></span>
                <span class="text-xs sm:text-sm font-black text-white">منوهای تحلیلی رصدخانه اتوپلازا تهران</span>
                <span class="text-[11px] px-2 py-0.5 rounded-full bg-[#e85a2a]/15 text-[#ff7b47] border border-[#e85a2a]/30 font-mono font-bold">۱۷ صفحه مستقل</span>
            </div>
            <div class="flex items-center gap-2">
                <button type="button" onclick="closeObservatoryMegaMenu()" class="p-1 rounded-lg text-white/40 hover:text-white hover:bg-white/10 transition">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
            </div>
        </div>

        <!-- 4 Columns Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {"".join(col_htmls)}
        </div>

        <!-- Footer of Mega Menu -->
        <div class="mt-4 pt-3.5 border-t border-white/10 flex flex-wrap items-center justify-between gap-3 text-xs text-white/60">
            <div class="flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                <span>پایش زنده ۳۶۰ درجه • ۱٬۰۹۴ رکورد داده استخراج‌شده</span>
            </div>
            <div class="flex items-center gap-3">
                <a href="index.html#observatory-atlas" class="text-[#ff7b47] hover:underline font-bold flex items-center gap-1">
                    <span>مشاهده اطلس کامل در صفحه اصلی</span>
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
                </a>
                <span>•</span>
                <a href="autoplaza-datak-report.pdf" target="_blank" class="hover:text-white transition">سند رسمی دیتاک (PDF)</a>
            </div>
        </div>
    </div>
    """

def generate_header(current_page="index.html"):
    home_link = "#hero" if current_page == "index.html" else "index.html"
    mega_menu = generate_mega_menu_html(current_page)
    
    # Active indicator helpers
    def nav_active(page):
        return "text-[#ff7b47] font-bold" if current_page == page else "text-white/80 hover:text-white font-medium"

    return f"""
    <!-- Header: Authentic Tehran Auto Plaza Luxury Dark Navigation -->
    <header class="fixed inset-x-0 top-0 z-50 transition-all duration-300 bg-[#050505]/95 backdrop-blur-md text-white border-b border-white/10">
        <div class="mx-auto flex h-[4.5rem] max-w-[1400px] items-center justify-between gap-3 px-4 md:h-[5rem] md:px-8">
            <!-- Logo Section -->
            <a href="{home_link}" class="flex items-center gap-3 group shrink-0">
                <div class="relative h-11 w-8 md:h-12 md:w-9 flex items-center shrink-0 drop-shadow-[0_4px_16px_rgba(232,90,42,0.35)]">
                    <img src="assets/apz1.png" alt="لوگوی اتو پلازا تهران" class="h-full w-full object-contain group-hover:scale-105 transition-transform">
                </div>
                <div class="relative h-8 w-[5.5rem] md:h-9 md:w-[6.75rem] flex items-center shrink-0">
                    <img src="assets/apz2-light.png" alt="اتوپلازا تهران" class="h-full w-full object-contain object-right">
                </div>
            </a>

            <!-- Desktop Nav Links -->
            <nav class="hidden lg:flex items-center gap-4 xl:gap-5 text-[0.85rem]">
                <a href="{home_link}" class="cursor-pointer transition {nav_active('index.html')}">صفحه اصلی</a>
                <a href="timeline.html" class="cursor-pointer transition {nav_active('timeline.html')}">تایم‌لاین رویدادها</a>
                <a href="posts.html" class="cursor-pointer transition {nav_active('posts.html')}">پست‌ها و ریلزها</a>
                <a href="influencers.html" class="cursor-pointer transition {nav_active('influencers.html')}">شبکه اینفلوئنسرها</a>
                <a href="news.html" class="cursor-pointer transition {nav_active('news.html')}">خبرگزاری‌ها</a>
                <a href="critiques.html" class="cursor-pointer transition {nav_active('critiques.html')}">رصدخانه X</a>

                <!-- The Enhanced Mega Menu Dropdown Trigger -->
                <div class="relative" id="observatory-nav-dropdown-wrapper">
                    <button type="button" onclick="toggleObservatoryMegaMenu(event)" class="inline-flex items-center gap-2 px-3 py-1.5 rounded-xl bg-gradient-to-r from-white/[0.08] to-white/[0.02] border border-white/15 text-white font-bold text-xs hover:border-[#e85a2a]/60 hover:text-white transition-all shadow-sm">
                        <svg class="w-4 h-4 text-[#e85a2a]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
                        <span>منوهای تحلیلی رصدخانه</span>
                        <span class="px-1.5 py-0.2 rounded bg-[#e85a2a]/20 text-[#ff7b47] text-[10px] font-mono font-bold">۱۷ بخش</span>
                        <svg class="w-3.5 h-3.5 text-white/50 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    {mega_menu}
                </div>
            </nav>

            <!-- Header CTA & Actions -->
            <div class="flex items-center gap-2 sm:gap-3">
                <a href="autoplaza-datak-report.pdf" target="_blank" class="btn-ghost hidden xl:inline-flex items-center gap-2 rounded-full px-4 py-2 text-xs font-bold text-white hover:border-[#e85a2a]/60">
                    <svg class="w-4 h-4 text-[#e85a2a]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    <span>سند رسمی دیتاک</span>
                </a>
                <a href="https://autoplaza.ir/" target="_blank" rel="noopener noreferrer" class="btn-ghost hidden sm:inline-flex items-center gap-1.5 rounded-full px-3.5 py-2 text-xs font-semibold text-white/90 hover:border-[#e85a2a]/60">
                    <span>autoplaza.ir</span>
                    <svg class="w-3.5 h-3.5 text-[#ff7b47]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                </a>
                
                <!-- Quick Menu Toggle Button (Visible on mobile/tablet) -->
                <button type="button" onclick="toggleMobileDrawer()" class="lg:hidden p-2 rounded-xl bg-white/[0.05] border border-white/10 text-white hover:text-[#e85a2a] transition flex items-center gap-1.5 text-xs font-bold" aria-label="منوی رصدخانه">
                    <svg class="w-5 h-5 text-[#e85a2a]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                    <span class="hidden sm:inline">منوهای تحلیلی</span>
                </button>
            </div>
        </div>
    </header>
    """

def generate_mobile_drawer(current_page="index.html"):
    categories = [
        ("social", "شبکه‌های اجتماعی و افکار عمومی", "text-cyan-400"),
        ("media", "رویدادها و پوشش رسانه‌ای", "text-amber-400"),
        ("analysis", "کالبدشکافی و پرونده‌های ویژه", "text-emerald-400"),
        ("data", "اسناد، زیرساخت و آمار کلان", "text-purple-400")
    ]
    
    sections_html = ""
    for cat_key, cat_title, cat_color in categories:
        cat_items = [s for s in sections_catalog if s["category_key"] == cat_key]
        links = ""
        for s in cat_items:
            is_active = (current_page == s["file"])
            active_class = "border-[#e85a2a]/60 bg-[#e85a2a]/15 text-white" if is_active else "border-white/5 bg-white/[0.02] text-white/80"
            links += f"""
            <a href="{s['file']}" onclick="toggleMobileDrawer()" class="flex items-center justify-between p-2.5 rounded-xl border transition text-xs {active_class}">
                <div class="flex items-center gap-2 truncate">
                    {s['icon_svg']}
                    <span class="font-bold text-white truncate">{s['title']}</span>
                </div>
                <span class="text-[10px] font-mono text-white/50 shrink-0">{s['metric']}</span>
            </a>
            """
        sections_html += f"""
        <div class="space-y-1.5 pt-2">
            <span class="text-[11px] font-bold {cat_color} block px-1">{cat_title}</span>
            <div class="space-y-1">
                {links}
            </div>
        </div>
        """

    return f"""
    <!-- Mobile Drawer Overlay -->
    <div id="mobile-drawer-overlay" onclick="toggleMobileDrawer()" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden transition-opacity"></div>
    
    <!-- Mobile Drawer Panel -->
    <aside id="mobile-drawer" class="fixed top-0 bottom-0 start-0 z-50 w-80 max-w-[85vw] bg-[#08080a] border-e border-white/10 shadow-2xl p-5 overflow-y-auto transform -translate-x-full rtl:translate-x-full transition-transform duration-300 space-y-4">
        <div class="flex items-center justify-between pb-3 border-b border-white/10">
            <div class="flex items-center gap-2">
                <img src="assets/apz1.png" alt="اتوپلازا تهران" class="h-8 w-6 object-contain">
                <span class="text-sm font-black text-white">منوهای تحلیلی رصدخانه</span>
            </div>
            <button onclick="toggleMobileDrawer()" class="p-1 rounded-lg text-white/50 hover:text-white hover:bg-white/10 transition">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
        </div>

        <div class="space-y-1">
            <a href="index.html" class="flex items-center gap-2 p-2.5 rounded-xl bg-white/[0.04] text-xs font-bold text-white hover:bg-[#e85a2a]/20 border border-white/5 transition">
                <svg class="w-4 h-4 text-[#e85a2a]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
                <span>صفحه اصلی رصدخانه (هاب مرکزی)</span>
            </a>
        </div>

        <div class="space-y-3">
            {sections_html}
        </div>

        <div class="pt-4 border-t border-white/10 space-y-2">
            <a href="autoplaza-datak-report.pdf" target="_blank" class="w-full btn-ghost py-2.5 px-3 text-xs font-bold flex items-center justify-center gap-2">
                <svg class="w-4 h-4 text-[#e85a2a]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                <span>دانلود سند رسمی دیتاک (PDF)</span>
            </a>
            <a href="https://autoplaza.ir/" target="_blank" rel="noopener noreferrer" class="w-full btn-ghost py-2.5 px-3 text-xs font-semibold flex items-center justify-center gap-1.5 text-white/90">
                <span>وب‌سایت رسمی autoplaza.ir ↗</span>
            </a>
        </div>
    </aside>
    """

def generate_floating_menu():
    return """
    <!-- Floating Quick Menu Button -->
    <button id="floating-menu-btn" onclick="toggleObservatoryMegaMenu(event)" class="fixed bottom-5 start-5 z-40 px-3.5 py-2 sm:px-4 sm:py-2.5 rounded-full bg-gradient-to-r from-[#e85a2a] to-[#d44a1c] text-white text-xs font-bold shadow-[0_8px_30px_rgba(232,90,42,0.5)] border border-[#ff6b35]/60 hover:scale-105 transition-all flex items-center gap-2">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
        <span>منوهای تحلیلی (۱۷ بخش)</span>
    </button>
    """

def generate_footer(current_page="index.html"):
    return """
    <!-- Authentic Tehran Auto Plaza Luxury Dark Footer -->
    <footer class="border-t border-white/10 bg-[#050505] text-white/70 mt-20 pt-16 pb-12">
        <div class="max-w-[1400px] mx-auto px-4 md:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-10 pb-12 border-b border-white/10">
                <!-- Col 1: Branding -->
                <div class="space-y-4 md:col-span-1">
                    <div class="flex items-center gap-3">
                        <div class="relative h-12 w-9 flex items-center drop-shadow-[0_4px_16px_rgba(232,90,42,0.4)]">
                            <img src="assets/apz1.png" alt="اتوپلازا تهران" class="h-full w-full object-contain">
                        </div>
                        <div class="relative h-8 w-[6.5rem] flex items-center">
                            <img src="assets/apz2-light.png" alt="اتوپلازا تهران" class="h-full w-full object-contain object-right">
                        </div>
                    </div>
                    <p class="text-xs leading-relaxed text-white/60">
                        اتوپلازا تهران - بزرگ‌ترین مجتمع تخصصی خودرو و سبک زندگی در خاورمیانه. نمایشگاه‌ها، فرصت‌ها و اکوسیستم تحلیلی داده‌محور.
                    </p>
                    <div class="pt-2 flex items-center gap-2">
                        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-[11px] font-medium bg-[#e85a2a]/10 text-[#ff7b47] border border-[#e85a2a]/30">
                            <span class="w-1.5 h-1.5 rounded-full bg-[#e85a2a] animate-pulse"></span>
                            پایگاه جامع داده‌کاوی رسانه‌ای
                        </span>
                    </div>
                </div>

                <!-- Col 2: Top Analytical Pages -->
                <div class="space-y-3">
                    <h4 class="text-sm font-bold text-white uppercase tracking-wider">صفحات مستقل تحلیلی</h4>
                    <ul class="space-y-2 text-xs">
                        <li><a href="timeline.html" class="hover:text-[#e85a2a] transition">تایم‌لاین جامع رویدادها (۷۸ فاز)</a></li>
                        <li><a href="posts.html" class="hover:text-[#e85a2a] transition">پست‌ها و ریلزهای اینستاگرام (۱۳۰ مدیا)</a></li>
                        <li><a href="influencers.html" class="hover:text-[#e85a2a] transition">دایرکتوری اینفلوئنسرها (۵۸ پیج)</a></li>
                        <li><a href="news.html" class="hover:text-[#e85a2a] transition">پوشش خبرگزاری‌ها (۳۴ رسانه رسمی)</a></li>
                        <li><a href="audio-sentiment.html" class="hover:text-[#e85a2a] transition">واکاوی صوتی و کلامی اینستاگرام</a></li>
                        <li><a href="critiques.html" class="hover:text-[#e85a2a] transition">رصدخانه توییت‌ها و شبکه X (۱۷۵ توییت)</a></li>
                    </ul>
                </div>

                <!-- Col 3: Special Dossiers & Data -->
                <div class="space-y-3">
                    <h4 class="text-sm font-bold text-white uppercase tracking-wider">پرونده‌ها و داده‌های کلان</h4>
                    <ul class="space-y-2 text-xs">
                        <li><a href="ai-audit.html" class="hover:text-[#e85a2a] transition">کالبدشکافی ۱۹ ایجنت هوش مصنوعی</a></li>
                        <li><a href="investigation.html" class="hover:text-[#e85a2a] transition">پرونده کارآگاهی و لایه‌های پنهان</a></li>
                        <li><a href="market-guild.html" class="hover:text-[#e85a2a] transition">تحلیل صنفی، جوایز و تعارض منافع</a></li>
                        <li><a href="campaigns.html" class="hover:text-[#e85a2a] transition">کمپین‌ها و تخفیف ۲۰۰ میلیونی</a></li>
                        <li><a href="platforms.html" class="hover:text-[#e85a2a] transition">توزیع پلتفرمی داده‌ها</a></li>
                        <li><a href="rawpdf.html" class="hover:text-[#e85a2a] transition">متن کامل سند رسمی دیتاک (PDF)</a></li>
                    </ul>
                </div>

                <!-- Col 4: Architecture & Provenance -->
                <div class="space-y-3">
                    <h4 class="text-sm font-bold text-white uppercase tracking-wider">شناسنامه و داده‌کاوی</h4>
                    <div class="space-y-2 text-xs text-white/60 leading-relaxed">
                        <p>داده‌کاوی، متدولوژی پژوهش و معماری سیستم توسط <strong>ریک سانچز</strong> و به کمک <strong>ایجنت هوشمند مستر هرمس</strong> پیاده‌سازی شده است.</p>
                        <p>استخراج متادیتای زنده اینستاگرام با اتصال به <strong>باکس API</strong> و تحلیل کلان‌داده با اتکا به سامانه <strong>دیتاک (دستان)</strong> انجام گرفته است.</p>
                        <div class="pt-2">
                            <a href="https://autoplaza.ir/" target="_blank" rel="noopener noreferrer" class="text-[#ff7b47] hover:underline font-bold">وب‌سایت رسمی: autoplaza.ir ↗</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Bottom Row: Copyright & Meta -->
            <div class="pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-white/50">
                <p>پایگاه مستقل رصد و داده‌کاوی رسانه‌ای اتوپلازا تهران • پاییز ۱۴۰۵</p>
                <div class="flex items-center gap-4">
                    <a href="https://autoplaza.ir/" target="_blank" rel="noopener noreferrer" class="hover:text-white transition">autoplaza.ir</a>
                    <span>•</span>
                    <a href="autoplaza-datak-report.pdf" target="_blank" class="hover:text-white transition">سند PDF دیتاک</a>
                    <span>•</span>
                    <a href="https://github.com/autoplazaterhan/autoplazaterhan.github.io" target="_blank" class="hover:text-white transition">مخزن گیت‌هاب</a>
                </div>
            </div>
        </div>
    </footer>
    """

def generate_atlas_grid():
    cards_html = ""
    for s in sections_catalog:
        cards_html += f"""
        <div class="apz-card glass-panel rounded-2xl p-5 border border-white/10 hover:border-[#e85a2a]/60 transition-all flex flex-col justify-between group">
            <div class="space-y-3">
                <div class="flex items-center justify-between gap-2">
                    <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-white/[0.04] text-white/70 border border-white/10">{s['category_title']}</span>
                    <span class="text-[10px] font-mono text-[#ff7b47] font-bold">{s['metric']}</span>
                </div>
                <div class="flex items-center gap-3">
                    <div class="p-2.5 rounded-xl bg-black/50 border border-white/10 text-white shrink-0 group-hover:border-[#e85a2a]/50 group-hover:scale-105 transition-all">
                        {s['icon_svg']}
                    </div>
                    <div>
                        <h4 class="text-sm font-bold text-white group-hover:text-[#ff7b47] transition-colors">{s['title']}</h4>
                        <p class="text-[11px] text-white/50">{s['subtitle']}</p>
                    </div>
                </div>
                <p class="text-xs text-slate-300 leading-relaxed line-clamp-2">
                    {s['desc']}
                </p>
            </div>

            <div class="pt-4 mt-4 border-t border-white/10 flex items-center justify-between gap-2">
                <a href="{s['file']}" class="btn-primary px-3.5 py-1.5 text-xs font-bold inline-flex items-center gap-1.5 shadow-sm">
                    <span>مشاهده صفحه مستقل</span>
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
                </a>
                <button type="button" onclick="switchTab('{s['id']}'); document.getElementById('observatory-tabs').scrollIntoView({{behavior: 'smooth'}})" class="btn-ghost px-2.5 py-1.5 text-xs text-white/70 hover:text-white transition">
                    پیش‌نمایش سریع ↓
                </button>
            </div>
        </div>
        """

    return f"""
    <!-- Observatory Analytical Atlas: 17 Key Modules Grid -->
    <section id="observatory-atlas" class="space-y-6 pt-6">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-white/10 pb-4">
            <div>
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-[#e85a2a]/15 text-[#ff7b47] border border-[#e85a2a]/30 mb-2">
                    <span class="w-2 h-2 rounded-full bg-[#e85a2a] animate-pulse"></span>
                    <span>اطلس و نقشه دسترسی به داده‌ها</span>
                </div>
                <h3 class="text-2xl sm:text-3xl font-black text-white">منوهای تحلیلی رصدخانه اتوپلازا تهران (۱۷ بخش مستقل)</h3>
                <p class="text-xs sm:text-sm text-slate-300 mt-1 max-w-3xl leading-relaxed">
                    تمامی بخش‌های پژوهشی، داده‌کاوی اینستاگرام، اسناد رسمی دیتاک و تحلیل‌های رسانه‌ای در صفحات مستقل با لینک مستقیم و دسترسی سریع در دسترس هستند.
                </p>
            </div>
            <div class="flex items-center gap-2 shrink-0">
                <span class="text-xs text-white/60 font-mono">۱۷ صفحه تحلیلی مجزا</span>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {cards_html}
        </div>
    </section>
    """

print("Components ready.")

def generate_standalone_page(sec_meta, sec_html):
    clean_sec_html = re.sub(r'(<section[^>]*class="[^"]*)hidden([^"]*")', r'\1\2', sec_html, count=1)
    
    # Related sections (3 other sections from catalog)
    related = [s for s in sections_catalog if s["id"] != sec_meta["id"]][:3]
    related_cards = ""
    for r in related:
        related_cards += f"""
        <a href="{r['file']}" class="glass-panel rounded-xl p-4 border border-white/10 hover:border-[#e85a2a]/50 transition flex items-center justify-between gap-3 group">
            <div class="flex items-center gap-3">
                <div class="p-2 rounded-lg bg-black/40 border border-white/5 text-white group-hover:scale-105 transition">
                    {r['icon_svg']}
                </div>
                <div>
                    <h5 class="text-xs font-bold text-white group-hover:text-[#ff7b47] transition">{r['title']}</h5>
                    <span class="text-[10px] text-white/50 font-mono">{r['metric']}</span>
                </div>
            </div>
            <svg class="w-4 h-4 text-white/40 group-hover:text-[#e85a2a] group-hover:translate-x-[-2px] rtl:group-hover:translate-x-[2px] transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
        </a>
        """

    header = generate_header(sec_meta["file"])
    drawer = generate_mobile_drawer(sec_meta["file"])
    floating_btn = generate_floating_menu()
    footer = generate_footer(sec_meta["file"])

    page_html = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl" class="dark scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{sec_meta['title']} | رصدخانه اتوپلازا تهران</title>
    <meta name="description" content="{sec_meta['desc']}">
    <link rel="canonical" href="https://autoplazaterhan.github.io/{sec_meta['file']}" />
    <meta name="robots" content="index, follow" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        apz: {{
                            black: '#050505',
                            bg: '#0a0a0a',
                            card: '#0f0f11',
                            surface: '#151518',
                            orange: '#e85a2a',
                            'orange-deep': '#d44a1c',
                            'orange-glow': '#ff6b35',
                            red: '#fb2c36'
                        }},
                        dark: {{
                            950: '#050505',
                            900: '#0a0a0a',
                            800: '#111111',
                            700: '#181818',
                            600: '#222222',
                            500: '#333333'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        :root {{
            --background: #050505;
            --foreground: #f5f5f5;
            --orange: #e85a2a;
            --orange-deep: #d44a1c;
            --orange-glow: #ff6b35;
            --accent: #e85a2a;
        }}
        * {{
            font-family: 'Vazirmatn', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
            letter-spacing: 0 !important;
        }}
        body {{
            background-color: #050505;
            color: #f5f5f5;
            overflow-x: hidden;
        }}
        ::selection {{
            background: #e85a2a;
            color: #ffffff;
        }}
        .glass-panel {{
            background: rgba(255, 255, 255, 0.025);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }}
        .glass-panel:hover {{
            border-color: rgba(232, 90, 42, 0.45);
        }}
        .apz-card {{
            background: rgba(18, 18, 20, 0.75);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }}
        .btn-primary {{
            background: linear-gradient(135deg, #e85a2a 0%, #d44a1c 100%);
            color: #ffffff;
            border-radius: 9999px;
            font-weight: 700;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 4px 20px -4px rgba(232, 90, 42, 0.4);
        }}
        .btn-primary:hover {{
            box-shadow: 0 6px 30px 0 rgba(232, 90, 42, 0.65);
            transform: translateY(-1px);
        }}
        .btn-ghost {{
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.14);
            color: #ffffff;
            border-radius: 9999px;
            transition: all 0.3s ease;
        }}
        .btn-ghost:hover {{
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(232, 90, 42, 0.4);
        }}
    </style>
</head>
<body class="min-h-screen text-neutral-100 antialiased selection:bg-[#e85a2a] selection:text-white bg-[#050505]">
    {header}
    {drawer}

    <!-- Page Dossier Header & Breadcrumb -->
    <div class="pt-24 md:pt-28 pb-6 bg-gradient-to-b from-white/[0.04] to-transparent border-b border-white/10">
        <div class="max-w-[1400px] mx-auto px-4 md:px-8 space-y-4">
            <!-- Breadcrumbs -->
            <nav class="flex items-center gap-2 text-xs text-white/50" aria-label="Breadcrumb">
                <a href="index.html" class="hover:text-white transition flex items-center gap-1">
                    <svg class="w-3.5 h-3.5 text-[#e85a2a]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
                    <span>صفحه اصلی</span>
                </a>
                <span>/</span>
                <a href="index.html#observatory-atlas" class="hover:text-white transition">منوهای تحلیلی رصدخانه</a>
                <span>/</span>
                <span class="text-[#ff7b47] font-semibold">{sec_meta['title']}</span>
            </nav>

            <!-- Title & Quick Actions -->
            <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
                <div class="space-y-2">
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-[#e85a2a]/15 text-[#ff7b47] border border-[#e85a2a]/30">
                        <span>{sec_meta['category_title']}</span>
                        <span>•</span>
                        <span class="font-mono">{sec_meta['metric']}</span>
                    </div>
                    <h1 class="text-2xl sm:text-3xl md:text-4xl font-black text-white">{sec_meta['title']}</h1>
                    <p class="text-xs sm:text-sm text-slate-300 max-w-3xl leading-relaxed">{sec_meta['desc']}</p>
                </div>
                <div class="flex items-center gap-2.5 shrink-0">
                    <a href="index.html#observatory-atlas" class="btn-ghost px-4 py-2 text-xs font-bold inline-flex items-center gap-2">
                        <svg class="w-4 h-4 text-[#e85a2a]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
                        <span>هاب رصدخانه</span>
                    </a>
                    <a href="autoplaza-datak-report.pdf" target="_blank" class="btn-primary px-4 py-2 text-xs font-bold inline-flex items-center gap-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                        <span>سند رسمی دیتاک</span>
                    </a>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Section Content -->
    <main class="max-w-[1400px] mx-auto px-4 md:px-8 py-8 space-y-8">
        {clean_sec_html}

        <!-- Related Sections Navigator -->
        <div class="glass-panel rounded-2xl p-6 border border-white/10 mt-12 space-y-4">
            <div class="flex items-center justify-between pb-2 border-b border-white/10">
                <span class="text-xs font-bold text-white flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-[#e85a2a]"></span>
                    سایر بخش‌های تحلیلی مرتبط
                </span>
                <a href="index.html#observatory-atlas" class="text-xs text-[#ff7b47] hover:underline font-bold">مشاهده تمام ۱۷ بخش ↗</a>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                {related_cards}
            </div>
        </div>
    </main>

    {floating_btn}
    {footer}

    <script src="assets/js/observatory_core.js"></script>
    {sec_meta['extra_scripts']}
</body>
</html>
"""
    return page_html

# Main execution loop
clean_ranges = {
    "posts": (654, 15849),
    "timeline": (15852, 18879),
    "platforms": (18882, 18965),
    "campaigns": (18968, 19151),
    "critiques": (19155, 19319),
    "news": (19326, 21038),
    "broadcast": (21043, 21213),
    "specs": (21216, 21241),
    "rawpdf": (21244, 21276),
    "faq": (21279, 21387),
    "investigation": (21390, 21477),
    "audio-sentiment": (21485, 22221),
    "influencers": (22224, 25588),
    "production": (25593, 25692),
    "hashtags": (25696, 25929),
    "ai-audit": (25934, 26221),
    "market-guild": (26226, 26369)
}

with open(os.path.join(workspace_dir, "index.html"), "r", encoding="utf-8") as f:
    index_raw = f.read()

lines = index_raw.splitlines(True)

# Generate 17 standalone pages
generated_files = []
for sec_meta in sections_catalog:
    sid = sec_meta["id"]
    start, end = clean_ranges[sid]
    sec_content = "".join(lines[start-1:end])
    page_html = generate_standalone_page(sec_meta, sec_content)
    
    out_path = os.path.join(workspace_dir, sec_meta["file"])
    with open(out_path, "w", encoding="utf-8") as out_f:
        out_f.write(page_html)
    generated_files.append((sec_meta["file"], os.path.getsize(out_path)))

print("Generated standalone pages:")
for fname, fsize in generated_files:
    print(f" - {fname:20}: {fsize:,} bytes")

# Now update index.html
print("Updating index.html with new Header, Mega Menu, Mobile Drawer, Atlas Grid, Tab Banners, and Footer...")

# 1. Replace header
new_header = generate_header("index.html")
new_drawer = generate_mobile_drawer("index.html")
new_floating = generate_floating_menu()
new_footer = generate_footer("index.html")
new_atlas = generate_atlas_grid()

# Replace <header ... </header>
header_pattern = re.compile(r'<header class="fixed inset-x-0 top-0.*?<!-- Header CTA & Actions -->.*?</div>\s*</div>\s*</header>', re.DOTALL)
if header_pattern.search(index_raw):
    index_raw = header_pattern.sub(new_header + "\n" + new_drawer, index_raw, count=1)
    print("Replaced header and added mobile drawer.")
else:
    print("WARNING: Header regex did not match, using fallback replacement.")
    # Fallback: slice before hero
    h_idx = index_raw.find('<header class="fixed')
    hero_idx = index_raw.find('<!-- Hero:')
    if h_idx != -1 and hero_idx != -1:
        index_raw = index_raw[:h_idx] + new_header + "\n" + new_drawer + "\n" + index_raw[hero_idx:]
        print("Replaced header via fallback slicing.")

# 2. Insert Observatory Atlas Grid before #tab-posts
atlas_insert_marker = '<!-- Tab: Posts & Reels (Prioritized Gallery with Covers & Direct Links) -->'
if atlas_insert_marker in index_raw:
    index_raw = index_raw.replace(atlas_insert_marker, new_atlas + "\n\n        " + atlas_insert_marker)
    print("Inserted Observatory Atlas Grid before #tab-posts.")
else:
    tab_posts_marker = '<section id="tab-posts"'
    if tab_posts_marker in index_raw:
        index_raw = index_raw.replace(tab_posts_marker, new_atlas + "\n\n        " + tab_posts_marker)
        print("Inserted Observatory Atlas Grid before tab_posts_marker.")

# 3. Add Quick Banner inside each tab
for s in sections_catalog:
    tab_tag = f'<section id="tab-{s["id"]}"'
    banner_html = f"""
    <div class="glass-panel rounded-xl p-3 px-4 border border-[#e85a2a]/30 bg-gradient-to-r from-[#e85a2a]/15 via-dark-900 to-transparent flex flex-wrap items-center justify-between gap-3 text-xs mb-4">
        <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-[#e85a2a] animate-pulse"></span>
            <span class="text-white/90">شما در حال مشاهده پیش‌نمایش این بخش در صفحه اصلی هستید. برای دسترسی به آدرس مستقیم و اشتراک‌گذاری، صفحه اختصاصی را باز کنید:</span>
        </div>
        <a href="{s['file']}" class="btn-primary px-3.5 py-1.5 text-xs font-bold inline-flex items-center gap-1.5 shadow-sm">
            <span>مشاهده صفحه کامل و اختصاصی ↗</span>
        </a>
    </div>
    """
    # Find section tag and inject banner right after opening tag
    pattern = re.compile(rf'(<section id="tab-{re.escape(s["id"])}"[^>]*>)', re.IGNORECASE)
    if pattern.search(index_raw):
        index_raw = pattern.sub(r'\g<1>' + '\n' + banner_html, index_raw, count=1)

print("Injected tab preview banners into all tabs.")

# 4. Replace footer
footer_pattern = re.compile(r'<!-- Authentic Tehran Auto Plaza Luxury Dark Footer -->.*?</footer>', re.DOTALL)
if footer_pattern.search(index_raw):
    index_raw = footer_pattern.sub(new_footer, index_raw, count=1)
    print("Replaced footer.")
else:
    f_idx = index_raw.find('<footer')
    f_end = index_raw.find('</footer>')
    if f_idx != -1 and f_end != -1:
        index_raw = index_raw[:f_idx] + new_footer + index_raw[f_end+9:]
        print("Replaced footer via fallback.")

# 5. Insert floating menu and observatory_core.js before </body>
if 'assets/js/observatory_core.js' not in index_raw:
    index_raw = index_raw.replace('</body>', f'{new_floating}\n<script src="assets/js/observatory_core.js"></script>\n</body>')
    print("Injected floating button and observatory_core.js.")

# Write updated index.html
with open(os.path.join(workspace_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_raw)
print(f"Updated index.html (size: {os.path.getsize(os.path.join(workspace_dir, 'index.html')):,} bytes).")

# 6. Generate updated sitemap.xml
sitemap_urls = [
    ("https://autoplazaterhan.github.io/", "1.0", "daily"),
]
for s in sections_catalog:
    sitemap_urls.append((f"https://autoplazaterhan.github.io/{s['file']}", "0.9", "weekly"))

sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
for loc, prio, freq in sitemap_urls:
    sitemap_xml += f"""  <url>
    <loc>{loc}</loc>
    <lastmod>2026-11-08</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>
"""
sitemap_xml += "</urlset>\n"

with open(os.path.join(workspace_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

print("Updated sitemap.xml with 18 URLs.")
