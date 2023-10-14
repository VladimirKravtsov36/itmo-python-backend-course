from fastapi import APIRouter

from db.create import create_experiments_table

router = APIRouter()


@router.on_event("startup")
def startup_db_client():
    create_experiments_table()
