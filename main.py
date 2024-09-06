
from schema.user_schema import UserSchema, AttendanceSchema, ReportSchema
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from controllers.user_controller import UserController
from controllers.auth_controller import AuthController
from controllers.attendance_controller import AttendanceController
from controllers.report_controller import ReportController
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Permite los métodos HTTP especificados
    allow_headers=["*"],  # Permite todos los encabezados en las solicitudes
)

user_controller = UserController()
auth_controller = AuthController()
attendance_controller = AttendanceController()
reports_controller = ReportController()
connected_clients: List[WebSocket] = []

class UserCredentials(BaseModel):
    username: str
    password: str

@app.post("/api/insert/user")
def insert_user(user_data: UserSchema):
    try:
        data = user_data.dict()
        data.pop("id", None)  # Eliminar el campo id si existe
        return user_controller.write(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.get("/api/get/user/{user_id}")
def get_user(user_id: int):
    try:
        return user_controller.read(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.put("/api/update/user/{user_id}")
def update_user(user_id: int, user_data: UserSchema):
    try:
        data = user_data.dict()
        return user_controller.update(user_id, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.delete("/api/delete/user/{user_id}")
def delete_user(user_id: int):
    try:
        return user_controller.delete(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.post("/api/authenticate")
def authenticate(user_credentials: UserCredentials):
    try:
        user_info = auth_controller.authenticate_user(user_credentials.username, user_credentials.password)
        if user_info:
            return user_info
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@app.get("/api/get/all_users")
def get_all_users():
    try:
        # Aquí llamamos a un método en el controlador para obtener todos los usuarios
        return user_controller.get_all_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    
@app.websocket("/ws/attendance")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Opcional: Procesar el mensaje recibido desde el cliente
    except WebSocketDisconnect:
        connected_clients.remove(websocket)

@app.post("/api/insert/attendance")
async def insert_attendance(attendance_data: AttendanceSchema):
    try:
        data = attendance_data.dict()
        data.pop("id", None)
        result = attendance_controller.insert_attendance(data)
        # Notificar a los clientes conectados
        for client in connected_clients:
            await client.send_json({"message": "new_attendance", "data": data})
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.get("/api/get/all_attendance")
def get_all_requests():
    try:
        return attendance_controller.get_all_requests()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    
@app.put("/api/update/attendance/{attendance_id}")
def update_attendance(attendance_id: int):
    try:
        # Supongamos que 'attendance_controller' es una instancia de la clase que tiene el método 'update_attendance'
        state = "Revisado"
        response = attendance_controller.update_attendance(attendance_id, state)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    
@app.post("/api/insert/reports")
async def insert_reports(reports_data: ReportSchema):
    try:
        data = reports_data.dict()
        data.pop("id", None)
        result = attendance_controller.insert_reports(data)
        # Notificar a los clientes conectados
        for client in connected_clients:
            await client.send_json({"message": "new_attendance", "data": data})
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    

@app.get("/api/get/all_reports")
def get_all_reports():
    try:
        return reports_controller.get_all_reports()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")