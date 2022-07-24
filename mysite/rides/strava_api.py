import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


def getAthleteStat(athlete_id):
    # Configure OAuth2 access token for authorization: strava_oauth
    swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

    # create an instance of the API class
    api_instance = swagger_client.AthletesApi()
    id = 789 # Long | The identifier of the athlete. Must match the authenticated athlete.

    try: 
        # Get Athlete Stats
        api_response = api_instance.getStats(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AthletesApi->getStats: %s\n" % e)

