# Function to check if it is a strike
def is_strike(pins_hit, throw_number):
    return pins_hit == 15 and throw_number == 1

def calculate_score(frame_number, throw_number, pins_hit):
    score = 0
    strike = False
    
    # Calculate score for current frame
    if is_strike(pins_hit, throw_number):  # Strike
        score += 15
        strike = True
    else:
        score += pins_hit  # Add pins hit for current throw

    return score, strike


