import streamlit as st

from services.api_client import Track


def render_track(track: Track, *, show_like_button: bool = False) -> None:
    cols = st.columns([5, 1])
    with cols[0]:
        st.markdown(f"**{track.title}** · {track.artist}")
        st.caption(f"{track.genre} · {track.plays:,} прослушиваний")
    if show_like_button:
        liked_ids = {t.id for t in st.session_state["liked_tracks"]}
        is_liked = track.id in liked_ids
        with cols[1]:
            if st.button("❤️" if is_liked else "🤍", key=f"like_{track.id}"):
                if is_liked:
                    st.session_state["liked_tracks"] = [
                        t for t in st.session_state["liked_tracks"] if t.id != track.id
                    ]
                else:
                    st.session_state["liked_tracks"].append(track)
                st.rerun()
