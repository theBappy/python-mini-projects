print("Welcome to the quiz world!!!")

playing = input("Do you want to play now? ")
if playing.lower() == "no":
    print("Ok next time we will play")
    quit()

print("Let's start playing")

question_list  = [
    "What is capital of India?",
    "What does CPU stands for?",
    "What does RAM stands for?",
    "Which is the dynamically type programming language?",
    "What does SQL used for?"
]
answer_list  = [
    "delhi",
    "central processing unit",
    "random access memory",
    "python",
    "database"
]

score = 0
while playing:
    for question in question_list:
        ans = input(question)
        for ans in answer_list:
            if ans.lower:
                score += 1
            break
    playing = False

print("Yot got ", str(score) + " questions correct")
print("Your score is ", str((score/6) * 100) + "%.")
