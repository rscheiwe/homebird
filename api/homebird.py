from fastapi import APIRouter, HTTPException, Path
from typing import List, Any
from api.schemas import HomeSchema, HomeId, SewerType
from tinydb import TinyDB, Query
from api.create_db import create_db
from urllib.parse import unquote

homes_router = APIRouter()

homebird_db = create_db()


@homes_router.get("/homes", response_model=List[HomeSchema])
async def read_all_homes(
        sewer_type: SewerType,
) -> List:
    """
    **Retrieve all homes.**<br><br> Choose `sewer_type` to filter results. Select `any` to return all results.
    """
    try:
        if sewer_type.value == 'any':
            data = homebird_db.all()
            return data
        else:
            Home = Query()
            data = homebird_db.search(Home['property']['sewer'] == sewer_type.value)
            return data
    except:
        raise HTTPException(status_code=404, detail=f"Homes not found")


# @homes_router.get("/homes-ids",)
@homes_router.get("/homes-ids", response_model=List[HomeId])
async def read_all_homes_ids() -> List:
    """
    **Retrieve list of home_ids for testing.**
    """
    try:
        data = homebird_db.all()
        return [
            {key: value for key, value in obj.items() if key == "id"}
            for obj in data
        ]
    except:
        raise HTTPException(status_code=404, detail=f"Home IDs not found")


@homes_router.get("/homes/{home_address}", response_model=List[HomeSchema])
async def read_home_by_address(
        home_address: str,
) -> Any:
    """
    **Retrieve home by address.**<br><br>
    `home_address` is dispatched from the main API and is unique to an authenticated user.
    """
    try:
        Home = Query()
        decoded_uri = unquote(home_address)
        data = homebird_db.search(Home.property_address == decoded_uri)
        if data:
            return data
    except:
        raise HTTPException(status_code=404, detail=f"Home with id: {home_address} not found")
