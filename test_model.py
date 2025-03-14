from transformers import pipeline

qa_pipeline = pipeline("text-generation", model="gpt2")
print("Model loaded successfully!")

