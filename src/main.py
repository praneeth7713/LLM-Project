from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
qa_pipeline = pipeline("text-generation", model="gpt2")  # Example model


@app.get("/")
def read_root():
    return {"message": "LLM Fintech Solution Running Successfully!"}


@app.get("/predict/")
def predict(query: str):
    response = qa_pipeline(query, max_length=100)
    return {"response": response[0]["generated_text"]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
