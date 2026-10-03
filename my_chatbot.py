import ollama

def load_document(filename):
    with open(filename, 'r') as f:
        return f.read()

def ask_question(document_text, question):
    prompt = "Answer the question using ONLY the information in this document.\n\nDocument:\n" + document_text + "\n\nQuestion: " + question + "\n\nAnswer:"
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

document = load_document('mydocument.txt')
question = input("Ask a question about the document: ")
answer = ask_question(document, question)
print("\nAnswer:", answer)