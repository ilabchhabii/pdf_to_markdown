from unstructured.partition.pdf import partition_pdf
from src.core.utils.file_utils import get_output_path
from unstructured.staging.base import elements_to_json
def pdf_to_raw_elements(file_path, infer_table_structure=True):
    return partition_pdf(
        filename=file_path,
        extract_images_in_pdf=False,
        infer_table_structure=infer_table_structure,
        chunking_strategy="by_title",
        output_format="markdown"
    )

def parse_pdf_unstructured(pdf_path, output_directory):
    print(f"Parsing PDF with unstructured parser: {pdf_path}")
    try:
        raw_elements = pdf_to_raw_elements(file_path=pdf_path)
        # print(f"{elements_to_json(raw_elements, indent=2)}")

        output_path = get_output_path(pdf_path, output_directory)
        with open(output_path, "w") as f:
            for element in raw_elements:
                f.write(element.text + "\n")
        
        print(f"Markdown file created: {output_path}")
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
    
