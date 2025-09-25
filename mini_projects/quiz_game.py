
questions = (
    "Which country has the highest life expectancy?",
    "What is the most common surname in the United States?",
    "Who was the Ancient Greek God of the Sun?",
    "How many minutes are in a full week?",
    "How many faces does a Dodecahedron have?"
)

options = ((
"A. Hong Kong", "B. USA", "C. Australia", "D. India"
), ("A. Smith", "B. Doe", "C. Martin", "D. Philips"), ("A. Sun", "B. Mars", "C. Apollo", "D. Jupiter"), ("A. 11,340", "B. 10,080", "C. 10,090", "D. 11,350"), ("A. 13", "B. 23", "C. 10", "D. 12"))

answers = ("A","A","C","B","D")

guesses = []

score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess= input("Enter (A, B, C, D): ").upper()
    guesses.append(guess) 
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("-------------------------------")
print("          RESULTS              ")
print("-------------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}.")