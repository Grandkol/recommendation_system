import streamlit as st


def init_session_state() -> None:
    st.session_state.setdefault("page", "home")
    st.session_state.setdefault("liked_tracks", [])


def go_to(page: str) -> None:
    st.session_state["page"] = page
    st.rerun()
