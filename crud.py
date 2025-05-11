from sqlalchemy.orm import Session
from models import User, Organization, Service, Incident
from schemas import UserCreate, OrganizationCreate, ServiceCreate, IncidentCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_organization(db: Session, organization: OrganizationCreate):
    db_organization = Organization(name=organization.name, owner_id=organization.owner_id)
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization


def create_service(db: Session, service: ServiceCreate):
    db_service = Service(
        name=service.name, status=service.status, organization_id=service.organization_id
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service


def create_incident(db: Session, incident: IncidentCreate):
    db_incident = Incident(
        title=incident.title,
        description=incident.description,
        status=incident.status,
        service_id=incident.service_id,
        organization_id=incident.organization_id,
    )
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident


def get_services(db: Session):
    return db.query(Service).all()


def get_incidents(db: Session):
    return db.query(Incident).all()