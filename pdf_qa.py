import os
import boto3
import json
from dotenv import load_dotenv
from PyPDF2 import PdfReader

load_dotenv()

AWS_REGION = os.getenv("AWS_DEFAULT_REGION")
MODEL_ID = os.getenv("BEDROCK_MODEL_ID")

def extract_text_from_pdf(pdf_path):
    text = ""
    reader = PdfReader(pdf_path)

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text

def ask_bedrock(context, question):
    client = boto3.client(
        "bedrock-runtime",
        region_name=AWS_REGION,
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )

    prompt = f"""
You are a helpful assistant.

Use the following PDF content to answer the user's question.

PDF Content:
{context}

Question:
{question}

Answer:
"""

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 500,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    result = json.loads(response["body"].read())
    return result["content"][0]["text"]
