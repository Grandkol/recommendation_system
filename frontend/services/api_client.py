"""Stub API client. Returns mock data until the backend is wired up."""
from dataclasses import dataclass


@dataclass
class Track:
    id: int
    title: str
    artist: str
    genre: str
    plays: int


_MOCK_LIBRARY: list[Track] = [
    Track(1, "Bohemian Rhapsody", "Queen", "Rock", 2_500_000_000),
    Track(2, "Blinding Lights", "The Weeknd", "Pop", 4_100_000_000),
    Track(3, "Take Five", "Dave Brubeck", "Jazz", 180_000_000),
    Track(4, "Lose Yourself", "Eminem", "Hip-Hop", 1_400_000_000),
    Track(5, "Smells Like Teen Spirit", "Nirvana", "Rock", 1_700_000_000),
    Track(6, "Levitating", "Dua Lipa", "Pop", 2_000_000_000),
    Track(7, "So What", "Miles Davis", "Jazz", 90_000_000),
    Track(8, "HUMBLE.", "Kendrick Lamar", "Hip-Hop", 1_300_000_000),
    Track(9, "Hotel California", "Eagles", "Rock", 1_500_000_000),
    Track(10, "Shape of You", "Ed Sheeran", "Pop", 5_900_000_000),
    Track(11, "Billie Jean", "Michael Jackson", "Pop", 1_900_000_000),
    Track(12, "Sicko Mode", "Travis Scott", "Hip-Hop", 1_100_000_000),
]


def get_popular(limit: int = 10) -> list[Track]:
    return sorted(_MOCK_LIBRARY, key=lambda t: t.plays, reverse=True)[:limit]


def get_personalized_top(genres: list[str], limit: int = 10) -> list[Track]:
    if not genres:
        return get_popular(limit)
    matches = [t for t in _MOCK_LIBRARY if t.genre in genres]
    return sorted(matches, key=lambda t: t.plays, reverse=True)[:limit]


def search_tracks(query: str) -> list[Track]:
    if not query:
        return []
    q = query.lower()
    return [
        t for t in _MOCK_LIBRARY
        if q in t.title.lower() or q in t.artist.lower()
    ]


def all_genres() -> list[str]:
    return sorted({t.genre for t in _MOCK_LIBRARY})
