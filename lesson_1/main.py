from fastapi import FastAPI
from lesson_1.routers import books


app = FastAPI()


@app.get("/status")
async def status():
    return {"status": "running"}


app.include_router(books.router, prefix="/books")
