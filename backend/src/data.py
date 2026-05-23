import pandas as pd
from pydantic import BaseModel

from config import settings

#TODO будет для фильмов, игр, так что затем вынесу в models папку.
class Track(BaseModel):
    id: int
    title: str
    artist: str
    album: str
    plays: int
    explicit: bool


def load_library() -> list[Track]:
    df = pd.read_csv(settings.resolved_csv_path(), encoding="ISO-8859-1", thousands=",")
    df = df.dropna(subset=["Track", "Artist", "Spotify Streams"]).reset_index(drop=True)
    df["Album Name"] = df["Album Name"].fillna("")
    df["Explicit Track"] = df["Explicit Track"].fillna(0).astype(int).astype(bool)

    return [
        Track(
            id=i + 1,
            title=str(row["Track"]),
            artist=str(row["Artist"]),
            album=str(row["Album Name"]),
            plays=int(row["Spotify Streams"]),
            explicit=bool(row["Explicit Track"]),
        )
        for i, row in df.iterrows()
    ]

def get_popular(limit: int = 10) -> list[Track]:
    return sorted(load_library(), key=lambda t: t.plays, reverse=True)[:limit]


def get_personalized_top(artists: list[str], limit: int = 10) -> list[Track]:
    if not artists:
        return get_popular(limit)
    matches = [t for t in load_library() if t.artist in artists]
    return sorted(matches, key=lambda t: t.plays, reverse=True)[:limit]


def search_tracks(query: str) -> list[Track]:
    if not query:
        return []
    q = query.lower()
    return [t for t in load_library() if q in t.title.lower() or q in t.artist.lower()]


def  all_artists(limit: int = 200) -> list[str]:
    by_plays: dict[str, int] = {}
    for t in load_library():
        by_plays[t.artist] = by_plays.get(t.artist, 0) + t.plays
    ranked = sorted(by_plays.items(), key=lambda kv: kv[1], reverse=True)
    return [a for a, _ in ranked[:limit]]
