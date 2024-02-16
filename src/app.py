import tkinter as tk
from gui import BowlingGUI
from calculations import calculate_score

def main():
    root = tk.Tk()
    app = BowlingGUI(root, calculate_score)
    root.mainloop()

if __name__ == "__main__":
    main()
