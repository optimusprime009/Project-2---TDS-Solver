from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
import shutil
import os
import zipfile
import pandas as pd

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/api/")
async def answer_question(question: str = Form(...), file: UploadFile = None):
    if file:
        temp_dir = "temp_files"
        os.makedirs(temp_dir, exist_ok=True)
        file_path = os.path.join(temp_dir, file.filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        if file.filename.endswith(".zip"):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
                for extracted_file in zip_ref.namelist():
                    if extracted_file.endswith(".csv"):
                        csv_path = os.path.join(temp_dir, extracted_file)
                        df = pd.read_csv(csv_path)
                        if "answer" in df.columns:
                            answer = str(df["answer"].iloc[0])
                            return {"answer": answer}
    
    # Default behavior for text-based questions
    answer = "This is a placeholder answer. Implement LLM integration here."
    return {"answer": answer}
