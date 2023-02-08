from pydantic import BaseModel


class HomeSchema(BaseModel):
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


class HomeId(BaseModel):
    id: int


class HomeDB(HomeSchema):
    id: int




