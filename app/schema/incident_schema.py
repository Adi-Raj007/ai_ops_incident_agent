from pydantic import BaseModel, Field
from typing import Literal


class IncidentClassification(BaseModel):
    """
    Strict schema for incident classification output.
    """

    incident_type: Literal["cpu", "disk", "service", "unknown"] = Field(
        ...,
        description="Type of system incident"
    )

    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence score between 0 and 1"
    )
