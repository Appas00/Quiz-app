Flask-Based Quiz Web Application
This project is a web-based quiz application developed using Python’s Flask framework. It allows users to take multiple-choice quizzes, calculate scores, and view results with interactive and user-friendly UI features. The questions are sourced from a CSV file, making it easy to manage and update quiz content.
•	To create an interactive quiz platform using Python and Flask.
•	To implement a clean and responsive frontend using HTML, CSS, and JavaScript.
•	To load and process quiz questions dynamically from a CSV file.
•	To provide score calculation and feedback on quiz completion.
•	To enhance the user experience with animations and visual effects (e.g., confetti on high scores).
Tools and Technologies
•	Backend: Flask (Python)
•	Frontend: HTML, CSS, JavaScript
•	Data Storage: CSV File for Questions
Features
•	Dynamic quiz generation from CSV data.
•	Multiple-choice questions with custom-styled options.
•	Instant score calculation.
•	Responsive design for desktop and mobile.
•	Celebration animation for high scores.
•	Lightweight and easy to deploy.
Folder Structure
php
CopyEdit
project-root/
│
├── app.py                     # Main Flask application
├── questions.csv              # CSV file containing quiz questions and answers
│
├── static/
│   ├── style.css              # Main stylesheet
│   └── confetti.js (optional) # JS file for celebratory effect
│
└── templates/
    ├── index.html             # Home page
    ├── quiz.html              # Quiz interface
    └── result.html            # Result display
Sample CSV Format
csv
CopyEdit
question,option1,option2,option3,option4,answer
What is the capital of France?,Paris,London,Berlin,Madrid,Paris
Which language is used in Flask?,Python,Java,C++,Ruby,Python
How to Run
1.	Install Flask
Ensure Flask is installed in your Python environment.
bash
CopyEdit
pip install flask
2.	Run the Application
bash
CopyEdit
python app.py
3.	Open in Browser
Visit http://127.0.0.1:5000 to access the quiz.
Learning Outcomes
•	Gained practical experience in web development with Flask.
•	Learned how to handle CSV files in Python.
•	Designed responsive and animated user interfaces.
•	Implemented user interaction with radio buttons and JavaScript.
This project demonstrates how Flask can be effectively used to develop interactive web applications. It integrates frontend technologies and backend logic to provide a seamless quiz-taking experience. The use of CSV for question storage makes the system lightweight and easily extendable.

