# DESIGN.md: Tehran Auto Plaza (اتو پلازا تهران)
> Visual Identity & Anti-Slop Specification for `autoplazaterhan.github.io`
> Synchronized directly with official brand identity from `https://autoplaza.ir/`

---

## 1. Project Identity & Soul

- **Brand:** اتو پلازا تهران (Tehran Auto Plaza)
- **Scale:** ۸۵٬۰۰۰ مترمربع وسعت، ۹۰ شوروم تخصصی، ۳٬۰۰۰ ظرفیت پارکینگ
- **Location:** تهران، کیلومتر ۱۱ بزرگراه لشگری (جاده مخصوص کرج)، نبش خیابان ۳۰
- **Nature of Interface:** رصدخانه جامع داده‌کاوی، تحلیل رسانه‌ای و پایش ۳۶۰ درجه کلان‌پروژه اتوپلازا تهران (۵۵ پست رسمی، ۵۸ اینفلوئنسر تخصصی خودرو، ۱۳۷ توییت نقادانه شبکه X، تلگرام، تحلیل سند رسمی هوش مصنوعی دیتاک و پایش اختصاصی BoxAPI).
- **Official Brand URLs:**
  - وب‌سایت اصلی: [autoplaza.ir](https://autoplaza.ir/)
  - سوپراپلیکیشن: [app.autoplaza.ir](https://app.autoplaza.ir/)
  - اینستاگرام رسمی: [@tehranautoplaza](https://www.instagram.com/tehranautoplaza/)

---

## 2. Anti-Slop Dials

- **ENERGY: 2** (Confident, focused, luxury automotive engineering; sharp contrast, authoritative telemetry, zero generic decorative fluff).
- **RHYTHM: 2** (Varied density: high-density data matrices and telemetry feeds alongside expansive architectural imagery and readable dossier text).
- **MOTION: 1** (Subtle, purposeful transitions: 200ms to 300ms cubic-bezier; no gratuitous endless floating, shaking, or bouncing).

---

## 3. Visual Identity (autoplaza.ir Synchronization)

### 3.1 Color Palette
Strict 3 core colors + 1 accent rule (anti-slop R-29):

- **Core 1 (Background):**
  - `--background: #000000;` (Pure deep automotive black)
  - `--surface-1: #0a0a0a;` (First elevation)
  - `--surface-2: #121214;` (Card base and container background)
- **Core 2 (Typography & Lines):**
  - Text Primary: `#ffffff` (Headings, primary metrics)
  - Text Body: `#f5f5f5` & `rgba(255, 255, 255, 0.85)`
  - Text Muted: `rgba(255, 255, 255, 0.55)`
  - Border Lines: `rgba(255, 255, 255, 0.10)` (Architectural clean grid)
- **Core 3 (AutoPlaza Brand Orange):**
  - `--orange: #e85a2a;` (Primary brand accent from autoplaza.ir)
  - `--orange-deep: #d44a1c;` (Hover and interactive active states)
  - `--orange-glow: #ff6b35;` (Single deliberate focal point accent)
- **Deliberate Accents (Semantic):**
  - Alert / High-Urgency Critique: `#fb2c36` (Red 500)
  - Live Telemetry / Verification: `#10b981` (Emerald 500)

### 3.2 Typography & Fonts
- **Primary Brand Font:** `RaviFaNum` (Official brand font of `autoplaza.ir`, self-hosted in `assets/fonts/`).
  - Native Persian numerals (`۰-۹`) built into glyphs.
  - Weights loaded: Thin (100), Light (300), Regular (400), Medium (500), SemiBold (600), Bold (700), Black (900), ExtraBlack (950).
- **Secondary Fallback:** `Vazirmatn`, `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`.
- **Tracking:** Strictly `letter-spacing: 0 !important;` (Persian typography standard).
- **Direction & Alignment:** Strict RTL (`dir="rtl"`), logical CSS classes (`start`, `end`, `ms-`, `me-`, `ps-`, `pe-`).

### 3.3 Brand Assets & Logos
- **Emblem Icon:** `assets/apz1.png` (Geometric AutoPlaza crest).
- **Logotype Script:** `assets/apz2-light.png` ("اتو پلازا تهران" official wordmark).
- **Architectural Photography:** `assets/hero-plaza.jpg`, `assets/intro.jpg`, `assets/experience-2.jpg`.
- **Official Marquee Ticker:**
  `AUTOMOTIVE DESTINATION مقصد جامع خودرو TEHRAN AUTO PLAZA ۹۰ شوروم COMING SOON ۸۵٬۰۰۰ مترمربع`

---

## 4. Anti-Slop Rule Enforcements (miqdadbadjuber/anti-slop)

1. **R-01 (No Generic Gradients):** Zero blue-to-purple, cyan, or pastel orb gradients. Palette is 100% anchored in AutoPlaza automotive black and brand orange `#e85a2a`.
2. **R-05 & C-3 (Content-Driven Architecture):** No generic hero-cards template. Layout is shaped strictly around the 13 specialized intelligence domains of Tehran Auto Plaza.
3. **R-08 (No Decorative Arrows):** Arrows reserved strictly for actionable navigation and external link hops.
4. **R-09 & R-16 (Zero AI Buzzwords & Capsule Badges):** No "AI Powered", "Revolutionary", "Cutting-edge", or "Next-Gen" vanity pills. Every metric is real (55 posts, 58 influencers, 137 tweets, Datak PDF, BoxAPI telemetry).
5. **R-10 (Glassmorphism Dose Cap):** Glass blur restricted to fixed header and sticky tab bar. Content cards remain solid dark surfaces (`#0a0a0a` / `#121214`) for sharp contrast and legibility.
6. **R-11 (Corner Radius Variety):** Rounded-full strictly for circular counters and main CTA buttons; rounded-xl and rounded-2xl for content containers; rounded-md for status badges.
7. **R-12 & R-13 (Restrained Elevation & Glow):** Glow capped at single focal telemetry indicators.
8. **R-20 (Brand Identity Test):** Completely unique to Tehran Auto Plaza.
9. **Zero Emojis in UI:** UI iconography is 100% SVG line icons or numeric tags. No cartoonish emojis in UI elements.
10. **Zero Em-Dash:** Complete prohibition of the em-dash character (`-`) across all copy.

---

## 5. Delivery Gate Checklist

- [x] Block 1: Hard Gate (contrast verified, no broken states, real data only).
- [x] Block 2: Purpose-Gate (every style decision serves identity or readability).
- [x] Block 3: Liveliness (ENERGY 2 / RHYTHM 2 / MOTION 1, RaviFaNum font, brand marquee ticker, authentic assets).
- [x] Block 4: Craftsmanship & Quality Locks (VibeFarsi RTL, Persian digits, zero em-dash, zero UI emojis).
