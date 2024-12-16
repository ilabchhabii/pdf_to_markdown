import os
from src.config.config import Config
from src.core.utils.file_utils import create_directories
from src.core.llamaparse.parser import parse_pdf_llama_parse
from src.core.unstructured.parser import parse_pdf_unstructured

def process_pdf_files(input_dir, output_dir, use_llama_parse = True):
    create_directories(input_dir, output_dir)

    while True:
        try:
            pdfs = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]
            if not pdfs:
                break
            processed_any = False
            for pdf in pdfs:
                pdf_path = os.path.join(input_dir, pdf)
                markdown_filename = pdf.replace(".pdf", ".md")
                markdown_path = os.path.join(output_dir, markdown_filename)
                
                if not os.path.exists(markdown_path):
                    if use_llama_parse:
                        result = parse_pdf_llama_parse(pdf_path, output_dir)
                    else:
                        result = parse_pdf_unstructured(pdf_path, output_dir)
                    
                    if result:
                        processed_any = True
                        print(f"Processed {pdf} and saved as {markdown_filename}")
                else:
                    print(f"Skipping {pdf} as {markdown_filename} already exists")
            if not processed_any:
                print("No new PDFs to process. Exiting...")
                break
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error processing PDF: {e}")
            break

if __name__ == "__main__":
    Config.validate()
    input_dir = "pdf_files_us"
    output_dir = "markdown_files_us"
    process_pdf_files(input_dir, output_dir, use_llama_parse = False)
