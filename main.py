from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import User, Organization, Service, Incident
from schemas import UserCreate, OrganizationCreate, ServiceCreate, IncidentCreate
from crud import (
    create_user,
    create_organization,
    create_service,
    create_incident,
    get_services,
    get_incidents,
)

app = FastAPI()

# Create all tables
Base.metadata.create_all(bind=engine)


@app.post("/users/")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)


@app.post("/organizations/")
def create_organization_endpoint(
    organization: OrganizationCreate, db: Session = Depends(get_db)
):
    return create_organization(db=db, organization=organization)


@app.post("/services/")
def create_service_endpoint(service: ServiceCreate, db: Session = Depends(get_db)):
    return create_service(db=db, service=service)


@app.get("/services/")
def get_services_endpoint(db: Session = Depends(get_db)):
    return get_services(db=db)


@app.post("/incidents/")
def create_incident_endpoint(incident: IncidentCreate, db: Session = Depends(get_db)):
    return create_incident(db=db, incident=incident)


@app.get("/incidents/")
def get_incidents_endpoint(db: Session = Depends(get_db)):
    return get_incidents(db=db)