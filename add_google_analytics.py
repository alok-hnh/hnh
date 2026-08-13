import os
import re

GA_SNIPPET = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-ZQLC2P562C"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-ZQLC2P562C');
</script>"""

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
folders = [".", "us", "ca", "hk", "in"]
processed_files = []

for folder in folders:
    folder_path = os.path.join(ROOT_DIR, folder)
    if not os.path.exists(folder_path):
        continue
    for f in os.listdir(folder_path):
        if f.endswith(".html"):
            filepath = os.path.join(folder_path, f)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Check if GA is already present
            if "G-ZQLC2P562C" in content:
                print(f"Skipping {f} (already has GA tag)")
                continue
            
            # Insert after <head>
            if "<head>" in content:
                new_content = content.replace("<head>", f"<head>\n{GA_SNIPPET}", 1)
            elif "</head>" in content:
                new_content = content.replace("</head>", f"{GA_SNIPPET}\n</head>", 1)
            else:
                print(f"Warning: No <head> tag found in {filepath}")
                continue
                
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(new_content)
            processed_files.append(filepath)
            print(f"Added GA to {os.path.relpath(filepath, ROOT_DIR)}")

print(f"\nTotal HTML files updated with GA tag: {len(processed_files)}")
