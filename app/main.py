from fastapi import FastAPI

from routers import experiments, db, metrics


app = FastAPI()

app.include_router(experiments.router)
app.include_router(db.router)
app.include_router(metrics.router)
