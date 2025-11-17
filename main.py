from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до локальної MongoDB
client = MongoClient("mongodb://127.0.0.1:27017")
db = client.catsDB
cats_collection = db.cats

# ==========================
# CREATE
# ==========================
def create_cat(name, age, features):
    try:
        cat = {"name": name, "age": age, "features": features}
        result = cats_collection.insert_one(cat)
        print(f"Added cat with id: {result.inserted_id}")
    except Exception as e:
        print(f"Error adding cat: {e}")

# ==========================
# READ
# ==========================
def get_all_cats():
    try:
        cats = list(cats_collection.find())
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Error fetching cats: {e}")

def get_cat_by_name(name):
    try:
        cat = cats_collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"No cat found with name: {name}")
    except Exception as e:
        print(f"Error fetching cat: {e}")

# ==========================
# UPDATE
# ==========================
def update_cat_age(name, new_age):
    try:
        result = cats_collection.update_one({"name": name}, {"$set": {"age": new_age}})
        print(f"Matched {result.matched_count}, Modified {result.modified_count}")
    except Exception as e:
        print(f"Error updating age: {e}")

def add_cat_feature(name, feature):
    try:
        result = cats_collection.update_one({"name": name}, {"$push": {"features": feature}})
        print(f"Matched {result.matched_count}, Modified {result.modified_count}")
    except Exception as e:
        print(f"Error adding feature: {e}")

# ==========================
# DELETE
# ==========================
def delete_cat_by_name(name):
    try:
        result = cats_collection.delete_one({"name": name})
        print(f"Deleted {result.deleted_count} cat(s)")
    except Exception as e:
        print(f"Error deleting cat: {e}")

def delete_all_cats():
    try:
        result = cats_collection.delete_many({})
        print(f"Deleted {result.deleted_count} cat(s)")
    except Exception as e:
        print(f"Error deleting all cats: {e}")

# ==========================
# Приклад використання
# ==========================
if __name__ == "__main__":
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    get_all_cats()
    get_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_cat_feature("barsik", "любить гратися з м'ячиком")
    get_cat_by_name("barsik")
    # delete_cat_by_name("barsik")
    # delete_all_cats()

