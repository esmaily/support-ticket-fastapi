from fastapi import APIRouter, status

api_router = APIRouter()


@api_router.get(
    "/list",
    status_code=status.HTTP_200_OK,
    description="user ticket list",
    responses={}
)
async def ticket_list():
    return {
        "nane": "ticket list"
    }
