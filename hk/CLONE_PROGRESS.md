# Clone Project Progress Context

This document tracks the migration of the Harbour & Hills website from a WordPress CMS into a static HTML/CSS/JS architecture. 

## Locations & Pages Roadmap

### 1. Hong Kong (hk)
*   [x] **Homepage (index.html):** Completed
*   [x] **Homepage Alternate (index-alt.html):** Completed (Alternate Lottie map hero)
*   [x] **About Page (about.html):** Completed
*   [x] **Services Page (services.html):** Completed
*   [x] **Why Choose H&H Page (why-hh.html):** Completed
*   [x] **CSR Page (csr.html):** Completed
*   [x] **Contact Page (contact.html):** Completed
*   [x] **Privacy Policy Page (privacy-policy.html):** Completed









### 2. India (in)
*   [x] Homepage: Completed
*   [x] **About Page (about.html):** Completed
*   [x] **Why Choose H&H Page (why-hh.html):** Completed
*   [x] **Services Page (services.html):** Completed
*   [x] **Contact Page (contact.html):** Completed

### 3. USA (usa)
*   [x] **Homepage (index.html):** Completed
*   [x] **About Page (about.html):** Completed
*   [x] **Services Page (services.html):** Completed
*   [ ] **Why Choose H&H Page (why-hh.html):** Pending
*   [ ] **Contact Page (contact.html):** Pending

### 4. Canada (ca)
*   [ ] Homepage: Pending
*   [x] **About Page (about.html):** Completed
*   [x] **Services Page (services.html):** Completed
*   [x] **Why Choose H&H Page (why-hh.html):** Completed

---

## Technical Context & Integration Notes
*   **Design Variance:** 7/10
*   **Motion Intensity:** 7/10
*   **Visual Density:** 4/10
*   **Fonts:** Inter Display (loaded via Google Fonts CSS link / local assets)
*   **Frameworks:** Lenis (smooth scroll), Swiper (sliders), Anime.js (reveals & transitions), Barba.js (page loads)
*   **Structure:** `/assets/css/`, `/assets/js/`, `/assets/images/`, `/assets/fonts/`

## Recent Fixes & Updates
*   **Animating Orb Transparency (HK):** Fixed the faint square outline and circular background projection in `hk/index.html` by smoothing image alpha boundaries (`vision-circle.png` / `vision-face.png`) and changing the `js-vision-light` radial-gradient outer color to `#000000 100%`.
*   **India Homepage Layout Alignment:** Removed the extra "One World, One Money" and "Artificial Intelligence" sections from `in/index.html`, cleaned the footer to display only the India address, and removed the "CSR" menu link and H-Intelligence Login button/menu to align the header content and div nesting alignment exactly with the live production site.
*   **Restored Missing Video Asset:** Downloaded and linked `bg-video-india.mp4` to the shared `assets/images/` folder to support the KPO/BPO section's video background.
