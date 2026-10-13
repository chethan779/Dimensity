import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------------------
# WORD CATEGORIES WITH LEVELS
# ---------------------------------------
WORDS = {
    "Animals": {
        "Easy": ["cat", "dog", "cow", "lion"],
        "Medium": ["elephant", "giraffe", "dolphin"],
        "Hard": ["chameleon", "hippopotamus", "orangutan"]
    },
    "Countries": {
        "Easy": ["india", "china", "egypt"],
        "Medium": ["brazil", "australia", "germany"],
        "Hard": ["kazakhstan", "uzbekistan", "switzerland"]
    },
    "Food": {
        "Easy": ["rice", "milk", "bread"],
        "Medium": ["noodles", "dosa", "biryani"],
        "Hard": ["guacamole", "lasagna", "tiramisu"]
    },
    "Technology": {
        "Easy": ["mouse", "robot", "phone"],
        "Medium": ["python", "laptop", "android"],
        "Hard": ["microprocessor", "neuralnetwork", "encryption"]
    },
    "Space": {
        "Easy": ["sun", "moon", "star"],
        "Medium": ["planet", "galaxy", "nebula"],
        "Hard": ["supernova", "andromeda", "exoplanet"]
    }
}

# Hangman pictures (unchanged)
HANGMAN_PICS = [
    """
    +---+
        |
        |
        |
       ===
    """,
    """
    +---+
    O   |
        |
        |
       ===
    """,
    """
    +---+
    O   |
    |   |
        |
       ===
    """,
    """
    +---+
    O   |
   /|   |
        |
       ===
    """,
    """
    +---+
    O   |
   /|\\  |
        |
       ===
    """,
    """
    +---+
    O   |
   /|\\  |
   /    |
       ===
    """,
    """
    +---+
    O   |
   /|\\  |
   / \\  |
       ===
    """
]


# ---------------------------------------
# SYSTEM FONT DETECTION & THEMING
# ---------------------------------------
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

THEME = {
    "bg": "#000000",
    "surface": "#121212",
    "surface_sec": "#1E1E1E",
    "surface_elevated": "#2A2A2A",
    "accent": "#F43F5E",
    "accent_cyan": "#00E5FF",
    "text": "#FFFFFF",
    "text_muted": "#A0A0A0",
    "border": "#282828",
    "btn_action": "#34D399",
}

# ---------------------------------------
# MAIN GAME CLASS
# ---------------------------------------
class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Hangman Game — Dimensity")
        self.root.configure(bg=THEME["bg"])

        try:
            sw = self.root.winfo_screenwidth()
            sh = self.root.winfo_screenheight()
            self.root.geometry(f"{sw}x{sh}+0+0")
            self.root.attributes("-fullscreen", True)
        except Exception:
            self.root.geometry("800x650")

        self.root.bind("<Escape>", lambda e: self.root.destroy())

        # Top Control Bar
        self.top_bar = tk.Frame(self.root, bg=THEME["surface"], height=52)
        self.top_bar.pack(side="top", fill="x")
        self.top_bar.pack_propagate(False)

        tk.Label(self.top_bar, text="🎮 Hangman Arcade", font=(FONT_MAIN, 15, "bold"),
                 fg=THEME["accent"], bg=THEME["surface"]).pack(side="left", padx=20)

        tk.Button(self.top_bar, text="✕ Close (Esc)", font=(FONT_MAIN, 11, "bold"),
                  bg=THEME["surface_sec"], fg=THEME["text"],
                  activebackground=THEME["surface_elevated"], activeforeground=THEME["text"],
                  bd=0, padx=14, pady=6, cursor="hand2",
                  command=self.root.destroy).pack(side="right", padx=16)

        # Main Central Container
        self.container = tk.Frame(self.root, bg=THEME["bg"])
        self.container.pack(fill="both", expand=True)

        self.category = tk.StringVar(value="Animals")
        self.level = tk.StringVar(value="Easy")

        self.create_settings_ui()

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # ---------------------------------------
    # SETTINGS SCREEN
    # ---------------------------------------
    def create_settings_ui(self):
        self.clear_container()

        center_card = tk.Frame(self.container, bg=THEME["surface"],
                               highlightbackground=THEME["border"], highlightthickness=1,
                               padx=36, pady=32)
        center_card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(center_card, text="🎮 HANGMAN GAME", font=(FONT_MAIN, 24, "bold"),
                 fg=THEME["accent"], bg=THEME["surface"]).pack(pady=(0, 6))

        tk.Label(center_card, text="Classic word puzzle powered by Dimensity",
                 font=(FONT_MAIN, 12), fg=THEME["text_muted"], bg=THEME["surface"]).pack(pady=(0, 20))

        tk.Label(center_card, text="Select Category:", font=(FONT_MAIN, 13, "bold"),
                 fg=THEME["text"], bg=THEME["surface"]).pack(anchor="w", pady=(8, 4))
        cat_menu = tk.OptionMenu(center_card, self.category, *WORDS.keys())
        cat_menu.config(font=(FONT_MAIN, 12), bg=THEME["surface_sec"], fg=THEME["text"],
                        activebackground=THEME["surface_elevated"], activeforeground=THEME["accent"],
                        bd=0, highlightthickness=0, width=22)
        cat_menu["menu"].config(bg=THEME["surface_sec"], fg=THEME["text"], font=(FONT_MAIN, 12))
        cat_menu.pack(pady=(0, 12))

        tk.Label(center_card, text="Select Difficulty:", font=(FONT_MAIN, 13, "bold"),
                 fg=THEME["text"], bg=THEME["surface"]).pack(anchor="w", pady=(8, 4))
        lvl_menu = tk.OptionMenu(center_card, self.level, "Easy", "Medium", "Hard")
        lvl_menu.config(font=(FONT_MAIN, 12), bg=THEME["surface_sec"], fg=THEME["text"],
                        activebackground=THEME["surface_elevated"], activeforeground=THEME["accent"],
                        bd=0, highlightthickness=0, width=22)
        lvl_menu["menu"].config(bg=THEME["surface_sec"], fg=THEME["text"], font=(FONT_MAIN, 12))
        lvl_menu.pack(pady=(0, 24))

        start_btn = tk.Button(center_card, text="▶ START GAME", font=(FONT_MAIN, 13, "bold"),
                              command=self.start_game, bg=THEME["surface_elevated"], fg=THEME["accent_cyan"],
                              activebackground=THEME["surface_sec"], activeforeground=THEME["text"],
                              bd=0, padx=28, pady=10, cursor="hand2")
        start_btn.pack(pady=4)

    # ---------------------------------------
    # START GAME
    # ---------------------------------------
    def start_game(self):
        self.word = random.choice(WORDS[self.category.get()][self.level.get()])
        self.guessed = ["_"] * len(self.word)
        self.used = []
        self.wrong = 0

        # Hints
        if self.level.get() == "Easy":
            self.guessed[0] = self.word[0]
            self.guessed[-1] = self.word[-1]
        elif self.level.get() == "Medium":
            if len(self.word) > 0:
                idx = random.randint(0, len(self.word) - 1)
                self.guessed[idx] = self.word[idx]

        self.build_game_ui()

    # ---------------------------------------
    # GAME UI
    # ---------------------------------------
    def build_game_ui(self):
        self.clear_container()

        game_card = tk.Frame(self.container, bg=THEME["surface"],
                             highlightbackground=THEME["border"], highlightthickness=1,
                             padx=40, pady=24)
        game_card.place(relx=0.5, rely=0.5, anchor="center")

        self.hangman_label = tk.Label(game_card, text=HANGMAN_PICS[self.wrong],
                                      font=("Courier", 13, "bold"), justify="left",
                                      fg=THEME["accent_cyan"], bg=THEME["surface"])
        self.hangman_label.pack(pady=(0, 10))

        self.word_label = tk.Label(game_card, text=" ".join(self.guessed),
                                   font=(FONT_MAIN, 26, "bold"),
                                   fg=THEME["text"], bg=THEME["surface"])
        self.word_label.pack(pady=10)

        self.used_label = tk.Label(game_card, text="Used: ", font=(FONT_MAIN, 12),
                                   fg=THEME["text_muted"], bg=THEME["surface"])
        self.used_label.pack(pady=4)

        input_frame = tk.Frame(game_card, bg=THEME["surface"])
        input_frame.pack(pady=10)

        self.entry = tk.Entry(input_frame, font=(FONT_MAIN, 16), width=6, justify="center",
                              bg=THEME["surface_sec"], fg=THEME["accent"],
                              insertbackground=THEME["text"], bd=1, relief="solid")
        self.entry.pack(side="left", padx=8)
        self.entry.focus()
        self.entry.bind("<Return>", lambda e: self.check_guess())

        tk.Button(input_frame, text="Guess", font=(FONT_MAIN, 12, "bold"),
                  command=self.check_guess, bg=THEME["surface_elevated"], fg=THEME["text"],
                  activebackground=THEME["surface_sec"], activeforeground=THEME["accent"],
                  bd=0, padx=16, pady=6, cursor="hand2").pack(side="left", padx=4)

        btn_row = tk.Frame(game_card, bg=THEME["surface"])
        btn_row.pack(pady=14)

        tk.Button(btn_row, text="💡 Hint", font=(FONT_MAIN, 11, "bold"),
                  command=self.hint, bg=THEME["surface_sec"], fg=THEME["text_muted"],
                  bd=0, padx=14, pady=6, cursor="hand2").pack(side="left", padx=6)

        tk.Button(btn_row, text="◀ Menu", font=(FONT_MAIN, 11, "bold"),
                  command=self.create_settings_ui, bg=THEME["surface_sec"], fg=THEME["text_muted"],
                  bd=0, padx=14, pady=6, cursor="hand2").pack(side="left", padx=6)

    # ---------------------------------------
    # CHECK GUESS
    # ---------------------------------------
    def check_guess(self):
        letter = self.entry.get().lower().strip()
        self.entry.delete(0, tk.END)

        if not letter.isalpha() or len(letter) != 1:
            messagebox.showwarning("Invalid", "Enter a single letter!")
            return

        if letter in self.used:
            messagebox.showwarning("Used", "You already used that letter!")
            return

        self.used.append(letter)

        if letter in self.word:
            for i, ch in enumerate(self.word):
                if ch == letter:
                    self.guessed[i] = letter
        else:
            self.wrong += 1

        self.update_ui()

    # ---------------------------------------
    # HINT SYSTEM
    # ---------------------------------------
    def hint(self):
        unopened = [i for i, ch in enumerate(self.guessed) if ch == "_"]
        if unopened:
            idx = random.choice(unopened)
            self.guessed[idx] = self.word[idx]
            self.update_ui()

    # ---------------------------------------
    # UPDATE UI
    # ---------------------------------------
    def update_ui(self):
        idx = min(self.wrong, len(HANGMAN_PICS) - 1)
        self.hangman_label.config(text=HANGMAN_PICS[idx])
        self.word_label.config(text=" ".join(self.guessed))
        self.used_label.config(text="Used: " + ", ".join(self.used))

        if "_" not in self.guessed:
            messagebox.showinfo("WIN 🎉", f"You guessed the word: {self.word}")
            self.create_settings_ui()

        elif self.wrong >= len(HANGMAN_PICS) - 1:
            messagebox.showerror("GAME OVER 💀", f"The word was: {self.word}")
            self.create_settings_ui()


# ---------------------------------------
# RUN THE GAME (safe wrapper)
# ---------------------------------------
def run_hangman(parent_window=None):
    """
    parent_window: if provided -> embed in a Toplevel attached to parent_window
                   if None -> run in standalone Tk() (useful for subprocess)
    """
    if parent_window is None:
        # Standalone mode: create independent root and run mainloop
        root = tk.Tk()
        HangmanGUI(root)
        root.mainloop()
        return None
    else:
        # Embedded mode: create a Toplevel attached to the parent window
        try:
            win = tk.Toplevel(parent_window)
        except Exception:
            # fallback: if something went wrong with Toplevel, create independent Tk
            root = tk.Tk()
            HangmanGUI(root)
            root.mainloop()
            return None

        # Make the toplevel behave well with the parent (no aggressive grab)
        win.transient(parent_window)
        try:
            win.focus_force()
        except Exception:
            pass

        # install safe close handler that does minimal cleanup
        def _on_close():
            try:
                # if current grab belongs to this window, release it safely
                if win.grab_current() is not None:
                    try:
                        win.grab_release()
                    except Exception:
                        pass
            except Exception:
                pass
            try:
                win.destroy()
            except Exception:
                pass
            try:
                parent_window.focus_force()
            except Exception:
                pass

        win.protocol("WM_DELETE_WINDOW", _on_close)

        # build UI and return immediately (non-blocking)
        HangmanGUI(win)
        return win


# Allow running hangman.py directly
if __name__ == "__main__":
    run_hangman(parent_window=None)
