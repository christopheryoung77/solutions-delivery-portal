from dataclasses import dataclass

from .base import BaseModel


@dataclass
class AccountManager(BaseModel):

    name: str = ""

    customers: int = 0
