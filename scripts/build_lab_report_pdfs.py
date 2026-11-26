"""Build one downloadable PDF report per experiment in the lab reports site."""

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    ListFlowable,
    Preformatted,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf"

REPORTS = [
    {
        "file": "experiment-01-html5.pdf",
        "number": "EXPERIMENT 01",
        "title": "HTML5 Elements and Semantic Web Pages",
        "summary": "Create a structured, accessible web page that demonstrates HTML5 elements, forms, tables, multimedia, and interactive controls.",
        "stack": "HTML5, CSS, JavaScript",
        "requirements": ["Modern web browser", "Code editor such as VS Code", "Optional Live Server extension"],
        "topics": ["Document structure and semantic landmarks", "Text formatting, lists, and tables", "Forms, input types, and validation", "Images, audio, video, progress, and meter", "Details, datalist, and dialog interactions"],
        "steps": ["Open the Experiment 1 source page in an editor and review its HTML5 document structure.", "Inspect the semantic header, navigation, main, section, and footer landmarks.", "Try the text formatting, list, and table examples.", "Submit the form examples and inspect their input types and validation behavior.", "Use the multimedia and interactive examples, including details, datalist, and dialog controls.", "Open the page in a browser and check the layout and controls at desktop and narrow widths."],
        "outcome": "A single browser page demonstrates key HTML5 content and interactive elements with semantic structure and accessible labels.",
        "location": "lab/Exp_01/code.html",
        "snippet_source": "lab/Exp_01/code.html",
        "snippet_language": "HTML",
        "snippet": "<header>\n  <h1>Experiment 1: HTML5 Elements Demo</h1>\n  <nav>\n    <ul>\n      <li><a href=\"#about\">About</a></li>\n      <li><a href=\"#form-section\">Form</a></li>\n    </ul>\n  </nav>\n</header>\n<main>\n  <section id=\"about\">\n    <article id=\"article-section\">",
    },
    {
        "file": "experiment-02-css-styling.pdf",
        "number": "EXPERIMENT 02",
        "title": "CSS Styling, Selectors, Layout, and Motion",
        "summary": "Compare CSS application methods and practice selectors, responsive layouts, transitions, and keyframe animations.",
        "stack": "HTML5, CSS3, Flexbox, CSS Grid",
        "requirements": ["Modern web browser", "Code editor", "No package installation required"],
        "topics": ["External, internal, and inline CSS", "Type, class, ID, attribute, pseudo-class, and pseudo-element selectors", "Box model and responsive media queries", "Flexbox and CSS Grid", "Transitions, transforms, and keyframe animations"],
        "steps": ["Open each HTML page in the parta through partf folders.", "Compare the external stylesheet, embedded style block, and inline style attribute.", "Review selector examples and try hover or focus interactions.", "Resize the browser to observe the responsive Flexbox and Grid layouts.", "Hover over the animated elements and inspect their transitions and keyframes.", "Change a CSS value, save, refresh, and compare the result."],
        "outcome": "The experiment shows how CSS controls presentation, selection, layout, responsive behavior, and visual motion.",
        "location": "lab/Exp2/README.md and parta-partf HTML files",
        "snippet_source": "lab/Exp2/partf/index-animations.html",
        "snippet_language": "CSS",
        "snippet": ".transition-box {\n  transition: all 0.4s ease;\n}\n\n.transition-box:hover {\n  transform: translateY(-5px) scale(1.05);\n  background: #e74c3c;\n  box-shadow: 0 10px 30px rgba(231, 76, 60, 0.3);\n  border-radius: 20px;\n}",
    },
    {
        "file": "experiments-07-08-es6-todo.pdf",
        "number": "EXPERIMENTS 07 AND 08",
        "title": "JavaScript ES6 To-Do Application",
        "summary": "Build an interactive task list using ES6 classes, array methods, DOM updates, and event delegation.",
        "stack": "HTML, CSS, JavaScript ES6",
        "requirements": ["Modern web browser", "Code editor", "No server or package installation required"],
        "topics": ["Task class and in-memory state", "Arrow functions, destructuring, and spread syntax", "forEach, filter, and map", "DOM creation and event delegation", "Keyboard and click events"],
        "steps": ["Open todo.html and confirm the task input, Add button, and list are visible.", "Enter a task and select Add or press Enter.", "Select a task title to toggle its completed state.", "Select Delete beside a task and confirm that only that task is removed.", "Add several tasks and repeat the complete and delete actions.", "Refresh the page and observe that in-memory tasks reset."],
        "outcome": "Users can add, complete, and delete tasks. The page demonstrates ES6 syntax and DOM event handling; task state resets on refresh.",
        "location": "lab/Exp7_8/todo.html and app.js",
        "snippet_source": "lab/Exp7_8/app.js",
        "snippet_language": "JavaScript",
        "snippet": "class Task {\n  constructor(title) {\n    this.id = Date.now();\n    this.title = title;\n    this.completed = false;\n  }\n}\n\nconst addTask = () => {\n  const title = input.value.trim();\n  if (!title) return;\n  tasks = [...tasks, new Task(title)];\n  renderTasks();\n};",
    },
    {
        "file": "experiment-12a-express-ejs.pdf",
        "number": "EXPERIMENT 12(A)",
        "title": "Express Routes, Requests, and EJS Views",
        "summary": "Create an Express server with response formats, route and query parameters, POST endpoints, and server-rendered EJS templates.",
        "stack": "Node.js, Express, EJS",
        "requirements": ["Node.js and npm", "Modern browser", "REST client for POST requests"],
        "topics": ["Text, HTML, and JSON responses", "Route parameters and query strings", "JSON and form request bodies", "EJS server-side rendering"],
        "steps": ["From lab/Exp12_A, run npm install and then npm start.", "Open http://localhost:3000/text, /html, and /json to compare response types.", "Try /user/42 and /product/books/7 for route parameters.", "Try /search?q=express&page=1&limit=5 and the /calculate query endpoint.", "Open /home, /users, and /profile/42 to view EJS-rendered pages.", "Use a REST client to POST JSON or form data to /user, /register, and /login."],
        "outcome": "The running server returns multiple content types, reads URL and request data, and renders dynamic pages with EJS.",
        "location": "lab/Exp12_A/app.js and views/",
        "snippet_source": "lab/Exp12_A/app.js",
        "snippet_language": "JavaScript · Express",
        "snippet": "app.get('/user/:id', (req, res) => {\n  const userId = req.params.id;\n  res.json({ message: 'User details', userId: userId });\n});\n\napp.get('/search', (req, res) => {\n  const { q, page, limit } = req.query;\n  res.json({ searchQuery: q, page: page || 1, limit: limit || 10 });\n});",
    },
    {
        "file": "experiment-12b-cookies-sessions.pdf",
        "number": "EXPERIMENT 12(B)",
        "title": "Cookies and Sessions in Express",
        "summary": "Demonstrate client-side cookies and server-side sessions in separate Express examples.",
        "stack": "Node.js, Express, cookie-parser, express-session",
        "requirements": ["Node.js and npm", "Browser", "Terminal"],
        "topics": ["Setting, reading, and deleting cookies", "Session creation and visit counts", "Session destruction", "Middleware-based state management"],
        "steps": ["Open a terminal in lab/Exp12_B and run npm install.", "Run node cookie-example.js and visit /set-cookie, /get-cookie, and /delete-cookie.", "Stop the cookie server, then run node session-example.js.", "Visit the session root route and refresh to observe the visit counter.", "Visit /destroy and return to the root to observe a fresh session.", "Compare where cookie values and session data are maintained."],
        "outcome": "The examples show how cookies persist in the browser and how Express sessions keep server-side state associated with a session identifier.",
        "location": "lab/Exp12_B/cookie-example.js and session-example.js",
        "snippet_source": "lab/Exp12_B/session-example.js",
        "snippet_language": "JavaScript · Express Session",
        "snippet": "app.get('/', (req, res) => {\n  if (req.session.views) {\n    req.session.views++;\n    res.send(`Welcome back! You visited ${req.session.views} times.`);\n  } else {\n    req.session.views = 1;\n    res.send('Welcome to the session demo. Refresh to count visits.');\n  }\n});",
    },
    {
        "file": "experiment-13-mongoose-mongodb.pdf",
        "number": "EXPERIMENT 13",
        "title": "MongoDB User Management with Mongoose",
        "summary": "Connect an Express application to MongoDB and use Mongoose schemas, validation, and database operations for user management.",
        "stack": "Node.js, Express, MongoDB, Mongoose, dotenv",
        "requirements": ["Node.js and npm", "MongoDB service or connection URI", "Browser"],
        "topics": ["Mongoose User schema and model", "Required and unique fields", "Signup, login, and user listing routes", "Asynchronous database access and error handling"],
        "steps": ["Open a terminal in lab/mongoose-demo and run npm install.", "Start MongoDB or configure MONGODB_URI in a local .env file.", "Run npm start and open the local server in a browser.", "Create a user through the signup form and inspect validation behavior.", "Try logging in and viewing the users list.", "Review how the schema and routes map requests to MongoDB documents."],
        "outcome": "The application uses Mongoose to validate and persist users in MongoDB and exposes signup, login, and listing behavior.",
        "location": "lab/mongoose-demo/Server.js",
        "snippet_source": "lab/mongoose-demo/Server.js",
        "snippet_language": "JavaScript · Mongoose",
        "snippet": "const userSchema = new mongoose.Schema({\n  username: { type: String, required: true, unique: true },\n  email: { type: String, required: true, unique: true },\n  password: { type: String, required: true },\n  createdAt: { type: Date, default: Date.now }\n});\n\nconst User = mongoose.model('User', userSchema);",
    },
    {
        "file": "experiment-15-django-todo.pdf",
        "number": "EXPERIMENT 15",
        "title": "Django To-Do Application with SQLite",
        "summary": "Build a Django MVT application that stores tasks and supports create, list, completion toggle, and delete actions.",
        "stack": "Python, Django, SQLite",
        "requirements": ["Python", "Django installed", "Browser and terminal"],
        "topics": ["Task model and SQLite persistence", "Django views and URL routing", "Template rendering", "Create, toggle, and delete operations"],
        "steps": ["Open a terminal in lab/Exp15/django_todo_app.", "Install Django if it is not available in the environment.", "Run python manage.py migrate to prepare the SQLite database.", "Run python manage.py runserver and open the local address shown in the terminal.", "Create a task, toggle its completion state, and delete it from the list.", "Inspect the Task model, views, URL patterns, and templates."],
        "outcome": "The Django application demonstrates the MVT pattern and stores task records in a local SQLite database.",
        "location": "lab/Exp15/django_todo_app/",
        "snippet_source": "lab/Exp15/django_todo_app/todo/models.py",
        "snippet_language": "Python · Django ORM",
        "snippet": "from django.db import models\n\nclass Task(models.Model):\n    title = models.CharField(max_length=200)\n    completed = models.BooleanField(default=False)\n    created_at = models.DateTimeField(auto_now_add=True)\n\n    def __str__(self):\n        return self.title",
    },
    {
        "file": "experiment-15b-django-uv.pdf",
        "number": "EXPERIMENT 15(B)",
        "title": "Multi-App Django and Python Project Management",
        "summary": "Explore a Django project split into applications and a Python project configured with uv for dependency and environment management.",
        "stack": "Python, Django, uv, SQLite",
        "requirements": ["Python 3.14 or newer for the uv college project", "uv", "Browser and terminal"],
        "topics": ["Django apps for todo, tasks, and student API responsibilities", "Models, views, URLs, and templates", "pyproject.toml project metadata", "uv dependency synchronization and command execution"],
        "steps": ["Inspect lab/Exp15B to compare the Django app project and the uv-managed college project.", "In the uv exp/college folder, run uv sync to create the environment from pyproject.toml.", "Run Django migrations with uv run python manage.py migrate.", "Start the development server with uv run python manage.py runserver.", "Open the local site and inspect project routes and app boundaries.", "Review pyproject.toml and uv.lock to see how dependencies are declared and locked."],
        "outcome": "The experiment demonstrates modular Django organization and reproducible Python environment management with uv.",
        "location": "lab/Exp15B/",
        "snippet_source": "lab/Exp15B/uv exp/college/pyproject.toml",
        "snippet_language": "TOML · uv project",
        "snippet": "[project]\nname = \"college\"\nrequires-python = \">=3.14\"\ndependencies = [\n    \"django>=6.1.2\",\n]",
    },
    {
        "file": "exam-01b-eisenhower-matrix.pdf",
        "number": "EXAM 01(B)",
        "title": "Eisenhower Matrix To-Do Application",
        "summary": "Organize tasks into four priority quadrants using urgency and importance in a server-rendered application.",
        "stack": "Node.js, Express, EJS, MongoDB",
        "requirements": ["Node.js and npm", "MongoDB connection", "Browser"],
        "topics": ["Urgent and important task classification", "Create, edit, complete, and delete actions", "Express routing and EJS rendering", "MongoDB-backed task persistence"],
        "steps": ["Open lab/Exam01B and install the project dependencies with npm install.", "Configure the MongoDB connection required by the application.", "Start the Express server using the package scripts.", "Add tasks and set their urgent and important properties.", "Check that tasks appear in the corresponding Do, Schedule, Delegate, or Eliminate quadrant.", "Edit, complete, redo, and delete tasks to inspect the application workflow."],
        "outcome": "Tasks are grouped into a four-quadrant priority matrix and managed through an Express and EJS interface backed by MongoDB.",
        "location": "lab/Exam01B/",
        "snippet_source": "lab/Exam01B/app.js",
        "snippet_language": "JavaScript · MongoDB",
        "snippet": "const matrix = {\n  doTasks: tasks.filter(t => t.isUrgent && t.isImportant),\n  scheduleTasks: tasks.filter(t => !t.isUrgent && t.isImportant),\n  delegateTasks: tasks.filter(t => t.isUrgent && !t.isImportant),\n  eliminateTasks: tasks.filter(t => !t.isUrgent && !t.isImportant)\n};\n\nres.render('index', { matrix });",
    },
    {
        "file": "fastapi-docker-lab.pdf",
        "number": "FASTAPI DOCKER LAB",
        "title": "Containerizing a FastAPI Application",
        "summary": "Build and run a small FastAPI service locally and package it into a Docker image for container execution.",
        "stack": "Python, FastAPI, Uvicorn, Docker",
        "requirements": ["Python and pip", "Docker Desktop or Docker Engine for container steps", "Terminal and browser"],
        "topics": ["FastAPI GET routes and path parameters", "Uvicorn ASGI server", "Docker image and container lifecycle", "Port mapping to the host"],
        "steps": ["Open a terminal in lab/FastAPI Docker Lab.", "Install Python dependencies with pip install -r requirements.txt.", "Run uvicorn main:app --reload and try /, /about, and /hello/Akshat.", "Build a container image with docker build -t fastapi-student-lab .", "Run it with docker run --rm -p 8000:8000 fastapi-student-lab.", "Open the mapped local address and try the routes again."],
        "outcome": "The API runs directly under Uvicorn and inside a Docker container with its service port mapped to the host.",
        "location": "lab/FastAPI Docker Lab/",
        "snippet_source": "lab/FastAPI Docker Lab/main.py",
        "snippet_language": "Python · FastAPI",
        "snippet": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/hello/{name}')\ndef hello(name: str):\n    return {\"message\": f\"Hello, {name}!\"}",
    },
]


def register_fonts():
    font_dir = Path(r"C:\Windows\Fonts")
    regular = font_dir / "arial.ttf"
    bold = font_dir / "arialbd.ttf"
    if regular.exists() and bold.exists():
        pdfmetrics.registerFont(TTFont("LabSans", str(regular)))
        pdfmetrics.registerFont(TTFont("LabSans-Bold", str(bold)))
        return "LabSans", "LabSans-Bold"
    return "Helvetica", "Helvetica-Bold"


FONT, BOLD = register_fonts()
NAVY = colors.HexColor("#173257")
BLUE = colors.HexColor("#2F64C5")
MUTED = colors.HexColor("#5C6D84")
PALE = colors.HexColor("#EDF3FC")
LINE = colors.HexColor("#DCE4EF")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Kicker", fontName=BOLD, fontSize=8, leading=10, textColor=BLUE, spaceAfter=6, tracking=1.1))
styles.add(ParagraphStyle(name="ReportTitle", fontName=BOLD, fontSize=21, leading=25, textColor=NAVY, spaceAfter=9))
styles.add(ParagraphStyle(name="Summary", fontName=FONT, fontSize=10, leading=15, textColor=MUTED, spaceAfter=12))
styles.add(ParagraphStyle(name="SectionHead", fontName=BOLD, fontSize=11, leading=14, textColor=NAVY, spaceBefore=12, spaceAfter=6, keepWithNext=True))
styles.add(ParagraphStyle(name="BodyLab", fontName=FONT, fontSize=9, leading=13, textColor=colors.HexColor("#243349"), spaceAfter=5))
styles.add(ParagraphStyle(name="SmallLab", fontName=FONT, fontSize=8, leading=11, textColor=MUTED))
styles.add(ParagraphStyle(name="BulletLab", fontName=FONT, fontSize=9, leading=12.5, textColor=colors.HexColor("#243349"), leftIndent=2, spaceAfter=3))
styles.add(ParagraphStyle(name="CodeSample", fontName="Courier", fontSize=7, leading=9, textColor=colors.HexColor("#18263A"), backColor=colors.HexColor("#F3F6FA"), borderColor=LINE, borderWidth=0.5, borderPadding=8, spaceBefore=3, spaceAfter=8))


def para(text, style="BodyLab"):
    return Paragraph(escape(text), styles[style])


def page_chrome(canvas, doc):
    canvas.saveState()
    width, height = letter
    canvas.setFillColor(NAVY)
    canvas.rect(0, height - 0.22 * inch, width, 0.22 * inch, stroke=0, fill=1)
    canvas.setFont(BOLD, 8)
    canvas.setFillColor(NAVY)
    canvas.drawString(0.72 * inch, height - 0.5 * inch, "BACKEND DEVELOPMENT LAB")
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.6)
    canvas.line(0.72 * inch, 0.52 * inch, width - 0.72 * inch, 0.52 * inch)
    canvas.setFont(FONT, 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.72 * inch, 0.34 * inch, "Experiment report")
    canvas.drawRightString(width - 0.72 * inch, 0.34 * inch, f"Page {doc.page}")
    canvas.restoreState()


def bullets(items):
    return ListFlowable(
        [para(item, "BulletLab") for item in items],
        bulletType="bullet",
        bulletFontName=FONT,
        bulletFontSize=6,
        bulletColor=BLUE,
        leftIndent=14,
        bulletDedent=5,
        spaceAfter=4,
    )


def numbered(items):
    return ListFlowable(
        [para(item, "BulletLab") for item in items],
        bulletType="1",
        start="1",
        bulletFontName=BOLD,
        bulletFontSize=8,
        bulletColor=BLUE,
        leftIndent=22,
        bulletDedent=8,
        spaceAfter=4,
    )


def build_report(report):
    target = OUTPUT / report["file"]
    doc = BaseDocTemplate(
        str(target),
        pagesize=letter,
        leftMargin=0.72 * inch,
        rightMargin=0.72 * inch,
        topMargin=0.82 * inch,
        bottomMargin=0.68 * inch,
        title=report["title"],
        author="Backend Development Lab",
        subject=report["summary"],
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main", leftPadding=0, rightPadding=0, topPadding=0.04 * inch, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="report", frames=[frame], onPage=page_chrome)])

    story = [
        para(report["number"], "Kicker"),
        para(report["title"], "ReportTitle"),
        para(report["summary"], "Summary"),
    ]
    details = Table(
        [[para("TECHNOLOGY STACK", "Kicker"), para("PROJECT FILES", "Kicker")],
         [para(report["stack"], "BodyLab"), para(report["location"], "SmallLab")]],
        colWidths=[3.2 * inch, 3.65 * inch],
        hAlign="LEFT",
    )
    details.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.extend([details, Spacer(1, 6)])
    story.append(para("Aim and Overview", "SectionHead"))
    story.append(para(report["summary"]))
    story.append(para("Requirements", "SectionHead"))
    story.append(bullets(report["requirements"]))
    story.append(para("Concepts and Components", "SectionHead"))
    story.append(bullets(report["topics"]))
    story.append(para("Procedure", "SectionHead"))
    story.append(numbered(report["steps"]))
    story.append(KeepTogether([
        para("Expected Learning Outcome", "SectionHead"),
        para(report["outcome"]),
    ]))
    story.append(KeepTogether([
        para("Code Snippet", "SectionHead"),
        para(f"{report['snippet_language']} · {report['snippet_source']}", "SmallLab"),
        Preformatted(report["snippet"], styles["CodeSample"]),
    ]))

    OUTPUT.mkdir(parents=True, exist_ok=True)
    doc.build(story)
    print(f"Created {target.relative_to(ROOT)}")


if __name__ == "__main__":
    for item in REPORTS:
        build_report(item)
