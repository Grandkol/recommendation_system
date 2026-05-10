import streamlit as st

from components.music_card import render_track
from services.api_client import search_tracks
from state import go_to


def render() -> None:
    if st.button("← Назад"):
        go_to("home")

    st.title("Моя медиатека")
    st.caption("Добавляй треки, которые нравятся. Так рекомендации станут точнее.")

    query = st.text_input("Найти трек или исполнителя")
    if query:
        results = search_tracks(query)
        if results:
            st.subheader("Результаты поиска")
            for t in results:
                render_track(t, show_like_button=True)
        else:
            st.info("Ничего не нашлось.")

    liked = st.session_state["liked_tracks"]
    st.subheader(f"Понравилось ({len(liked)})")
    if not liked:
        st.caption("Пока пусто. Лайкни что-нибудь, чтобы появилось здесь.")
    else:
        for t in liked:
            render_track(t)
