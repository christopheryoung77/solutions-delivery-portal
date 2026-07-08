from dataclasses import dataclass

from .base import BaseModel


@dataclass
class WorkItem(BaseModel):

    work_type: str = ""

    customer: str = ""

    account_manager: str = ""

    assigned_to: str = ""

    status: str = ""

    status_description: str = ""

    request_details: str = ""

    priority: str = ""

    due_date: str = ""
