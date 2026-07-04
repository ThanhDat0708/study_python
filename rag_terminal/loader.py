#  load file txt
def txt_loader(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
def pdf_loader(file_path):
    pass
def docx_loader(file_path):
    pass
def html_loader(file_path):
    pass