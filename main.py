import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-this")

SMTP_USERNAME = os.environ.get("SMTP_USERNAME")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
CONTACT_RECEIVER = "ziyanda1507@gmail.com"

PHOTO_FILENAME = "profile.jpg"

PROFILE = {
    "name": "Thobelani Z. Zulu",
    "role": "Backend Developer",
    "tagline": "Turning logic into systems, one line at a time. I build backend applications and APIs with Python, Flask, and SQL, and I'm comfortable working across C#, HTML, and CSS. Self",
    "location": "South Africa",
    "status": "Open to connecting and new opportunities",
    "bio": (
        "I'm a self-taught backend developer with a strong focus on Python,"
        "and hands-on experience with C#, SQL, HTML, and CSS through course work and self-directed projects. I enjoy solving problems,"
        "working well with others,"
        "and I'm always looking to learn something new."
    ),
    "core_stack": ["Python", "Flask", "SQL", "Machine Learning", "MySQL", "REST APIs"],
    "skills": {
        "Languages": [
            {"name": "Python", "icon": "devicon-python-plain colored"},
            {"name": "C#", "icon": "devicon-csharp-plain colored"},
            {"name": "SQL", "icon": "devicon-mysql-plain colored"},
            {"name": "HTML", "icon": "devicon-html5-plain colored"},
            {"name": "CSS", "icon": "devicon-css3-plain colored"},
        ],
        "Frameworks & Libraries": [
            {"name": "Flask", "icon": "devicon-flask-original"},
            {"name": "Tkinter", "icon": "devicon-python-plain colored"},
            {"name": "smtplib", "icon": None},
            {"name": "Requests", "icon": "devicon-python-plain colored"},
            {"name": "BeautifulSoup", "icon": None},
        ],
        "Data & ML": [
            {"name": "Machine Learning", "icon": None},
            {"name": "Business Intelligence", "icon": None},
            {"name": "Big Data Fundamentals", "icon": None},
            {"name": "Data Modelling", "icon": None},
            {"name": "Predictive Analytics", "icon": None},
        ],
        "Databases": [
            {"name": "MySQL", "icon": "devicon-mysql-plain colored"},
            {"name": "Relational Design & Querying", "icon": None},
            {"name": "sqlalchemy", "icon": None},
        ],
        "APIs & Integrations": [
            {"name": "REST APIs", "icon": None},
            {"name": "Sheety API", "icon": None},
            {"name": "Google Sheets API", "icon": "devicon-google-plain colored"},
            {"name": "Web Scraping", "icon": None},
        ],
        "Concepts": [
            {"name": "Object-Oriented Programming", "icon": None},
            {"name": "Full-Stack Web Development", "icon": None},
            {"name": "Agile Teamwork", "icon": None},
            {"name": "Research & Presentation", "icon": None},
        ],
    },
    "soft_skills": [
        "Analytical & Problem-Solving",
        "Proactive & Eager to Learn",
        "Collaboration & Teamwork",
        "Adaptability",
    ],
    "socials": {
        "github": "https://github.com/Thobelani0107",
        "linkedin": "https://linkedin.com/in/thobelani-zulu-983210326",
        "email": "mailto:ziyanda1507@gmail.com",
    },
}

EDUCATION = [
    {
        "school": "Durban University of Technology",
        "qualification": "Bachelor of Information and Communication Technology Honours",
        "years": "2026 - Present",
        "details": (
            "Electives in Advanced Data Analytics and Advanced Cybersecurity"

        ),
    },
    {
        "school": "Durban University of Technology",
        "qualification": "Bachelor of Information and Communication Technology",
        "years": "2023 - 2025",
        "details": (
            "Electives in Machine Learning and Business Intelligence, with SQL "
            "and database management as core modules. Graduated with practical "
            "software development skills in Python, C#, and web technologies."
        ),
    },
    {
        "school": "Magwegwana",
        "qualification": "National Senior Certificate",
        "years": "2022",
        "details": (
            "Commerce studies include Accounting, Economics, Business Studies and Pure Mathematics"
        ),
    },
]

CERTIFICATIONS = [
    {"name": "Bachelor of Information and Communication Technology", "issuer": "Durban University of Technology"},
    {"name": "AI Fundamentals", "issuer": "Microsoft & Durban University of Technology"},
    {"name": "Basic Excel for Data Analytics", "issuer": "IBM"},
    {"name": "Presenting Data", "issuer": "HP LIFE / HP Foundation"},
    {"name": "Computer Hardware Basics", "issuer": "Cisco Networking Academy"},
]

PROJECTS = [
    {
        "title": "Real-Time Taxi Demand Prediction",
        "description": (
            "Led a team research project to design and build a predictive model "
            "identifying high-demand taxi zones in real time, applying machine "
            "learning to historical and live data to support dynamic pricing "
            "decisions. Responsible for model architecture, team coordination, "
            "and presenting findings."
        ),
        "tech": ["Python", "Machine Learning", "Data Modelling"],
        "link": "https://github.com/Project-301-Group",
        "image": "project-taxi-demand.png",
    },
    {
        "title": "DUT Lost & Found Web Platform",
        "description": (
            "Designed and developed a full-stack lost and found portal for "
            "Durban University of Technology, building RESTful routes with "
            "Flask for item submission, search, and retrieval."
        ),
        "tech": ["Python", "Flask", "HTML/CSS"],
        "link": "https://github.com/Inhlwathi-Bytes/Lost-and-Found",
        "image": "project-lost-and-found.png",
    },
    {
        "title": "School Library Management System",
        "description": (
            "Collaborated with a team to build a library management website "
            "handling book records, loans, and user accounts. Responsible for "
            "database design and back-end integration."
        ),
        "tech": ["C#", "MySQL"],
        "link": "https://github.com/Izimpisi/Sastri-Library-Backend",
        "image": "project-library-system.png",
    },
    {
        "title": "Pong",
        "description": (
            "Recreate pong game with Tkinter GUI "
            "support multiple player"
        ),
        "tech": ["Python", "TKinter"],
        "link": "https://github.com/Thobelani0107/Day_20_pong_game.git",
        "image": "pong.png",
    },
    {
        "title": "Snake Game",
        "description": (
            "Recreated snake game with a Tkinter GUI, "
        ),
        "tech": ["Python", "Tkinter"],
        "link": "https://github.com/Thobelani0107/day_20_of_100days_coding_using_python",
        "image": "snake.png",
    },
]




def get_context(**extra):
    """Shared context injected into every template (nav, profile, photo)."""
    photo_path = os.path.join(app.static_folder, "images", PHOTO_FILENAME)
    context = {
        "profile": PROFILE,
        "has_photo": os.path.exists(photo_path),
        "photo_filename": PHOTO_FILENAME,
    }
    context.update(extra)
    return context


@app.route("/")
def home():
    return render_template("index.html", **get_context())


@app.route("/about")
def about():
    return render_template("about.html", **get_context())


@app.route("/skills")
def skills():
    return render_template("skills.html", **get_context())


@app.route("/education")
def education():
    return render_template(
        "education.html",
        **get_context(education=EDUCATION, certifications=CERTIFICATIONS)
    )


@app.route("/projects")
def projects():
    return render_template("projects.html", **get_context(projects=PROJECTS))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        sender_email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not sender_email or not message:
            flash("Please fill in every field.", "error")
            return redirect(url_for("contact"))

        try:
            msg = MIMEMultipart()
            msg["From"] = SMTP_USERNAME
            msg["To"] = CONTACT_RECEIVER
            msg["Reply-To"] = sender_email
            msg["Subject"] = f"Portfolio message from {name}"
            body = f"Name: {name}\nEmail: {sender_email}\n\n{message}"
            msg.attach(MIMEText(body, "plain"))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
                server.send_message(msg)

            flash("Message sent — thanks for reaching out!", "success")
        except Exception:
            flash("Something went wrong sending that. Try emailing me directly instead.", "error")

        return redirect(url_for("contact"))

    return render_template("contact.html", **get_context())


if __name__ == "__main__":
    app.run(debug=True)