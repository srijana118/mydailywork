import json


def load_questions():
    with open("questions.json", "r") as file:
        questions = json.load(file)
    return questions


def print_welcome():
    print("\nWelcome to the Quiz Game!")
    print("Rules:")
    print("- You will be asked multiple-choice questions with options (A, B, C, D).")
    print("- Type the option letter corresponding to your answer.")
    print("- Each correct answer awards 1 mark.")
    print("- There is no negative marking for wrong answers.")
    print("- Your final result will be displayed as score and percentage.\n")

    input("Are you ready to start the quiz? Press Enter to continue...")
    print()


def get_option_text(options, letter):
    index = ord(letter) - ord('A')
    return options[index]


def start_quiz(questions):
    score = 0
    total = len(questions)

    for i, q in enumerate(questions, start=1):
        print(f"Question {i} of {total}")
        print(q["question"])

        for opt in q["options"]:
            print(opt)

        while True:
            user_answer = input("Enter your answer (A/B/C/D): ").upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            print("Invalid input. Please enter A, B, C or D.")

        correct_letter = q["answer"]
        correct_text = get_option_text(q["options"], correct_letter)

        if user_answer == correct_letter:
            print("Correct answer\n")
            score += 1
        else:
            print("Wrong answer")
            print(f"Correct answer: {correct_text}\n")

    return score


def show_result(score, total):
    percentage = (score / total) * 100

    print("Final Result")
    print("------------")
    print(f"Score      : {score}/{total}")
    print(f"Percentage : {percentage:.2f}%")

    if percentage >= 80:
        print("Performance: Excellent")
    elif percentage >= 60:
        print("Performance: Very Good")
    elif percentage >= 50:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")


def play_again():
    choice = input("\nDo you want to play again (yes/no): ").lower()
    return choice == "yes"


# ---------------- MAIN PROGRAM ----------------

while True:
    print_welcome()
    questions = load_questions()
    final_score = start_quiz(questions)
    show_result(final_score, len(questions))

    if not play_again():
        print("\nThank you for playing the Quiz Game.")
        break
