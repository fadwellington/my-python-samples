def compareStrings():
    print("Enter the same word twice\n")
    String1 = input("Type a word: ")
    String2 = input("Type that word again: ")
    # .lower() String method to ignore if any capitalization is used
    if String1.lower() == String2.lower():
        print("Thanks!")
    # used elif rather than else only because the assignment calls to use both operators
    elif String1.lower() != String2.lower():
        print("That's not what I asked!")


compareStrings()
