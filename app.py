
from utility.rest_response import RestResponse
from utility import request_validator


def handler(event, context):
  print(event)

  respTemplate = RestResponse({
    'Access-Control-Allow-Origin' : '*'
  })

  path = event['requestContext']['resourcePath']
  httpMethod = event['httpMethod']
  pathParams = event['pathParameters']
  servicePath = path.split('/')

  if len(servicePath) < 2:
    return respTemplate.Resp(RestResponse.BAD_REQUEST)

  # Validate request params
  if httpMethod == 'GET':
    return

  if httpMethod == 'POST':
    postBody = event['body']

  return





