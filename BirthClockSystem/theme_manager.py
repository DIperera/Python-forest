# theme_manager.py

from ttkthemes import ThemedTk

# Themes dictionary remains the same
THEMES = {
    "light": "plastik",  # bright
    "dark": "equilux"    # dark
}

current_theme = "light"

def toggle_theme(window):
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    window.set_theme(THEMES[current_theme])

    # Set background color only for the window
    bg_color = "white" if current_theme == "light" else "#2b2b2b"
    window.configure(background=bg_color)

def get_current_theme():
    return current_theme
