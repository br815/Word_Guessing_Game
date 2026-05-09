from process_file import process_file
from process_text import process_text
from game import word_guessing_game

# Boolean for main.py (MAIN) to print debug print statements if desired.
MAIN_DEBUGGER = False



if __name__ == "__main__":
    # Provide name of the sub-directory with input files.
    dir_with_texts = "texts"

    try:
        while True:
            # Attempt to get valid input text from file.
            text_in = process_file(dir_with_texts)

            # If file processing failed, user must choose another file.
            if text_in is None:
                continue

            # Attempt to process input text.
            word_list = process_text(text_in)

            # If text processing failed, user must choose another file.
            if word_list is None:
                continue

            # Valid word list generated.
            break
        # End of user input validation loop
    # Try-except block is necessary in the event that the provided directory does not exist.
    except FileNotFoundError as err_msg:
        print(err_msg)
        exit()

    if MAIN_DEBUGGER:
        print("***LIST OF VALID WORD FROM MAIN():***")
        print(word_list)
    
    test_list = ["Algorithms", "algorithmic", "algorithm", "debris", "rockstar", "callous", "germane"]
    if MAIN_DEBUGGER:
        # Call word_guessing_game() on the test list
        word_guessing_game(test_list)
    else:
        # Call word_guessing_game() on the processed word list
        word_guessing_game(word_list)
# End of main()