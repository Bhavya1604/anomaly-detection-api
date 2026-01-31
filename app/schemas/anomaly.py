from pydantic import BaseModel
from typing import List, Optional

class AnomalyRequest(BaseModel):
    series: List[float]
    threshold: Optional[float] = 1.5
