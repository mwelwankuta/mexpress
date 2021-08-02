import json

p = open('data/data.json')
data = json.load(p)[0]

def route_response(router = None, request_body = None):
    # get route method
    is_method_post = request_body != None 
    is_method_get = request_body == None or router == None

    posts = data['posts']
    users = data['users']
    if is_method_get:
        ## get requests go here:
        if router.split('?')[0] == '/posts':
            # get request code on [ / ] route go here
            parameters = router.split('?')
            if len(parameters) > 1:
                # if parameters are passed
                params = parameters[1]
                return({'body': posts[int(params) - 1]})
            else:
                return {'body': posts}

    if is_method_post:
        ## post requests go here:            
        if (router.split('?')[0] == '/login'):
            # post request logic on [ /login ] route go here
            for i in range(0, len(users)):
                #route params
                parameters = router.split('?')

                if len(parameters) == 1:
                    username = request_body['username']
                    password = request_body['password']

                    if username == users[i]['username']  and users[i]['password'] == password:
                        return {'body': users[i]}
                    else:
                        if len(users) == i + 1:
                            return {'body':'User not found'}
                        else:
                            continue
                else:
                    # code to execute if params were passed
                    pass
                    
                

p.close()