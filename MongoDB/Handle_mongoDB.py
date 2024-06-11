from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubeManagerpy:youtubeManagerpy@rakteem.o1odsdj.mongodb.net/", tlsAllowInvalidCertificates=True)
#  not a good practice.

db = client["ytManager"]
video_collection = db["videos"]

print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"Id : {video['_id']} | Name : {video['name']} | Time : {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, name, time):
    video_collection.update_one({"_id": ObjectId(video_id)}, {"$set": {"name": name, "time": time}})

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\n **** Youtube Manager ****")
        print("1. List of all youtube videos ")
        print("2. Add a new video")
        print("3. Update a video ")
        print("4. Delete a video")
        print("5. Exit")
        choice = int(input("Enter your choice : "))

        if choice  == 1:
            list_videos()
        elif choice == 2:
            name = input("Enter the name : ")
            time = input("Enter the time : ")
            add_video(name, time)
        elif choice == 3:
            video_id = input("Enter your id to update : ")
            name = input("Enter the name : ")
            time = input("Enter the time : ")
            update_video(video_id, name, time)
        elif choice == 4:
            video_id = input("Enter your id to update : ")
            delete_video(video_id)
        elif choice == 5:
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()