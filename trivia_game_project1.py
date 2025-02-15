import random #it will generate the random numbers...

questions = {
    "what is the keyword to define a function in python?" : "def",
    "which data type is used to store the True, False values?" : "boolean",
    "what is the correct file extension for python files?" : ".py",
    "which symbol is used to comment in python?" : "#",
    "what function is used to take the input from the user?" : "input()",
    "how do you start a for loop in python?" : "for",
    "what is the output of 2 ** 3 in pyhton?" : "8",
    "what keyword is used to import the module?" : "import",
    "what does the length function returns?" : "length"
}

def trivia_game():
    # global questions
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selelected_questions = random.sample(questions_list, total_questions)


    for idx, question in enumerate(selelected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("your answer: ").lower().strip()
        correct_answer = questions[question]

        if user_answer == correct_answer:
            print("Correct..!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is : {correct_answer}.\n")

    if score >= 4:
        print(f"well done.. Your score is {score}/{total_questions}")
    elif score >=2:
        print(f"Need to improve.. Your score is {score}/{total_questions}")
    else:
        print(f"Poor!.. Your score is {score}/{total_questions}")
trivia_game()