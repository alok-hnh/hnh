with open('ca/index.html', 'r', encoding='utf-8') as f:
    ca_html = f.read()

with open('usa/index.html', 'r', encoding='utf-8') as f:
    usa_html = f.read()

import re

def get_block(name, html):
    # Find head, body tag, preloader, page-wrapper, scripts
    print(f"\n=== {name} ===")
    
    # Html style
    html_tag = re.search(r'<html[^>]*>', html)
    if html_tag:
        print(f"Html tag: {html_tag.group(0)}")
        
    # Body tag
    body_tag = re.search(r'<body[^>]*>', html)
    if body_tag:
        print(f"Body tag: {body_tag.group(0)}")
        
    # Preloader tag
    preloader_tag = re.search(r'<div[^>]*js-preloader[^>]*>', html)
    if preloader_tag:
        print(f"Preloader: {preloader_tag.group(0)[:150]}...")
    else:
        print("Preloader NOT found!")
        
    # Page wrapper tag
    wrapper_tag = re.search(r'<div[^>]*js-page-wrapper[^>]*>', html)
    if wrapper_tag:
        print(f"Page wrapper: {wrapper_tag.group(0)}")
    else:
        print("Page wrapper NOT found!")
        
    # Scripts at end
    scripts = re.findall(r'<script[^>]*>.*?</script>', html, re.DOTALL)
    print(f"Script count: {len(scripts)}")
    for s in scripts[-3:]:
        print(f"  - {s[:100]}...")

get_block("Canada Index", ca_html)
get_block("USA Index", usa_html)
