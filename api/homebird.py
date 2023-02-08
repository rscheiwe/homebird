from fastapi import APIRouter, HTTPException, Path
from typing import List, Any
from api.models import HomeSchema, HomeDB, HomeId
from pysondb.db import JsonDatabase
from api.create_db import create_db

router = APIRouter()

homebird_db: JsonDatabase = create_db()


@router.get("/homes", response_model=List[HomeDB])
async def read_all_homes() -> List:
    """
    Retrieve all homes.
    """
    try:
        data = homebird_db.getAll()
    except:
        raise HTTPException(status_code=404, detail=f"Homes not found")
    return data


@router.get("/homes-ids", response_model=List[HomeId])
async def read_all_homes_ids() -> List:
    """
    Retrieve list of home_ids for testing.
    """
    try:
        data = homebird_db.getAll()
    except:
        raise HTTPException(status_code=404, detail=f"Home IDs not found")
    return [
        {key: value for key, value in obj.items() if key == "id"}
        for obj in data
    ]


@router.get("/homes/{home_id}", response_model=HomeDB)
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
