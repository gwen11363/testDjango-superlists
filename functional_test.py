from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
#browser.get("http://railway.hinet.net/Foreign/TW/etno_roundtrip.html")

assert 'Django' in browser.title
