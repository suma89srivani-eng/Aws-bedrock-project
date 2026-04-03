# AWS Bedrock PDF QA Project Notes

## Project Goal
Build a PDF Question Answering application using AWS Bedrock and Python.

## Features
- Upload or load a PDF file
- Extract text from PDF
- Ask questions based on PDF content
- Use AWS Bedrock foundation model for answering

## Technologies Used
- Python
- AWS Bedrock
- Boto3
- PDF text extraction libraries

## Files
- `app.py` → Main app entry point
- `pdf_qa.py` → PDF extraction and QA logic
- `test_bedrock.py` → Bedrock API connection test
- `requirements.txt` → Dependencies

## Future Improvements
- Add Streamlit UI
- Add multiple PDF support
- Add chunking + embeddings
- Add retrieval-based QA
