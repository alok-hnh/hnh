import re

GA_SNIPPET = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-ZQLC2P562C"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-ZQLC2P562C');
</script>"""

FILES = [
    "index.html",
    "us/index.html", "us/about.html", "us/contact.html", "us/services.html", "us/why-hh.html",
    "ca/index.html", "ca/about.html", "ca/contact.html", "ca/services.html", "ca/why-hh.html",
    "hk/index.html", "hk/about.html", "hk/contact.html", "hk/csr.html", "hk/index-alt.html", "hk/privacy-policy.html", "hk/services.html", "hk/why-hh.html",
    "in/index.html", "in/about.html", "in/contact.html", "in/services.html", "in/why-hh.html"
]

for f in FILES:
    try:
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
        if "G-ZQLC2P562C" not in content:
            if "<head>" in content:
                content = content.replace("<head>", f"<head>\n{GA_SNIPPET}", 1)
            elif "</head>" in content:
                content = content.replace("</head>", f"{GA_SNIPPET}\n</head>", 1)
            with open(f, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"Updated {f}")
        else:
            print(f"Already contains GA: {f}")
    except Exception as e:
        print(f"Error on {f}: {e}")
