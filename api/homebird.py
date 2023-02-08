from fastapi import APIRouter, HTTPException, Path
from typing import List, Any
from api.models import HomeSchema, HomeId, SewerType
from tinydb import TinyDB, Query
from api.create_db import create_db, create_db_from_scratch

homes_router = APIRouter()

homebird_db = create_db()


@homes_router.get("/homes", response_model=List[HomeSchema])
async def read_all_homes() -> List:
    """
    Retrieve all homes.
    """
    try:
        data = homebird_db.all()
    except:
        raise HTTPException(status_code=404, detail=f"Homes not found")
    return data


# @homes_router.get("/homes-ids",)
@homes_router.get("/homes-ids", response_model=List[HomeId])
async def read_all_homes_ids() -> List:
    """
    Retrieve list of home_ids for testing.
    """
    try:
        data = homebird_db.all()
    except:
        raise HTTPException(status_code=404, detail=f"Home IDs not found")
    return [
        {key: value for key, value in obj.items() if key == "id"}
        for obj in data
    ]


@homes_router.get("/homes/{home_id}", response_model=List[HomeSchema])
async def read_home_by_id(
        home_id: int = Path(..., gt=0),
) -> Any:
    """
    Retrieve home by ID.
    """
    Home = Query()

    data = homebird_db.search(Home.id == home_id)
    if data:
        return data
    raise HTTPException(status_code=404, detail=f"Home with id: {home_id} not found")



@homes_router.get("/homes/")
async def read_home_by_sewer_type(
        sewer_type: SewerType,
) -> Any:
    """
    Retrieve home by Sewer Type.
    """
    Home = Query()

    data = homebird_db.search(Home['property']['sewer'] == sewer_type)
    if data:
        return data
    raise HTTPException(status_code=404, detail=f"Home with id: {sewer_type} not found")
