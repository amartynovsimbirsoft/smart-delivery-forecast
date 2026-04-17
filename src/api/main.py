from fastapi import FastAPI

app = FastAPI(title="Forecast API")

@app.get("/")
def root():
    return {"message": "Forecast API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}