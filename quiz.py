def ask_question(question, options, correct_option):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4:
                return answer == correct_option
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": 3
        },
        {
            "question": "Which language is primarily used for web development?",
            "options": ["Python", "JavaScript", "C++", "Java"],
            "answer": 2
        },
        {
            "question": "Who wrote 'Macbeth'?",
            "options": ["Shakespeare", "Tolstoy", "Hemingway", "Austen"],
            "answer": 1
        }
    ]

    score = 0
    total = len(questions)

    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

    print("\n🎉 Quiz Complete!")
    print(f"Your Score: {score} out of {total}")
    percentage = (score / total) * 100
    print(f"Percentage: {percentage:.2f}%")
    
if __name__ == "__main__":
    run_quiz()