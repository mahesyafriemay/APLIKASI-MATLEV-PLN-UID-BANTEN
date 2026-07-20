"""
Komponen UI bersama untuk SIMONA.

Prinsip desain: HANYA menyuntikkan <style> CSS murni lewat st.markdown — TIDAK
membuat elemen HTML struktural baru (tidak ada <div> custom, tidak ada kartu
HTML manual, dst). Semua layout tetap pakai komponen native Streamlit
(st.image, st.columns, st.container(border=True), st.title, dst), lalu
dipercantik dengan CSS yang menarget elemen bawaan Streamlit.

Ini jalan tengah antara "polos banget" dan "HTML custom yang berisiko" —
CSS murni jauh lebih kecil kemungkinan bentrok dengan React/JS Streamlit
dibanding menyuntik struktur HTML baru.
"""

import streamlit as st
from pathlib import Path

ASSETS_DIR = Path(__file__).parent / "assets"


def get_favicon():
    path = ASSETS_DIR / "logo_pln.png"
    return str(path) if path.exists() else None


def inject_style():
    """CSS murni saja — tidak ada elemen HTML lain yang disuntikkan."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&family=Inter:wght@400;500;600&display=swap');

        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
        h1, h2, h3, h4 { font-family: 'Plus Jakarta Sans', sans-serif !important; }

        /* gambar (logo, foto hero) dikasih sudut membulat halus */
        [data-testid="stImage"] img { border-radius: 12px; }

        /* metric card lebih rapi */
        div[data-testid="stMetric"] {
            background: #F7F9FC; border-radius: 12px; padding: 14px 16px;
            border: 1px solid #E7ECF5;
        }
        div[data-testid="stMetricValue"] { font-family: 'Plus Jakarta Sans', sans-serif; color: #0B3D91; }

        /* tombol utama warna biru konsisten */
        button[kind="primary"] { background-color: #0F62D6 !important; border-color: #0F62D6 !important; }

        /* container dengan border dikasih sudut membulat */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 14px !important;
        }
    </style>
    """, unsafe_allow_html=True)


def render_topbar():
    """Topbar pakai st.columns + st.image (native), dipercantik CSS saja."""
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 4, 1], vertical_alignment="center")
        with col1:
            logo_path = ASSETS_DIR / "logo_danantara.png"
            if logo_path.exists():
                st.image(str(logo_path), width=130)
        with col2:
            st.markdown("#### SIMONA")
            st.caption("Maturity Level Gudang Distribusi — UID Banten")
        with col3:
            logo_path = ASSETS_DIR / "logo_pln.png"
            if logo_path.exists():
                st.image(str(logo_path), width=55)
    st.write("")


def render_sidebar_profile():
    role = st.session_state.get("role")
    fullname = st.session_state.get("fullname")
    unit_name = st.session_state.get("unit_name")

    with st.sidebar:
        with st.container(border=True):
            st.markdown(f"**{fullname}**")
            st.caption(f"{role} · {unit_name}")
        if st.button("Ganti Role / Logout", use_container_width=True, key="logout_btn"):
            for k in ["role", "unit_id", "unit_name", "fullname", "is_authenticated"]:
                st.session_state.pop(k, None)
            st.rerun()
        st.divider()


def render_hero(badge_text: str = "", title_html: str = "", subtitle: str = ""):
    """Hero halaman login — semua elemen (logo, foto, judul) disatukan dalam 1 container."""
    import re
    plain_title = re.sub(r"<[^>]+>", "", title_html) if title_html else "SIMONA"

    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 3, 1], vertical_alignment="center")
        with col1:
            logo_path = ASSETS_DIR / "logo_danantara.png"
            if logo_path.exists():
                st.image(str(logo_path), width=150)
        with col3:
            logo_path = ASSETS_DIR / "logo_pln.png"
            if logo_path.exists():
                st.image(str(logo_path), width=70)

        bg_path = ASSETS_DIR / "hero_bg.jpg"
        if bg_path.exists():
            st.image(str(bg_path), use_container_width=True)

        st.title(plain_title)
        if subtitle:
            st.write(subtitle)

    st.write("")
