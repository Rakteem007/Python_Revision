import sqlite3

con = sqlite3.connect("youtube_videos.db")

cursor = con.cursor()

# query 
cursor.execute('''
    CREATE  TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES(?, ?)", (name, time))
    con.commit()

def update_videos(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    con.commit()

def main():
    while True:
        print("\n Youtube Videos with sqlite3")
        print("1. List of all videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit")
        choice = input("Enter your choice : ")

        match choice:
            case '1': 
                list_videos()
            case '2':
                name = input("Enter the name : ")
                time = input("Enter the name : ")
                add_videos(name, time)
            case '3':
                video_id = input("Enter the video id : ")
                name = input("Enter the name : ")
                time = input("Enter the name : ")
                update_videos(video_id, name, time)
            case '4':
                video_id = input("Enter the video id : ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid Input")


if __name__ == "__main__":
    main()