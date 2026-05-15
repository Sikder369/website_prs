import streamlit as st

# ----------------------------------------------------
# PAGE SETTINGS
# This controls browser tab title, icon, and page width
# ----------------------------------------------------
st.set_page_config(
    page_title="Pallab Sikdar | Travel Vlogger",
    page_icon="🌍",
    layout="wide"
)

# CUSTOM CSS
# CSS is used to make the website colorful and beautiful
# Think of CSS as the "dress and makeup" of your website
#==========================================

st.markdown("""
<style>
/* Main page background */
.stApp {
    background: linear-gradient(135deg, #fff7e6, #e3f2fd);
}

/* Hero section design */
.hero {
    padding: 70px 30px;
    border-radius: 30px;
    text-align: center;
    color: white;
    background: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)),
    url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
    background-size: cover;
    background-position: center;
}

/* Main name */
.hero h1 {
    font-size: 60px;
    margin-bottom: 10px;
}

/* Tagline */
.hero h3 {
    font-size: 28px;
    color: #ffdd57;
}

/* White content cards */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
    margin: 10px 0px;
}

/* Section title */
.section-title {
    font-size: 36px;
    font-weight: bold;
    color: #0d47a1;
    margin-top: 35px;
}

/* Small colorful badge */
.badge {
    display: inline-block;
    padding: 8px 15px;
    background-color: #ff7043;
    color: white;
    border-radius: 20px;
    margin: 5px;
}
</style>
""", unsafe_allow_html=True)


# ----------------------------------------------------
# SIDEBAR MENU
# Sidebar is like the website's remote control 🎮
# ----------------------------------------------------
# ----------------------------------------------------
# SIDEBAR BOX MENU
# These buttons look more like separate tab boxes 📦
# ----------------------------------------------------

# ----------------------------------------------------
# SIDEBAR BOX MENU
# ----------------------------------------------------

st.sidebar.markdown("## 🌍 Travel Menu")

# Sidebar buttons
home_btn = st.sidebar.button("🏠 Home", use_container_width=True)
photo_btn = st.sidebar.button("📸 Upload Photo", use_container_width=True)
story_btn = st.sidebar.button("📝 Travel Story", use_container_width=True)
vlog_btn = st.sidebar.button("🎥 Vlog", use_container_width=True)
destination_btn = st.sidebar.button("📍 Destinations", use_container_width=True)
gallery_btn = st.sidebar.button("🖼️ Gallery", use_container_width=True)
contact_btn = st.sidebar.button("📬 Contact", use_container_width=True)

# ----------------------------------------------------
# REMEMBER CURRENT PAGE
# session_state remembers clicked page
# ----------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

# Change page when button clicked
if home_btn:
    st.session_state.page = "🏠 Home"

elif photo_btn:
    st.session_state.page = "📸 Upload Photo"

elif story_btn:
    st.session_state.page = "📝 Travel Story"

elif vlog_btn:
    st.session_state.page = "🎥 Vlog"

elif destination_btn:
    st.session_state.page = "📍 Destinations"

elif gallery_btn:
    st.session_state.page = "🖼️ Gallery"

elif contact_btn:
    st.session_state.page = "📬 Contact"

# VERY IMPORTANT
# This creates the page variable
page = st.session_state.page

# This page variable controls which page opens
st.markdown("""
<style>

/* Sidebar button design */
section[data-testid="stSidebar"] button {
    background: linear-gradient(135deg, #ff7e5f, #feb47b);
    color: white;
    border-radius: 15px;
    border: none;
    padding: 15px;
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
}

section[data-testid="stSidebar"] button:hover {
    background: linear-gradient(135deg, #43cea2, #185a9d);
    color: white;
    transform: scale(1.03);
}

</style>
""", unsafe_allow_html=True)

# HERO SECTION
# This is the first big attractive section users see
# ----------------------------------------------------

# ----------------------------------------------------
# HOME PAGE
# ----------------------------------------------------
if page == "🏠 Home":
    st.markdown("""
    <div class="hero">
        <h1>🌍 Pallab Sikdar</h1>
        <h3>Journey that Never Ends</h3>
        <p style="font-size:20px;">
            Traveller | Vlogger | Storyteller | Dream Chaser
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">✈️ About My Journey</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
            caption="Every road has a story...",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <div class="card">
            <h2>Hello, I am Pallab 👋</h2>
            <p>
            I love travelling, discovering new places, capturing beautiful moments,
            and sharing stories through videos and photos.
            </p>
            <p>
            This page is my travel diary, vlog space, and memory album.
            </p>
        </div>
        """, unsafe_allow_html=True)


# ----------------------------------------------------
# PHOTO UPLOAD PAGE
# ----------------------------------------------------
elif page == "📸 Upload Photo":
    st.markdown('<div class="section-title">📸 Upload My Travel Photo</div>', unsafe_allow_html=True)

    uploaded_photo = st.file_uploader(
        "Upload a travel photo",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_photo is not None:
        st.image(
            uploaded_photo,
            caption="My travel memory ❤️",
            use_container_width=True
        )
    else:
        st.info("Upload your travel photo here.")


# ----------------------------------------------------
# TRAVEL STORY PAGE
# ----------------------------------------------------
elif page == "📝 Travel Story":
    st.markdown('<div class="section-title">📝 My Travel Story</div>', unsafe_allow_html=True)

    story = st.text_area(
        "Write your travel story here",
        placeholder="Example: Today I visited a beautiful place..."
    )

    if story:
        st.markdown(f"""
        <div class="card">
            <h3>My Story</h3>
            <p>{story}</p>
        </div>
        """, unsafe_allow_html=True)


# ----------------------------------------------------
# VLOG PAGE
# ----------------------------------------------------
elif page == "🎥 Vlog":
    st.markdown('<div class="section-title">🎥 My Travel Vlog</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>Watch My Journey</h3>
    </div>
    """, unsafe_allow_html=True)

    st.video("https://www.youtube.com/watch?v=YyrlGU0mEz8")
    st.video("https://www.youtube.com/watch?v=YyrlGU0mEz8")


# ----------------------------------------------------
# DESTINATIONS PAGE
# ----------------------------------------------------
elif page == "📍 Destinations":
    st.markdown('<div class="section-title">📍 My Favorite Destinations</div>', unsafe_allow_html=True)

    d1, d2, d3 = st.columns(3)

    with d1:
        st.markdown('<div class="card"><h2>🏔️ Mountains</h2><p>Roads that touch the clouds.</p></div>', unsafe_allow_html=True)

    with d2:
        st.markdown('<div class="card"><h2>🌊 Beaches</h2><p>Sunsets, waves, and peace.</p></div>', unsafe_allow_html=True)

    with d3:
        st.markdown('<div class="card"><h2>🏙️ Cities</h2><p>Culture, food, and lights.</p></div>', unsafe_allow_html=True)


# ----------------------------------------------------
# GALLERY PAGE
# ----------------------------------------------------
elif page == "🖼️ Gallery":
    st.markdown('<div class="section-title">🖼️ Travel Gallery</div>', unsafe_allow_html=True)

    g1, g2, g3 = st.columns(3)

    with g1:
        st.image("https://images.unsplash.com/photo-1469474968028-56623f02e42e", caption="Mountains", use_container_width=True)

    with g2:
        st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e", caption="Beach", use_container_width=True)

    with g3:
        st.image("https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1", caption="Road Trip", use_container_width=True)


# ----------------------------------------------------
# CONTACT PAGE
# ----------------------------------------------------
elif page == "📬 Contact":
    st.markdown('<div class="section-title">📬 Follow My Journey</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>Let’s connect!</h3>
        <p>📧 Email: your-email@example.com</p>
        <p>▶️ YouTube: Add your channel link</p>
        <p>📘 Facebook: Add your page link</p>
        <p>📷 Instagram: Add your Instagram link</p>
    </div>
    """, unsafe_allow_html=True)