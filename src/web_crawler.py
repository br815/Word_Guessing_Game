import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def web_crawler(url, depth=1, visited=set()):
    if depth == 0 or url in visited:
        return

    visited.add(url)

    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text()

    # save text
    with open(f"texts/{hash(url)}.txt", "w", encoding="utf-8") as f:
        f.write(text)

    # follow links
    for link in soup.find_all("a", href=True):
        next_url = urljoin(url, link["href"])
        web_crawler(next_url, depth - 1, visited)
# End of web_crawler()


#def text_scraper()





#def text_cleaner()