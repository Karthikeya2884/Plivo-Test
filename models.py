from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    organization_id = Column(Integer, ForeignKey("organizations.id"))

    organization = relationship("Organization", back_populates="users")


class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    users = relationship("User", back_populates="organization")
    services = relationship("Service", back_populates="organization")
    incidents = relationship("Incident", back_populates="organization")


class ServiceStatus(enum.Enum):
    OPERATIONAL = "Operational"
    DEGRADED = "Degraded Performance"
    PARTIAL_OUTAGE = "Partial Outage"
    MAJOR_OUTAGE = "Major Outage"


class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    status = Column(Enum(ServiceStatus), default=ServiceStatus.OPERATIONAL)
    organization_id = Column(Integer, ForeignKey("organizations.id"))

    organization = relationship("Organization", back_populates="services")


class Incident(Base):
    __tablename__ = "incidents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(Enum(ServiceStatus), default=ServiceStatus.MAJOR_OUTAGE)
    service_id = Column(Integer, ForeignKey("services.id"))
    organization_id = Column(Integer, ForeignKey("organizations.id"))

    service = relationship("Service")
    organization = relationship("Organization", back_populates="incidents")