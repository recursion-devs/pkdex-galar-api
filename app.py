
import json
from utility.rest_response import RestResponse
from utility import request_validator


def handler(event, context):
  respTemplate = RestResponse({
    'Access-Control-Allow-Origin' : '*'
  })

  queryStringParams = event['queryStringParameters']
  path = event['requestContext']['resourcePath']
  httpMethod = event['httpMethod']
  pathParams = event['pathParameters']
  pathSegments = path.split('/')
  eventBody = event['body']

  if len(pathSegments) < 2:
    return respTemplate.Resp(RestResponse.BAD_REQUEST)

  modulePath = pathSegments[1]
  servicePath = pathSegments[2]

  print('URL SEGMENTS:')
  print(pathSegments)
  print(modulePath)
  print(servicePath)

  # Validate Request Params
  if not request_validator._validate_params(modulePath, servicePath, queryStringParams, eventBody, httpMethod):
    return respTemplate.Resp(RestResponse.BAD_REQUEST)


  # Import module + service
  serviceModule = __import__('service.' + modulePath + '.' + servicePath, fromlist=[servicePath])
  return serviceModule._exe(pathParams, queryStringParams, eventBody, httpMethod)







