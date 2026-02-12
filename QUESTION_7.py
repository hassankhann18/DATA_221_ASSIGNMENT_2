# NAME: HASSAN ADNAN
# UCID: 30217418
# QUESTION 7

import requests
from bs4 import BeautifulSoup

def main():
    url = "https://en.wikipedia.org/wiki/Data_science"

    #page_html = requests.get(url).text
    response = requests.get(url)
    page_html = response.text

    soup = BeautifulSoup(page_html, "html.parser")

    title_tag = soup.find("title")

    if title_tag is not None:
        print("Page Title: ", title_tag.text.strip())
    else:
        print("Page Title: Not Found")

    #content_div = soup.find("div", id = "mw-content-text")
    content_div = soup.find("div", id="mw-content-text")
    if content_div is None:
        print("Content not found")
        return

    paragraphs = content_div.find_all("p")

    first_good_paragraph = None
    for p in paragraphs:
        text = p.get_text().strip()
        text_no_spaces = "".join(text.split())
        if len(text_no_spaces) >= 50:
            first_good_paragraph = text
            break

    if first_good_paragraph is None:
        print(" No Paragraph with at least 50 characters was found. ")
    else:
        print(" Paragraph with at least 50 characters was found. ")
        print(first_good_paragraph)

if __name__ == "__main__":
    main()



