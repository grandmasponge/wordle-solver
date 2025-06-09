file_words = []  # List to store words from the file
five_letter_words = []  # List to store 5-letter words

def read_file():
    """Read words from words.txt and store them in file_words list"""
    global file_words
    with open('words.txt', 'r') as file:
        for line in file:
           
            file_words.append(line.strip())

def write_file():
    """Write 5-letter words to five_letter_words.txt"""
    global file_words, five_letter_words
    with open('five_letter_words.txt', 'w') as file:
        for word in file_words:
            if len(word) == 5:  # If our word has five letters
                five_letter_words.append(word)  # Add to our 5-letter words list
                file.write(word + '\n')  # Write with newline


read_file()
write_file()


green_letters = []  # Correct letters in correct position
green_positions = []  # Positions of green letters
yellow_letters = []  # Correct letters in wrong position
yellow_positions = []  # Positions of yellow letters
invalid_letters = []  # Letters not in the word
words_left = five_letter_words.copy()  # Start with all 5-letter words

def user_guess(guess: str):
    """Process user's guess and update letter tracking lists"""
    global green_letters, green_positions, yellow_letters, yellow_positions, invalid_letters
    
    if len(guess) != 10:  # Each guess should be 5 letters + 5 results (10 chars)
        print("Guess is not a valid length (should be 5 letters + 5 results)")
        return
    
    position = 1  # Tracks letter position (1-5)
    for i in range(0, 10, 2):  # Process pairs of characters (letter + result)
        guess_letter = guess[i].lower()
        guess_result = guess[i+1].lower()
        
        if guess_result == 'g':
            green_letters.append(guess_letter)
            green_positions.append(position)
        elif guess_result == 'y':
            yellow_letters.append(guess_letter)
            yellow_positions.append(position)
        elif guess_result == 'i':
            invalid_letters.append(guess_letter)
        else:
            print(f"Invalid result code: {guess_result}")
            return
        
        position += 1  # Move to next position

def get_words() -> list[str]:
    """Return a list of valid words based on current constraints"""
    global words_left, green_letters, green_positions, yellow_letters, yellow_positions, invalid_letters
    
    new_words = []
    
    for word in words_left:
        valid = True
        
        # Check invalid letters
        for char in word:
            if char in invalid_letters:
                valid = False
                break
        
        # Check green letters (correct position)
        for letter, pos in zip(green_letters, green_positions): # zip just takes two lists and pairs the first item in the the first list and the first item in the second lsit

            if word[pos-1] != letter:  
                valid = False
                break
        
        # Check yellow letters (present but wrong position)
        for letter, pos in zip(yellow_letters, yellow_positions):
            if letter not in word or word[pos-1] == letter:
                valid = False
                break
        
        if valid:
            new_words.append(word)
    
    return new_words

# Main game loop
game_playing = True
while game_playing:
    print("Enter your guess (5 letters + 5 results, e.g., 'crane cg ri ay ng ei')")
    print("g = green, y = yellow, i = invalid")
    guess = input().replace(" ", "")  # Remove any spaces
    
    user_guess(guess)
    possible_words = get_words()

    for word in possible_words:
        print(word)
    
    print("Are you finished? (yes/no)")
    done = input().lower()
    if done == "yes":
        game_playing = False