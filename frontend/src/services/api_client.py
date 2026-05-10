from dataclasses import dataclass

import requests

from config import settings

API_BASE_URL = settings.backend_url
_TIMEOUT = settings.request_timeout


@dataclass
class Track:
    id: int
    title: str
    artist: str
    album: str
    plays: int
    explicit: bool


def _to_track(d: dict) -> Track:
    return Track(
        id=d["id"],
        title=d["title"],
        artist=d["artist"],
        album=d["album"],
        plays=d["plays"],
        explicit=d["explicit"],
    )


def get_popular(limit: int = 10) -> list[Track]:
    r = requests.get(
        f"{API_BASE_URL}/popular", params={"limit": limit}, timeout=_TIMEOUT
    )
    r.raise_for_status()
    return [_to_track(t) for t in r.json()]


def get_personalized_top(artists: list[str], limit: int = 10) -> list[Track]:
    r = requests.get(
        f"{API_BASE_URL}/top",
        params={"artists": artists, "limit": limit},
        timeout=_TIMEOUT,
    )
    r.raise_for_status()
    return [_to_track(t) for t in r.json()]


def search_tracks(query: str) -> list[Track]:
    if not query:
        return []
    r = requests.get(
        f"{API_BASE_URL}/search", params={"query": query}, timeout=_TIMEOUT
    )
    r.raise_for_status()
    return [_to_track(t) for t in r.json()]


def all_artists() -> list[str]:
    r = requests.get(f"{API_BASE_URL}/artists", timeout=_TIMEOUT)
    r.raise_for_status()
    return r.json()
