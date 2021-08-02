<h1 align="center">MExpress 🔥</h1>
<h3 align="center" style="font-weight:bold;">a mock python server with post and get requests</h3>

## Building MExpress

no third party libraries used

- **Language Used**: Python
- **Duration**: 5 hour

## File Structure
| File           | Description                   |
|----------------|-------------------------------|
| `main.py`      | sending mock requests         |
| `routes.py`    | declaring request endpoints   |
| `fetch.py`     | checks for post or get request|
| `mxexpress.py` | mock server                   |


## Getting Started

 in the root directory run `python3 -m main` to send a request or `python -m main` if on windows

## Fetching 

 to  fetch from an endpoint created, open `main.py`
 here is a sample of how to fetch from an endpoint

### Two Ways of fetching  | GET Request:

1. **Full fetch method**: proving fetch route and a second argument as of type dictionary

```py 
    fetch('/', {'method':'get'})
```

1.  **Shortened fetch method**: proving fetch route
```py
    fetch('/')
```

### Get Request

 ```py
    response = fetch('/')
    print(response['body'])
 ```
### Post Request

 ```py
    fetch_data = fetch('/', {'method':'post', 'body':'typescript'})
    print(fetch_data['body'])
 ```
## Creating Endpoints

 to create an endpoint open `routes.py`
 here is a sample of how to create an endpoint

## Get Endpoint
  each requests is represented by an if statement for example

  ```py
    if router.split('?')[0] == '/':
  ```

## Get Endpoint Example

full code in `main.py`

```py
   if router.split('?')[0] == '/':
            # get request code on [ / ] route go here
            parameters = router.split('?')
            if len(parameters) > 1:
                # if parameters are passed
                params = parameters[1]
                return({'body': posts[int(params) - 1]})
            else:
                return {'body': posts}
```

## Post Endpoint

  each requests is represented by an if statement for example
  ```py
    if router.split('?')[0] == '/login':
  ```

## Post Endpoint Example
full code in `routes.py`

```py
    if (router.split('?')[0] == '/login'):
            # post request logic on [ /login ] route go here
            
            for i in range(0, len(users)):
                #route params
                parameters = router.split('?')

                username = request_body['username']
                password = request_body['password']

                if username == users[i]['username']  and users[i]['password'] == password:
                    return {'body': users[i]}
                else:
                    if len(users) == i + 1:
                        return {'body':'User not found'}
                    else:
                        continue
```


## Endpoint parameters
  ```py
    # GRABBING ENDPOINT PARAMS
    parameters = router.split('?')[1]

    # ADDING ENDPOINT PARAMS
    response = fetch('/posts?2') 
    # code above gets passes 2 as parameter

    # another example 
    response = fetch('/posts?john_doe')
    # code above gets passes john_dpe as parameter
  ```
## Why i made this

1. I had no existing python code on my github
1. I always wanted to upload python code to my [GitHub Account](https://github.com/mwelwankuta)

## Contact
- Twitter [@Merlee4t](https://twitter.com/Merlee4t)