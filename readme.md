# PDF to DOCX Converter

This is a Flask web application that allows users to upload PDF files and convert them to DOCX format. The application supports scanned PDF files and can extract text from them, including text in Vietnamese.

## Features

- Upload PDF files and convert them to DOCX format.
- Support for scanned PDF files using PyMuPDF for text extraction.
- Full support for Vietnamese text extraction.
- Easy to use web interface.

## Installation

1.  Clone the repository:

        ```bash
        git clone https://github.com:tathiyennhi/pdf-to-docx-converter-python.git
        cd pdf-to-docx-converter
        ```

    s

2.  Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Upload a PDF file and click on the "Convert" button.

4. The converted DOCX file will be downloaded automatically.

## Dependencies

- Flask==2.1.1
- werkzeug==2.1.1
- python-docx==0.8.11
- PyMuPDF==1.19.6

## Project Structure

pdf-to-docx-converter/
│
├── app.py
├── requirements.txt
├── uploads/
│
└── templates/
└── index.html

## Notes

- Make sure the `uploads` directory is writable.
- The application deletes the uploaded PDF file after conversion to save space.

## License

This project is licensed under the MIT License.
