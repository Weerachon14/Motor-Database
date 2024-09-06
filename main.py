from fastapi import FastAPI
from bson import ObjectId, json_util
import json
from pydantic import BaseModel
from pymongo.mongo_client import MongoClient

uri = "mongodb://localhost:27017"
#เวลาเข้าmongo ต้องใช้เป็น mongodb://mongoadmin:mongoadmin@localhost:4322/?authMechanism=DEFAULT

client = MongoClient(uri, connect=False)
print('🚀 Connected to MongoDB...')
# Send a ping to confirm a successful connection
try:
    db = client['motor']
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = FastAPI()


class Motors_record(BaseModel):
    motor_id:str
    motor_name:str
    factory:str
    Series:str
    IOT:str
class Sensors_record(BaseModel):
    motor_id:str
    Temperture:str     
    Voltage:str
    Current:str
    Accelerometer:str
    Vibration:str
    
class User_record(BaseModel):
    user_id:str
    motor_id:str
    username:str
    email:str
    



# @app.post("/add/user")
# def create_user(user_data:UserModel):
#     #Check is username exist
#     users = db.user.find_one({'username':user_data.username})
#     if users:
#         return {"error":"username already used."}
#     db.user.insert_one(dict(user_data))
#     return {"success":f"user {user_data.username} created"}
# @app.get("/")
# async def read_root():
#     return {"message": "Hello, FastAPI!"}

# @app.post("/Motor_record")
# async def record_motor(dummy_data:Motors_record):
#     random_data = dummy_data.dict()
#     random_data["_id"] = ObjectId()
    
#     #await คือสั่งให้รอ insert ให้เสร็จ
#     result = await collection_motor.insert_one(random_data)
#     if result.inserted_id:         
#         return {"msg": "Motor added successfully", "MotorId": str(result.inserted_id)}     
#     else:         
#         raise HTTPException(status_code=400, detail="Error adding user")
    
# @app.post("/Sensors_record")
# async def record_sensor(dummy_data:Sensors_record):
#     random_data = dummy_data.dict()
#     random_data["_id"] = ObjectId()
    
#     #await คือสั่งให้รอ insert ให้เสร็จ
#     result = await collection_sensor.insert_one(random_data)
#     if result.inserted_id:         
#         return {"msg": "sensor added successfully", "sensorId": str(result.inserted_id)}     
#     else:         
#         raise HTTPException(status_code=400, detail="Error adding user")

# @app.post("/User_record")
# async def record_user(dummy_data:User_record):
#     random_data = dummy_data.dict()
#     random_data["_id"] = ObjectId()
    
#     #await คือสั่งให้รอ insert ให้เสร็จ
#     result = await collection_user.insert_one(random_data)
#     if result.inserted_id:         
#         return {"msg": "User added successfully", "userId": str(result.inserted_id)}     
#     else:         
#         raise HTTPException(status_code=400, detail="Error adding user")
    
@app.get("/")
def index():
    users = db.user.find_one()
    return {"Users": json.loads(json_util.dumps(users))}


@app.get("/username/{username}")
def find_username(username):
    users = db.user.find_one({'username':username})
    return {"users": json.loads(json_util.dumps(users))}

@app.post("/addUser")
def create_user(user_data:User_record):
    #Check is username exist
    users = db.User.find_one({'user':user_data.username})
    if users:
        return {"error":"username already used."}
    db.User.insert_one(dict(user_data))
    return {"success":f"user {user_data.username} created"}





    
#step get body from postman

#save to database

#response success or fail

# db = client["motor"]

# db_info = db.list_collection_names()
# print(db_info)

# server_info = client.server_info()
# print(server_info)
# collection = db["Motors"]


# def insert_random_data():
#     # สุ่มข้อมูล
#     random_id = random.randint(1, 100)
#     random_string = ''.join(random.choices(string.ascii_letters, k=10)) 
#     random_location = random.choice(["Bangkok", "Chiang Mai", "Phuket"]) 
#     random_series = random.choice(["A", "B", "C"]) 


#     result = collection.insert({
#         "ID": random_id,
#         "Name": random_string,
#         "Location": random_location,
#         "Series": random_series
#     })
#     print("Show!!!!!:",random_id,random_string,random_location,random_series)
#     return result.inserted_id  # คืนค่า _id ของเอกสารที่เพิ่ม

# document_id = insert_random_data()
# print("Inserted document with ID:", document_id)