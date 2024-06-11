
import json

def load_data():
    try:
        # open as read so as not to create file infinite times.
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("*"*50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video["name"]} ~ {video["time"]}")
    print("*"*50)

def add_video(videos):
    name = input("Enter the name ")
    time = input("Enter the time ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    index=int(input("Enter the video number to update : "))

    if index >= 1 and index <= len(videos):
        name = input("Update Name : ")
        time = input("Updated Time : ")
        videos[index-1]={"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("The video selected is not available. ")

def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to be deleted : "))

    if index >= 1 and index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
         print("The video selected is not available. ")

def main():
    videos= load_data()
    while True:
        print("\n ********** Youtube Manager **********")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video")
        print("Exit the app ")
        choice = input("Enter the choice : ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

# dunder --> industry style code
if __name__ == "__main__":
    main()