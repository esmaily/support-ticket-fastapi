from fastapi import FastAPI
from starlette.config import Config
from router import router
from config import settings

app = FastAPI()

config = Config(".env")  # parse .env file for env variables

ENVIRONMENT = config("ENVIRONMENT")  # get current env name
SHOW_DOCS_ENVIRONMENT = ("local", "staging")  # explicit list of allowed envs

app_configs = {"title": settings.PROJECT_NAME}
if ENVIRONMENT not in SHOW_DOCS_ENVIRONMENT:
    app_configs["openapi_url"] = None  # set url for docs as null

app = FastAPI(**app_configs)
app.include_router(router, prefix=settings.API_V1, tags=["api/v1"])


@app.get(
    "/",
    description="index page",
    responses={}
)
async def index_page():
    return {
        "nane": "index page"
    }
