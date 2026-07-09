# Harbour & Hills Design System

This document outlines the visual tokens, typography, grid specifications, and animation patterns extracted from the live site, to be used consistently across all location pages.

## 🎨 Color Palette

*   **Background / Base Dark:** `bg-darkGray` (`#0c0f19`)
*   **Accent Color:** `bg-green` / `text-green` (`#00d97e`) — used for interactive icons, hover states, menu pills, and locations indicators.
*   **Text Colors:**
    *   Primary Light: `text-white` (`#ffffff`)
    *   Primary Dark: `text-charcoal` (`#0c0f19` or `#0c0f19`)
    *   Muted Mids: `text-gray` / `text-mediumGrey` (`#707070` or `#8e8e8e`)
*   **Borders / Dividers:** `border-gray` / `border-mediumGrey` (subtle separators)

## 🔤 Typography

*   **Display Font:** `Inter` (Sans-serif)
    *   Main Headlines: `text-h1` / `text-4xl md:text-6xl tracking-tighter leading-none`
    *   Subheadings: `text-big` / `text-gray`
*   **Body Font:** `Inter` (Sans-serif)
    *   Text paragraphs: `text-base text-gray leading-relaxed max-w-[65ch]`

## 📏 Layout & Spacing

*   **Guttters:** `page-margin` (responsive inline padding matching the brand design)
*   **Containers:** `content-wrapper js-content-wrapper` (padded-top container to clear the fixed header)
*   **Grids:** Responsive CSS grids with tailwind columns:
    *   Desktop standard: `grid grid-cols-12 gap-x-8 gap-y-8`
    *   Mobile: collapse to single columns (`col-span-12`)

## 🎬 Animation Specifications

*   **Smooth Scroll:** Powered by `Lenis` (Smooth scroll library).
*   **Text & Element Reveal:** Staggered fade, vertical translation, and blur reveals powered by `Anime.js` (staggered delay, `opacity: [0, 1]`, `top: ['1rem', '0']`, `filter: ['blur(5px)', 'blur(0px)']`).
*   **Hover Interaction:** Dynamic background transitions with `transition-all duration-300 ease-custom`.
*   **Location / Transition Hooks:** Barba-like transition schemes for page-swapping when navigating locations.
