import os
import re
import sys

def validate_html_page(filepath, is_homepage=False):
    if not os.path.exists(filepath):
        print(f"Error: {filepath} does not exist!")
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Strip speculationrules scripts to prevent false positives
    content = re.sub(r'<script type="speculationrules">.*?</script>', '', content, flags=re.DOTALL)
    
    errors = []
    
    # 1. Preloader check
    has_preloader = 'js-preloader' in content
    if is_homepage and not has_preloader:
        errors.append("Homepage index.html must contain the preloader container HTML (js-preloader).")
    elif not is_homepage and has_preloader:
        errors.append("Inner page must NOT contain the preloader container HTML (js-preloader).")
        
    # 2. WP content uploads check
    wp_uploads = re.findall(r'wp-content/uploads', content)
    if wp_uploads:
        errors.append(f"Found {len(wp_uploads)} absolute WordPress upload links.")
        
    # 3. Year/Month subdirectories check
    year_month = re.findall(r'\.\./assets/images/20\d\d/\d\d?/', content)
    if year_month:
        errors.append(f"Found {len(year_month)} image paths with year/month subdirectories.")
        
    # 4. Obfuscated Cloudflare emails
    cf_emails = re.findall(r'email-protection', content)
    if cf_emails:
        errors.append(f"Found {len(cf_emails)} Cloudflare email obfuscation tags.")
        
    # 5. Correct scripts check
    main_js_ref = '../assets/js/main.js' in content or 'assets/js/main.js' in content
    if not main_js_ref:
        errors.append("Missing reference to main.js.")
        
    globals_block = 'window.wpcf7_recaptcha' in content
    if not globals_block:
        errors.append("Missing WordPress globals script block.")
        
    grecaptcha_mock = 'window.grecaptcha' in content or 'grecaptcha.execute' in content
    if not grecaptcha_mock:
        errors.append("Missing grecaptcha mock in WordPress script block.")
        
    # 6. Dropdown location link check
    is_hk_file = 'hk/' in filepath.replace('\\', '/')
    is_in_file = 'in/' in filepath.replace('\\', '/')
    
    has_hk_link = 'hk/index.html' in content or '../hk/index.html' in content or (is_hk_file and 'index.html' in content)
    has_in_link = 'in/index.html' in content or '../in/index.html' in content or (is_in_file and 'index.html' in content)
    
    if not has_hk_link:
        errors.append("Missing location link to Hong Kong (hk/index.html or relative).")
    if not has_in_link:
        errors.append("Missing location link to India (in/index.html or relative).")
        
    # Check if there are external links to self page that should be relative
    self_links = re.findall(r'href="https://(?:www\.)?harbourandhills\.com/(?:usa|hk|in)/[^"]+"', content)
    if self_links:
         print(f"Info: Found {len(self_links)} self-referencing absolute link tags in body/nav.")
         
    if errors:
        print(f"Validation FAILED for {filepath}:")
        for err in errors:
            print(f"  - [ ] {err}")
        return False
    else:
        print(f"Validation PASSED for {filepath}!")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 validate_page.py <filepath> [--homepage]")
        sys.exit(1)
        
    path = sys.argv[1]
    is_home = "--homepage" in sys.argv
    validate_html_page(path, is_home)
