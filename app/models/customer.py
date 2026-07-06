from dataclasses import dataclass

from .base import BaseModel


@dataclass
class Customer(BaseModel):

    name: str = ""

    account_manager: str = ""

    active_requests: int = 0
