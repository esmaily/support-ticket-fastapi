from fastapi import FastAPI
from starlette.config import Config

config = Config(".env")  # parse .env file for env variables

ENVIRONMENT = config("ENVIRONMENT")  # get current env name
SHOW_DOCS_ENVIRONMENT = ("local", "staging")  # explicit list of allowed envs

app_configs = {"title": "Support Ticket API"}
if ENVIRONMENT not in SHOW_DOCS_ENVIRONMENT:
   app_configs["openapi_url"] = None  # set url for docs as null

app = FastAPI(**app_configs)