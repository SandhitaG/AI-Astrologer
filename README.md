# Simple AI Astrologer (Rule‑Based Demo)
<img width="1919" height="839" alt="image" src="https://github.com/user-attachments/assets/e62a779c-3327-4dc5-9092-60b2107253e4" />

A Streamlit app that collects birth details (Name, Date, Time, Place), produces a pleasant, rule‑based astrology reading, and answers one free‑text question.

## Features
- Clean, single-page Streamlit UI.
- Rule-based reading using:
  - Western zodiac (by birth month/day)
  - Chinese zodiac (by birth year)
  - Numerology life path number
  - Time‑of‑day flavor (morning/day/evening/night)
- One free-text question with lightweight intent detection (career, love, health, money, study, travel).
- Download your reading as a text file.
- Educational demo — no external APIs, works offline.

## Tech
- Python 3.9+
- Streamlit

## Setup & Run (Local)
```bash

# 1) Install dependencies
pip install -r requirements.txt

# 2) Run the app
streamlit run app.py
```

Open the local URL shown in the terminal (usually http://localhost:8501).

## Project Structure
```
ai-astrologer/
├─ app.py                 # Streamlit UI
├─ astrology_logic.py     # Rule-based logic
├─ requirements.txt
```
