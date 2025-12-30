import streamlit as st

# ---------- Page config ----------
st.set_page_config(
    page_title="AI Career Guidance",
    page_icon="🎓",
    layout="wide"
)

# ---------- Session state ----------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---------- Custom CSS ----------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F7F6F3;
        color: #2E2E2E;
    }

    h1, h2, h3 {
        color: #5B6C8F;
    }

    /* NAV BAR */
    .navbar {
        position: sticky;
        top: 0;
        z-index: 999;
        background-color: #5B6C8F;
        padding: 0.6rem 2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-radius: 0 0 12px 12px;
    }

    .nav-left {
        font-size: 1.2rem;
        font-weight: 700;
        color: white;
    }

    .nav-right button {
        background: transparent;
        color: white;
        border: none;
        font-size: 0.95rem;
        margin-left: 1.2rem;
        cursor: pointer;
        font-weight: 500;
    }

    .nav-right button:hover {
        text-decoration: underline;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #5B6C8F;
        color: white;
        border-radius: 8px;
        padding: 0.6em 1em;
        border: none;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #7FA8A0;
    }

    /* Feature cards */
    .feature-box {
        background-color: #E8DFD8;
        padding: 1.2em;
        border-radius: 12px;
        height: 100%;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- NAV BAR ----------
nav = st.container()
with nav:
    st.markdown(
        """
        <div class="navbar">
            <div class="nav-left">🎓 AI Career Guidance</div>
            <div class="nav-right">
                <form action="" method="post">
                    <button name="nav" value="Home">Home</button>
                    <button name="nav" value="Assessment">Assessment</button>
                    <button name="nav" value="About">About</button>
                    <button name="nav" value="Login">Login</button>
                </form>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- Handle navigation ----------
query_params = st.experimental_get_query_params()
if "nav" in query_params:
    st.session_state.page = query_params["nav"][0]

# ---------- Page routing ----------
if st.session_state.page == "Home":
    st.title("Helping students choose their future, intelligently")

    st.markdown(
        """
        This platform uses **psychometric assessments**, **academic interests**,
        and **AI-driven analysis** to help high school students make
        informed university and career decisions.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-box">
                <h3>🧠 Psychometric Testing</h3>
                <p>Structured assessments to understand how students think and learn.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="feature-box">
                <h3>🎯 Career Matching</h3>
                <p>AI-based mapping to university courses and career clusters.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="feature-box">
                <h3>📊 Personalised Insights</h3>
                <p>Clear explanations and reports designed for students and parents.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

elif st.session_state.page == "Assessment":
    st.title("Sample Assessment")
    st.write("This is where your psychometric questions will live.")

elif st.session_state.page == "About":
    st.title("About the Platform")
    st.write("Built to reduce confusion, anxiety, and bad advice.")

elif st.session_state.page == "Login":
    st.title("Login / Sign Up")
    st.write("Authentication coming soon. Streamlit is trying its best.")

