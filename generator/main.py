import sys
import os

# Add the parent directory (root) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def init_site(project_name):
    if not os.path.exists(project_name):
        os.makedirs(project_name)
        with open(f"{project_name}/index.html", "w") as f:
            f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Welcome</title>\n</head>\n<body>\n<h1>Hello World!</h1>\n</body>\n</html>")
        print(f"Project '{project_name}' initialized.")
    else:
        print(f"Project '{project_name}' already exists.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3 or sys.argv[1] != "init":
        print("Usage: python main.py init <project_name>")
    else:
        init_site(sys.argv[2])


def create_theme(theme_name, project_name="mysite"):
    theme_path = f"{project_name}/themes/{theme_name}"
    os.makedirs(theme_path, exist_ok=True)
    with open(f"{theme_path}/index.html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>{{ Title }}</title>\n</head>\n<body>\n{{ Content }}</body>\n</html>")
    print(f"Theme '{theme_name}' created at '{theme_path}'.")

# Add to main logic
if sys.argv[1] == "new" and sys.argv[2] == "theme":
    if len(sys.argv) < 4:
        print("Usage: python main.py new theme <theme_name>")
    else:
        create_theme(sys.argv[3])



def create_content(project_name="mysite"):
    content_path = f"{project_name}/content"
    os.makedirs(content_path, exist_ok=True)
    with open(f"{content_path}/index.md", "w") as f:
        f.write("# Welcome\nThis is your homepage.")
    print(f"Content directory created at '{content_path}'.")

def new_page(page_name, project_name="mysite"):
    page_path = f"{project_name}/content/{page_name}.md"
    with open(page_path, "w") as f:
        f.write(f"# {page_name.capitalize()}\nThis is the {page_name} page.")
    print(f"Page '{page_name}' created at '{page_path}'.")

# Add to main logic
if sys.argv[1] == "new" and sys.argv[2] == "page":
    if len(sys.argv) < 4:
        print("Usage: python main.py new page <page_name>")
    else:
        new_page(sys.argv[3])


from generator.server import watch_and_serve

if sys.argv[1] == "serve":
    watch_and_serve("mysite", port=8000)

