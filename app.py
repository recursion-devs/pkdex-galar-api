
from utility.rest_response import RestResponse


def handler(event, context):
  respTemplate = RestResponse({
    'Access-Control-Allow-Origin' : '*'
  })

  path = event['requestContext']['resourcePath']
  httpMethod = event['httpMethod']
  pathParams = event['pathParameters']
  servicePath = path.split('/')

  if len(servicePath) <= 1:
    return respTemplate.Resp(RestResponse.BAD_REQUEST)

  if httpMethod == 'GET':
    return

  if httpMethod == 'POST':
    postBody = event['body']

  return





