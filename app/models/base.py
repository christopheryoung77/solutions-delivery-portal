"""
Atlas Domain Model

Base business object.

These are NOT SQLAlchemy models.
They represent business entities.

Author: Project Atlas
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseModel:

    created_at: datetime | None = None
    updated_at: datetime | None = None

    def touch(self):

        self.updated_at = datetime.now()
