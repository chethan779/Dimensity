import os
import sys
import time
import pickle
import csv
import subprocess
import tkinter as tk
_tk_mod = tk
from tkinter import messagebox, filedialog, Listbox, Scrollbar, END
from tkinter import scrolledtext
import tkinter.font as tkfont
from PIL import Image, ImageTk
import customtkinter as ctk

# Enable Windows DPI awareness if on Windows
try:
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
if BASE_PATH not in sys.path:
    sys.path.append(BASE_PATH)

# ==============================================================================
# SYSTEM FONT DETECTION & FALLBACKS
# ==============================================================================
def detect_system_font():
    """Detect high quality native vector fonts on Linux, macOS, or Windows."""
    try:
        fams = set(tkfont.families())
        candidates = [
            "JetBrains Mono ExtraBold", "JetBrains Mono",
            "Noto Sans Mono", "Noto Sans", "Liberation Sans", "DejaVu Sans",
            "Cantarell", "Ubuntu", "Segoe UI", "SF Pro Display", "Helvetica", "Arial"
        ]
        for f in candidates:
            if f in fams:
                return f
    except Exception:
        pass
    return "sans-serif"

FONT_MAIN = detect_system_font()
try:
    _fams = set(tkfont.families())
    FONT_EXTRABOLD = "JetBrains Mono ExtraBold" if "JetBrains Mono ExtraBold" in _fams else FONT_MAIN
except Exception:
    FONT_EXTRABOLD = FONT_MAIN

# ==============================================================================
# DESIGN SYSTEM TOKENS (PURE BLACK HIGH-CONTRAST THEME)
# ==============================================================================
THEME = {
    "bg": "#000000",                 # Pure pitch black background
    "surface_glass": "#0D0D0D",      # Deep black glass panel
    "surface_primary": "#141414",    # Jet black card surface
    "surface_secondary": "#1E1E1E",  # Secondary interactive surface
    "surface_elevated": "#2A2A2A",   # Elevated / hover surface
    "accent_primary": "#38BDF8",     # Bright sky blue
    "accent_secondary": "#00F0FF",   # Electric cyan
    "accent_green": "#34D399",       # Neon emerald
    "accent_gold": "#FFB703",        # Warm amber / gold
    "accent_aqua": "#00F5D4",        # Luminous cyber aqua
    "accent_rose": "#FB7185",        # Coral / rose
    "accent_violet": "#A78BFA",      # Vivid purple / violet
    "text_primary": "#FFFFFF",       # Pure white high-contrast text
    "text_secondary": "#A0A0A0",     # Neutral grey text
    "border": "#282828",             # Crisp border
    "border_subtle": "#1A1A1A",      # Subtle border
    "success": "#34D399",
    "warning": "#FFB703",
    "error": "#F87171",
}

# ==============================================================================
# SINGLETON WINDOW & PROCESS REGISTRY (ZERO-LAG CACHING)
# ==============================================================================
active_windows = {}
active_processes = {}
current_active_window = [None]

def hide_child_window(name, event=None):
    """Safely hide a child window and return user to the desktop home."""
    win = active_windows.get(name)
    if win is not None:
        try:
            if win.winfo_exists():
                win.withdraw()
        except Exception:
            pass
    if current_active_window[0] == name:
        current_active_window[0] = None
    return "break"

def track_cached_window(name, win):
    """Register window and attach hide-on-close handler for zero-lag instant reopening."""
    active_windows[name] = win

    win.protocol("WM_DELETE_WINDOW", lambda: hide_child_window(name))
    win.bind("<Escape>", lambda e: hide_child_window(name))

def focus_existing_window(name):
    """Bring existing running window to foreground instantly if it is already open."""
    win = active_windows.get(name)
    if win is not None:
        try:
            if win.winfo_exists():
                if hasattr(win, "_reset_home"):
                    win._reset_home()
                win.deiconify()
                win.lift()
                win.focus_force()
                current_active_window[0] = name
                return True
        except Exception:
            pass
        active_windows.pop(name, None)
    return False

def launch_singleton_process(app_name, cmd_args):
    """Launch an independent child process non-blocking with zero main thread lag."""
    proc = active_processes.get(app_name)
    if proc is not None:
        if proc.poll() is None:
            try:
                subprocess.Popen(["xdotool", "search", "--pid", str(proc.pid), "windowactivate"],
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception:
                pass
            return proc
        else:
            active_processes.pop(app_name, None)

    try:
        proc = subprocess.Popen(cmd_args, close_fds=True)
        active_processes[app_name] = proc
        return proc
    except Exception as e:
        messagebox.showerror(f"{app_name.capitalize()} Error", f"Could not launch {app_name}:\n{e}")
        return None

# ==============================================================================
# ROOT / BASE DESKTOP
# ==============================================================================
root = tk.Tk()
root.title("Dimensity 1.0")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.configure(bg=THEME["bg"])
root.attributes("-fullscreen", True)

# Desktop canvas for wallpaper & overlays (Pure Black)
canvas = tk.Canvas(root, width=screen_width, height=screen_height,
                   bg=THEME["bg"], highlightthickness=0, bd=0)
canvas.pack(fill="both", expand=True)

# ----------------- WALLPAPER RESTORATION -----------------
wallpaper_paths = [
    os.path.join(BASE_PATH, "assets", "wallpaper.png"),
    os.path.join(BASE_PATH, "assets", "Wallpaper.png"),
]
wallpaper_file = None
for p in wallpaper_paths:
    if os.path.isfile(p):
        wallpaper_file = p
        break

bg_photo_image = None
if wallpaper_file:
    try:
        raw_img = Image.open(wallpaper_file)
        raw_img = raw_img.convert("RGB")
        scaled_img = raw_img.resize((screen_width, screen_height), Image.Resampling.BILINEAR)
        bg_photo_image = ImageTk.PhotoImage(scaled_img)
        canvas.create_image(0, 0, image=bg_photo_image, anchor="nw")
    except Exception as e:
        print(f"Failed to load wallpaper: {e}")

# ==============================================================================
# PRELOAD ASSETS TO ELIMINATE APP OPENING LAG
# ==============================================================================
PRELOADED_GAME_PHOTOS = {}
games_specs = [
    ("PONG", "pong-logo.jpg", "pong", [sys.executable, os.path.join(BASE_PATH, "pong.py")], 0, 0, "#00F0FF", "🏓"),
    ("BRICK BREAKER", "brick breaker.jpg", "brick", [sys.executable, os.path.join(BASE_PATH, "collision.py")], 0, 1, "#FFB703", "🧱"),
    ("HANG MAN", "hang.jpg", "hangman", [sys.executable, os.path.join(BASE_PATH, "hangman.py")], 1, 0, "#FB7185", "🪢"),
    ("ASPHALT", "asphalt.jpg", "asphalt", [sys.executable, os.path.join(BASE_PATH, "asphalt.py")], 1, 1, "#34D399", "🏎️"),
]

def preload_game_images():
    card_w, card_h = 240, 140
    for title, icon_file, proc_name, cmd_args, row_idx, col_idx, color, emoji in games_specs:
        icon_path = os.path.join(BASE_PATH, icon_file)
        if os.path.isfile(icon_path):
            try:
                img = Image.open(icon_path)
                img = img.convert("RGB")
                img = img.resize((card_w, card_h), Image.Resampling.BILINEAR)
                PRELOADED_GAME_PHOTOS[proc_name] = ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"Preload error for {icon_file}: {e}")

preload_game_images()

# ==============================================================================
# DESKTOP CLOCK SYSTEM (Top-Right Frosted Glass Badge, Zero Collision)
# ==============================================================================
class DesktopClock:
    """Polished frosted glass desktop clock matching Dimensity UI with curated non-generic palette."""
    def __init__(self, parent_canvas):
        self.canvas = parent_canvas
        self.after_id = None

        # Frosted glass badge matching the cyber aesthetic
        self.card = tk.Frame(parent_canvas, bg="#080808",
                             highlightbackground="#1E293B", highlightthickness=1,
                             padx=20, pady=10)
        self.win_id = self.canvas.create_window(screen_width - 24, 24, anchor="ne", window=self.card)

        # Time label (Luminous Cyber Aqua #00F5D4, JetBrains Mono ExtraBold)
        self.time_lbl = tk.Label(self.card, text="", font=(FONT_EXTRABOLD, 28, "bold"),
                                 fg="#00F5D4", bg="#080808")
        self.time_lbl.pack(anchor="e", pady=(0, 2))

        # Bottom row for Day and Date with generous clearance
        self.bottom_row = tk.Frame(self.card, bg="#080808")
        self.bottom_row.pack(anchor="e")

        # Day label (Sunburst Amber Gold #FFB703, JetBrains Mono ExtraBold)
        self.day_lbl = tk.Label(self.bottom_row, text="", font=(FONT_EXTRABOLD, 12, "bold"),
                                fg="#FFB703", bg="#080808")
        self.day_lbl.pack(side="left")

        self.dot_lbl = tk.Label(self.bottom_row, text="  •  ", font=(FONT_MAIN, 11, "bold"),
                                fg="#334155", bg="#080808")
        self.dot_lbl.pack(side="left")

        # Date label (Cool Ice Hologram #7DD3FC, JetBrains Mono)
        self.date_lbl = tk.Label(self.bottom_row, text="", font=(FONT_MAIN, 11, "bold"),
                                 fg="#7DD3FC", bg="#080808")
        self.date_lbl.pack(side="left")

        self.update_clock()

    def update_clock(self):
        if not self.card.winfo_exists():
            return

        now = time.localtime()
        time_str = time.strftime("%I:%M %p", now)
        day_str = time.strftime("%A", now)
        date_str = time.strftime("%d %B %Y", now)

        if self.time_lbl.cget("text") != time_str:
            self.time_lbl.config(text=time_str)
        if self.day_lbl.cget("text") != day_str:
            self.day_lbl.config(text=day_str)
        if self.date_lbl.cget("text") != date_str:
            self.date_lbl.config(text=date_str)

        self.after_id = self.card.after(1000, self.update_clock)

    def stop(self):
        if self.after_id is not None:
            try:
                self.card.after_cancel(self.after_id)
            except Exception:
                pass
            self.after_id = None

desktop_clock = DesktopClock(canvas)

# ==============================================================================
# SETTINGS & ABOUT WINDOW (FULLSCREEN, CLEAN, ZERO-LAG INSTANT REOPENING)
# ==============================================================================
def open_settings():
    if focus_existing_window("settings"):
        return

    settings_win = tk.Toplevel(root)
    track_cached_window("settings", settings_win)
    settings_win.title("About & Settings — Dimensity")
    settings_win.geometry(f"{screen_width}x{screen_height}+0+0")
    settings_win.configure(bg=THEME["bg"])
    settings_win.attributes("-fullscreen", True)
    current_active_window[0] = "settings"

    # Header Bar
    header = tk.Frame(settings_win, bg=THEME["surface_glass"], height=56)
    header.pack(fill="x", side="top")
    header.pack_propagate(False)

    tk.Label(header, text="⚙️ Dimensity 1.0", font=(FONT_EXTRABOLD, 18, "bold"),
             fg=THEME["accent_violet"], bg=THEME["surface_glass"]).pack(side="left", padx=20)
    tk.Label(header, text="Ecosystem Settings & Information", font=(FONT_MAIN, 11),
             fg=THEME["text_secondary"], bg=THEME["surface_glass"]).pack(side="left", padx=4)

    close_btn = tk.Button(header, text="✕ Close (Esc)", font=(FONT_EXTRABOLD, 11, "bold"),
                          bg=THEME["surface_secondary"], fg=THEME["text_primary"],
                          activebackground=THEME["surface_elevated"], activeforeground=THEME["accent_primary"],
                          bd=0, padx=16, pady=6, cursor="hand2",
                          command=lambda: hide_child_window("settings"))
    close_btn.pack(side="right", padx=16)

    # Clean centered container (No visible scrollbar bar needed)
    center_frame = tk.Frame(settings_win, bg=THEME["bg"])
    center_frame.pack(fill="both", expand=True, padx=60, pady=24)

    # Card helper
    def make_card(parent, title, accent_color):
        card = tk.Frame(parent, bg=THEME["surface_primary"],
                        highlightbackground=THEME["border"], highlightthickness=1,
                        padx=24, pady=16)
        card.pack(fill="x", pady=(0, 18))
        tk.Label(card, text=title, font=(FONT_MAIN, 15, "bold"),
                 fg=accent_color, bg=THEME["surface_primary"]).pack(anchor="w", pady=(0, 10))
        return card

    # 1. About Card
    about_card = make_card(center_frame, "ℹ️ About the System", THEME["accent_secondary"])
    about_text = (
        "Dimensity is a simulated user interface desktop ecosystem created by "
        "Prism Operating Systems Limited and powered by Prism technology. "
        "Designed to behave like a lightweight, self-contained desktop operating system, it brings "
        "multiple applications together into one seamless environment. With an integrated "
        "scientific calculator, intelligent desktop clock, and file management system, Dimensity allows "
        "users to interact seamlessly. It includes a dynamic calendar planner, a built-in game library, "
        "and a personal AI chatbot powered by the Gemini API."
    )
    tk.Label(about_card, text=about_text, font=(FONT_MAIN, 12),
             fg=THEME["text_primary"], bg=THEME["surface_primary"],
             wraplength=int(screen_width * 0.75), justify="left").pack(anchor="w")

    # 2. Authors Card
    authors_card = make_card(center_frame, "👥 Authors & Contributions", THEME["accent_primary"])
    authors_data = [
        ["Dushyanth R", "Developed Pong, E-Files, AI Framework & E-Calci integration"],
        ["Jivesh",      "Built E-Calendar and Asphalt Game"],
        ["Chethan S",   "Developed Clock System, Desktop UX & TAURUS AI Assistant"],
        ["Chethan P N", "Developed Brick Breaker and Hangman"]
    ]

    table_frame = tk.Frame(authors_card, bg=THEME["surface_primary"])
    table_frame.pack(fill="x", pady=(4, 6))

    tk.Label(table_frame, text="Contributor", font=(FONT_MAIN, 12, "bold"),
             fg=THEME["accent_gold"], bg=THEME["surface_primary"], width=22, anchor="w").grid(row=0, column=0, pady=4)
    tk.Label(table_frame, text="Role & Modules", font=(FONT_MAIN, 12, "bold"),
             fg=THEME["accent_gold"], bg=THEME["surface_primary"], width=60, anchor="w").grid(row=0, column=1, pady=4)

    for r, (name, role) in enumerate(authors_data, start=1):
        bg_row = THEME["surface_secondary"] if r % 2 == 0 else THEME["surface_primary"]
        tk.Label(table_frame, text=name, font=(FONT_MAIN, 12, "bold"),
                 fg=THEME["text_primary"], bg=bg_row, width=22, anchor="w", padx=8, pady=6).grid(row=r, column=0, sticky="ew")
        tk.Label(table_frame, text=role, font=(FONT_MAIN, 12),
                 fg=THEME["text_secondary"], bg=bg_row, width=60, anchor="w", padx=8, pady=6).grid(row=r, column=1, sticky="ew")

    # 3. Roadmap Card
    roadmap_card = make_card(center_frame, "🚀 What's Next?", THEME["accent_green"])
    roadmap_text = (
        "• Session management and user profile customization\n"
        "• Weather forecast dashboard integration\n"
        "• Built-in encryption and decryption security tools\n"
        "• Enhanced multi-modal AI capabilities with offline mode"
    )
    tk.Label(roadmap_card, text=roadmap_text, font=(FONT_MAIN, 12),
             fg=THEME["text_primary"], bg=THEME["surface_primary"],
             justify="left").pack(anchor="w")

# ==============================================================================
# DESKTOP HEADER & BRANDING (Top-Left Sleek Glass Badge)
# ==============================================================================
top_badge = tk.Frame(canvas, bg=THEME["surface_glass"],
                     highlightbackground=THEME["border"], highlightthickness=1,
                     padx=16, pady=8)
canvas.create_window(24, 24, anchor="nw", window=top_badge)

tk.Label(top_badge, text="DIMENSITY 1.0", font=(FONT_MAIN, 15, "bold"),
         fg=THEME["text_primary"], bg=THEME["surface_glass"]).pack(side="left", padx=(4, 6))

tk.Label(top_badge, text="powered by PRISM", font=(FONT_MAIN, 11, "italic"),
         fg=THEME["accent_secondary"], bg=THEME["surface_glass"]).pack(side="left", padx=(0, 16))

settings_btn = tk.Button(top_badge, text="⚙️ Settings",
                         font=(FONT_MAIN, 11, "bold"),
                         bg=THEME["surface_secondary"], fg=THEME["accent_violet"],
                         activebackground=THEME["surface_elevated"], activeforeground=THEME["text_primary"],
                         bd=0, padx=12, pady=4, cursor="hand2", relief="flat",
                         command=open_settings)
settings_btn.bind("<Enter>", lambda e: settings_btn.config(bg=THEME["surface_elevated"]))
settings_btn.bind("<Leave>", lambda e: settings_btn.config(bg=THEME["surface_secondary"]))
settings_btn.pack(side="left")

# ==============================================================================
# E-FILES DIRECTORIES & LOGIC (FULLSCREEN)
# ==============================================================================
def resolve_directory(base_candidates):
    for d in base_candidates:
        if os.path.isdir(d):
            return d
    preferred = base_candidates[0]
    os.makedirs(preferred, exist_ok=True)
    return preferred

def resolve_subdir(parent, preferred, aliases):
    for name in [preferred] + aliases:
        p = os.path.join(parent, name)
        if os.path.isdir(p):
            return p
    p = os.path.join(parent, preferred)
    os.makedirs(p, exist_ok=True)
    return p

BASE_DIR = resolve_directory([
    os.path.join(BASE_PATH, "E-Files"),
    os.path.join(BASE_PATH, "E-files")
])
TEXT_DIR = resolve_subdir(BASE_DIR, "Text", ["text"])
BINARY_DIR = resolve_subdir(BASE_DIR, "binary", ["Binary"])
CSV_DIR = resolve_subdir(BASE_DIR, "CSV", ["csv"])

def open_efiles():
    if focus_existing_window("efiles"):
        return

    ewin = tk.Toplevel(root)
    track_cached_window("efiles", ewin)
    ewin.title("E-Files — Dimensity Explorer")
    ewin.geometry(f"{screen_width}x{screen_height}+0+0")
    ewin.configure(bg=THEME["bg"])
    ewin.attributes("-fullscreen", True)
    current_active_window[0] = "efiles"

    # Top Control Bar
    top_bar = tk.Frame(ewin, bg=THEME["surface_glass"], height=54)
    top_bar.pack(side="top", fill="x")
    top_bar.pack_propagate(False)

    title_lbl = tk.Label(top_bar, text="📁 E-Files Explorer", font=(FONT_EXTRABOLD, 16, "bold"),
                         fg=THEME["accent_primary"], bg=THEME["surface_glass"])
    title_lbl.pack(side="left", padx=20)

    breadcrumb_lbl = tk.Label(top_bar, text="Home", font=(FONT_MAIN, 12),
                              fg=THEME["text_secondary"], bg=THEME["surface_glass"])
    breadcrumb_lbl.pack(side="left", padx=8)

    tk.Button(top_bar, text="✕ Close (Esc)", font=(FONT_EXTRABOLD, 11, "bold"),
              bg=THEME["surface_secondary"], fg=THEME["text_primary"],
              activebackground=THEME["surface_elevated"], activeforeground=THEME["accent_primary"],
              bd=0, padx=14, pady=6, cursor="hand2",
              command=lambda: hide_child_window("efiles")).pack(side="right", padx=16)

    # Content Area
    content = tk.Frame(ewin, bg=THEME["bg"])
    content.pack(fill="both", expand=True, padx=40, pady=20)

    home_panel = tk.Frame(content, bg=THEME["bg"])
    type_panel = tk.Frame(content, bg=THEME["bg"])
    action_panel = tk.Frame(content, bg=THEME["bg"])
    for p in (home_panel, type_panel, action_panel):
        p.place(relx=0, rely=0, relwidth=1, relheight=1)

    state = {"mode": None, "file_type": None}

    def raise_panel(panel, breadcrumb=""):
        breadcrumb_lbl.config(text=f"› {breadcrumb}" if breadcrumb else "Home")
        panel.lift()

    def style_btn(parent, text, cmd, fg_col=THEME["text_primary"], **kwargs):
        cfg = {
            "font": (FONT_MAIN, 13, "bold"),
            "bg": THEME["surface_secondary"],
            "fg": fg_col,
            "activebackground": THEME["surface_elevated"],
            "activeforeground": THEME["accent_primary"],
            "bd": 0,
            "padx": 24,
            "pady": 12,
            "cursor": "hand2"
        }
        cfg.update(kwargs)
        btn = tk.Button(parent, text=text, command=cmd, **cfg)
        btn.bind("<Enter>", lambda e: btn.config(bg=THEME["surface_elevated"]))
        btn.bind("<Leave>", lambda e: btn.config(bg=cfg["bg"]))
        return btn

    def back_button(parent, cmd):
        return style_btn(parent, "◀ Back", cmd, font=(FONT_MAIN, 12, "bold"),
                         bg=THEME["surface_primary"], padx=16, pady=8)

    # Editor implementation
    def start_editor(file_type, mode="new"):
        for w in action_panel.winfo_children():
            w.destroy()

        editor_top = tk.Frame(action_panel, bg=THEME["bg"])
        editor_top.pack(fill="x", pady=(0, 10))

        tk.Label(editor_top, text=f"{mode.upper()} — {file_type.upper()} FILE",
                 font=(FONT_MAIN, 20, "bold"), fg=THEME["accent_primary"],
                 bg=THEME["bg"]).pack(side="left")

        input_row = tk.Frame(action_panel, bg=THEME["bg"])
        input_row.pack(fill="x", pady=6)

        tk.Label(input_row, text="Filename (without extension):", fg=THEME["text_primary"],
                 bg=THEME["bg"], font=(FONT_MAIN, 12, "bold")).pack(side="left", padx=(0, 10))
        fname_entry = tk.Entry(input_row, width=32, font=(FONT_MAIN, 13),
                               bg=THEME["surface_secondary"], fg=THEME["text_primary"],
                               insertbackground=THEME["accent_primary"], bd=1, relief="solid")
        fname_entry.pack(side="left")

        editor_area = scrolledtext.ScrolledText(action_panel, width=100, height=18,
                                                font=(FONT_MAIN, 12),
                                                bg=THEME["surface_primary"], fg=THEME["text_primary"],
                                                insertbackground=THEME["accent_primary"],
                                                bd=1, highlightthickness=0)
        editor_area.pack(fill="both", expand=True, pady=10)

        def perform_save():
            name = fname_entry.get().strip()
            if not name:
                messagebox.showerror("Filename", "Please provide a filename.")
                return
            ext_map = {"text": ".txt", "binary": ".bin", "csv": ".csv"}
            dir_map = {"text": TEXT_DIR, "binary": BINARY_DIR, "csv": CSV_DIR}
            final_path = os.path.join(dir_map[file_type], name + ext_map[file_type])
            content_data = editor_area.get("1.0", END)

            try:
                if file_type == "text":
                    mode_flag = "a" if mode == "append" else "w"
                    with open(final_path, mode_flag, encoding="utf-8") as f:
                        f.write(content_data)
                elif file_type == "binary":
                    lines = [ln.strip() for ln in content_data.split("\n") if ln.strip()]
                    if mode == "append" and os.path.exists(final_path):
                        existing = []
                        try:
                            with open(final_path, "rb") as f:
                                while True:
                                    try:
                                        obj = pickle.load(f)
                                        if isinstance(obj, list):
                                            existing.extend(obj)
                                        else:
                                            existing.append(obj)
                                    except EOFError:
                                        break
                        except Exception:
                            existing = []
                        lines = existing + lines
                    with open(final_path, "wb") as f:
                        pickle.dump(lines, f)
                elif file_type == "csv":
                    mode_flag = "a" if mode == "append" else "w"
                    lines = [ln for ln in content_data.split("\n") if ln.strip()]
                    with open(final_path, mode_flag, newline="", encoding="utf-8") as f:
                        writer = csv.writer(f)
                        for ln in lines:
                            writer.writerow([cell.strip() for cell in ln.split(",")])
                messagebox.showinfo("Saved", f"File saved successfully:\n{final_path}")
            except Exception as e:
                messagebox.showerror("Save Error", str(e))

        btn_row = tk.Frame(action_panel, bg=THEME["bg"])
        btn_row.pack(fill="x", pady=8)
        style_btn(btn_row, "💾 SAVE", perform_save, bg=THEME["surface_elevated"]).pack(side="left", padx=6)
        style_btn(btn_row, "Clear", lambda: editor_area.delete("1.0", END)).pack(side="left", padx=6)
        back_button(btn_row, lambda: select_type(file_type)).pack(side="right", padx=6)

        raise_panel(action_panel, f"{state['mode'].capitalize()} › {file_type.upper()} › Editor")

    # Home Panel (Choose Read or Write)
    home_center = tk.Frame(home_panel, bg=THEME["bg"])
    home_center.pack(expand=True)

    tk.Label(home_center, text="Select Operation Mode", font=(FONT_MAIN, 26, "bold"),
             fg=THEME["text_primary"], bg=THEME["bg"]).pack(pady=20)

    btns = tk.Frame(home_center, bg=THEME["bg"])
    btns.pack(pady=24)

    def go_to_type(selected_mode):
        state["mode"] = selected_mode
        for w in type_panel.winfo_children():
            w.destroy()

        tp_center = tk.Frame(type_panel, bg=THEME["bg"])
        tp_center.pack(expand=True)

        tk.Label(tp_center, text=f"{selected_mode.upper()} — Select File Format",
                 font=(FONT_MAIN, 24, "bold"), fg=THEME["accent_primary"],
                 bg=THEME["bg"]).pack(pady=20)

        tf = tk.Frame(tp_center, bg=THEME["bg"])
        tf.pack(pady=20)
        style_btn(tf, "📄 TEXT (.txt)", lambda: select_type("text"), fg_col=THEME["accent_primary"]).pack(side="left", padx=16)
        style_btn(tf, "📦 BINARY (.bin)", lambda: select_type("binary"), fg_col=THEME["accent_gold"]).pack(side="left", padx=16)
        style_btn(tf, "📊 CSV (.csv)", lambda: select_type("csv"), fg_col=THEME["accent_green"]).pack(side="left", padx=16)

        back_button(tp_center, lambda: raise_panel(home_panel, "")).pack(pady=24)
        raise_panel(type_panel, selected_mode.capitalize())

    style_btn(btns, "📖 READ ARCHIVES", lambda: go_to_type("read"), fg_col=THEME["accent_secondary"], padx=36, pady=16).pack(side="left", padx=24)
    style_btn(btns, "✏️ WRITE NEW FILES", lambda: go_to_type("write"), fg_col=THEME["accent_green"], padx=36, pady=16).pack(side="left", padx=24)

    def select_type(ftype):
        state["file_type"] = ftype
        for w in action_panel.winfo_children():
            w.destroy()

        header_lbl = tk.Label(action_panel, text=f"{state['mode'].upper()} — {ftype.upper()} ARCHIVE",
                              font=(FONT_MAIN, 22, "bold"), fg=THEME["accent_primary"],
                              bg=THEME["bg"])
        header_lbl.pack(pady=(0, 10))

        if state["mode"] == "read":
            dir_map = {"text": TEXT_DIR, "binary": BINARY_DIR, "csv": CSV_DIR}
            folder = dir_map[ftype]
            files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

            list_frame = tk.Frame(action_panel, bg=THEME["bg"])
            list_frame.pack(fill="x", pady=6)

            if not files:
                tk.Label(list_frame, text=f"No {ftype} files found in {os.path.basename(folder)}.",
                         fg=THEME["text_secondary"], bg=THEME["bg"],
                         font=(FONT_MAIN, 13)).pack(pady=16)
            else:
                tk.Label(list_frame, text="Select a file to view:", fg=THEME["text_primary"],
                         bg=THEME["bg"], font=(FONT_MAIN, 12, "bold")).pack(anchor="w")

                lb = Listbox(list_frame, bg=THEME["surface_primary"], fg=THEME["accent_secondary"],
                             selectbackground=THEME["accent_primary"], selectforeground="#000000",
                             width=60, height=6, font=(FONT_MAIN, 12), bd=1)
                lb.pack(fill="x", pady=4)
                for f in sorted(files):
                    lb.insert(END, f)

                st = scrolledtext.ScrolledText(action_panel, width=100, height=14,
                                               bg=THEME["surface_primary"], fg=THEME["text_primary"],
                                               font=(FONT_MAIN, 12), bd=1, highlightthickness=0)
                st.pack(fill="both", expand=True, pady=8)

                def open_file():
                    try:
                        sel = lb.get(lb.curselection())
                    except Exception:
                        messagebox.showwarning("Select", "Please select a file from the list first.")
                        return
                    path = os.path.join(folder, sel)
                    st.delete("1.0", END)
                    try:
                        if ftype == "text":
                            with open(path, "r", encoding="utf-8", errors="replace") as f:
                                st.insert("1.0", f.read())
                        elif ftype == "csv":
                            with open(path, encoding="utf-8", errors="replace") as f:
                                reader = csv.reader(f)
                                for r in reader:
                                    st.insert(END, ", ".join(r) + "\n")
                        elif ftype == "binary":
                            records = []
                            with open(path, "rb") as f:
                                while True:
                                    try:
                                        records.append(pickle.load(f))
                                    except EOFError:
                                        break
                            if len(records) == 1 and isinstance(records[0], list):
                                st.insert("1.0", "\n".join(str(item) for item in records[0]))
                            else:
                                st.insert("1.0", "\n".join(str(rec) for rec in records))
                    except Exception as e:
                        messagebox.showerror("Error", f"Cannot read file:\n{e}")

                btn_row = tk.Frame(action_panel, bg=THEME["bg"])
                btn_row.pack(fill="x", pady=4)
                style_btn(btn_row, "📂 OPEN SELECTED", open_file, fg_col=THEME["accent_secondary"], bg=THEME["surface_elevated"]).pack(side="left")

        else:
            write_center = tk.Frame(action_panel, bg=THEME["bg"])
            write_center.pack(expand=True)
            style_btn(write_center, "✨ Create New File",
                      lambda: start_editor(ftype, mode="new"), fg_col=THEME["accent_green"], padx=32, pady=14).pack(pady=12)
            style_btn(write_center, "➕ Append to Existing File",
                      lambda: start_editor(ftype, mode="append"), fg_col=THEME["accent_gold"], padx=32, pady=14).pack(pady=12)

        bottom_row = tk.Frame(action_panel, bg=THEME["bg"])
        bottom_row.pack(side="bottom", fill="x", pady=10)
        back_button(bottom_row, lambda: go_to_type(state["mode"])).pack(side="left")
        raise_panel(action_panel, f"{state['mode'].capitalize()} › {ftype.upper()}")

    ewin._reset_home = lambda: raise_panel(home_panel, "")
    raise_panel(home_panel, "")
    ewin.lift()
    ewin.focus_force()

# ==============================================================================
# APP LAUNCHERS (ZERO-LAG SINGLETON PROCESSES)
# ==============================================================================
def open_chatbot():
    launch_singleton_process("chatbot", [sys.executable, os.path.join(BASE_PATH, "torrus_ai.py")])

def open_calendar():
    launch_singleton_process("calendar", [sys.executable, os.path.join(BASE_PATH, "ecalendar.py")])

def open_calculator():
    launch_singleton_process("calci", [sys.executable, os.path.join(BASE_PATH, "CALCI.py")])

# ==============================================================================
# E-PLAY LAUNCHER (ZERO-LAG INSTANT GAME HUB)
# ==============================================================================
def open_eplay():
    if focus_existing_window("eplay"):
        return

    eplay_window = tk.Toplevel(root)
    track_cached_window("eplay", eplay_window)
    eplay_window.title("E-Play — Game Launcher")
    eplay_window.geometry(f"{screen_width}x{screen_height}+0+0")
    eplay_window.configure(bg=THEME["bg"])
    eplay_window.attributes("-fullscreen", True)
    current_active_window[0] = "eplay"

    # Top Bar
    top_bar = tk.Frame(eplay_window, bg=THEME["surface_glass"], height=54)
    top_bar.pack(side="top", fill="x")
    top_bar.pack_propagate(False)

    tk.Label(top_bar, text="🎮 E-Play Game Hub", font=(FONT_EXTRABOLD, 16, "bold"),
             fg=THEME["accent_green"], bg=THEME["surface_glass"]).pack(side="left", padx=20)

    tk.Button(top_bar, text="✕ Close (Esc)", font=(FONT_EXTRABOLD, 11, "bold"),
              bg=THEME["surface_secondary"], fg=THEME["text_primary"],
              activebackground=THEME["surface_elevated"], activeforeground=THEME["accent_primary"],
              bd=0, padx=14, pady=6, cursor="hand2",
              command=lambda: hide_child_window("eplay")).pack(side="right", padx=16)

    # Title area
    title_box = tk.Frame(eplay_window, bg=THEME["bg"])
    title_box.pack(pady=(28, 16))
    tk.Label(title_box, text="SELECT A GAME", font=(FONT_EXTRABOLD, 32, "bold"),
             fg=THEME["text_primary"], bg=THEME["bg"]).pack()
    tk.Label(title_box, text="Launch arcade classics directly inside Dimensity",
             font=(FONT_MAIN, 13), fg=THEME["text_secondary"], bg=THEME["bg"]).pack(pady=4)

    # 2x2 Game Cards Container
    games_container = tk.Frame(eplay_window, bg=THEME["bg"])
    games_container.pack(expand=True, pady=10)

    for title, icon_file, proc_name, cmd_args, row_idx, col_idx, card_color, emoji_icon in games_specs:
        card = tk.Frame(games_container, bg=THEME["surface_primary"],
                        highlightbackground=THEME["border"], highlightthickness=1,
                        padx=14, pady=12)
        card.grid(row=row_idx, column=col_idx, padx=24, pady=16)

        photo = PRELOADED_GAME_PHOTOS.get(proc_name)

        def make_launch_cmd(pname=proc_name, cargs=cmd_args):
            return lambda: launch_singleton_process(pname, cargs)

        if photo is not None:
            btn = tk.Button(card, image=photo, text=f"  {emoji_icon} {title}  ", compound="bottom",
                            font=(FONT_MAIN, 13, "bold"),
                            bg=THEME["surface_primary"], fg=card_color,
                            activebackground=THEME["surface_elevated"], activeforeground=THEME["text_primary"],
                            bd=0, cursor="hand2", command=make_launch_cmd())
            btn.image = photo
            btn.pack()
        else:
            btn = tk.Button(card, text=f"▶ PLAY {emoji_icon} {title}", width=22, height=6,
                            font=(FONT_MAIN, 13, "bold"),
                            bg=THEME["surface_secondary"], fg=card_color,
                            activebackground=THEME["surface_elevated"], activeforeground=THEME["text_primary"],
                            bd=0, cursor="hand2", command=make_launch_cmd())
            btn.pack()

# ==============================================================================
# DOCK (VIBRANT COLORS, APPROPRIATE EMOJIS, HIGH CONTRAST)
# ==============================================================================
dock_frame = tk.Frame(canvas, bg=THEME["surface_glass"],
                      highlightbackground=THEME["border"], highlightthickness=1,
                      padx=12, pady=6)
dock_frame.place(relx=0.5, rely=0.93, anchor="s")

DOCK_APPS = [
    {
        "emoji": "🤖",
        "title": "Taurus AI",
        "color": "#00F0FF",       # Electric Cyan
        "cmd": open_chatbot
    },
    {
        "emoji": "🎮",
        "title": "E-Play",
        "color": "#34D399",       # Neon Emerald
        "cmd": open_eplay
    },
    {
        "emoji": "🧮",
        "title": "E-Calci",
        "color": "#FBBF24",       # Radiant Gold
        "cmd": open_calculator
    },
    {
        "emoji": "📁",
        "title": "E-Files",
        "color": "#38BDF8",       # Sky Blue
        "cmd": open_efiles
    },
    {
        "emoji": "📅",
        "title": "E-Calendar",
        "color": "#FB7185",       # Coral Rose
        "cmd": open_calendar
    },
]

for app in DOCK_APPS:
    btn = tk.Button(
        dock_frame,
        text=f"{app['emoji']}  {app['title']}",
        command=app["cmd"],
        font=(FONT_MAIN, 13, "bold"),
        bg=THEME["surface_secondary"],
        fg=app["color"],
        activebackground=THEME["surface_elevated"],
        activeforeground=THEME["text_primary"],
        bd=0,
        padx=18,
        pady=10,
        cursor="hand2"
    )

    def attach_hover(b, col):
        b.bind("<Enter>", lambda e: b.config(bg=THEME["surface_elevated"], fg=THEME["text_primary"]))
        b.bind("<Leave>", lambda e: b.config(bg=THEME["surface_secondary"], fg=col))

    attach_hover(btn, app["color"])
    btn.pack(side="left", padx=6, pady=4)

# Global fullscreen & exit shortcuts
root.bind("<F11>", lambda e: root.attributes("-fullscreen", not root.attributes("-fullscreen")))

def on_desktop_close():
    desktop_clock.stop()
    for w in list(active_windows.values()):
        try:
            w.destroy()
        except Exception:
            pass
    root.destroy()

def on_desktop_escape(event=None):
    # 1. Check if a tracked child window is currently active
    active_name = current_active_window[0]
    if active_name and active_name in active_windows:
        win = active_windows[active_name]
        try:
            if win.winfo_exists() and win.state() == "normal":
                win.withdraw()
                current_active_window[0] = None
                return "break"
        except Exception:
            pass
        current_active_window[0] = None
        return "break"

    # 2. Also check any other open window in active_windows
    for name, w in list(active_windows.items()):
        try:
            if w.winfo_exists() and w.state() == "normal":
                w.withdraw()
                current_active_window[0] = None
                return "break"
        except Exception:
            pass

    # 3. If no child window is open and user is on home desktop:
    on_desktop_close()
    return "break"

root.bind_all("<Escape>", on_desktop_escape)
root.protocol("WM_DELETE_WINDOW", on_desktop_close)

# Background pre-warming for zero-lag instant app opening
def prewarm_windows():
    try:
        open_settings()
        if "settings" in active_windows:
            active_windows["settings"].withdraw()
    except Exception:
        pass
    try:
        open_efiles()
        if "efiles" in active_windows:
            active_windows["efiles"].withdraw()
    except Exception:
        pass
    try:
        open_eplay()
        if "eplay" in active_windows:
            active_windows["eplay"].withdraw()
    except Exception:
        pass
    current_active_window[0] = None

root.after(100, prewarm_windows)

if __name__ == "__main__":
    root.mainloop()
