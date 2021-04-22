from pymongo import MongoClient

import settings

# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
# client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_uri)
# client = MongoClient(settings.mongodb_uri, settings.port)
client = MongoClient(settings.mongodb_uri)

db = client['demo']