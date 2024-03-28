import os
import json
from scraper import NewSeasonScraper
from typing import List
from interfaces import AnimeI


class WatchList:
    def __init__(self):
        self.path = "database/anime_list.json"
        self.anime_list: List[AnimeI] = []

    def create_anime_list(self):
        with open(self.path, "w") as file:
            json.dump(self.anime_list, file)

    def read_anime_list(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as file:
                self.anime_list = json.load(file)
        else:
            self.create_anime_list()
            with open(self.path, "r") as file:
                self.new_season = json.load(file)

    def add_anime(self, anime: AnimeI):
        self.anime_list.append(anime)
        self.create_anime_list()

    def remove_anime(self, anime_title: str):
        self.anime_list = [
            anime for anime in self.anime_list if anime["title"] != anime_title
        ]
        self.create_anime_list()

    def update_anime(self, anime_title: str, new_data: AnimeI):
        for anime in self.anime_list:
            if anime["title"] == anime_title:
                anime.update(new_data)
                break

        self.create_anime_list()


class NewSeason:
    def __init__(self):
        self.path = "database/new_season.json"
        self.new_season = NewSeasonScraper().new_season

    def create_new_season(self):
        with open(self.path, "w") as file:
            json.dump(self.new_season, file)

    def update_new_season(self):
        self.new_season = NewSeasonScraper().get_new_season()
        self.create_new_season()

    def read_new_season(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as file:
                self.new_season = json.load(file)
        else:
            self.update_new_season()
            with open(self.path, "r") as file:
                self.new_season = json.load(file)

    def remove_anime(self, anime_title: str):
        self.new_season = [
            anime for anime in self.new_season if anime["title"] != anime_title
        ]
        self.create_new_season()
