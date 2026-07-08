from dataclasses import dataclass

from .base import BaseModel


@dataclass
class Engineer(BaseModel):

    name: str = ""

    speciality: str = ""

    workload: int = 0
