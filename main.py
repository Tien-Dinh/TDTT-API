import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

app = FastAPI(
    title="Cloud AI Summarization API",
    description="API tóm tắt văn bản sử dụng Hugging Face Inference API.",
    version="1.0.0"
)

class RemoteSummarizationModel:
    def __init__(self):
        if not HF_TOKEN:
            raise RuntimeError("Thiếu HF_TOKEN. Vui lòng cấu hình trong file .env")
        self.client = InferenceClient(
            provider="hf-inference",
            api_key=HF_TOKEN
        )
        self.model_name = "facebook/bart-large-cnn"

    def summarize(self, text: str):
        try:
            result = self.client.summarization(
                text,
                model=self.model_name
            )
            return result.summary_text
        except Exception as e:
            raise RuntimeError(f"Lỗi từ Hugging Face: {str(e)}")

ai_model = RemoteSummarizationModel()

class SummaryRequest(BaseModel):
    text: str =  Field(..., min_length=50, description="Văn bản cần tóm tắt (>= 50 ký tự)")

@app.get("/")
async def root():
    return {
        "message": "API Tóm tắt văn bản sử dụng Hugging Face Inference API",
        "model": "facebook/bart-large-cnn"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "ok", 
        "message": "API Backend hoạt động bình thường và đã nạp HF_TOKEN"
    }

@app.post("/predict")
async def predict(request: SummaryRequest):    
    try:
        summary = ai_model.summarize(request.text)
        return {
            "original_length": len(request.text),
            "summary_text": summary
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)