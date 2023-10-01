from fastapi import FastAPI

from routers.experiments_router import experiments_router


app = FastAPI()

app.include_router(experiments_router)
