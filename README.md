# 📋 Taskify 📝

Taskify is a simple and elegant **Flask-based task management web application**, built with Python, Flask, SQLAlchemy, and Jinja2 templates.  
It allows you to create, update, and delete todos, manage your user profile, and features a stylish login form with Lottie animations.

![Static Badge](https://img.shields.io/badge/flask-%23000000)  ![Static Badge](https://img.shields.io/badge/Python%203-%23000000)  ![Static Badge](https://img.shields.io/badge/SQLAlchemy-%23000000)  ![Static Badge](https://img.shields.io/badge/Bootstrap%204-%23000000)   ![Static Badge](https://img.shields.io/badge/HTML-%23000000)  ![Static Badge](https://img.shields.io/badge/CSS-%23000000)  ![Static Badge](https://img.shields.io/badge/DataBase-%23000000)  ![Static Badge](https://img.shields.io/badge/Jinja2-%23000000)





---

## 🌟 Features
- ✅ Add, edit, and delete tasks (todos)  
- ✅ User profile with editable name, email, and bio  
- ✅ Login form (with Flask-WTF validation)  
- ✅ Flash messages for actions  
- ✅ Responsive design with Bootstrap  
- ✅ SQLite database with SQLAlchemy and Flask-Migrate  
- ✅ Clean, modern UI with Lottie animations

---

## 🛠️ Tech Stack
- Python 3
- Flask
- Jinja2 templates
- Flask-WTF
- SQLAlchemy
- Flask-Migrate
- Bootstrap 4
- Lottie Animations

---

## 📦 Installation & Setup

### 🔗 Clone the repository
```bash
git clone https://github.com/Shivam04sharma/taskify-flask.git
cd taskify
--

🐍 Create virtual environment
bash
Copy
Edit
python -m venv env
# Activate the virtual environment:
source env/bin/activate        # On Linux/Mac
env\Scripts\activate           # On Windows

--

📥 Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

--

🗄️ Initialize the database
bash
Copy
Edit
flask db init
flask db migrate
flask db upgrade

--

▶️ Run the app
bash
Copy
Edit
python app.py
Then open your browser and visit:
👉 http://127.0.0.1:5000

---

📁 Project Structure
swift
Copy
Edit
taskify/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── update.html
│   ├── profile.html
│   ├── login.html
│   ├── about.html
│   └── feedback.html
├── static/
│   └── (optional css/js/images)
└── README.md

----


🚀 Deployment
You can deploy Taskify to free platforms like:

Render.com

Railway.app

Fly.io

---

Make sure to include:
requirements.txt
Procfile with:

makefile
Copy
Edit
web: python app.py

---

📝 License
This project is licensed under the MIT License — see the LICENSE file for details.

---

👨‍💻 Author
Shivam Sharma
Built with ❤️ using Python & Flask.
Feel free to fork, open issues, or submit pull requests!





