from linkedin_v2 import linkedin
from prettytable import PrettyTable
import json

CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
RETURN_URL = 'YOUR_REDIRECT_URL'
#
#If you do not have a token yet, keep the below variable blank. If you already have a token, assign the token string to this variable
#
accesstoken_str  = ""

if(not accesstoken_str):

    authentication = linkedin.LinkedInAuthentication(CLIENT_ID, CLIENT_SECRET, RETURN_URL, permissions=["r_liteprofile r_emailaddress"])
    # Optionally one can send custom "state" value that will be returned from OAuth server
    # It can be used to track your user state or something else (it's up to you)
    # Be aware that this value is sent to OAuth server AS IS - make sure to encode or hash it
    #authorization.state = 'your_encoded_message'

    print authentication.authorization_url  # open this url on your browser to login and obtain access code
    print("")
    print("Copy the URL to a browser and click go. Copy code value back from the redirect page")
    print("")
    auth_code = raw_input("Authorization Code from RedirectURL:")
    print ("Using Auth Code: " + auth_code)

    authentication.authorization_code = auth_code
    accesstoken = authentication.get_access_token()

    if(not accesstoken):
        print("Access Token Could not be Obtained: ")
        quit()

    #print("Access Token:" + accesstoken[0])
    #print("Expires in:" + str(accesstoken[1]))
    #
    # Create the application instance using the fetched token
    #
    application = linkedin.LinkedInApplication(authentication)
else:
    #
    # Create the application instance using the available token
    #
    application = linkedin.LinkedInApplication(token=accesstoken_str)

#Get own Profile

#my_profile = application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])
my_profile = application.get_profile()
#print(my_profile)
print(json.dumps(my_profile, indent=1))
#my_conn = application.get_connections()
#print(my_conn)
