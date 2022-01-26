# Question 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays
# them out face down in sequence on a table. She challenges Bob to pick out the card containing a given number by turning 
# over as few cards as possible. Write a function to help Bob locate the card.

# Systematic Strategy To Apply For Solving Problems:
# 1. State the problem clearly. Identify the input & output formats.
# 2. Come up with some example inputs & outputs. Try to cover all edge cases.
# 3. Come up with a correct solution for the problem. State it in plain English.
# 4. Implement the solution and test it using example inputs. Fix bugs, if any.
# 5. Analyze the algorithm's complexity and identity inefficiencies, if any.
# 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6. 


# Test Cases
cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

# Locate card function
def locate_card(cards, query):
    # Create a variable position with the value 0
    position = 0
    
    # Set up a loop for repetition 
    while True:
        # Check if element at the current position matches the query 
        if cards[position] == query:
            # Answer found! Return and exit...
            return position 
        # Increment the position 
        position += 1
        
        # Check if we have reached the end of the array
        if position == len(cards):
            # Number not found, return -1
            return -1

# Testing the function 
result = locate_card(cards, query)
print(result)

# After running tests, locate card function:
def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1
            


def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) / 2
        mid_number = cards[mid]

        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number", mid_number )

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1
    return -1

# Helper Function for locate_cards
def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, " mid_number", mid_number)
    if mid_number == query:
        if mid - 1 >= 0 and cards[mid-1] == query:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "left"
    else:
        return "right"

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1
    return -1

