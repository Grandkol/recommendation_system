from fastapi import APIRouter, Query

from data import (
    Track,
    all_artists,
    get_personalized_top,
    get_popular,
    search_tracks,
)

router = APIRouter()


@router.get("/popular", response_model=list[Track])
def popular(limit: int = 10) -> list[Track]:
    return get_popular(limit)


@router.get("/top", response_model=list[Track])
def top(
    artists: list[str] = Query(default_factory=list),
    limit: int = 10,
) -> list[Track]:
    return get_personalized_top(artists, limit)


@router.get("/search", response_model=list[Track])
def search(query: str = "") -> list[Track]:
    return search_tracks(query)


@router.get("/artists", response_model=list[str])
def artists() -> list[str]:
    return all_artists()
