import string

POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def compute_score(word):
    # Compute the score for the given word
    score = 0
    for letter in word:
        if letter in string.ascii_letters:                    #got to look into a lot of things that make life easier on python
            score += POINTS[ord(letter.upper()) - ord('A')]
    return score

def main():
    # Get input words from both players
    word1 = input("Player 1: ")
    word2 = input("Player 2: ")

    # Score both words
    score1 = compute_score(word1)
    score2 = compute_score(word2)

    # Print the winner
    if score1 > score2:
        print("Our winner is player 1.")
    elif score2 > score1:
        print("Our winner is player 2.")
    else:
        print("That's a tie!")

if __name__ == '__main__':  #here emsure if the code is being run independently without the need for additional software or programs to be installed or connected.
    main()   
