from fastapi import APIRouter, HTTPException, Path
from typing import List, Any

from pysondb.db import JsonDatabase
from api.create_db import create_db

from dummy_db.house_canary_data import house_one


router = APIRouter()


@router.get("/homes")
async def read_all_homes():
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"health_check": "health status OK!"}


@router.get("/homes/{home_id}")
async def read_home(
        home_id,
) -> Any:
    """
    Retrieve home by ID.
    """

    homebird_db = create_db()

    if home_id:
        q = {"garage_type_parking": "underground_basement"}
        data = homebird_db.getById(313137202477298579)
    # else:
    #     home = None
    if not data:
        raise HTTPException(status_code=404, detail=f"Home with id: {home_id} not found")
    return data
