from pydantic import BaseModel


class Pollution(BaseModel):
    ts: str
    aqius: int
    mainus: str
    aqicn: int
    maincn: str


class Weather(BaseModel):
    ts: str
    tp: int
    pr: int
    hu: int
    ws: float
    wd: int
    ic: str


class Location(BaseModel):
    type: str
    coordinates: list[float]


class AirVisual(BaseModel):
    city: str
    state: str
    country: str
    location: Location
    current: dict = {
        'pollution': Pollution,
        'weather': Weather
    }


class AirVisualModel(BaseModel):
    status: str
    data: AirVisual
