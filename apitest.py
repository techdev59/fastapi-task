import requests

BASE_URL = "http://127.0.0.1:8000"

def signup(email, password):
    response = requests.post(f"{BASE_URL}/signup", json={"email": email, "password": password})
    return response.json()

def login(email, password):
    response = requests.post(f"{BASE_URL}/login", json={"email": email, "password": password})
    return response.json()

def add_post(token, text):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/addpost", json={"text": text}, headers=headers)
    print(response.content)
    return response.json()

def get_posts(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/getposts", headers=headers)
    return response.json()

def delete_post(token, post_id):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BASE_URL}/deletepost/{post_id}", headers=headers)
    return response.json()

# Example usage
if __name__ == "__main__":
    email = "test@example.com"
    password = "password123"

    # Signup
    print("Signing up...")
    signup_response = signup(email, password)
    print(signup_response)

    # Login
    print("Logging in...")
    login_response = login(email, password)
    # print(login_response)
    token = login_response["access_token"]

    # Add Post
    print("Adding post...")
    print(token)
    add_post_response = add_post(token, "This is a test post.")
    print(add_post_response)
    post_id = add_post_response["id"]

    # Get Posts
    print("Getting posts...")
    get_posts_response = get_posts(token)
    print(get_posts_response)

    # Delete Post
    # print("Deleting post...")
    delete_post_response = delete_post(token, post_id)
    print(delete_post_response)