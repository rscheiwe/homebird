from fastapi import APIRouter
from api.models import HeartbeatSchema

health_router = APIRouter()


@health_router.get("/heartbeat", response_model=HeartbeatSchema)
async def health_check():
    """
    Aliveness check.
    """
    return {"health_check": "health status OK!"}