def GetTextFileName():
    # This function was developed using ChatGPT, as required by the SG1 specification.

    # Windows does not allow these characters in filenames.
    invalid_characters = '<>:"/\\|?*'

    # Windows also reserves these device names, regardless of extension.
    reserved_names = {
        "CON", "PRN", "AUX", "NUL",
        "COM1", "COM2", "COM3", "COM4", "COM5",
        "COM6", "COM7", "COM8", "COM9",
        "LPT1", "LPT2", "LPT3", "LPT4", "LPT5",
        "LPT6", "LPT7", "LPT8", "LPT9"
    }

    while True:
        filename = input("Enter the name of the text file: ")

        # Reject an empty filename.
        if filename == "":
            print("Error: You must enter a filename.")
            continue

        # The filename must end in .txt, without regard to capitalization.
        if not filename.lower().endswith(".txt"):
            print("Error: The filename must end with '.txt'.")
            continue

        # Check for characters that Windows does not permit.
        bad_character = next(
            (char for char in invalid_characters if char in filename),
            None
        )

        if bad_character is not None:
            print(
                f"Error: The filename contains the invalid character "
                f"'{bad_character}'. Windows filenames cannot contain "
                f"the characters < > : \" / \\ | ? *."
            )
            continue

        # Windows filenames cannot end with a space or period.
        # This also catches a name such as "example.txt. ".
        if filename.endswith(" ") or filename.endswith("."):
            print(
                "Error: A Windows filename cannot end with a space or period."
            )
            continue

        # Check the filename portion before ".txt" against reserved names.
        base_name = filename[:-4]

        if base_name.upper() in reserved_names:
            print(
                f"Error: '{base_name}' is a reserved Windows device name "
                "and cannot be used as a filename."
            )
            continue

        # A filename consisting only of ".txt" has no actual name.
        if base_name == "":
            print("Error: You must provide a filename before '.txt'.")
            continue

        return filename
    
    
    
    
    
inputFile = GetTextFileName()
    
    
print(inputFile)
    
    
    
    
    
    
    