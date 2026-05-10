import streamlit as st

from components.music_card import render_track
from services.api_client import get_popular
from state import go_to


def render() -> None:
    if st.button("← Назад"):
        go_to("home")

    st.title("Популярное прямо сейчас")
    for t in get_popular(10):
        render_track(t, show_like_button=True)
