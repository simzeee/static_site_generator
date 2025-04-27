import os
import shutil

# os.path.exists
# os.listdir
# os.path.join
# os.path.isfile
# os.mkdir
# shutil.copy
# shutil.rmtree


def static_to_public(source_dir, dest_dir):
    # delete contents of destination dir
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isfile(source_path):
            # It's a file, copy it
            shutil.copy(source_path, dest_path)
            print(f"Copied file: {source_path} to {dest_path}")
        else:
            os.mkdir(dest_path)
            print(f"Created directory: {dest_path}")
            static_to_public(source_path, dest_path)


def main():
    static_to_public("static", "public")

# /Users/johnsims/Learn_Programming/static_site_generator/static
# /Users/johnsims/Learn_Programming/static_site_generator/public
# /Users/johnsims/Learn_Programming/static_site_generator/src/main.py
if __name__ == "__main__":
    main()
