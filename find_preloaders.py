import os
import glob

html_files = glob.glob('in/*.html') + glob.glob('hk/*.html')

print(f"Checking {len(html_files)} regional html files:")
for path in html_files:
    # Skip index.html since it is the homepage
    if os.path.basename(path) == 'index.html':
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    has_preloader = 'js-preloader' in content
    # Check if html tag has overflow: hidden
    has_hidden = 'overflow: hidden' in content
    # Check if page-wrapper has visibility: hidden
    has_visibility = 'visibility: hidden' in content
    
    print(f"  - {path}: has_preloader={has_preloader}, has_hidden={has_hidden}, has_visibility={has_visibility}")
