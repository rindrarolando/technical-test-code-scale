import tkinter as tk
from calculations import is_strike

class BowlingGUI:
    def __init__(self, root, calculate_score):
        self.root = root
        self.calculate_score = calculate_score
        self.previous_scores = []  # Initialize empty list for previous scores
        self.last_data = {'frame_number': 0, 'throw_number': 0, 'pins_hit': 0}  # Initialize last data dictionary
        self.previous_pins_hit = [0, 0]

        # Create labels for last data
        self.last_data_frame_label = tk.Label(root, text="Last Data - Frame Number : ")
        self.last_data_frame_label.grid(row=7, column=0)
        self.last_data_frame_display = tk.Label(root, text="0")
        self.last_data_frame_display.grid(row=7, column=1)

        self.last_data_throw_label = tk.Label(root, text="Last Data - Throw Number : ")
        self.last_data_throw_label.grid(row=8, column=0)
        self.last_data_throw_display = tk.Label(root, text="0")
        self.last_data_throw_display.grid(row=8, column=1)

        # Create a button to reset data
        self.reset_button = tk.Button(root, text="Reset Data", command=self.reset_data)
        self.reset_button.grid(row=9, columnspan=2)

        # Rest of the code remains the same
        self.frame_label = tk.Label(root, text="Frame number : ")
        self.frame_label.grid(row=0, column=0)
        self.frame_entry = tk.Entry(root)
        self.frame_entry.grid(row=0, column=1)

        self.throw_label = tk.Label(root, text="Throw number : ")
        self.throw_label.grid(row=1, column=0)
        self.throw_entry = tk.Entry(root)
        self.throw_entry.grid(row=1, column=1)

        self.pins_label = tk.Label(root, text="Pins hit : ")
        self.pins_label.grid(row=2, column=0)
        self.pins_entry = tk.Entry(root)
        self.pins_entry.grid(row=2, column=1)

        self.submit_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.submit_button.grid(row=3, columnspan=2)

        self.score_label = tk.Label(root, text="Actual Score : ")
        self.score_label.grid(row=4, columnspan=2)
        
        self.strike_or_spare_label = tk.Label(root, text="Strike ? Spare ?")
        self.strike_or_spare_label.grid(row=5, column=0)
        
        self.got_it_button_strike_or_spare = tk.Button(root, text="Got it", command=self.got_it_strike_or_spare)
        self.got_it_button_strike_or_spare.grid(row=5, column=1)
        
        self.bonus_label = tk.Label(root, text="Bonus ?")
        self.bonus_label.grid(row=6, column=0)
        
        self.got_it_button_bonus = tk.Button(root, text="Got it", command=self.got_it_bonus)
        self.got_it_button_bonus.grid(row=6, column=1)

    def calculate(self):
        # Get input values from entry fields
        try:
            frame_number = int(self.frame_entry.get())
            throw_number = int(self.throw_entry.get())
            pins_hit = int(self.pins_entry.get())
        except ValueError:
            # Display error message if input is not a valid integer
            self.score_label.config(text="Error: Invalid input")
            return

        # Check for valid input values
        if not (1 <= frame_number <= 5 and 1 <= throw_number <= 4 and 0 <= pins_hit <= 15):
            self.score_label.config(text="Error: Invalid input")
            return
        
        # Reset previous_pins_hit if it's a new frame
        if frame_number != self.last_data['frame_number']:
            self.previous_pins_hit = [0, 0]

        # Calculate score and update GUI
        score, strike = self.calculate_score(frame_number, throw_number, pins_hit)
        self.previous_scores.append(score)  # Add current frame's score to the list of previous frames
        self.score_label.config(text=f"Actual Score: {sum(self.previous_scores)}")  # Display total score
        
        if strike is True:
            self.strike_or_spare_label.config(text="IT IS A STRIKE !!!")
            if self.check_bonus(frame_number):
                self.bonus_label.config(text="Last Frame, additional throws allowed !")
        
        total_pins_hit = sum(self.previous_pins_hit[:throw_number]) + pins_hit
        
        if strike is False and self.is_spare_second_throw(total_pins_hit, 2):
            self.strike_or_spare_label.config(text="IT IS A SPARE !!!")
            if self.check_bonus(frame_number):
                self.bonus_label.config(text="Last Frame, additional throws allowed !")
        elif strike is False and self.is_spare_third_throw(total_pins_hit, 3):
            self.strike_or_spare_label.config(text="IT IS A SPARE !!!")
            if self.check_bonus(frame_number):
                self.bonus_label.config(text="Last Frame, additional throws allowed !")

        if throw_number<3: 
            self.previous_pins_hit[throw_number - 1] = pins_hit
            
        # Update last data
        self.last_data['frame_number'] = frame_number
        self.last_data['throw_number'] = throw_number
        self.update_last_data()

    def update_last_data(self):
        # Update the labels with the last data
        self.last_data_frame_display.config(text=str(self.last_data['frame_number']))
        self.last_data_throw_display.config(text=str(self.last_data['throw_number']))

    def reset_data(self):
        # Clear previous frames and reset last data
        self.previous_scores = []
        self.last_data = {'frame_number': 0, 'throw_number': 0}
        self.update_last_data()
        self.score_label.config(text="Actual Score: 0")
    
    def is_spare_second_throw(self, total_pins_hit, throw_number):
        # Check if it's a spare on the second throw
        return total_pins_hit == 15 and throw_number == 2

    def is_spare_third_throw(self, total_pins_hit, throw_number):
        # Check if it's a spare on the third throw
        return total_pins_hit == 15 and throw_number == 3
    
    def check_bonus(self, frame_number):
        if frame_number == 5:
            return True
        return False
    
    def got_it_strike_or_spare(self):
        self.strike_or_spare_label.config(text="Strike ? Spare ?")
            
    def got_it_bonus(self):
        self.bonus_label.config(text="Bonus ?")
