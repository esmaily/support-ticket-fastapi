from fastapi import APIRouter, status

api_router = APIRouter()


@api_router.get(
    "/login",
    status_code=status.HTTP_200_OK,
    description="for test",
    responses={}
)
async def login():
    return {
        "title": "login page",
        "link": "google.com"
    }
