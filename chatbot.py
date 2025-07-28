from transformers import pipeline

def generate_response(question, context):
    generator = pipeline('text-generation', model='distilbert-base-uncased')
    prompt = f"Frage: {question}\nKontext: {context}\nAntwort:"
    result = generator(prompt, max_length=100, do_sample=True)
    return result[0]['generated_text']
