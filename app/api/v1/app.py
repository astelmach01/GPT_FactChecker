from fastapi import FastAPI

from app.settings import settings

app = FastAPI(
    title=settings.project_name, openapi_url=f"/{settings.API_V1_STR}/openapi.json"
)

# include all the routers here
# app.include_router(, prefix='/v1')
