from flask import Flask, render_template, request, redirect, url_for
import csv
import random

app = Flask(__name__)
CSV_FILE = "questions.csv"

def get_categories():
    categories = set()
    try:
        with open(CSV_FILE, mode="r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    categories.add(row[0])
    except FileNotFoundError:
        pass
    return sorted(categories)

def load_questions_by_category(category):
    questions = []
    try:
        with open(CSV_FILE, mode="r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0].lower() == category.lower():
                    questions.append({
                        'question': row[1],
                        'options': row[2:6],
                        'answer': row[6]
                    })
    except FileNotFoundError:
        pass
    return questions

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        category = request.form.get("category")
        return redirect(url_for("quiz", category=category))
    categories = get_categories()
    return render_template("index.html", categories=categories)


@app.route("/quiz/<category>", methods=["GET", "POST"])
def quiz(category):
    questions = load_questions_by_category(category)
    if request.method == "POST":
        user_answers = request.form
        score = 0
        for i, q in enumerate(questions):
            correct = q['answer']
            user_answer = user_answers.get(f"q{i}")
            if user_answer == correct:
                score += 1
        return render_template("result.html", score=score, total=len(questions))
    return render_template("quiz.html", questions=questions, category=category)

@app.route("/add", methods=["GET", "POST"])
def add_question():
    if request.method == "POST":
        category = request.form["category"]
        question = request.form["question"]
        options = [request.form[f"option{i+1}"] for i in range(4)]  # ✅ Fixed here
        answer = request.form["answer"]
        if answer not in ["1", "2", "3", "4"]:
            return "Invalid answer number."
        with open(CSV_FILE, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([category, question] + options + [answer])
        return redirect(url_for("index"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
