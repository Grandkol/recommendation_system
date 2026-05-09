import streamlit as st


if "page" not in st.session_state:
    st.session_state["page"] = "home"

# ── Роутер — решает какую страницу показать ──────────────────────
page = st.session_state["page"]

def show_home():
    st.title("Что ищем сегодня?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎬 Фильмы", use_container_width=True):
            st.session_state["page"] = "movies"
            st.rerun()   # перезапускаем скрипт — роутер покажет нужную страницу

    with col2:
        if st.button("🎮 Игры", use_container_width=True):
            st.session_state["page"] = "games"
            st.rerun()


def show_games():
    if st.button("← Назад"):
        st.session_state["page"] = "home"
        st.rerun()

    st.title("Найти игру")

    with st.form("game_form"):
        genre = st.selectbox("Жанр", ["RPG", "Shooter", "Strategy", "Indie"])
        platform = st.multiselect("Платформа", ["PC", "PlayStation", "Xbox", "Switch"])
        max_price = st.slider("Максимальная цена ($)", 0, 70, 30)
        min_score = st.slider("Минимальный Metacritic", 50, 100, 70)
        submitted = st.form_submit_button("🔍 Найти игры")

    # if submitted:
    #     with st.spinner("Подбираем игры..."):
    #         resp = requests.post(f"{API}/recommend/games", json={
    #             "genre":     genre,
    #             "platforms": platform,
    #             "max_price": max_price,
    #             "min_score": min_score,
    #         })
    #
    #     if resp.status_code == 200:
    #         games = resp.json()["results"]
    #         show_results(games, kind="game")
    #     else:
    #         st.error("Что-то пошло не так. Попробуй ещё раз.")


if page == "home":
    show_home()
elif page == "movies":
    show_movies()
elif page == "games":
    show_games()