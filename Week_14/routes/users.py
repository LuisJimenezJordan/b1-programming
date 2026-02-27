from fastapi import APIRouter, HTTPException
from schema import User, UserCreate
from user_store import UserStore

router = APIRouter()
store = UserStore("users.txt")

def get_next_id():
    users = store.load()
    return max([u["id"] for u in users], default=0) + 1

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    users = store.load()
    new_user = {"id": get_next_id(), "name": user.name, "email": user.email}
    users.append(new_user)
    store.save(users)
    return new_user

@router.get("/", response_model=list[User])
def get_all_users():
    return store.load()

@router.get("/search", response_model=list[User])
def search_users(q: str):
    users = store.load()
    return [u for u in users if q.lower() in u["name"].lower()]

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = store.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserCreate):
    updated_data = {"name": user_update.name, "email": user_update.email}
    success = store.update_user(user_id, updated_data)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return store.find_by_id(user_id)

@router.delete("/{user_id}")
def delete_user(user_id: int):
    success = store.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}