from pydantic import BaseModel
from typing import Optional


class CarOffer(BaseModel):
    id: int
    name: str
    type: str
    price: str
    old_price: Optional[str] = None
    image_url: str
    transmission: str
    fuel: str
    seats: str
    liked: bool = False
