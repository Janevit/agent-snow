
import json
from incident_finder import IncidentFinder

def lambda_handler(event, context):
    
    print(event)
    
    agent = event['agent']
    actionGroup = event['actionGroup']
    function = event['function']
    # parameters = event.get('parameters', [])
    parameters = {param['name']: param['value'] for param in event['parameters']}

    # Execute your business logic here. For more information, refer to: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html
    responseBody =  {
        "TEXT": {
            "body": json.dumps(handle_request(function, parameters))
            # "body": "The function {} was called successfully!".format(function)
        }
    }

    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': responseBody
        }

    }

    dummy_function_response = {'response': action_response, 'messageVersion': event['messageVersion']}
    print("Response: {}".format(dummy_function_response))

    return dummy_function_response


def handle_request(function, parameters):
    if function == "getIncidentNumber":
        return IncidentFinder.get_incident(parameters.get('incidentNumber'))
#    elif function == "getCurrentTime":
#        return TimeFinder.get_current_time(parameters.get('latitude'), parameters.get('longitude'))
#    elif function == "getCurrentWeather":
#        return WeatherFinder.get_current_weather(parameters.get('latitude'), parameters.get('longitude'))
    else:
        return {"error": "Invalid API path"}
