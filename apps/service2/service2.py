
from fastapi import APIRouter

router = APIRouter()

@router.get("/service2")
async def service2():
    pass

