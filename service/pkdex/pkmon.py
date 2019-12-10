
import os
from wrappers.aws.dynamodb import Dynamodb

global PARAMS
PARAMS = {
  'qparams' : [],
  'rbody' : []
}

# TODO: Get Pokemon By ID
# /pkdex/pkmon/{id}
def _exe(pathParams, queryParams, eventBody, method):
  if method == 'GET':
    dynamodb = Dynamodb(
      os.environ['pdexTableName']
    )
    itemKey = {
      'partition' : {
        'S' : 'pokeDex'
      },
      'objectid' : {
        'S' : pathParams['dexId']
      }
    }
    ret = dynamodb.get_item(itemKey)
    print("RETURN PKMON")
    print(ret)
    return ret['Item']


  return {}






