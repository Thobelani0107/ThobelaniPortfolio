import os
from flask import Flask, render_template

app = Flask(__name__)

PHOTO_FILENAME = "profile.jpg"  # rename your photo to this and drop it in static/images/

# Fill this in with your own details — used across the templates
PROJECTS = [
    {
        "title": "Project One",
        "description": "Short description of what this project does and why you built it.",
        "tech": ["Python", "Flask"],
        "link": "https://github.com/yourusername/project-one",
        "image": "project-one.png",
    },
    {
        "title": "Project Two",
        "description": "Short description of what this project does and why you built it.",
        "tech": ["SQL", "JavaScript"],
        "link": "https://github.com/yourusername/project-two",
        "image": "project-two.png",
    },
]

EDUCATION = [
    {
        "school": "Durban University of Technology",
        "qualification": "Bachelor of Information and Communication Technology Honours",
        "years": "2026 - Current",
        "details": "Relevant coursework, achievements, or projects here.",
    },
    {
        "school": "Durban University of Technology",
        "qualification": "Bachelor of Information and Communication Technology",
        "years": "2022 - 2025",
        "details": "Relevant coursework, achievements, or projects here.",
    },
    {
        "school": "Magwegwana High School",
        "qualification": "Matric",
        "year": "2022",
        "details": "Commerce, include Accounting, Economies, Business Study and Mathematics",
    },
]

PROFILE = {
    "name": "Your Name",
    "role": "ICT Graduate",
    "tagline": "Building reliable systems, one commit at a time.",
    "location": "Johannesburg, South Africa",
    "status": "Available for opportunities",
    "bio": (
        "I'm a recent ICT graduate interested in software development, "
        "networks, and problem-solving with code. I like turning "
        "requirements into working systems, and I'm always learning "
        "something new."
    ),
    "skills": ["Python", "Flask", "SQL", "Networking", "Git", "Linux"],
    "soft_skills": ["Communication", "Teamwork", "Problem-Solving", "Adaptability", "Time Management"],
    "socials": {
        "github": "https://github.com/yourusername",
        "linkedin": "https://linkedin.com/in/yourusername",
        "email": "mailto:you@example.com",
    },
}


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
    return render_template("education.html", **get_context(education=EDUCATION))


@app.route("/projects")
def projects():
    return render_template("projects.html", **get_context(projects=PROJECTS))


@app.route("/contact")
def contact():
    return render_template("contact.html", **get_context())


if __name__ == "__main__":
    app.run(debug=True)