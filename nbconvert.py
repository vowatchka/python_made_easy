"""
Модуль для конвертации примеров решений практических задач из формата
Jupyter Notebook в формат Markdown.
"""

import os


DIRS = [
    "practices",
    "projects",
]
OUT_FORMAT = "markdown"
OUTPUT_DIR = "web"


def main():
    for dir_ in DIRS:
        for file_name in os.listdir(dir_):
            if os.path.splitext(file_name)[1].lower() == ".ipynb":
                input_file = os.path.join(dir_, file_name)
                output_dir = os.path.join(OUTPUT_DIR, dir_)

                os.system(f'jupyter nbconvert "{input_file}" --to={OUT_FORMAT} --output-dir="{output_dir}"')


main()
