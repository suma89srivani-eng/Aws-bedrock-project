import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def test_bedrock_connection():
    try:
        client = boto3.client(
            "bedrock-runtime",
            region_name=os.getenv("AWS_DEFAULT_REGION"),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
        )

        print("✅ AWS Bedrock client initialized successfully.")
        print("Model configured:", os.getenv("BEDROCK_MODEL_ID"))

    except Exception as e:
        print("❌ Error connecting to AWS Bedrock:")
        print(e)

if __name__ == "__main__":
    test_bedrock_connection()
