from pathlib import Path
# Boolean for process_file.py (PF) to print debug print statements if desired.
PF_DEBUGGER = False



def select_file_from_dir(dir_name):
    # Build path to target directory.
    dir = Path(dir_name)

    # List comprehension used to get all files in the target directory.
    files = [
        file 
        for file 
        in dir.iterdir() 
        if file.is_file()]

    # First make sure that the list contains any files to begin with.
    if len(files) == 0:
        #print("ERROR: Folder \"%s\" contains no files." %dir_name)
        #return None
        # Instead of returning None (which results in an infinite loop in main()), raise an exception.
        raise FileNotFoundError("ERROR: Folder \"%s\" contains no files." %dir_name)

    # Display files with numbers & parantheses: 1), 2), ... etc.
    print("\nPlease select an input file from the following list:")
    for number, file in enumerate(files, start=1):
        print(f"{number}) {file.name}")

    # User input validation loop.
    while True:
        user_input = input("Choose a file number: ").strip()

        # Case 1: input is not int only.
        if not user_input.isdigit():
            print("ERROR: Input must be within valid range and contain no other characters.")
            continue

        # If this point has been reached, input must be an int and can be cast as such.
        choice = int(user_input)

        # Case 2: int is out of range.
        if choice < 1 or choice > len(files):
            print("ERROR: %i is outside valid range." %choice)
            continue

        # Valid input received.
        break
    # End of user input validation loop

    # Choose user-specified file.
    selected_file = files[choice-1]

    return selected_file
# End of select_file_from_dir()



def read_selected_file(input_file):
    # Read selected file.
    with open(input_file, "r", encoding="utf-8") as f:
        input_file_text = f.read()

    # Ensure that the file contains text (ie. doesn't contain only whitespace).
    if input_file_text.strip() == "":
        print("ERROR: File \"%s\" contains no text." %input_file.name)
        return None
    
    return input_file_text
# End of read_selected_file()



# Function to print list of filenames in a given directory,
# prompt user to select a file, open file and read in its contents,
# and return the contents.
def process_file(directory_name):

    selected_file = select_file_from_dir(directory_name)

    raw_text = read_selected_file(selected_file)

    if PF_DEBUGGER:
        print("***RAW_TEXT FROM PROCESS_FILE() IS:***\n\"%s\"" %raw_text)
    
    return raw_text
# End of process_file()