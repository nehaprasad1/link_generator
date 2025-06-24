
import os

folders = [
    "templates",
    "static"
]

files = {
    "main.py": "",
    "models.py": "",
    "requirements.txt": "",
    "templates/index.html": "",
    "static/style.css": "",
    "static/script.js": "",
    ".gitignore": "venv/\n__pycache__/\n*.pyc\ndatabase.db\n.env"
}

# Step 1: Create folders first
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Step 2: Create files, only create parent folder if needed
for path, content in files.items():
    dir_name = os.path.dirname(path)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Project structure created successfully!")
