"""
Komponen UI bersama untuk SIMONA — topbar, hero, styling bermerek PLN/Danantara.
"""

import streamlit as st
import base64
from pathlib import Path

ASSETS_DIR = Path(__file__).parent / "assets"


@st.cache_data(show_spinner=False)
def _load_logo_b64(filename: str) -> str:
    path = ASSETS_DIR / filename
    if not path.exists():
        return ""
    return base64.b64encode(path.read_bytes()).decode()


def get_favicon():
    path = ASSETS_DIR / "logo_pln.png"
    return str(path) if path.exists() else None


def inject_style():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        h1, h2, h3, h4, .simona-brand-name, .simona-hero-title {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }

        .block-container { padding-top: 2.5rem !important; }

        /* ---- topbar nav ala website resmi ---- */
        .simona-topbar {
            display: flex; align-items: center; justify-content: space-between;
            padding: 14px 28px; margin: 0 -1rem 1.75rem -1rem;
            background: #FFFFFF;
            border: 1px solid #E7ECF5;
            border-radius: 14px;
            box-shadow: 0 1px 4px rgba(16,24,40,0.04);
        }
        .simona-topbar-brand { display: flex; align-items: center; gap: 12px; }
        .simona-topbar-brand img { height: 30px; object-fit: contain; }
        .simona-topbar-divider { width: 1px; height: 24px; background: #DCE2EE; }
        .simona-brand-name { color: #0B3D91; font-size: 1.05rem; font-weight: 700; margin: 0; letter-spacing: 0.2px; }
        .simona-brand-sub { color: #8891A3; font-size: 0.72rem; font-weight: 500; margin: 0; }
        .simona-topbar-right img { height: 30px; object-fit: contain; }

        /* ---- hero section (halaman login) ---- */
        .simona-hero {
            position: relative; overflow: hidden;
            margin: 0 -1rem 1.75rem -1rem; padding: 44px 48px 52px 48px;
            background-size: cover; background-position: center;
            border-radius: 20px;
            border: 1px solid #E7ECF5;
        }
        .simona-hero::after {
            content: ""; position: absolute; inset: 0; z-index: 0;
            background:
                linear-gradient(100deg, rgba(7,20,50,0.93) 0%, rgba(11,61,145,0.88) 45%, rgba(11,61,145,0.55) 100%);
            pointer-events: none;
        }
        .simona-hero::before {
            content: ""; position: absolute; inset: 0; z-index: 1;
            background-image:
                radial-gradient(circle at 85% 15%, rgba(41,182,246,0.22) 0%, transparent 45%),
                repeating-linear-gradient(115deg, rgba(255,255,255,0.02) 0px, rgba(255,255,255,0.02) 1px, transparent 1px, transparent 64px);
            pointer-events: none;
        }
        .simona-hero-logos {
            position: relative; z-index: 2; display: flex; align-items: center; gap: 12px;
        }
        .simona-hero-logos img { height: 30px; object-fit: contain; }
        .simona-hero-content {
            position: relative; z-index: 2; margin-top: 36px;
        }
        .simona-hero-badge {
            display: inline-block; background: rgba(255,255,255,0.12);
            color: #E8F0FF; padding: 6px 14px; border-radius: 999px; font-size: 0.78rem;
            font-weight: 600; margin-bottom: 18px; border: 1px solid rgba(255,255,255,0.25);
        }
        .simona-hero-title {
            color: #FFFFFF; font-size: 2.5rem; font-weight: 800;
            line-height: 1.15; margin: 0 0 14px 0; max-width: 760px;
        }
        .simona-hero-title .accent { color: #6FD3FF; }
        .simona-hero-subtitle {
            color: rgba(255,255,255,0.85); font-size: 1.0rem;
            font-weight: 400; max-width: 620px; line-height: 1.55; margin-bottom: 20px;
        }
        .simona-hero-chips { display: flex; gap: 10px; flex-wrap: wrap; }
        .simona-hero-chip {
            background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.22);
            color: #F0F5FF; font-size: 0.78rem; font-weight: 600;
            padding: 6px 13px; border-radius: 999px;
        }

        /* ---- generic ---- */
        div[data-testid="stMetric"] {
            background: #FFFFFF;
            border-radius: 14px; padding: 16px 18px; border: 1px solid #E7ECF5;
            box-shadow: 0 1px 3px rgba(16,24,40,0.04);
        }
        div[data-testid="stMetricLabel"] { font-weight: 600; color: #475066; }
        div[data-testid="stMetricValue"] { font-family: 'Plus Jakarta Sans', sans-serif; color: #0B3D91; }

        .stTabs [data-baseweb="tab-list"] { gap: 28px; }
        .stTabs [data-baseweb="tab"] {
            border-radius: 8px 8px 0 0; font-weight: 600; color: #5B6478; padding: 8px 4px;
        }
        .stTabs [aria-selected="true"] { color: #0F62D6 !important; }
        [data-baseweb="tab-highlight"] { background-color: #0F62D6 !important; }
        [data-baseweb="tab-border"] { background-color: #E7ECF5 !important; }

        div[data-testid="stExpander"] { border: 1px solid #E7ECF5; border-radius: 12px; }
        section[data-testid="stSidebar"] { background: #F7F9FC; }

        [data-testid="stSidebarNav"] ul { padding: 0 10px; }
        [data-testid="stSidebarNav"] a {
            border-radius: 10px; padding: 9px 14px; margin: 2px 0;
            font-weight: 500; color: #37415A;
        }
        [data-testid="stSidebarNav"] a:hover { background: #E9EFFC; }
        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background: #0F62D6; color: #FFFFFF !important; font-weight: 600;
        }
        [data-testid="stSidebarNav"] a[aria-current="page"] span { color: #FFFFFF !important; }

        .sidebar-profile {
            background: #FFFFFF; border: 1px solid #E7ECF5; border-radius: 12px;
            padding: 12px 14px; margin: 10px 0 8px 0;
        }
        .sidebar-profile-name { margin: 0; font-weight: 700; color: #1A1F36; font-size: 0.92rem; }
        .sidebar-profile-meta { margin: 2px 0 0 0; color: #7A8399; font-size: 0.78rem; }

        button[kind="primary"] { background-color: #0F62D6 !important; border-color: #0F62D6 !important; }
        div.stButton > button { border-radius: 8px !important; font-weight: 500 !important; }
    </style>
    """, unsafe_allow_html=True)


def render_topbar():
    pln_b64 = _load_logo_b64("logo_pln.png")
    dan_b64 = _load_logo_b64("logo_danantara.png")

    left_logo = f'<img src="data:image/png;base64,{dan_b64}" alt="Danantara Indonesia">' if dan_b64 else ""
    right_logo = f'<img src="data:image/png;base64,{pln_b64}" alt="PLN">' if pln_b64 else ""

    st.markdown(f"""
    <div class="simona-topbar">
        <div class="simona-topbar-brand">
            {left_logo}
            <div class="simona-topbar-divider"></div>
            <div>
                <p class="simona-brand-name">SIMONA</p>
                <p class="simona-brand-sub">Maturity Level Gudang Distribusi — UID Banten</p>
            </div>
        </div>
        <div class="simona-topbar-right">{right_logo}</div>
    </div>
    """, unsafe_allow_html=True)


def render_sidebar_profile():
    role = st.session_state.get("role")
    fullname = st.session_state.get("fullname")
    unit_name = st.session_state.get("unit_name")

    with st.sidebar:
        st.markdown(
            '<div class="sidebar-profile">'
            f'<p class="sidebar-profile-name">{fullname}</p>'
            f'<p class="sidebar-profile-meta">{role} &middot; {unit_name}</p>'
            '</div>', unsafe_allow_html=True,
        )
        if st.button("Ganti Role / Logout", use_container_width=True, key="logout_btn"):
            for k in ["role", "unit_id", "unit_name", "fullname", "is_authenticated"]:
                st.session_state.pop(k, None)
            st.rerun()


def render_hero(badge_text: str = "SIMONA — Sistem Monitoring & Self Assessment Unit PLN",
                title_html: str = "SIMONA", subtitle: str = ""):
    pln_b64 = _load_logo_b64("logo_pln.png")
    dan_b64 = _load_logo_b64("logo_danantara.png")
    bg_b64 = _load_logo_b64("hero_bg.jpg")

    left_logo = (
        f'<img src="data:image/png;base64,{dan_b64}" alt="Danantara Indonesia" '
        f'style="filter:invert(1) brightness(1.6);">'
    ) if dan_b64 else ""
    right_logo = f'<img src="data:image/png;base64,{pln_b64}" alt="PLN">' if pln_b64 else ""
    bg_style = f'style="background-image: url(data:image/jpeg;base64,{bg_b64});"' if bg_b64 else ""

    st.markdown(f"""
    <div class="simona-hero" {bg_style}>
        <div class="simona-hero-logos">
            {left_logo}
            <div class="simona-topbar-divider" style="background: rgba(255,255,255,0.3);"></div>
            {right_logo}
        </div>
        <div class="simona-hero-content">
            <div class="simona-hero-badge">{badge_text}</div>
            <p class="simona-hero-title">{title_html}</p>
            <p class="simona-hero-subtitle">{subtitle}</p>
            <div class="simona-hero-chips">
                <span class="simona-hero-chip">7 Unit Gudang</span>
                <span class="simona-hero-chip">29 Indikator</span>
                <span class="simona-hero-chip">6 Aspek Penilaian</span>
                <span class="simona-hero-chip">Real-time Monitoring</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
