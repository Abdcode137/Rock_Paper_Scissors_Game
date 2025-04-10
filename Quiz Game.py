class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        user_answer = input("Your answer: ")
        if user_answer.lower() == question.answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f" Wrong! The correct answer was: {question.answer}\n")
    print(f"You got {score}/{len(questions)} correct!")

question_prompts = [
    "1. What is the capital of France?\n(a) Madrid\n(b) Berlin\n(c) Paris\n(d) Rome\n",
    "2. What is 5 * 6?\n(a) 30\n(b) 20\n(c) 11\n(d) 26\n",
    "3. Which planet is known as the Red Planet?\n(a) Earth\n(b) Mars\n(c) Jupiter\n(d) Saturn\n",
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
]

run_quiz(questions)
