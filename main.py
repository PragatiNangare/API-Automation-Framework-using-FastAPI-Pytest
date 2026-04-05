from fastapi import FastAPI
from fastapi import HTTPException


app = FastAPI()

users = [
    {"id": 1, "name": "Pragati", "job": "QA"},
    {"id": 2, "name": "Rahul", "job": "Developer"}
]

@app.get("/users")
def get_all_users():
    return users

@app.get("/users/{user_id}")
def get_users(user_id: int):
    for user in users:
        if user["id"]== user_id:
            return user
    
    raise HTTPException(status_code=404, detail="User not found")
        
@app.post("/users")
def create_user(user: dict):
    new_id = len(users) + 1
    user["id"] = new_id
    users.append(user)
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int,updated_user: dict):
    for user in users:
        if user["id"]== user_id:
            user["name"]=updated_user["name"]
            user["job"] = updated_user["job"]
            return user
        
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["id"]== user_id:
            users.remove(user)
            return {"message":"User deleted"}
        
    raise HTTPException(status_code=404, detail="User not found")


   
   
    


