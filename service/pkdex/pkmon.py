
import os
from wrappers.aws.dynamodb import Dynamodb

global PARAMS
PARAMS = {
  'rparams' : ['id'],
  'rbody' : []
}

# TODO: Get Pokemon By ID
# /pkdex/pkmon/{id}
def _exe(params, eventBody, method):
  if method == 'GET':
    dynamodb = Dynamodb(
      os.environ['pdexTableName']
    )
    itemKey = {
      'partition' : {
        'S' : 'pokeDex'
      },
      'objectid' : {
        'S' : params
      }
    }
    dynamodb.get_item(itemKey)


  return





