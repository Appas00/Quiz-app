
🧠 Flask Quiz Application
A simple, responsive web-based quiz application built with Flask, HTML, CSS, and Python. Users can answer multiple-choice questions loaded from a CSV file, get real-time score feedback, and enjoy an animated result screen with celebration effects for high scores.
🚀 Features
•	📄 Dynamic quiz questions from CSV
•	✅ Multiple-choice options with custom-styled radio buttons
•	🎯 Score calculation and result display
•	🎉 Confetti celebration on high scores
•	💻 Responsive and animated UI with modern design
🛠️ Tech Stack
•	Backend: Python, Flask
•	Frontend: HTML, CSS, JavaScript
•	Data Source: CSV file
📁 Project Structure
project-folder/
│
├── static/
│   ├── style.css
│   └── confetti.js (optional, for celebration)
├── templates/
│   ├── index.html
│   ├── quiz.html
│   └── result.html
├── questions.csv
├── app.py
└── README.md
🏁 Getting Started
1. Clone the Repository
git clone https://github.com/yourusername/flask-quiz-app.git
cd flask-quiz-app
2. Install Requirements
pip install flask
3. Run the App
python app.py
Open your browser and go to: http://127.0.0.1:5000
📦 CSV Format Example (questions.csv)
question, option1, option2, option3, option4, answer
What is the capital of France? Paris, London, Berlin, Madrid
Which language is used in Flask? Python, Java, C++, Ruby
🎉 Celebration Effect
If the user gets a high score (e.g., 80%+), a confetti or colorful animation is shown to celebrate the achievement. You can customize this with simple JavaScript or a confetti library.
📸 Screenshots
(You can add screenshots of the quiz and result page here.)
📄 License
This project is open-source and available under the MIT License.

