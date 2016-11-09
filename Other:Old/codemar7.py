import requests

page = requests.get("https://github.com/presnick/runestone")
print page.text[:1000]
