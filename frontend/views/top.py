import streamlit as st

from components.music_card import render_track
from services.api_client import all_genres, get_personalized_top
from state import go_to


def render() -> None:
    if st.button("← Назад"):
        go_to("home")

    st.title("Топ для тебя")
    st.caption("Подбираем треки под твои предпочтения.")

    with st.form("top_form"):
        genres = st.multiselect("Любимые жанры", all_genres())
        limit = st.slider("Сколько треков показать", 5, 20, 10)
        submitted = st.form_submit_button("Подобрать")

    if submitted:
        tracks = get_personalized_top(genres, limit)
        if not tracks:
            st.info("По выбранным жанрам ничего не нашлось.")
            return
        for t in tracks:
            render_track(t, show_like_button=True)
