import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any


class NewSeasonScraper:
    def __init__(self):
        self.url = "https://myanimelist.net/anime/season"
        self.new_season: List[Dict[str, Any]] = []

    # fetches the MAL Seasonal Anime page
    def fetch(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            return response.text
        else:
            return "Error fetching page"

    # formats the anime data into a dictionary
    def anime_formatter(self, anime: Any):
        date = anime.find("span", {"class": "js-start_date"}).text[4:]
        formatted_date = f"{date[2:]}/{date[:2]}"

        img = anime.find("div", {"class": "image"}).a.img
        img_src = img["src"] if img and "src" in img.attrs else img["data-src"]

        return {
            "title": anime.find("span", {"class": "js-title"}).text,
            "start_date": formatted_date,
            "url": anime.find("div", {"class": "image"}).a["href"],
            "image": img_src,
        }

    # scrapes the MAL Seasonal Anime page and returns a list of anime
    def get_new_season(self):
        soup = BeautifulSoup(self.fetch(), "html.parser")

        season: List[Dict[str, Any]] = []

        for anime in soup.find_all(
            "div",
            {
                "class": "js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1"
            },
        ):
            gay = bool(anime.find("span", {"class": "genre"}, text={"Boys Love"}))

            if not gay:
                a = self.anime_formatter(anime)
                season.append(a)

        self.new_season = sorted(season, key=lambda anime: anime["start_date"])

        return self.new_season
