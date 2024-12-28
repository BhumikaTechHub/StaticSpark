import markdown
from jinja2 import Template

import os

def build_blog_index(posts, template, output_path):
    posts_list = "\n".join([f"<li><a href='{post['url']}'>{post['title']}</a></li>" for post in posts])
    rendered = template.render(Title="Blog", Content=f"<ul>{posts_list}</ul>")

    with open(f"{output_path}/blog.html", "w") as f:
        f.write(rendered)

def build_site(project_name="mysite"):
    content_path = f"{project_name}/content"
    #theme_path = f"{project_name}/themes/default/index.html"
    theme_path = os.path.join(project_name, "themes", "default", "index.html")

    output_path = f"{project_name}/public"

    os.makedirs(output_path, exist_ok=True)

    with open(theme_path, "r") as theme_file:
        template = Template(theme_file.read())

    posts = []
    for root, _, files in os.walk(content_path):
        for md_file in files:
            if md_file.endswith(".md"):
                with open(f"{root}/{md_file}", "r") as f:
                    md_content = f.read()
                    html_content = markdown.markdown(md_content)

                    title = md_content.split("\n")[0].replace("#", "").strip()
                    relative_path = os.path.relpath(root, content_path)
                    output_file = md_file.replace(".md", ".html")

                    if relative_path == "blog":
                        posts.append({"title": title, "url": f"blog/{output_file}"})

                    output_dir = f"{output_path}/{relative_path}"
                    os.makedirs(output_dir, exist_ok=True)

                    with open(f"{output_dir}/{output_file}", "w") as out_f:
                        out_f.write(template.render(Title=title, Content=html_content))

    if posts:
        build_blog_index(posts, template, output_path)

    print(f"Site built successfully at '{output_path}'.")

'''

def build_site(project_name="mysite"):
    content_path = f"{project_name}/content"
    theme_path = f"{project_name}/themes/default/index.html"
    output_path = f"{project_name}/public"

    os.makedirs(output_path, exist_ok=True)

    with open(theme_path, "r") as theme_file:
        template = Template(theme_file.read())

    for md_file in os.listdir(content_path):
        if md_file.endswith(".md"):
            with open(f"{content_path}/{md_file}", "r") as f:
                md_content = f.read()
                html_content = markdown.markdown(md_content)

                title = md_content.split("\n")[0].replace("#", "").strip()
                rendered = template.render(Title=title, Content=html_content)

                output_file = md_file.replace(".md", ".html")
                with open(f"{output_path}/{output_file}", "w") as out_f:
                    out_f.write(rendered)

    print(f"Site built successfully at '{output_path}'.")

'''