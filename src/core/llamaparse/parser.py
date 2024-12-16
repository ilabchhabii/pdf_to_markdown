import os
from llama_parse import LlamaParse
from src.core.utils.file_utils import get_output_path
from src.core.utils.key_rotation import rotate_key
from src.config.config import Config
def parse_pdf_llama_parse(pdf_path, output_dir):
    print("Parsing PDF with LlamaParse...", pdf_path)
    output_path = get_output_path(pdf_path, output_dir)
    if os.path.exists(output_path):
        return output_path
    max_keys = len(Config.LLAMA_CLOUD_API_KEYS)
    attempts = 0
    while attempts < max_keys:
        try:
            documents = LlamaParse(result_type="markdown").load_data(pdf_path)
            with open(output_path, "w") as f:
                f.write("\n".join(doc.text for doc in documents))
            return output_path
        except Exception as e:
            print(f"Error parsing PDF: {e}")
            attempts += 1
            if not rotate_key(Config, attempts):
                break
    return None