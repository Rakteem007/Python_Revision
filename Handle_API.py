import requests

def fetch_userName():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url)
    data = response.json()

    if data["statusCode"] == 200 and data["success"]:
        user_data = data["data"]
        username = data["data"]["login"]["username"]
        country = data["data"]["location"]["country"]

        return username, country
    else:
        raise Exception("Failed to fetch user api")

def main():
    try:
        username, country = fetch_userName()
        print(f"Username : {username} \n Country : {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()