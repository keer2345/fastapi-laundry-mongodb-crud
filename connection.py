# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_uri)
db = client['usersdata']