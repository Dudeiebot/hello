import string

def coleman_liau_index():
    """
    Calculate the Coleman-Liau index of a given text and output the
    corresponding grade level required to understand it.
    """
    # Remove punctuation and convert to lowercase
    text = input("Enter a text: ")
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # Count the number of letters and words in the text
    words = text.split()
    num_letters = sum(len(word) for word in words)
    num_words = len(words)

    # Calculate the index
    L = (num_letters / num_words) * 100
    S = (len(text.split(".")) + len(text.split("?")) + len(text.split("!"))) / num_words * 100
    index = round (0.0588 * L - 0.296 * S - 15.8)
    

    # Output the grade level
    if index < 1:
        print("Grade level below 1 ")
    elif index >= 16:
        print("Grade level 16+ ")
    else:
        print("Grade level", index)

coleman_liau_index()
