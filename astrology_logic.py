from datetime import date, time
from typing import Dict

WESTERN_SIGNS = [
    ("Capricorn", (12, 22), (1, 19)),
    ("Aquarius", (1, 20), (2, 18)),
    ("Pisces", (2, 19), (3, 20)),
    ("Aries", (3, 21), (4, 19)),
    ("Taurus", (4, 20), (5, 20)),
    ("Gemini", (5, 21), (6, 20)),
    ("Cancer", (6, 21), (7, 22)),
    ("Leo", (7, 23), (8, 22)),
    ("Virgo", (8, 23), (9, 22)),
    ("Libra", (9, 23), (10, 22)),
    ("Scorpio", (10, 23), (11, 21)),
    ("Sagittarius", (11, 22), (12, 21)),
]

CHINESE_SIGNS = [
    "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
    "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
]

def get_western_zodiac(month: int, day: int) -> str:
    for sign, (start_m, start_d), (end_m, end_d) in WESTERN_SIGNS:
        if (month == start_m and day >= start_d) or (month == end_m and day <= end_d):
            return sign
        if start_m > end_m:  # Capricorn wraps year-end
            if (month == start_m and day >= start_d) or (month == end_m and day <= end_d):
                return sign
            if month > start_m or month < end_m:
                return sign
    # Fallback
    return "Capricorn"

def get_chinese_zodiac(year: int) -> str:
    # 1900 was the year of the Rat in the lunar cycle.
    return CHINESE_SIGNS[(year - 1900) % 12]

def digit_sum(n: int) -> int:
    s = 0
    for c in str(n):
        if c.isdigit():
            s += int(c)
    return s

def reduce_to_single_digit(n: int) -> int:
    while n > 9 and n not in (11, 22, 33):
        n = digit_sum(n)
    return n

def life_path_number(d: date) -> int:
    total = digit_sum(d.year) + digit_sum(d.month) + digit_sum(d.day)
    return reduce_to_single_digit(total)

CORE_TRAITS = {
    "Aries": "bold, pioneering, energetic",
    "Taurus": "grounded, patient, practical",
    "Gemini": "curious, witty, adaptable",
    "Cancer": "nurturing, intuitive, protective",
    "Leo": "confident, expressive, generous",
    "Virgo": "analytical, meticulous, helpful",
    "Libra": "harmonious, diplomatic, fair-minded",
    "Scorpio": "intense, transformative, strategic",
    "Sagittarius": "adventurous, philosophical, candid",
    "Capricorn": "ambitious, disciplined, responsible",
    "Aquarius": "innovative, humanitarian, unconventional",
    "Pisces": "empathetic, imaginative, gentle",
}

LIFE_PATH_THEMES = {
    1: "leadership and independence",
    2: "cooperation and harmony",
    3: "creativity and communication",
    4: "stability and structure",
    5: "freedom and change",
    6: "caregiving and responsibility",
    7: "analysis and spirituality",
    8: "power and material mastery",
    9: "compassion and service",
    11: "inspiration and intuition (master number)",
    22: "grand building and legacy (master number)",
    33: "master teacher and healing (master number)"
}

INTENT_KEYWORDS = {
    "career": ["career", "job", "work", "promotion", "startup", "business"],
    "love": ["love", "relationship", "marriage", "partner", "crush"],
    "health": ["health", "fitness", "illness", "energy", "wellness"],
    "money": ["money", "finance", "wealth", "income", "salary"],
    "study": ["study", "exam", "college", "admission", "research"],
    "travel": ["travel", "trip", "relocate", "move", "abroad"]
}

def generate_reading(name, place, dob, tob, western, chinese, life_path) -> str:
    # Simple time-of-day flavor
    hour = tob.hour
    if 5 <= hour < 12: tod = "morning-born (fresh starts, outward energy)"
    elif 12 <= hour < 17: tod = "day-born (clarity, visibility, recognition)"
    elif 17 <= hour < 21: tod = "evening-born (relationship focus, diplomacy)"
    else: tod = "night-born (deep intuition, inner growth)"

    core = CORE_TRAITS.get(western, "")
    theme = LIFE_PATH_THEMES.get(life_path, "unique life lessons")

    lines = []
    lines.append(f"Hello {name} from {place}!")
    lines.append(f"Your Western zodiac sign is **{western}** — often {core}.")
    lines.append(f"Your Chinese zodiac animal is **{chinese}**.")
    lines.append(f"Your Life Path Number is **{life_path}**, highlighting {theme}.")
    lines.append(f"You are {tod}.")
    lines.append("")
    # Sections
    lines.append("**Career & Growth**:")
    if western in ["Aries", "Leo", "Capricorn", "Virgo", "Aquarius"]:
        lines.append("Opportunities favor initiative and ownership. Set bolder goals and track them weekly.")
    else:
        lines.append("Collaboration and skill-depth will be your superpower. Invest in courses and mentorships.")
    if life_path in [1, 8, 22]:
        lines.append("This year amplifies leadership and material progress—negotiate, don't hesitate.")
    elif life_path in [3, 5]:
        lines.append("Creative and flexible projects thrive—embrace variety and public-facing work.")
    else:
        lines.append("Consistency beats speed—build habits that keep stacking results.")
    lines.append("")
    lines.append("**Love & Relationships**:")
    if western in ["Cancer", "Libra", "Pisces", "Taurus"]:
        lines.append("Heart-first choices win. Plan shared rituals and be vocal about needs.")
    else:
        lines.append("Balance independence with presence. Listening deeply brings closeness.")
    lines.append("")
    lines.append("**Health & Wellbeing**:")
    if western in ["Virgo", "Capricorn"]:
        lines.append("Structure your routines. Track sleep, hydration, and mobility; you'll feel the edge.")
    else:
        lines.append("Aim for rhythm, not perfection. Gentle cardio + breathwork suits your current arc.")
    lines.append("")
    lines.append("_Note: This is a simplified, rule-based reading for demonstration purposes._")
    return "\n".join(lines)

def answer_free_text(question: str, western: str, life_path: int) -> str:
    q = question.lower()

    # Detect time-based intent
    if "when" in q or "how soon" in q or "which month" in q:
        if "job" in q or "career" in q or "work" in q:
            if life_path in [1, 8, 22]:
                return "Career doors open strongly within the next 3–6 months. Stay proactive with applications."
            elif life_path in [3, 5]:
                return "Opportunities appear sooner than expected—watch the next 2–4 months for openings."
            else:
                return "Progress may feel slower, but steady—expect clarity within 6–9 months if consistent."
        else:
            return "Timing looks favorable in the coming season, though exact dates vary—focus on preparation now."

    # Normal intent detection
    selected = "general"
    for intent, keys in INTENT_KEYWORDS.items():
        if any(k in q for k in keys):
            selected = intent
            break

    if selected == "career":
        if life_path in [1, 8, 22]:
            return "Momentum is strong for leadership roles and negotiations. Pitch boldly in the next 4–6 weeks."
        return "Skill stacking pays off. Update your portfolio and ask for feedback—doors open from that."
    if selected == "love":
        if western in ["Libra", "Cancer", "Pisces", "Taurus"]:
            return "Prioritize emotional honesty and shared rituals. A warm, steady phase is forming."
        return "Practice presence. Honest conversations clear the air and invite deeper commitment."
    if selected == "health":
        return "Small daily rituals beat intense bursts. Focus on sleep, hydration, and 20 minutes of movement."
    if selected == "money":
        return "Budget with a weekly check-in. Negotiate recurring costs; invest in learning that compounds."
    if selected == "study":
        return "Create a 45/15 study rhythm. Active recall + spaced repetition will lift your scores quickly."
    if selected == "travel":
        return "Short trips refresh you now. Plan a 3–5 day break; meaningful connections may emerge."

    # Default fallback
    return "Trust your instincts and keep actions consistent for 21 days—you'll see a clear shift."
