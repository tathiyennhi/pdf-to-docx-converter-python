from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from docx import Document
import os
import fitz  # PyMuPDF

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def convert_pdf_to_docx(pdf_path, docx_path):
    doc = Document()
    
    # Using PyMuPDF to extract text from PDF
    with fitz.open(pdf_path) as pdf_document:
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text = page.get_text()
            doc.add_paragraph(text)

    # Save the document to DOCX file
    doc.save(docx_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '' or not allowed_file(file.filename):
        return redirect(url_for('index'))

    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    file.save(pdf_path)

    docx_filename = f'{os.path.splitext(os.path.basename(pdf_path))[0]}.docx'
    docx_path = os.path.join(app.config['UPLOAD_FOLDER'], docx_filename)

    convert_pdf_to_docx(pdf_path, docx_path)

    os.remove(pdf_path)

    return send_file(docx_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
