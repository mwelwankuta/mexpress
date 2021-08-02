from fetch import fetch

if(__name__ == '__main__'):

    # ---- POST REQUESTS ----
    # fetch_data = fetch('/login', {'method':'post', 'body':{'username':'john_doe','password':'4dsa14d03'}})

    # ---- GET REQUESTS ----
    # response = fetch('/posts')

    # with params
    # response = fetch('/posts/?2')

    response = fetch('/posts')

    print(response)