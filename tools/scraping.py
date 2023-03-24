from urllib.request import Request
from bs4 import BeautifulSoup
import settings as s
import pdb


def parsing_request(request_object: Request) -> BeautifulSoup:
    return BeautifulSoup(request_object.text, "html.parser")


def generate_url_next_page(url: str, page=1) -> str:
    if int(page) <= 1:
        return url[:34]
    page = str(page)
    return url[:34] + "/page/" + page


def get_news_tasmania(soup: BeautifulSoup) -> dict:
    list_news = soup.find_all("div", class_="blog-post-card__info")
    title_list = [a.find("a") for a in list_news]
    return {t_new.text: s.ROOT_URL +
                t_new.get('href') for t_new in title_list}
 

def get_last_news_tasmania(soup: BeautifulSoup):
    list_news = soup.find_all("div", class_="blog-post-card__info")
    title_list = list_news[0].find("a")
    return {title_list.text: s.ROOT_URL + title_list.get('href')}
    