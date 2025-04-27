import os
import shutil
import sys
from markdown_to_HTML import markdown_to_html_node, extract_title


def static_to_public(source_dir, dest_dir):
    # delete contents of destination dir
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
            print(f"Copied file: {source_path} to {dest_path}")
        else:
            os.mkdir(dest_path)
            print(f"Created directory: {dest_path}")
            static_to_public(source_path, dest_path)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # List all entries in the directory
    entries = os.listdir(dir_path_content)

    for entry in entries:
        # Create full paths
        content_path = os.path.join(dir_path_content, entry)

        # What if it's a file? What if it's a directory?
        if os.path.isfile(content_path) and content_path.endswith(".md"):
            # Determine the destination path
            # The file path should maintain the same structure but in the destination directory
            # and have .html extension instead of .md
            rel_path = os.path.relpath(content_path, dir_path_content)
            dest_file_path = os.path.join(
                dest_dir_path, rel_path.replace(".md", ".html")
            )

            # Make sure the destination directory exists
            os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)

            # Now generate the HTML (similar to what you already had)
            with open(content_path, "r") as f:
                markdown_content = f.read()
            with open(template_path, "r") as f:
                template_content = f.read()

            html_content = markdown_to_html_node(markdown_content).to_html()
            title = extract_title(markdown_content)

            final_html = template_content.replace("{{ Title }}", title)
            final_html = final_html.replace("{{ Content }}", html_content)
            final_html = final_html.replace('href="/', f'href="{basepath}')
            final_html = final_html.replace('src="/', f'src="{basepath}')

            # Write the final HTML to the destination file
            with open(dest_file_path, "w") as f:
                f.write(final_html)
        elif os.path.isdir(content_path):
            # Create the corresponding directory in the destination
            rel_dir_path = os.path.relpath(content_path, dir_path_content)
            new_dest_dir_path = os.path.join(dest_dir_path, rel_dir_path)
            os.makedirs(new_dest_dir_path, exist_ok=True)

            # Recursively process this directory
            generate_pages_recursive(content_path, template_path, new_dest_dir_path, basepath)


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'
    static_to_public("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
