from pydantic import BaseModel
from typing import List

class BatchRequest(BaseModel):
    nm_ids: List[int]

class ProductResponse(BaseModel):
    nm_id: int
    price: float
    name: str