from pydantic import BaseModel
from typing import Optional
from enum import Enum


class HeartbeatSchema(BaseModel):
    health_check: str


class PropertySchema(BaseModel):
    air_conditioning: str
    attic: str
    basement: str
    building_area_sq_ft: int
    building_condition_score: int
    building_quality_score: int
    construction_type: str
    exterior_walls: str
    fireplace: str
    full_bath_count: int
    garage_parking_of_cars: int
    garage_type_parking: str
    heating: str
    heating_fuel_type: str
    no_of_buildings: int
    no_of_stories: int
    number_of_bedrooms: int
    number_of_units: int
    partial_bath_count: int
    pool: str
    property_type: str
    roof_cover: str
    roof_type: str
    site_area_acres: float
    style: str
    total_bath_count: float
    total_number_of_rooms: int
    sewer: str
    subdivision: str
    water: str
    year_built: int
    zoning: str


class AssessmentSchema(BaseModel):
    apn: str
    assessment_year: int
    tax_year: int
    total_assessed_value: float
    tax_amount: float


class HomeId(BaseModel):
    id: int


class HomeAddress(BaseModel):
    property_address: str


class HomeSchema(BaseModel):
    id: int
    property_address: str
    property: Optional[PropertySchema] = None
    assessment: Optional[AssessmentSchema] = None

    class Config:
        orm_mode = True


class SewerType(str, Enum):
    municipal = "municipal"
    none = "none"
    storm = "storm"
    septic = "septic"
    yes = "yes"



