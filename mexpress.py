from routes import route_response

class mexpress:
    default_port = 3001

    def listen(port=default_port, message=''):
        if (message == None):
            print('Server Started on port')
        elif (message != None):
            print(f'Listening on port {port}')
        
    # get route
    def get(route):
        print(f'GET: route=[{route}]\n---------')
        response = route_response(route)
        return(response)

    # post route
    def post(route, body):
        if(body == None):
            response = route_response(route)
        else:
            print(f'POST: route=[{route}]\n---------')
            response = route_response(route, body)
            return(response)
