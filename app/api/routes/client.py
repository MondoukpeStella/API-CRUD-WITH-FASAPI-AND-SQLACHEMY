from fastapi import APIRouter, HTTPException, status
import sqlalchemy.exc
from app.models import (
    Client,
    Clients,
    ClientUpdate
)
import uuid
from app.database import SessionDep
import sqlalchemy

router = APIRouter()

@router.get("/", response_model=Clients)
def get_all_clients():
    pass

@router.post("/")
def create_client(client:Client, session: SessionDep) :
    try :
        session.add(client)
        session.commit()
        session.refresh(client)
        return client
    except sqlalchemy.exc.IntegrityError as e  :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Telephone number not available")

@router.get("/{id}", response_model=Client)
def get_client(id:str, session: SessionDep):
    client_id = uuid.UUID(id)
    client = session.get(Client, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/{id}")
def update_client(id:uuid.UUID, user:ClientUpdate):
    pass

@router.delete("/{id}")
def delete_client():
    pass