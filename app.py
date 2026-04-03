from pdf_qa import extract_text_from_pdf, ask_bedrock

def main():
    pdf_path = "data/sample.pdf"

    print("📄 Reading PDF...")
    pdf_text = extract_text_from_pdf(pdf_path)

    print("✅ PDF loaded successfully.")

    while True:
        question = input("\nAsk a question about the PDF (or type 'exit'): ")

        if question.lower() == "exit":
            print("👋 Exiting application.")
            break

        answer = ask_bedrock(pdf_text, question)
        print("\n🤖 Answer:")
        print(answer)

if __name__ == "__main__":
    main()
