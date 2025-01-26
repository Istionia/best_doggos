import os

# ==============================================
# STATUS THRESHOLDS
# ==============================================
HUNGER_CRITICAL = 80  # Warn if hunger exceeds this value
HAPPINESS_LOW = 30    # Warn if happiness drops below this value
ENERGY_LOW = 20       # Warn if energy drops below this value
HYGIENE_LOW = 20      # Warn if hygiene drops below this value
SKILL_LOW = 20        # Warn if skill drops below this value

# ==============================================
# GAME MESSAGES
# ==============================================
MESSAGES = {
    "welcome": "🐾 WOOF WOOF! We're so glad you're here! 🐾",
    "hungry_warning": "{name} is starving! Feed them soon!",
    "happiness_warning": "{name} is feeling lonely. Play with them!",
    "energy_warning": "{name} is exhausted. Let them rest!"
}

# ==============================================
# EMOJIS AND ASCII ART
# ==============================================
DOG_EMOJIS = {
    "happy": "🐶",
    "sad": "😢",
    "hungry": "🍖",
    "tired": "💤"
}

# ASCII art for dog moods
DOG_ART = {
    "happy": """
    ╭━━━━━━━━━━━━━╮
    │   ^  ^      │
    │  (◕ᴥ◕)     │
    ╰━━━━━━━━━━━━━╯
    """,
    "sad": """
    ╭━━━━━━━━━━━━━╮
    │   >  <      │
    │  (◕︵◕)     │
    ╰━━━━━━━━━━━━━╯
    """,
    "tired": """
    ╭━━━━━━━━━━━━━╮
    │   -  -      │
    │  (ᴥ_ᴥ)     │
    ╰━━━━━━━━━━━━━╯
    """,
    "hungry": """
    ╭━━━━━━━━━━━━━╮
    │   O  O      │
    │  (ᴥ‿ᴥ)     │
    ╰━━━━━━━━━━━━━╯
    """,
    "playful": """
    ╭━━━━━━━━━━━━━╮
    │   ^  ^      │
    │  (ᴥ‿ᴥ)     │
    ╰━━━━━━━━━━━━━╯
    """,
    "training": """
    ╭━━━━━━━━━━━━━╮
    │   •  •      │
    │  (ᴥ°ᴥ)     │
    ╰━━━━━━━━━━━━━╯
    """
}

# ==============================================
# TEXT FORMATTING
# ==============================================
TEXT_COLORS = {
    "warning": "\033[91m",  # Red
    "success": "\033[92m",  # Green
    "status": "\033[94m",   # Blue
    "reset": "\033[0m"      # Reset to default
}

# ==============================================
# FILE PATHS
# ==============================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
SAVES_DIR = os.path.join(DATA_DIR, "saved_games")
BREEDS_FILE = os.path.join(DATA_DIR, "breeds.json")
