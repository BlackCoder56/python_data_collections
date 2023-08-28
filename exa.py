def operation():
    word = "lmo"
    guess_word = ""
    count = 1
    limit_count = 3
    outOfCount = False

    while word != guess_word and not(outOfCount):
        if count <= limit_count:
            guess_word = input("Enter the guess word: ")
            count += 1
        else:
            outOfCount = True
    if outOfCount:
        print("You Lost!!")
    else:
        print("You won!!")





operation()