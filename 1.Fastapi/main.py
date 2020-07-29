from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_index():
    return {"Hello": "Bharath"}

@app.post("/scrape")
def trigger_scraping():
    return {"scraping": "yes"}


