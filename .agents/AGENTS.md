# Workspace Rules: Static Page Cloning Workflow & Guidelines

When cloning live pages (e.g. from `harbourandhills.com`) into the regional subfolders (`us/`, `hk/`, `in/`, `ca/`), follow these exact rules to ensure pages load successfully and match the live layout:

## 1. Bypassing Geo-IP Redirection
- Live URLs automatically redirect to regional folders based on IP.
- Always use the built-in `read_url_content` tool to fetch pages (as it executes from US servers and bypasses redirections). 
- Avoid using `curl` or proxy APIs locally as they are frequently blocked by Cloudflare (returning 522/connection errors).

## 2. Asset Path Localization
- Replace absolute WordPress upload links (`https://harbourandhills.com/wp-content/uploads/`) with relative paths to the assets folder (e.g., `../assets/images/`).
- **CRITICAL (Stalled Preloader Fix)**: Use regex in Python to strip any leftover year/month subdirectories (e.g. `2026/05/`, `2025/10/`) from image paths:
  ```python
  content = re.sub(r'\.\./assets/images/20\d\d/\d\d?/', '../assets/images/', content)
  ```
  If any images in the hidden preloader image cache list (`fixed -z-[9999]`) return a 404 error, the page preloader script will stall, leaving the page completely blank/black.

## 3. Required Stylesheets & Scripts
- Link stylesheets to `../assets/css/style.css`.
- Load the main script at the bottom: `<script src="../assets/js/main.js" defer></script>`.
- **CRITICAL (Prevent JS Crashes)**: Do **NOT** remove the inline script block defining the WordPress globals (`window.wp`, `window.wpcf7`, `window.wpcf7_recaptcha`) immediately preceding `main.js`:
  ```html
  <script>
    window.wp = { i18n: { __: function(str) { return str; }, setLocaleData: function() {} } };
    window.wpcf7 = { api: { root: "", namespace: "contact-form-7/v1" }, schemas: new Map() };
    window.wpcf7_recaptcha = { sitekey: "", actions: { homepage: "homepage", contactform: "contactform" } };
    // Mock grecaptcha to prevent main.js from crashing on static versions
    window.grecaptcha = {
      ready: function(cb) { cb(); },
      execute: function() { return Promise.resolve('mock-token'); }
    };
  </script>
  ```
  The preloader fade-out relies on `main.js` running without errors. If these global variables are missing, a ReferenceError exception is thrown, halting Javascript execution and freezing the preloader on screen.

## 4. Link & Email Formatting
- Replace all absolute domain links with relative ones (e.g. `https://www.harbourandhills.com/usa/about/` -> `about.html`).
- Ensure all regional redirects in the header location dropdown point to the correct relative paths (e.g. Hong Kong -> `../hk/index.html`, India -> `../in/index.html`).
- Decode any Cloudflare email obfuscation (`/cdn-cgi/l/email-protection`) into standard decoded `mailto:` links.

## 5. No Preloader on Inner Pages
- For all inner/inside pages (i.e. all pages except the homepage `index.html`), the **preloader HTML container** must be deleted.
- Specifically, remove:
  1. The preloader block: `<div class="fixed top-0 left-0 w-full h-[100dvh] js-preloader js-hnh-preloader ..."> ... </div>`.
  2. The hidden image preload block: `<div class="fixed -z-[9999] invisible bottom-0 left-0 bg-[red] ..."> ... </div>`.
- Do **NOT** remove the inline CSS style on the `<html>` tag (`style="overflow: hidden; pointer-events: none;"`) or the page-wrapper container (`style="visibility: hidden;"`). The main JS file (`main.js`) will detect that the preloader is absent, and dynamically clean up those styles to display the page instantly and trigger any enter transitions.

## 6. No Automatic Browser Subagent Testing
- Do **NOT** use the `browser_subagent` tool for automatic testing, screenshot capture, or console checking of layouts and pages.
- The user will perform all browser-side testing manually.
- Rely on verification scripts (such as tag checkers and link analyzers run via python command) to validate changes instead.


