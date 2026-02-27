from fastapi import APIRouter, HTTPException
from schema import User, UserCreate
import json
import os

router = APIRouter()

def read_users():
    if not os.path.exists("users.txt"):
        return []
    try:
        with open("users.txt", "r") as f:
            return json.load(f)
    except:
        return []

def write_users(users):
    with open("users.txt", "w") as f:
        json.dump(users, f, indent=2)

def get_next_id():
    users = read_users()
    return max([u["id"] for u in users], default=0) + 1

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    users = read_users()
    new_user = {"id": get_next_id(), "name": user.name, "email": user.email}
    users.append(new_user)
    write_users(users)
    return new_user

@router.get("/", response_model=list[User])
def get_all_users():
    return read_users()

@router.get("/search", response_model=list[User])
def search_users(q: str):
    users = read_users()
    return [u for u in users if q.lower() in u["name"].lower()]

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    users = read_users()
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserCreate):
    users = read_users()
    for i, u in enumerate(users):
        if u["id"] == user_id:
            users[i] = {"id": user_id, "name": user_update.name, "email": user_update.email}
            write_users(users)
            return users[i]
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
def delete_user(user_id: int):
    users = read_users()
    filtered = [u for u in users if u["id"] != user_id]
    if len(filtered) == len(users):
        raise HTTPException(status_code=404, detail="User not found")
    write_users(filtered)
    return {"message": "User deleted"}