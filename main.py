from fastapi import FastAPI
from resume_analysis_router import router as resume_analysis_router

app = FastAPI(title="Resume Analysis Test Server")

app.include_router(resume_analysis_router)

@app.get("/")
def root():
    return {"message": "resume analysis test server"}