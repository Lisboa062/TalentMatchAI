from fastapi import FastAPI

app = FastAPI(
    title="TalentMatch AI",
    version="0.1.0",
    description="AI powered resume and job matching API"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}