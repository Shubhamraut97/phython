def new_game():
    guesses = []
    correct_guesses = 0

    for key in questions:
        print("-------")
        print(key)
        for i in options[questions[key]]:
            print(i)
        guess = input("Enter a, b, c, or d: ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions[key], guess)

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0

def display_score(correct_guesses, guesses):
    print("------")
    print("Results")
    print("--------------")
    print("Answers:", end=" ")
    for key, value in questions.items():
        print(f"{key}: {value}", end=" ")
    print()
    print("Guesses:", end=" ")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")

def play_again():
    response = input("Do you want to play again? (yes/no) ").strip().lower()
    return response == "yes"

questions = {
    "Who created Python?": "A",
    "What year was Python created?": "B",
    "Is Earth round?": "C"
}
options = {
    "A": ["A. Guido van Rossum", "B. Me", "C. You", "D. Bill Gates"],
    "B": ["A. 1990", "B. 1991", "C. 1995", "D. 1997"],
    "C": ["A. Yes", "B. No", "C. Sometimes", "D. Never"]
}

while True:
    new_game()
    if not play_again():
        break

print("Goodbye")
