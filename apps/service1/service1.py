from fastapi import APIRouter

router = APIRouter()

@router.get("/service1")
async def service1():
    pass


@router.get("/service1/register")
async def service1_register():
    pass