# NAME: HASSAN ADNAN
# UCID: 30217418
# QUESTION 8

import requests
from bs4 import BeautifulSoup

def main():
    url = "https://en.wikipedia.org/wiki/Data_science"

    page_html = requests.get(url).text
    soup = BeautifulSoup(page_html, "html.parser")

    content_div = soup.find("div", id = "mw-content-text")
    if content_div is None:
        print("No content found")
        return
    all_h2_tags = content_div.find_all("h2")

    banned_words = ["References", "External Links", "See also", "Notes"]
    headings = []



