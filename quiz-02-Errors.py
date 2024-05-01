# Quiz questions and options
questions = [
    "What type of error occurs when the code violates the syntax rules of Python?",
    "What type of error occurs when there is incorrect indentation or mixing spaces with tabs?",
    "What type of error occurs when code is copied and pasted without proper consideration of formatting?"
]

options = [
    ["A) Syntax Errors", "B) Indentation Errors", "C) Name Errors", "D) Type Errors"],
    ["A) Syntax Errors", "B) Indentation Errors", "C) Name Errors", "D) Type Errors"],
    ["A) Syntax Errors", "B) Indentation Errors", "C) Name Errors", "D) Copy-Paste Formatting Errors"]
]

# Corresponding answers
answers = ["A", "B", "D"]

# Function to run the quiz
def run_quiz(questions, options, answers):
    score = 0
    total_questions = len(questions)
    for i in range(total_questions):
        print(f"Question {i+1}: {questions[i]}")
        for option in options[i]:
            print(option)
        user_answer = input("Your answer: ").strip().upper()
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is '{answers[i]}'")
        print()
    print(f"You got {score} out of {total_questions} correct.")

# Run the quiz
run_quiz(questions, options, answers)
