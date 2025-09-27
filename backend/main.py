from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import List

# Creamos la aplicación FastAPI
app = FastAPI()

# Definimos el modelo Ticket con sus campos
class Ticket(BaseModel):
    client: str                       # Nombre del cliente
    email: EmailStr                   # Email del cliente validado
    description: str                  # Descripción del ticket
    priority: str                     # Prioridad del ticket

# Lista para almacenar tickets en memoria
tickets: List[Ticket] = []

# Endpoint GET para verificar el estado de la API
@app.get("/health")
async def health_check():
    return {"ok": True}

# Endpoint POST para crear un ticket
@app.post("/tickets", status_code=201)
async def create_ticket(ticket: Ticket):
    tickets.append(ticket)
    return {"message": "Ticket creado exitosamente", "ticket": ticket}

# Endpoint GET para listar todos los tickets
@app.get("/tickets", response_model=List[Ticket])
async def list_tickets():
    return tickets
