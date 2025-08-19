import streamlit as st
from datetime import date, time, datetime
from astrology_logic import (
    get_western_zodiac, get_chinese_zodiac, life_path_number, 
    generate_reading, answer_free_text
)

st.set_page_config(page_title="AI Astrologer (Simple)", page_icon="🔮", layout="centered")

st.title("🔮 Simple AI Astrologer")
st.caption("Rule-based demo app — enter your birth details and ask a question.")

with st.form("birth_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name", placeholder="Your full name")
        dob = st.date_input("Date of Birth", value=date(2000, 1, 1), format="DD/MM/YYYY")
    with col2:
        tob = st.time_input("Time of Birth", value=time(12, 0))
        place = st.text_input("Place of Birth", placeholder="City, Country")

    question = st.text_area("Ask a free-text question (optional)", 
                            placeholder="e.g., What does my career path look like this year?",
                            height=100)
    submitted = st.form_submit_button("Get Reading ✨")

if submitted:
    if not name or not place:
        st.error("Please fill in your **Name** and **Place of Birth**.")
        st.stop()

    # Core calculations
    western = get_western_zodiac(dob.month, dob.day)
    chinese = get_chinese_zodiac(dob.year)
    life_path = life_path_number(dob)

    # Build the reading
    reading = generate_reading(
        name=name.strip(), place=place.strip(),
        dob=dob, tob=tob, western=western, chinese=chinese, life_path=life_path
    )

    st.subheader("🗒️ Your Personalized Reading")
    st.write(reading)

    if question.strip():
        st.subheader("💬 Answer to Your Question")
        st.write(answer_free_text(question, western, life_path))

    # Downloadable text file
    file_name = f"{name.replace(' ', '_')}_reading.txt"
    st.download_button(
        label="Download Your Reading",
        data=reading.encode("utf-8"),
        file_name=file_name,
        mime="text/plain"
    )

    with st.expander("Debug Info (for demo)"):
        st.json({
            "name": name,
            "place": place,
            "dob": dob.isoformat(),
            "tob": tob.strftime("%H:%M"),
            "western_zodiac": western,
            "chinese_zodiac": chinese,
            "life_path_number": life_path
        })

st.markdown("---")
st.caption("Built with ❤️ using Streamlit. This is a rule-based educational demo, not professional advice.")
