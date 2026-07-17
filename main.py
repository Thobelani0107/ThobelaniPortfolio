import os
from flask import Flask, render_template

app = Flask(__name__)

PHOTO_FILENAME = "profile.jpg"  # rename your photo to this and drop it in static/images/

PROFILE = {
    "name": "Thobelani Z. Zulu",
    "role": "ICT Graduate",
    "tagline": "Turning data into decisions, one model at a time.",
    "location": "Durban, South Africa",
    "status": "Open to graduate opportunities",
    "bio": (
        "Bachelor's graduate in Information Technology with a proactive, curious "
        "approach to learning and a strong record of translating problems into "
        "practical, data-driven solutions — including a team-led research project "
        "that built a real-time taxi demand prediction model to optimize pricing "
        "decisions. Comfortable working across cross-functional teams, with "
        "hands-on experience spanning software development, databases, "
        "automation, and analytics. Motivated by technology's role in building "
        "smarter, more sustainable systems."
    ),
    "core_stack": ["Python", "Flask", "SQL", "Machine Learning", "MySQL", "REST APIs"],
    "skills": {
        "Languages": ["Python", "C#", "SQL", "HTML", "CSS"],
        "Frameworks & Libraries": ["Flask", "Tkinter", "smtplib", "Requests", "BeautifulSoup"],
        "Data & ML": ["Machine Learning", "Business Intelligence", "Big Data Fundamentals", "Data Modelling", "Predictive Analytics"],
        "Databases": ["MySQL", "SQL (relational design & querying)"],
        "APIs & Integrations": ["REST APIs", "Sheety API", "Google Sheets API", "Web Scraping"],
        "Concepts": ["Object-Oriented Programming", "Full-Stack Web Development", "Agile Teamwork", "Research & Presentation"],
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
            "Electives includes Advanced Data Analytics and Advanced Cybersecurity "
        ),
    },{
        "school": "Durban University of Technology",
        "qualification": "Bachelor of Information and Communication Technology",
        "years": "2023 - 2025",
        "details": (
            "Electives in Machine Learning and Business Intelligence, with SQL "
            "and database management as core modules. Graduated with practical "
            "software development skills in Python, C#, and web technologies."
        ),
    },{
        "school": "Magwegwana High School",
        "qualification": "Matric",
        "years": "2022",
        "details": (
            "Commerce studies includes Accounting, Economics, Business Studies and Mathematics"
            "with 36 points"
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
        "link": "https://github.com/Thobelani0107",
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
        "link": "https://github.com/Thobelani0107",
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
        "link": "https://github.com/Thobelani0107",
        "image": "project-library-system.png",
    },
    {
        "title": "Automated Birthday Email System",
        "description": (
            "Built an automation script that reads a contacts list and sends "
            "personalized birthday emails automatically, integrating smtplib "
            "for delivery and the Sheety API to read/write Google Sheets."
        ),
        "tech": ["Python", "smtplib", "Sheety API"],
        "link": "https://github.com/Thobelani0107",
        "image": "project-birthday-email.png",
    },
    {
        "title": "Pomodoro Timer",
        "description": (
            "Developed a desktop productivity timer with a Tkinter GUI, "
            "supporting configurable work and break intervals."
        ),
        "tech": ["Python", "Tkinter"],
        "link": "https://github.com/Thobelani0107",
        "image": "project-pomodoro.png",
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


@app.route("/contact")
def contact():
    return render_template("contact.html", **get_context())


if __name__ == "__main__":
    app.run(debug=True)