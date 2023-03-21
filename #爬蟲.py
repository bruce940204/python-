#爬蟲
#原始網頁碼(html)
import urllib.request as req
url="https://university-tw.ldkrsi.men/caac/050/"
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"})
with req.urlopen(request) as response:
    date=response.read().decode("utf-8")
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
print(root.td)























