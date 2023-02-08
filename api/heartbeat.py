from fastapi import APIRouter

health_router = APIRouter()


@health_router.get("/heartbeat")
async def health_check():
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"health_check": "health status OK!"}