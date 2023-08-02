from fastapi import FastAPI

from app.api.v1.app import app


def create_app() -> FastAPI:
    return app
