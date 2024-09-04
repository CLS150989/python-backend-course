from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    mail: str 
    active: bool
   
users_list = [User(id=1,name="Nudo", mail="nudo@nudoscloud.com", active=True), 
            User(id=2,name="Chirco",mail="chico@nudoscloud.com", active=True),
             User(id=3,name="Ko",mail="ko@nudoscloud.com", active=True),
             User(id=4,name="Pepe",mail="pepe@nudoscloud.com", active=True),
             User(id=5,name="Punky",mail="punky@nudoscloud.com", active=True),
             User(id=6,name="Chara", mail="chara@google.com", active= False)
            ] 



@app.get("/")
async def root():
    return {"Welcome to Chara's server"}



@app.get("/charas-users")
async def users():
    return list(users_list)



@app.get("/user/{id}")
async def users_perID(id : int):
    
   return search_user(id) 
    
#calling user per id  / name through query parameter. Example: http://0.0.0.0:8000/user-query/?id=1

@app.get("/user-query-id")
async def calling_user_perquery_parameter_id(id : int):
    return search_user(id)


# @app.get("/user-query-name")
# async def calling_user_perquery_parameter_name(name : str):
#     indexed_user = filter(lambda user : user.name == name, users_list )
#     return list(indexed_user)
    
@app.post("/user")
async def add_user(user : User):
    if user in users_list:
    
    #type(search_user(user.id)) == User:
        return "user already created"
    else:
        users_list.append(user)
        return "new user created"
    
    
@app.put("/user")
async def update_user_per_id(user : User):
    
    found = False
    
    for index, update_user in enumerate(users_list):
        if update_user.id == user.id:   
            users_list[index] = user
            found = True
            return "user updated"
    
    if not found:
        return "user doesn't exist"
        
        
            
def search_user(id:int):
    indexed_user = filter(lambda user : user.id, users_list)
    try:
       return list(indexed_user)[id - 1] 
    except:
        return {"error": "no user found"}
    
    
    
    
    