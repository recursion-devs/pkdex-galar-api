
import os
from wrappers.aws.dynamodb import Dynamodb

global PARAMS
PARAMS = [
  ''
]


# TODO: Get Pokemon By ID
# /pkdex/pkmon/{id}
def _exe(params, eventBody, method):
  dynamodb = Dynamodb(
    os.environ['pdexTableName']
  )

  itemKey = {
    'partition' : {
      'S' : 'pokeDex'
    },
    'objectid' : {
      'S' : eventBody['']
    }
  }
  dynamodb.get_item(itemKey)


  return


