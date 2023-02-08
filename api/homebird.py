from fastapi import APIRouter, HTTPException, Path
from typing import List, Any

from pysondb.db import JsonDatabase
from api.create_db import create_db

router = APIRouter()

homebird_db: JsonDatabase = create_db()


@router.get("/homes")
async def read_all_homes():
    """
    Retrieve all homes.
    """
    data = homebird_db.getAll()

    if not data:
        raise HTTPException(status_code=404, detail=f"Homes not found")
    return data


@router.get("/homes-ids")
async def read_all_homes_ids():
    """
    Retrieve list of home_ids for testing.
    """
    data = homebird_db.getAll()
    return [{key: value for key, value in obj.items() if key == "id"} for obj in data]


@router.get("/homes/{home_id}")
async def read_home(
        home_id: int = Path(..., gt=0),
) -> Any:
    """
    Retrieve home by ID.
    """
    try:
        data = homebird_db.getById(home_id)
    except:
        raise HTTPException(status_code=404, detail=f"Home with id: {home_id} not found")
    return data
