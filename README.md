# 🌌 Dimensity OS

**Dimensity OS** is a lightweight, modern simulated desktop operating system built with Python, Tkinter, and Pygame. It features a curated dark-mode interface, responsive app launching, built-in productivity tools, an AI assistant, and a retro game arcade.

---

## ✨ Features & Applications

### 🖥️ Desktop Environment (`diamond3.py`)
- **Modern Dark UI**: High-contrast, clean layout with live digital clock, date display, and smooth dock navigation.
- **Settings & Personalization**: Dynamic wallpaper switching, UI adjustments, and user profile management.
- **Context-Aware Navigation**: Responsive keyboard shortcuts (press `Esc` to close apps or exit from home).

### 🧮 E-Calci (`CALCI.py`)
- Full-featured scientific calculator with clean theme grading.
- Dedicated mathematical modules for **Permutations & Combinations ($^nP_r$, $^nC_r$)**.
- Sequence solvers for **Arithmetic & Geometric Progressions (AP / GP)**.

### 🤖 Taurus AI (`torrus_ai.py`)
- Integrated desktop virtual assistant powered by Google Gemini API.
- Instant conversational answers and problem-solving right from the desktop.

### 📅 E-Calendar (`ecalendar.py`)
- Interactive calendar view with date picking and day scheduling.
- Built-in task and event planner.

### 📁 E-Files (`E-Files/`)
- Integrated file management system with multi-user authentication (`users.json`).
- Categorized storage for **Text**, **Binary**, and **CSV** data.

### 🎮 E-Play Arcade
Built-in retro games powered by Pygame and Tkinter:
- 🏓 **Pong**: Classic two-player / paddle table tennis.
- 🧱 **Brick Breaker**: Physics-based paddle collision game.
- 🔤 **Hangman**: Word puzzle guessing game.
- 🏎️ **2D Asphalt**: Fast-paced top-down obstacle racing game.

---

## 🛠️ Tech Stack
- **Language**: Python 3
- **GUI Framework**: Tkinter / CustomTkinter
- **Game Engine**: Pygame
- **AI Integration**: Google GenAI SDK (Gemini API)
- **Data Storage**: JSON / Flat files

---

## 🚀 Getting Started

### Prerequisites
Make sure Python 3.9+ and the required dependencies are installed:
```bash
pip install pygame pillow google-genai
