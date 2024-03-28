from typing import TypedDict, Literal


class AnimeI(TypedDict):
    title: str
    start_date: str
    url: str
    image: str
    tag: Literal[
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Unknown",
    ]


class NewSeasonAnimeI(TypedDict):
    title: str
    start_date: str
    url: str
    image: str
