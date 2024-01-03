import pymongo
from mongomock import MongoClient

client = MongoClient()
db = client["mydatabase"]

collection = db["student"]

print("Start")

student1 = {
    "name": "Ava",
    "address": "Slumpgatan 1"
}

student2 = {
    "name": "Erik",
    "address": "Tråkgatan 2"
}

student3 = {
    "name": "Berit",
    "address": "Lyckliga gatan 20",
    "points": 60
}

#collection.insert_one(student1)

print("\nInsert and print all students.")
collection.insert_many([student1, student2, student3])

all_students = collection.find()

for student in all_students:
    print(student)

# Find students with 60 points
print("\nInsert a student with 60 points and print him.")
points_60_students = collection.find({"points": 60})

for student in points_60_students:
    print(student)

# Update points for Ava and Erik
print("\nGive Ava and Erik points and print all students with a 'points' field.")
collection.update_one({"name": "Ava"}, {"$set": {"points": 70}})
collection.update_one({"name": "Erik"}, {"$set": {"points": 20}})

# Find students with the "points" field
students_with_points = collection.find({"points": {"$exists": True}})

for student in students_with_points:
    print(student)

# Find students with 20 points or more
print("\nGet all students with >20 points.")
points_20_or_more_students = collection.find({"points": {"$gte": 20}})

for student in points_20_or_more_students:
    print(student)

# Update all students to use an embedded document for their address
print("\nUpdate all students to use an embedded document for their address")
collection.update_many({}, {"$set": {"address": {"street": "", "postcode": 0, "city": ""}}})

all_students = collection.find()

for student in all_students:
    print(student)