from fastapi import FastAPI

from routers.experiments_router import router


app = FastAPI()

app.include_router(router)
