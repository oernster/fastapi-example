from typing import Optional
from fastapi import FastAPI
from routers import main, values, words


app = FastAPI()


app.include_router(main.router)
app.include_router(values.router)
app.include_router(words.router)
