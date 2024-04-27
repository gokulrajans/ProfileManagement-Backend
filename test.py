from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemFormat(BaseModel):
    id: int
    name: str
    mail: str

data = [{"id": 1,"name":"Gokulraj V", "mail":"gokul19.v@gmail.com"}, {"id": 2,"name":"Varatharajan", "mail":"varatharajan.s@gmail.com"}, {"id": 3,"name":"Gayathri V", "mail":"gayu.v@gmail.com"}]

@app.get("/get_all_user")
async def getAllUser():
    return data

@app.post("/addUser")
async def addUser(item: ItemFormat):
    data.append(item)
    return {"message": "User added Successfully"}

@app.put("/update/{item_id}")
async def updateUser(req):
    for i, stored_item in enumerate(req.data):
        if stored_item.id == req.item_id:
            data[i] = req.item
            return {"message": "Item updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/delete/{item_id}")
async def deleteUser(item_id: int):
    for i, stored_item in enumerate(data):
        if stored_item.id == item_id:
            del data[i]
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")