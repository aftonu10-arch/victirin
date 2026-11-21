import time
questions = {
"сколько планет в Солнечной системе?": "8",
"Столица Франции?": "Париж"
}

score = 0

for q, a in questions.items():
    start_time = time.time()
    user_answer = input(q + " ")
    end_time = time.time()
    if round(end_time - start_time, 1) > 5:
        print('вы не уложились в таймер 5 секунд')
        user_answer = 'wrong'
    print(f'Время ответа: {round(end_time - start_time, 1)} сек')
    if user_answer.lower() == a.lower():
        print("правильно")
        score += 1
    else:
        print("неверно")


print(f"ваш результат: {score} из {len(questions)}")