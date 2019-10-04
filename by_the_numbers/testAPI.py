import requests
import sys
import json


def getapiinfo(someurl):
    """

    :return:
    """

    ### some standing elemenets that allow for quick substitution in testing
    ##
    astronaut = "http://api.open-notify.org/astros.json"

    # Assigns ...

    v_val = someurl
    if v_val == None:
        v_val = astronaut

    if v_val == 'astronaut':
        v_val = astronaut

    if v_val == '1':
        v_val = "http://api.open-notify.org/this-api-doesnt-exist"

    if v_val == 'falcon':
        v_val = 'https://launchlibrary.net/1.3/rocket/falcon'

    if v_val =='quote':
        v_val = 'https://quote-garden.herokuapp.com/quotes/random'

    if v_val == 'kanye':
        v_val = 'https://opentdb.com/api.php?amount=1&category=17&difficulty=hard'

    if v_val == 'trump':
        v_val = 'https://api.tronalddump.io/random/quote'

    # Fetch and report

    """
    200: Everything went okay, and the result has been returned (if any).
    301: The server is redirecting you to a different endpoint. 
    This can happen when a company switches domain names, or an endpoint name is changed.
    400: The server thinks you made a bad request. 
    This can happen when you don’t send along the right data, among other things.
    401: The server thinks you’re not authenticated. 
    Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
    403: The resource you’re trying to access is forbidden: you don’t have the right permissions to see it.
    404: The resource you tried to access wasn’t found on the server.
    503: The server is not ready to handle the request. 
    """

    response = requests.get(v_val)
    print(response.status_code)
    print(' URL used is :',v_val)
    jstring = response.json()
    jstring = json.dumps(jstring, sort_keys=True, indent=4)
    #jstring = json.dumps(response.json(), sort_keys=True, indent=4)

    print(jstring)




if __name__ == "__main__":
        getapiinfo(sys.argv[1])