from gui_elements import *
from settings import *
from ttkthemes import *

if __name__ == "__main__":
    app = ThemedTk(theme = "supperhero")
    app.title("RustyLake-dle")
    app.configure(bg = BG_DARK)
    app.geometry("900x750")
    app.resizable(width = False, height = False)
    main_app = Game(app)
    main_app.mainloop()