import os


DIRS = [
    "practices",
    "projects",
]
OUT_FORMAT = "markdown"
OUTPUT_DIR = "web"


def main():
    for dir in DIRS:
        for file_name in os.listdir(dir):
            if os.path.splitext(file_name)[1].lower() == ".ipynb":
                input_file = os.path.join(dir, file_name)
                output_dir = os.path.join(OUTPUT_DIR, dir)

                os.system(f'jupyter nbconvert "{input_file}" --to={OUT_FORMAT} --output-dir="{output_dir}"')


main()
