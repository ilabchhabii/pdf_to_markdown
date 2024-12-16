import os

def create_directories(*dirs):
    for d in dirs:
        os.makedirs(d, exist_ok=True)

def get_output_path(pdf_path, output_dir):
    name = os.path.basename(pdf_path).replace(".pdf", ".md")
    return os.path.join(output_dir, name)
