import streamlit as st

from state import go_to


def render() -> None:
    st.title("🎵 Что послушаем?")
    st.caption("Выбери, что тебе сейчас интересно.")

    if st.button("Топ песен для меня", use_container_width=True):
        go_to("top")
    if st.button("Популярное в мире сейчас", use_container_width=True):
        go_to("popular")
    if st.button("Моя медиатека", use_container_width=True):
        go_to("library")
