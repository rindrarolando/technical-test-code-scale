import tkinter as tk

class BowlingGUI:
    def __init__(self, root, calculate_score):
        self.root = root
        self.calculate_score = calculate_score

        self.frame_label = tk.Label(root, text="Frame numéro : ")
        self.frame_label.grid(row=0, column=0)
        self.frame_entry = tk.Entry(root)
        self.frame_entry.grid(row=0, column=1)

        self.throw_label = tk.Label(root, text="Lancée numéro : ")
        self.throw_label.grid(row=1, column=0)
        self.throw_entry = tk.Entry(root)
        self.throw_entry.grid(row=1, column=1)

        self.pins_label = tk.Label(root, text="Nombre de quilles touchées : ")
        self.pins_label.grid(row=2, column=0)
        self.pins_entry = tk.Entry(root)
        self.pins_entry.grid(row=2, column=1)

        self.submit_button = tk.Button(root, text="Calculer", command=self.calculate)
        self.submit_button.grid(row=3, columnspan=2)

        self.score_label = tk.Label(root, text="Score actuel: ")
        self.score_label.grid(row=4, columnspan=2)

    def calculate(self):
        frame_number = int(self.frame_entry.get())
        throw_number = int(self.throw_entry.get())
        pins_hit = int(self.pins_entry.get())

        score = self.calculate_score(frame_number, throw_number, pins_hit)
        self.score_label.config(text=f"Score actuel: {score}")
