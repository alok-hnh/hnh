with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

lines = js.split('\n')
for idx, line in enumerate(lines):
    if 'grecaptcha' in line:
        print(f"Line {idx+1} contains grecaptcha:")
        print(line[:500] + "...")
