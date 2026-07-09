import re

with open('hk/about.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find the <body> tag and print everything around it
body_match = re.search(r'<body.*?(?:<main|<div class="page-wrapper)', content, re.DOTALL | re.IGNORECASE)
if body_match:
    print("Found around body:")
    print(body_match.group(0))
else:
    # Just print from body to 500 characters
    body_idx = content.find('<body')
    if body_idx != -1:
        print("From <body> onwards:")
        print(content[body_idx:body_idx+800])
    else:
        print("<body> tag not found!")
