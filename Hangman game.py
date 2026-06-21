word="python"
guess_word=["_","_","_","_","_","_"]

chances=6

while chances > 0:
    print("Word:", " ".join(guess_word))

    letter=input("Enter a letter: ")

    if letter in word:
        for i in range(len(word)):
            if word[i]== letter:
                guess_word[i]=letter
        print("Correct guess!")
    else:
        chances=1
        print("Wrong guess!")
        print("Chances left:", chances)
    if "_" not in guess_word:
        print("YOU WON!")
        print("The word is:", word)
        break
if "_" in guess_word:
    print("YOU LOST!")
    print("The word was:", word)
