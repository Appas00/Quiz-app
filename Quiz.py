import csv
from random import choice

CSV_FILE = "questions.csv"

def add_question():
    n = int(input("Enter Number of Questions: "))
    with open(CSV_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        for i in range(n):
            category = input("Enter Category: ")
            question = input("Enter Question: ")
            options = [input(f"Option {j+1}: ") for j in range(4)]
            answer = input("Enter the correct option number (1-4): ")

            if answer not in ["1", "2", "3", "4"]:
                print("Invalid answer number. Skipping this question.")
                continue

            writer.writerow([category, question] + options + [answer])
            print("Question Added Successfully...")

def get_categories():
    categories = set()
    try:
        with open(CSV_FILE, mode="r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:  # <- only if row is not empty
                    categories.add(row[0])
    except FileNotFoundError as msg:
        print(msg)
    return categories


def load_questions_by_category(selected_cat):
    questions = []
    try:
        with open(CSV_FILE, mode="r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0].lower() == selected_cat.lower():
                    questions.append({
                        'question': row[1],
                        'options': row[2:6],
                        'answer': row[6]
                    })
    except FileNotFoundError as msg:
        print(msg)
    return questions


def conduct_quiz():
    categories = get_categories()
    if not categories:
        print("No categories are found.")
        return
    print("Available Categories: ")
    for index, cat in enumerate(categories, 1):
        print(f"{index}. {cat}")

    selected_index = input("Select Category Number: ")
    if not selected_index.isdigit() or int(selected_index) not in range(1, len(categories) + 1):
        print("Invalid Category Selection.")
        return

    selected_category = list(categories)[int(selected_index) - 1]
    questions = load_questions_by_category(selected_category)

    if not questions:
        print("No questions found in this category.")
        return

    score = 0
    count = 0
    for q in questions:
        count += 1
        print(f"\nQ({count}) {q['question']}")
        for index, opt in enumerate(q['options'], 1):
            print(f"{index}: {opt}")
        user_opt = input("Enter Correct Option (1 to 4): ")

        if user_opt not in ["1", "2", "3", "4"]:
            print("Invalid Option number")
            continue

        if user_opt == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! Correct Option: {q['answer']}")

    print(f"\nFinal Score: {score} out of {count}")

def main():
    while True:
        print("\n--- Quiz Application ---")
        print("1. Add Question") 
        print("2. Play Quiz")
        print("3. Exit")
        op = input("Enter Option: ")

        if op == "1":
            add_question()
        elif op == "2":
            conduct_quiz()
        elif op == "3":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid Option")

main()
