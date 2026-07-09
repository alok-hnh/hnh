import os
import glob

js_files = glob.glob('assets/js/**/*.js', recursive=True)
print(f"Searching {len(js_files)} JS files in assets/js/ for 'grecaptcha':")

for path in js_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'grecaptcha' in content:
        print(f"  - Found in {path}!")
    else:
        print(f"  - Not found in {path}")
