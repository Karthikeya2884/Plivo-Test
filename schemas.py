from pydantic import BaseModel
from enum import Enum


class ServiceStatus(str, Enum):
    OPERATIONAL = "Operational"
    DEGRADED = "Degraded Performance"
    PARTIAL_OUTAGE = "Partial Outage"
    MAJOR_OUTAGE = "Major Outage"


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class OrganizationBase(BaseModel):
    name: str


class OrganizationCreate(OrganizationBase):
    owner_id: int


class ServiceBase(BaseModel):
    name: str
    status: ServiceStatus


class ServiceCreate(ServiceBase):
    organization_id: int


class IncidentBase(BaseModel):
    title: str
    description: str
    status: ServiceStatus


class IncidentCreate(IncidentBase):
    service_id: int
    organization_id: int