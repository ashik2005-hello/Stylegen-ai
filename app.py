import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="StyleSense AI", layout="wide")

# -----------------------------
# Helper Functions
# -----------------------------

def detect_skin_tone():
    tones = ["Warm", "Cool", "Neutral"]
    return random.choice(tones)

def seasonal_palette(tone):
    palettes = {
        "Warm": ["Coral", "Peach", "Olive", "Mustard"],
        "Cool": ["Lavender", "Blue", "Emerald", "Pink"],
        "Neutral": ["Beige", "Blush", "Teal", "Soft Red"]
    }
    return palettes.get(tone, [])

def generate_outfit(occasion, style):
    return {
        "Top": f"{style} styled top suitable for {occasion}",
        "Bottom": "Tailored trousers / skirt",
        "Footwear": "Matching stylish footwear",
        "Accessories": "Minimal accessories",
        "Layering": "Light jacket / shrug"
    }

def generate_makeup(occasion):
    return {
        "Foundation": "Natural matching foundation",
        "Lips": "Soft pink / nude tone",
        "Eyes": "Light shimmer",
        "Intensity": "Medium for special events"
    }

def generate_hairstyle():
    styles = ["Soft waves", "Sleek ponytail", "Layered open hair", "Elegant bun"]
    return random.choice(styles)

def fashion_quote():
    quotes = [
        "Fashion is the armor to survive everyday life.",
        "Style is a way to say who you are without speaking.",
        "Elegance never goes out of style."
    ]
    return random.choice(quotes)

# -----------------------------
# UI
# -----------------------------

st.title("✨ StyleSense – AI Fashion Recommendation System")

st.sidebar.header("User Inputs")

photo = st.sidebar.file_uploader("Upload your photo", type=["jpg", "png"])

skin_desc = st.sidebar.text_input("Describe your skin tone (optional)")
body_type = st.sidebar.text_input("Body Type")
height = st.sidebar.text_input("Height")
weight = st.sidebar.text_input("Weight")
hair = st.sidebar.text_input("Hair Type/Color")

occasion = st.sidebar.selectbox(
    "Select Occasion",
    ["Casual", "Office", "Wedding", "Festival", "Party", "Date", "Beach"]
)

style_pref = st.sidebar.selectbox(
    "Style Preference",
    ["Minimalist", "Ethnic", "Streetwear", "Formal", "Trendy"]
)

priority = st.sidebar.radio("Priority", ["Comfort", "Fashion", "Both"])

budget = st.sidebar.slider("Budget Range (₹)", 500, 10000, 2000)

color_pref = st.sidebar.text_input("Color Preference (optional)")

generate = st.sidebar.button("Generate Recommendations")

# -----------------------------
# Output Section
# -----------------------------

if generate:
    st.subheader("🧠 AI Analysis")

    skin_tone = detect_skin_tone()
    palette = seasonal_palette(skin_tone)

    st.write(f"**Detected Skin Tone:** {skin_tone}")
    st.write(f"**Recommended Color Palette:** {', '.join(palette)}")

    if photo:
        image = Image.open(photo)
        st.image(image, caption="Uploaded Photo", width=200)

    st.divider()

    # Outfit
    st.subheader("👗 Complete Outfit Recommendation")
    outfit = generate_outfit(occasion, style_pref)
    for key, value in outfit.items():
        st.write(f"**{key}:** {value}")

    # Makeup
    st.subheader("💄 Makeup Suggestions")
    makeup = generate_makeup(occasion)
    for key, value in makeup.items():
        st.write(f"**{key}:** {value}")

    # Hairstyle
    st.subheader("💇 Hairstyle Suggestion")
    st.write(generate_hairstyle())

    # Explanation
    st.subheader("📖 Why This Suits You")
    st.write(
        f"This outfit matches your {skin_tone} undertone and fits perfectly for a {occasion}. "
        f"It aligns with your {style_pref} preference and stays within ₹{budget}."
    )

    # Trend Insight
    st.subheader("🔥 Trend Insight")
    st.write("Pastel tones and minimalist layering are trending in India.")

    # Shopping Links (Dummy)
    st.subheader("🛍 Shopping Suggestions")
    st.markdown("[Buy on Myntra](https://www.myntra.com)")
    st.markdown("[Buy on Amazon](https://www.amazon.in)")
    st.markdown("[Buy on Ajio](https://www.ajio.com)")

    # Chat Assistant
    st.subheader("🤖 Style Chat Assistant")
    user_query = st.text_input("Ask something like: Suggest under ₹1500")
    if user_query:
        st.write("AI Response: Try a minimalist cotton kurti with neutral trousers under ₹1500.")

    st.divider()
    st.success("✨ " + fashion_quote())
