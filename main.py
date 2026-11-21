questions = {
"сколько планет в Солнечной системе?": "8",
"Столица Франции?": "Париж"
}

score = 0

for q, a in questions.items():
    user_answer = input(q + " ")
    if user_answer.lower() == a.lower():
        print("правильно")
        score += 1
    else:
        print("неверно")


print(f"ваш результат: {score} из {len(questions)}")