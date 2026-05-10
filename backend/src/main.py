from contextlib import asynccontextmanager
from loguru import logger

from fastapi import FastAPI
from routers import recomendations


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Service has started")
    yield
    logger.info("Service shutdown")


app = FastAPI(
    title="recomendations API",
    lifespan=lifespan,
)
app.include_router(recomendations.router, prefix="/api", tags=["items"])
