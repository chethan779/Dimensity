import customtkinter as ctk
import calendar
import datetime

# --- Design Tokens ---
COLOR_BG = "#0B1020"       # Deep navy background
COLOR_PANEL = "#151D2E"    # Primary surface
COLOR_SURFACE = "#1E293B"  # Secondary surface
COLOR_TODAY = "#34D399"    # Modern emerald for today
COLOR_TASK = "#FBBF24"     # Warm amber for tasks
COLOR_BDAY = "#EC4899"     # Pink/magenta for birthdays
COLOR_DEFAULT = "#1E293B"  # Default day cell
COLOR_ACCENT = "#60A5FA"   # Primary accent
COLOR_TEXT = "#F1F5F9"     # Primary text
import os

# --- System Font Detection ---
def _detect_font():
    try:
        import tkinter.font as tkfont
        fams = set(tkfont.families())
        for f in ["JetBrains Mono ExtraBold", "JetBrains Mono", "Noto Sans Mono", "Noto Sans", "Liberation Sans", "DejaVu Sans", "Ubuntu", "Segoe UI", "Arial"]:
            if f in fams:
                return f
    except Exception:
        pass
    return "JetBrains Mono"

FONT_MAIN = _detect_font()

# --- Design Tokens (Pure Black Theme) ---
COLOR_BG = "#000000"       # Pure black background
COLOR_PANEL = "#121212"    # Dark surface
COLOR_SURFACE = "#1E1E1E"  # Secondary surface
COLOR_TODAY = "#34D399"    # Modern emerald for today
COLOR_TASK = "#FBBF24"     # Warm amber for tasks
COLOR_BDAY = "#EC4899"     # Pink/magenta for birthdays
COLOR_DEFAULT = "#1E1E1E"  # Default day cell
COLOR_ACCENT = "#FB7185"   # Rose/Coral accent for calendar
COLOR_TEXT = "#FFFFFF"     # High-contrast white text
COLOR_MUTED = "#A0A0A0"    # Muted grey text

class UltimateCalendar(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("E-Calendar — Dimensity Planner")
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.geometry(f"{sw}x{sh}+0+0")
        self.configure(fg_color=COLOR_BG)
        self.attributes("-fullscreen", True)
        self.lift()
        self.focus_force()

        # Keyboard shortcuts & window exit
        self.bind_all("<Escape>", self.close_app)
        self.protocol("WM_DELETE_WINDOW", self.close_app)

        # --- Data ---
        self.today = datetime.date.today()
        self.year = self.today.year
        self.month = self.today.month
        self.selected_day = self.today.day

        self.events = {}  # {"2025-11-22": [{'text':'...', 'type':'task/bday','done':False}]}

        # Top Control Bar
        self.top_bar = ctk.CTkFrame(self, fg_color=COLOR_PANEL, height=54, corner_radius=0)
        self.top_bar.pack(side="top", fill="x")
        self.top_bar.pack_propagate(False)

        self.lbl_title = ctk.CTkLabel(
            self.top_bar, text="📅 E-Calendar Planner",
            font=(FONT_MAIN, 16, "bold"), text_color=COLOR_ACCENT
        )
        self.lbl_title.pack(side="left", padx=20)

        self.btn_close = ctk.CTkButton(
            self.top_bar, text="✕ Close (Esc)", width=110, height=34,
            fg_color=COLOR_SURFACE, hover_color="#273449",
            text_color=COLOR_TEXT, font=(FONT_MAIN, 12, "bold"),
            command=self.close_app
        )
        self.btn_close.pack(side="right", padx=16)

        # Layout Container
        self.content_container = ctk.CTkFrame(self, fg_color="transparent")
        self.content_container.pack(fill="both", expand=True, padx=24, pady=16)

        self.content_container.grid_columnconfigure(0, weight=3)
        self.content_container.grid_columnconfigure(1, weight=2)
        self.content_container.grid_rowconfigure(0, weight=1)

        # === LEFT: Calendar Panel ===
        self.frame_cal = ctk.CTkFrame(self.content_container, fg_color=COLOR_PANEL, corner_radius=12)
        self.frame_cal.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Navigation
        self.frame_nav = ctk.CTkFrame(self.frame_cal, fg_color="transparent")
        self.frame_nav.pack(fill="x", pady=15)

        self.btn_prev = ctk.CTkButton(self.frame_nav, text="◀", width=42, height=36,
                                      command=self.prev_month, fg_color=COLOR_SURFACE,
                                      hover_color="#273449", font=(FONT_MAIN, 13, "bold"))
        self.btn_prev.pack(side="left", padx=12)

        self.lbl_header = ctk.CTkLabel(self.frame_nav, text="Month Year",
                                       font=(FONT_MAIN, 20, "bold"), text_color=COLOR_TEXT)
        self.lbl_header.pack(side="left", expand=True)

        self.btn_next = ctk.CTkButton(self.frame_nav, text="▶", width=42, height=36,
                                      command=self.next_month, fg_color=COLOR_SURFACE,
                                      hover_color="#273449", font=(FONT_MAIN, 13, "bold"))
        self.btn_next.pack(side="right", padx=12)

        self.btn_today = ctk.CTkButton(self.frame_cal, text="Jump to Today",
                                       fg_color=COLOR_SURFACE, hover_color="#273449",
                                       text_color=COLOR_ACCENT, font=(FONT_MAIN, 12, "bold"),
                                       command=self.go_to_today)
        self.btn_today.pack(pady=4)

        # Grid for days
        self.frame_days = ctk.CTkFrame(self.frame_cal, fg_color="transparent")
        self.frame_days.pack(padx=12, pady=10)

        # === RIGHT: Event Panel ===
        self.frame_events = ctk.CTkFrame(self.content_container, fg_color=COLOR_PANEL, corner_radius=12)
        self.frame_events.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.lbl_event_header = ctk.CTkLabel(self.frame_events, text="Planner",
                                             font=(FONT_MAIN, 18, "bold"), text_color=COLOR_TEXT)
        self.lbl_event_header.pack(pady=15)

        self.scroll_list = ctk.CTkScrollableFrame(self.frame_events, fg_color="transparent")
        self.scroll_list.pack(fill="both", expand=True, padx=10)

        # Input for adding events
        self.frame_input = ctk.CTkFrame(self.frame_events, fg_color="transparent")
        self.frame_input.pack(fill="x", padx=10, pady=15)

        self.entry_text = ctk.CTkEntry(self.frame_input, placeholder_text="Add task or birthday...",
                                       height=38, font=(FONT_MAIN, 12),
                                       fg_color=COLOR_SURFACE, border_color="#334155")
        self.entry_text.pack(fill="x", pady=(0, 10))

        self.btn_add_task = ctk.CTkButton(
            self.frame_input, text="+ Task", height=34,
            fg_color=COLOR_TASK, hover_color="#E5A71F", text_color="#0B1020",
            font=(FONT_MAIN, 12, "bold"),
            command=lambda: self.add_item("task")
        )
        self.btn_add_task.pack(side="left", fill="x", expand=True, padx=3)

        self.btn_add_bday = ctk.CTkButton(
            self.frame_input, text="🎂 Birthday", height=34,
            fg_color=COLOR_BDAY, hover_color="#DB2777", text_color="white",
            font=(FONT_MAIN, 12, "bold"),
            command=lambda: self.add_item("bday")
        )
        self.btn_add_bday.pack(side="right", fill="x", expand=True, padx=3)

        # Initial draw
        self.update_calendar()
        self.show_events()

    def close_app(self, event=None):
        try:
            self.destroy()
        except Exception:
            pass
        if hasattr(self, "master") and self.master:
            try:
                self.master.destroy()
            except Exception:
                pass
        import sys
        sys.exit(0)

    # ---------------- CALENDAR ----------------
    def update_calendar(self):
        self.lbl_header.configure(text=f"{calendar.month_name[self.month]} {self.year}")

        for widget in self.frame_days.winfo_children():
            widget.destroy()

        # Day names
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            ctk.CTkLabel(self.frame_days, text=day, width=48, text_color=COLOR_MUTED,
                         font=(FONT_MAIN, 12, "bold")).grid(row=0, column=i, pady=(0, 6))

        # Dates
        month_matrix = calendar.monthcalendar(self.year, self.month)
        for r, week in enumerate(month_matrix):
            for c, day in enumerate(week):
                if day != 0:
                    key = f"{self.year}-{self.month}-{day}"
                    btn_color = COLOR_DEFAULT
                    text_color = COLOR_TEXT
                    has_bday = False
                    has_task = False
                    if key in self.events:
                        for item in self.events[key]:
                            if item['type'] == 'bday': has_bday = True
                            if item['type'] == 'task' and not item['done']: has_task = True
                    if has_bday:
                        btn_color = COLOR_BDAY
                        text_color = "white"
                    elif has_task:
                        btn_color = COLOR_TASK
                        text_color = "#0B1020"
                    if day == self.today.day and self.month == self.today.month and self.year == self.today.year:
                        btn_color = COLOR_TODAY
                        text_color = "#0B1020"

                    is_selected = (day == self.selected_day)
                    border = 2 if is_selected else 0
                    border_color = COLOR_ACCENT if is_selected else None
                    btn = ctk.CTkButton(
                        self.frame_days, text=str(day), width=48, height=48,
                        fg_color=btn_color, text_color=text_color,
                        border_width=border, border_color=border_color,
                        hover_color="#273449",
                        font=(FONT_MAIN, 13, "bold"),
                        command=lambda d=day: self.select_day(d)
                    )
                    btn.grid(row=r+1, column=c, padx=3, pady=3)

    def select_day(self, day):
        self.selected_day = day
        self.update_calendar()
        self.show_events()

    # ---------------- EVENTS ----------------
    def show_events(self):
        for w in self.scroll_list.winfo_children(): w.destroy()

        key = f"{self.year}-{self.month}-{self.selected_day}"
        self.lbl_event_header.configure(text=f"Plan: {key}")
        items = self.events.get(key, [])

        if not items:
            ctk.CTkLabel(self.scroll_list, text="No events planned for this day.",
                         text_color=COLOR_MUTED, font=(FONT_MAIN, 12)).pack(pady=20)
            return

        for index, item in enumerate(items):
            row = ctk.CTkFrame(self.scroll_list, fg_color=COLOR_SURFACE, corner_radius=8)
            row.pack(fill="x", pady=4, padx=2)

            chk = ctk.CTkCheckBox(
                row, text="", width=20,
                command=lambda i=index: self.toggle_done(key, i)
            )
            chk.pack(side="left", padx=8, pady=6)
            if item['done']:
                chk.select()

            display_text = item['text']
            text_col = COLOR_TEXT
            if item['type'] == 'bday':
                display_text = f"🎂 {display_text}"
                text_col = COLOR_BDAY
            if item['done']:
                text_col = COLOR_MUTED

            lbl = ctk.CTkLabel(row, text=display_text, text_color=text_col, anchor="w",
                               font=(FONT_MAIN, 12))
            lbl.pack(side="left", padx=4, fill="x", expand=True)

            btn_del = ctk.CTkButton(
                row, text="✕", width=28, height=28,
                fg_color="#F87171", hover_color="#EF4444", text_color="#0B1020",
                font=(FONT_MAIN, 11, "bold"),
                command=lambda i=index: self.delete_item(key, i)
            )
            btn_del.pack(side="right", padx=8, pady=6)

    def add_item(self, type_name):
        text = self.entry_text.get()
        if not text: return
        key = f"{self.year}-{self.month}-{self.selected_day}"
        if key not in self.events:
            self.events[key] = []
        new_item = {"text": text, "type": type_name, "done": False}
        self.events[key].append(new_item)
        self.entry_text.delete(0, "end")
        self.show_events()
        self.update_calendar()

    def delete_item(self, key, index):
        if key in self.events:
            self.events[key].pop(index)
            if not self.events[key]:
                del self.events[key]
        self.show_events()
        self.update_calendar()

    def toggle_done(self, key, index):
        self.events[key][index]['done'] = not self.events[key][index]['done']
        self.show_events()
        self.update_calendar()

    # ---------------- NAVIGATION ----------------
    def go_to_today(self):
        self.year, self.month, self.selected_day = self.today.year, self.today.month, self.today.day
        self.update_calendar()
        self.show_events()

    def next_month(self):
        self.month += 1
        if self.month > 12: self.month, self.year = 1, self.year + 1
        self.selected_day = 1
        self.update_calendar()
        self.show_events()

    def prev_month(self):
        self.month -= 1
        if self.month < 1: self.month, self.year = 12, self.year - 1
        self.selected_day = 1
        self.update_calendar()
        self.show_events()

if __name__ == "__main__":
    app = ctk.CTk()
    app.withdraw()
    cal = UltimateCalendar(app)
    cal.protocol("WM_DELETE_WINDOW", cal.close_app)
    app.bind_all("<Escape>", lambda e: cal.close_app())
    app.mainloop()
