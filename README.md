# 🦉 RustyLake-dle (Rusty Lake Character Guessing Game)

## 🎮 Rusty Lake Wordle Game - Individual Project

A character guessing game based on the Wordle/LoLdle format, developed using **Python** and the **Tkinter/ttkwidgets** libraries.

---

## 💻 Tech Stack

* **Primary Language:** Python
* **GUI Library:** Tkinter
* **GUI Enhancements:**
    * `ttkthemes` (for customizable themes)
    * `ttkwidgets` (for advanced widgets like the Auto-complete Combobox)
* **Data Handling:** `json` (for managing character database)
* **Other Libraries:** `dataclasses`, `typing` (part of Python Standard Library, used for code structure/hints)

---

## ✨ Features (Key Highlights) 🦉

* **Minimalist Tkinter UI/UX:** A clean, desktop-focused interface built.
* **Limited Attempts:** Allows a maximum of 6 guesses per game.
* **Intelligent Input:** Features an **auto-complete combobox** to easily input and select character names from the database using.
* **Visual Grid:** Displays a 6x5 game grid.
* **Attribute Feedback:** Provides color-coded feedback:
    * **Name:** Exact name match (Green) or **correct family** (Yellow).
    * **Gender**
    * **Status (List-based):** Full status match (Green) or **at least one shared status** (Yellow).
    * **First Game (Release Year):** Correct game title (Green) or the correct **release year only** (Yellow).
    * **Playable (Boolean)**
* **Color-Coded Results (Green, Yellow, Red):**
    * **Green (🟩):** Attribute is a **perfect match**.
    * **Yellow (🟨):** Attribute is a **partial match**.
    * **Red (🟥):** Attribute is **completely incorrect**.
* **Game State Display:** Clearly shows the remaining number of guesses and provides clear **Win/Loss messages** upon game completion.

---

## ⚙️ Prerequisites

To run this game, ensure you have the following installed on your system:

1. **Python 3.x**
2. The required Python libraries (listed in 'requirements.txt').

---

## 🚀 Installation and Setup

Follow these steps in your Terminal or Command Prompt:

### 1. Download the Source Code & Asset Folder

If you have cloned the repository, skip this step. If you received the code as a ZIP file, navigate to the extracted directory.

```Bash
# Optional: If downloading from GitHub (include Asset Folder)
git clone https://github.com/Lengoc06/rusty-lake-world-python.git
cd rusty-lake-world-python
```

Download Asset folder at: 
Extract to the same folder as ```main.py```
```Bash
# Folder Structure
.
├── asset
│ ├── answers.txt
│ └── allowed.txt
├── main.py
├── settings.py
├── sprite.py
└── ...
```

### 2. Install Dependencies

Install all necessary libraries using the requirements.txt file:

```Bash
pip install -r requirements.txt
```

### 3. Run the Game

Start the game using the main Python file:

```Bash
python main.py
```

---

## 🕹️ How to Play

1.  **The Goal:** Guess the mystery character within a limited number of attempts.
2.  **Make a Guess:** Start typing the character's name into the auto-complete input field. Select a name from the suggested list.
3.  **Submit:** Click the **Submit** button.
4.  **Analyze the Hints:** A panel of 5 attributes will display color-coded feedback. Use the rules below to interpret the results:
    * **🟩 Green:** The attribute is a perfect match.
    * **🟨 Yellow:** The attribute is a partial match (e.g., correct family name, correct release year, or one of the correct statuses matched).
    * **🟥 Red:** The attribute is incorrect.
5.  **Continue:** Use the color cues to eliminate incorrect characters and zero in on the solution.

---

## 🙏 Acknowledgements

* **Game Concept:** Inspired by the mechanics of the popular daily guessing games **Wordle** and **LoLdle**.
    * **Wordle:** https://www.nytimes.com/games/wordle/index.html
    * **LoLdle:** https://loldle.net/classic

* **Character Data:** Data compiled and referenced primarily from the **Rusty Lake Wiki** and official **Rusty Lake/Cube Escape** games.
    * **Rusty Lake wiki:** https://rusty-lake.fandom.com/wiki/Category:Characters
    * **Rusty Lake official website:** https://www.rustylake.com/

* **AI Assistance:** Special thanks to **Gemini AI** for providing assistance during the development and documentation phases, including:
    * Structuring and refining the content of this `README.md` file.
    * **Supporting the Graphical User Interface (GUI) development** by providing code snippets, structural advice, and assistance with integrating Tkinter, `ttkthemes`, and the **`ttkwidgets` Auto-complete Combobox**.

Sincere thanks to the Rusty Lake developers for creating such a rich and fascinating game universe!

This implementation is an individual adaptation and application of the learned techniques.