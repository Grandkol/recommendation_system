import streamlit as st

from state import init_session_state
from views import home, library, popular, top

PAGES = {
    "home": home.render,
    "top": top.render,
    "popular": popular.render,
    "library": library.render,
}


st.set_page_config(page_title="Music Recommender", page_icon="🎵")
init_session_state()
PAGES[st.session_state["page"]]()
