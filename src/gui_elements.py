import tkinter as tk
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
from game_logic import *
from settings import *

class Game(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.style = ttk.Style(self.master)
        self.style.configure("Game.TFrame", background = BG_DARK)
        self.config(style = "Game.TFrame")

        GAME_FONT = ("Consolas", 11, "bold")
        self.style.configure("Game.TLabel", font = GAME_FONT, foreground = FG_LIGHT, background = BG_DARK)
        self.style.configure("Game.TButton", font = ("Consolas", 10, "bold"))

        self.pack(fill = "both", expand = True)

        (self.char_data, self.names) = load_data(FILE_NAME)

        self.grid_labels: List[List[ttk.Label]] = []

        self.setup_game_style()

        self.create_widgets()

        self.start_new_game()

    def setup_game_style(self):
        self.style = ttk.Style(self.master)

        self.style.configure(
            "Game.TButton",
            font = ("Consolas", 10, "bold"),
            foreground = BLACK,
            background = BLUE,
            padding = [10, 5],
            relief = "flat",
            borderwidth = 0
        )

        self.style.map(
            "Game.TButton",
            background = [('active', LIGHTBLUE)],
            foreground = [('active', BLACK)]
        )

        self.style.configure(
            "Game.TCombobox",
            font = ("Consolas", 11),
            fieldbackground = BG_DARK,
            foreground = BLACK,
            selectbackground = BLUE,
            selectforeground = FG_LIGHT,
        )

        self.style.configure(
            "Game.TLabel",
            font = ("Consolas", 12),
            foreground = FG_LIGHT,
            backbround = BG_DARK
        )

        self.style.configure(
            "GameTitle.TLabel",
            font = ("Consolas", 20, "bold"),
            foreground = BLUE,
            background = BG_DARK
        )

    def create_widgets(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 0)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_rowconfigure(3, weight = 1)

        ttk.Label(
            self,
            text = "GUESS THE RUSTY LAKE CHARACTER",
            style = "GameTitle.TLabel"
        ).grid(row = 0, column = 1, pady = (20, 10))

        self.input_frame = ttk.Frame(self, padding = 15, style = "Gamr.TFrame")
        self.input_frame.grid(row = 1, column = 1, pady = 10)

        self.input_frame.grid_columnconfigure(0, weight = 0)
        self.input_frame.grid_columnconfigure(1, weight = 0)

        self.combobox = AutocompleteCombobox(
            self.input_frame,
            completevalues = self.names,
            width = 30,
            style = "Game.TCombobox"
        )
        self.combobox.grid(row = 0, column = 0, padx = (0, 10))

        self.guess_button = ttk.Button(
            self.input_frame,
            text = "GUESS",
            command = self.process_guess,
            style = "Game.TButton"
        )
        self.guess_button.grid(row = 0, column = 1)

        self.status_label = ttk.Label(
            self,
            text = "",
            font = ("Consolas", 14, "bold"),
            foreground = RED,
            background = BG_DARK,
            justify = "center"
        )
        self.status_label.grid(row = 2, column = 1, pady = (0, 10))

        self.grid_frame = ttk.Frame(self, padding = 10, style = "Game.TFrame")
        self.grid_frame.grid(row = 3, column = 1, sticky = 'n')

        for i in range(MAX_GUESS):
            row_labels = []
            for j in range(MAX_TILES):
                label = tk.Label(
                    self.grid_frame,
                    text = "",
                    bg = BG_DARK,
                    fg = FG_LIGHT,
                    font = ("Consolas", 10, "bold"),
                    wraplength = 100,
                    relief = "flat",
                    borderwidth = 1,
                    width = 15,
                    height = 5
                )
                self.grid_frame.grid_columnconfigure(j, weight = 1)
                self.grid_frame.grid_rowconfigure(i, weight = 1)

                label.grid(row = i, column = j, padx = 4, pady = 4, sticky = "nsew")
                row_labels.append(label)

            self.grid_labels.append(row_labels)

        self.end_game_frame = ttk.Frame(self, padding = 15, style = "Game.TFrame")

        self.replay_button = ttk.Button(
            self.end_game_frame,
            text = "REPLAY",
            command = self.start_new_game,
            style = "Game.TButton"
        )
        self.replay_button.pack(side = "left", padx = 5)

        self.exit_button = ttk.Button(
            self.end_game_frame,
            text = "EXIT",
            command = self.quit,
            style = "Game.TButton"
        )
        self.exit_button.pack(side = "right", padx = 5)

    def start_new_game(self):
        self.answer = select_secret_character(self.char_data)
        print(self.answer.name)
        self.guess_cnt = 0

        self.status_label.config(
            text = f"You have {MAX_GUESS} chances.",
            foreground = FG_LIGHT,
            background = BG_DARK,
            font = ("Consolas", 14, "bold")            
        )
        
        self.combobox.config(state = "normal")
        self.combobox.set("")
        self.combobox.focus_set()

        self.guess_button.config(state = "normal")

        try:
            self.end_game_frame.grid_forget()
        except:
            pass

        self.input_frame.grid(row = 1, column = 1, pady = 10)
        self.clear_grid()

    def clear_grid(self):
        for row in self.grid_labels:
            for label in row:
                label.config(
                    text = "",
                    bg = BG_DARK,
                    fg = FG_LIGHT,
                    relief = "flat"
                )

    def process_guess(self):
        guess_name = self.combobox.get()

        if guess_name not in self.char_data:
            # self.status_label.config(
            #     text = "CHARACTER NOT FOUND!",
            #     foreground = RED,
            #     background = BG_DARK,
            #     font = ("Consolas", 14, "bold")
            # )
            # self.status_label.update()
            return
        
        guess_char = self.char_data[guess_name]

        color_list = check(guess_char, self.answer)
        self.update_grid(self.guess_cnt, color_list, guess_char)

        self.guess_cnt += 1

        is_win = all(color == GREEN for color in color_list)

        if is_win:
            self.end_game(won = True)
            return
        
        if self.guess_cnt >= MAX_GUESS:
            self.end_game(won = False)
            return
        
        remaining = MAX_GUESS - self.guess_cnt
        self.status_label.config(
            text = f"You have {remaining} chances left.",
            foreground = FG_LIGHT,
            background = BG_DARK,
            font = ("Consolas", 14)
        )

        self.combobox.set("")
        self.combobox.focus_set()

    def update_grid(self, row: int, color_list: List, guess_char: Character):
        row_labels = self.grid_labels[row]

        attributes = [
            guess_char.name,
            guess_char.gender,
            ", ".join(guess_char.status),
            f"{guess_char.first_game}\n({guess_char.release_year})",
            "Playable" if guess_char.playable else "Not Playable"
        ]

        for i, label in enumerate(row_labels):
            color = color_list[i]
            text_content = attributes[i]
            label.config(
                text = text_content,
                bg = color,
                fg = FG_LIGHT,
                relief = "raised",
                borderwidth = 2
            )
        
    def end_game(self, won: bool):
        self.combobox.config(state = "disabled")
        self.guess_button.config(state = "disabled")

        self.input_frame.grid_forget()

        if won:
            win_message = f"YOU WIN!\nThe character is {self.answer.name}"
            self.status_label.config(
                text = win_message,
                foreground = GREEN,
                background = BG_DARK,
                font = ("Consolas", 20, "bold")
            )
        else:
            lose_message = f"YOU LOSE!\nThe character is {self.answer.name}"
            self.status_label.config(
                text = lose_message,
                foreground = RED,
                background = BG_DARK,
                font = ("Consolas", 20, "bold")
            )

        self.end_game_frame.grid(row = 4, column = 1, pady = 20)