from bs4 import BeautifulSoup
from requests import get, post
from threading import Thread

def validate_option(text, options):
    while True:
        option = input(text)
        if option.upper() in options:
            return option.upper()

def validate_ptwikipedia_url():
    while True:
        try:
            url = input("Enter PT-BR Wikipedia URL to be scraped (or leave blank for default URL): ")
            if url.strip():
                if "https://pt.wikipedia.org" not in url:
                    raise ValueError
            else:
                url = "https://pt.wikipedia.org/wiki/Jap%C3%A3o"
            return url
        except ValueError:
            print(f"Please enter a valid PT-BR Wikipedia website URL")

if __name__ == '__main__':
    url = validate_ptwikipedia_url()
    other_languages = False
    message = "Include internal Wikipedia links from languages other than the original page's language? "
    options = ["Y", "N"]
    option = validate_option(message, options)
    if option == "Y":
        other_languages = True
    if option == "N":
        other_languages = False
    response = get(url)
    tags = BeautifulSoup(response.text, "html5lib")
    title = tags.find("title")
    print(f"Página principal: {title.text}")
    external_links = tags.find_all("a", attrs={"class": "external_text"})
    external_links_list = [link["href"] for link in external_links]
    links = tags.find_all("a")
    for link in links:
        try:
            response_i = ""
            if other_languages:
                if (link["href"] not in external_links_list and link["href"][0] != "#"
                    and "//" not in link["href"]):
                    if "https" in link["href"] or "http" in link["href"] :
                        response_i = get(link["href"])
                    else:
                        response_i = get("https://pt.wikipedia.org" + link["href"])
                    tags_i = BeautifulSoup(response_i.text, "html5lib")
                    link_title = tags_i.find("title")
                    print(f"Página secundária: {link_title.text}")
            else:
                if (link["href"] not in external_links_list and link["href"][0] != "#" and
                   "https" not in link["href"] and "http" not in link["href"] and
                   "//" not in link["href"]):
                    response_i = get("https://pt.wikipedia.org" + link["href"])
                    tags_i = BeautifulSoup(response_i.text, "html5lib")
                    link_title = tags_i.find("title")
                    print(f"Página secundária: {link_title.text}")
        except KeyError as e:
            continue
            # print(f"Link reference to the original URL ('href' attribute not found for {link.text})")
        except Exception as e:
            print(f"Encountered an error: {e}")
