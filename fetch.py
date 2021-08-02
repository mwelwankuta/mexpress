from mexpress import mexpress as server

port = 5000
server.listen(port, f'listening on port {port}')

def route(route):
    if(route == None):
        return '/'
    else:
        return route

def fetch(request_router, args = None):
    route_value = route(request_router)

    if(args == None):
        return (server.get(route_value))
    else:
        method = args['method']

        # get route method
        is_method_post = method == 'post' or method == 'POST'   
        is_method_get = method == 'get' or method == 'GET'

        if(is_method_post):
            body = args['body']
            return server.post(route_value, body)

        if(is_method_get or args == None):
            return (server.get(route_value))
