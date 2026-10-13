import os
import sys
import re
import threading
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Gemini API Client initialization
API_KEY = os.getenv("Api_key") or os.getenv("API_KEY") or os.getenv("GEMINI_API_KEY")
client = None
model = "gemini-2.0-flash"

if API_KEY:
    try:
        from google import genai
        client = genai.Client(api_key=API_KEY)
    except Exception as e:
        client = None

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# ----------------- SYSTEM FONT DETECTION -----------------
def _detect_font():
    try:
        import tkinter.font as tkfont
        fams = set(tkfont.families())
        for f in ["JetBrains Mono ExtraBold", "JetBrains Mono", "Noto Sans Mono", "Noto Sans", "Liberation Sans", "DejaVu Sans", "Cantarell", "Ubuntu", "Segoe UI", "Arial"]:
            if f in fams:
                return f
    except Exception:
        pass
    return "JetBrains Mono"

FONT_MAIN = _detect_font()

# ----------------- DESIGN SYSTEM TOKENS -----------------
BG = "#000000"
HEADER_BG = "#0D0D0D"
HEADER_TEXT = "#FFFFFF"
TEXT = "#FFFFFF"
MUTED_TEXT = "#A0A0A0"
ACCENT_BLUE = "#38BDF8"
ACCENT_CYAN = "#00E5FF"
ENTRY_BG = "#121212"
ENTRY_BORDER = "#262626"
BTN_BG = "#1A1A1A"
BTN_HOVER = "#2A2A2A"
BOT_BUBBLE_BG = "#141414"
USER_BUBBLE_BG = "#1E1E1E"
STATUS_ONLINE = "#34D399"
STATUS_OFFLINE = "#FBBF24"

# ----------------- BASE APPLICATION ROOT -----------------
root = tk.Tk()
root.title("TAURUS AI — Dimensity")
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
root.geometry(f"{screen_w}x{screen_h}+0+0")
root.configure(bg=BG)
root.attributes("-fullscreen", True)
root.bind_all("<Escape>", lambda e: root.destroy())

# Top Bar / Header
header = tk.Frame(root, bg=HEADER_BG, height=54, bd=0)
header.pack(fill=tk.X, side=tk.TOP)
header.pack_propagate(False)

title_label = tk.Label(header, text="TAURUS AI", bg=HEADER_BG, fg=HEADER_TEXT,
                       font=(FONT_MAIN, 16, "bold"))
title_label.pack(side=tk.LEFT, padx=(18, 8))

subtitle_label = tk.Label(header, text="Personal AI Assistant", bg=HEADER_BG, fg=ACCENT_BLUE,
                          font=(FONT_MAIN, 13, "bold"))
subtitle_label.pack(side=tk.LEFT, padx=(0, 16))

# Status badge
status_text = "● Connected (Gemini)" if client is not None else "○ Offline (No API Key)"
status_color = STATUS_ONLINE if client is not None else STATUS_OFFLINE
status_label = tk.Label(header, text=status_text, bg=HEADER_BG, fg=status_color,
                        font=(FONT_MAIN, 11, "bold"))
status_label.pack(side=tk.LEFT, padx=8)

# Header right buttons
def btn_hover_on(b, bg_color):
    b.config(bg=bg_color)

def btn_hover_off(b, bg_color):
    b.config(bg=bg_color)

close_btn = tk.Button(header, text="✕ Close (Esc)", font=(FONT_MAIN, 11, "bold"),
                      bg="#273449", fg=TEXT, activebackground="#334155",
                      activeforeground=TEXT, bd=0, padx=14, pady=6,
                      cursor="hand2", command=root.destroy)
close_btn.pack(side=tk.RIGHT, padx=14)
close_btn.bind("<Enter>", lambda e: btn_hover_on(close_btn, "#334155"))
close_btn.bind("<Leave>", lambda e: btn_hover_off(close_btn, "#273449"))

# Helpers
def now_ts():
    return datetime.now().strftime("%I:%M %p")

def clear_chat():
    chat_box.config(state="normal")
    chat_box.delete("1.0", tk.END)
    chat_box.config(state="disabled")
    display_welcome_message()

clear_btn = tk.Button(header, text="Clear Chat", bg=BTN_BG, fg=HEADER_TEXT,
                      font=(FONT_MAIN, 11), relief="flat", bd=0,
                      padx=12, pady=4, command=clear_chat, cursor="hand2",
                      activebackground=BTN_HOVER, activeforeground=TEXT)
clear_btn.pack(side=tk.RIGHT, padx=4)
clear_btn.bind("<Enter>", lambda e: btn_hover_on(clear_btn, BTN_HOVER))
clear_btn.bind("<Leave>", lambda e: btn_hover_off(clear_btn, BTN_BG))

# ----------------- CHAT DISPLAY -----------------
chat_frame = tk.Frame(root, bg=BG)
chat_frame.pack(fill=tk.BOTH, expand=True, padx=18, pady=(12, 10))

chat_box = scrolledtext.ScrolledText(
    chat_frame,
    wrap=tk.WORD,
    state="disabled",
    bg=BG,
    fg=TEXT,
    font=(FONT_MAIN, 12),
    insertbackground=TEXT,
    borderwidth=0,
    highlightthickness=0
)
chat_box.pack(fill=tk.BOTH, expand=True)

# Message bubble styles
chat_box.tag_config(
    "bot_bubble",
    background=BOT_BUBBLE_BG,
    foreground=TEXT,
    lmargin1=16, lmargin2=24,
    rmargin=120,
    spacing1=4,
    spacing3=8,
    font=(FONT_MAIN, 12)
)

chat_box.tag_config(
    "user_bubble",
    background=USER_BUBBLE_BG,
    foreground=ACCENT_CYAN,
    lmargin1=120, lmargin2=120,
    rmargin=16,
    spacing1=4,
    spacing3=8,
    font=(FONT_MAIN, 12, "bold")
)

chat_box.tag_config("bot_avatar", font=("Segoe UI Emoji", 13), foreground=ACCENT_BLUE)
chat_box.tag_config("user_avatar", font=("Segoe UI Emoji", 13), foreground=TEXT)
chat_box.tag_config("typing", foreground=MUTED_TEXT, font=(FONT_MAIN, 11, "italic"), lmargin1=16)

def show_typing():
    chat_box.config(state="normal")
    chat_box.insert(tk.END, "🤖 Taurus AI is thinking...\n", "typing")
    chat_box.config(state="disabled")
    chat_box.see(tk.END)

def remove_typing():
    chat_box.config(state="normal")
    ranges = chat_box.tag_ranges("typing")
    if ranges:
        chat_box.delete(ranges[0], ranges[1])
    chat_box.config(state="disabled")

def insert_bot_message(text, ts=None):
    """Insert a left-aligned bubble with bot avatar."""
    msg = f"[{ts}] " if ts else ""
    chat_box.config(state="normal")
    chat_box.insert(tk.END, "🤖 ", "bot_avatar")
    chat_box.insert(tk.END, msg + text + "\n\n", "bot_bubble")
    chat_box.config(state="disabled")
    chat_box.see(tk.END)

def insert_user_message(text, ts=None):
    """Insert a right-aligned bubble with user avatar."""
    msg = f"[{ts}] " if ts else ""
    chat_box.config(state="normal")
    chat_box.insert(tk.END, "🙂 ", "user_avatar")
    chat_box.insert(tk.END, msg + text + "\n\n", "user_bubble")
    chat_box.config(state="disabled")
    chat_box.see(tk.END)

# ----------------- INPUT CONTROLS -----------------
input_container = tk.Frame(root, bg=BG)
input_container.pack(fill=tk.X, padx=18, pady=(0, 16))

input_border = tk.Frame(input_container, bg=ENTRY_BORDER, bd=1)
input_border.pack(fill=tk.X, expand=True)

inner_input = tk.Frame(input_border, bg=ENTRY_BG)
inner_input.pack(fill=tk.X, expand=True, padx=1, pady=1)

entry = tk.Entry(
    inner_input,
    bg=ENTRY_BG,
    fg=TEXT,
    font=(FONT_MAIN, 13),
    insertbackground=TEXT,
    relief="flat",
    bd=0
)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=12, ipady=10)

send_btn = tk.Button(
    inner_input,
    text="Send ➔",
    bg=BTN_BG,
    fg=TEXT,
    font=("Helvetica Neue", 11, "bold"),
    relief="flat",
    bd=0,
    activebackground=BTN_HOVER,
    activeforeground=TEXT,
    padx=16,
    pady=6,
    cursor="hand2"
)
send_btn.pack(side=tk.RIGHT, padx=6, pady=4)
send_btn.bind("<Enter>", lambda e: btn_hover_on(send_btn, BTN_HOVER))
send_btn.bind("<Leave>", lambda e: btn_hover_off(send_btn, BTN_BG))

# ----------------- SYSTEM APPS SHORTCUTS -----------------
ALLOWED_APPS = {
    "calci":      ("subprocess", os.path.join(BASE_PATH, "CALCI.py")),
    "brick_game": ("subprocess", os.path.join(BASE_PATH, "collision.py")),
    "asphalt":    ("subprocess", os.path.join(BASE_PATH, "asphalt.py")),
    "hangman":    ("subprocess", os.path.join(BASE_PATH, "hangman.py")),
    "pong":       ("subprocess", os.path.join(BASE_PATH, "pong.py")),
    "ecalendar":  ("subprocess", os.path.join(BASE_PATH, "ecalendar.py")),
    "listapps":   ("apps", None)
}

def _launch_subprocess(path):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    import subprocess
    subprocess.Popen([sys.executable, path])

def safe_launch(key):
    """Launch whitelisted app in background. Returns (ok:bool, msg:str)."""
    ent = ALLOWED_APPS.get(key.lower())
    if not ent:
        return False, f"App '{key}' is not in Dimensity OS. Available: {', '.join(ALLOWED_APPS.keys())}"
    typ, target = ent
    try:
        if typ == "subprocess":
            threading.Thread(target=_launch_subprocess, args=(target,), daemon=True).start()
            return True, f"Launching {key}..."
        if typ == "apps":
            return True, f"Available system apps: {', '.join(ALLOWED_APPS.keys())}"
        return False, "Unknown launch type."
    except Exception as e:
        return False, f"Failed to open {key}: {e}"

# ----------------- MESSAGE HANDLING & THREADED AI -----------------
def handle_send(event=None):
    user_text = entry.get().strip()
    if not user_text:
        return
    entry.delete(0, tk.END)

    insert_user_message(user_text, ts=now_ts())

    # Check for direct system command e.g. "open calci"
    m = re.match(r"^\s*open\s+([A-Za-z0-9_.-]+)\s*$", user_text, re.I)
    if m:
        app_key = m.group(1).lower()
        ok, msg = safe_launch(app_key)
        insert_bot_message(msg, ts=now_ts())
        return

    # Check if API client is available
    if client is None:
        explanation = (
            "No Gemini API key is configured yet.\n\n"
            "You can explore the chat interface and launch system apps, but AI responses "
            "are unavailable until you configure your API key.\n\n"
            "To configure your key, set the GEMINI_API_KEY (or Api_key / API_KEY) environment variable "
            "in your terminal or operating system and restart TAURUS AI."
        )
        insert_bot_message(explanation, ts=now_ts())
        return

    # Send request asynchronously to prevent UI freeze
    send_btn.config(state="disabled")
    entry.config(state="disabled")
    show_typing()

    def worker():
        bot_response = ""
        try:
            response = client.models.generate_content(
                model=model,
                contents=user_text
            )
            bot_response = response.text if (response and response.text) else "Received an empty response from Gemini."
        except Exception as e:
            err_msg = str(e).lower()
            if "quota" in err_msg or "exhausted" in err_msg or "429" in err_msg:
                bot_response = "Free-tier API quota reached. Please try again later or check your Gemini plan."
            elif "network" in err_msg or "connection" in err_msg or "timeout" in err_msg:
                bot_response = "Network connection error while contacting Gemini API. Please check your internet connection."
            else:
                bot_response = f"Error communicating with AI: {e}"

        def on_complete():
            remove_typing()
            insert_bot_message(bot_response, ts=now_ts())
            send_btn.config(state="normal")
            entry.config(state="normal")
            entry.focus_set()

        root.after(0, on_complete)

    threading.Thread(target=worker, daemon=True).start()

# Bindings
send_btn.config(command=handle_send)
entry.bind("<Return>", handle_send)
root.bind("<F11>", lambda e: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
root.bind_all("<Escape>", lambda e: root.destroy())

# Welcome message
def display_welcome_message():
    if client is None:
        welcome_text = (
            "Welcome to TAURUS AI! No Gemini API key is configured yet. "
            "You can explore the chat interface, but AI responses are unavailable until you configure your API key.\n\n"
            "• You can still launch system apps right now by typing commands like `open listapps` or `open calci`.\n"
            "• To enable AI features, set the GEMINI_API_KEY environment variable and restart TAURUS AI.\n\n"
            "Tip: Press F11 to toggle fullscreen, Esc to close & exit."
        )
    else:
        welcome_text = (
            "Welcome to TAURUS AI — your personal assistant.\n\n"
            "• Ask questions, get answers, and explore ideas.\n"
            "• Type commands like `open listapps` to launch system applications.\n\n"
            "Tip: Press F11 to toggle fullscreen, Esc to close & exit."
        )
    insert_bot_message(welcome_text)

display_welcome_message()
entry.focus_set()

if __name__ == "__main__":
    root.mainloop()

