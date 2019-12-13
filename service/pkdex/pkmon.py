
import os
import json

global PARAMS
global PKDEXDATA

PKDEXDATA = json.loads(open('data/pokedexv16.json','r').read())
PARAMS = {
  'qparams' : [],
  'rbody' : []
}

# TODO: Get Pokemon By ID
# /pkdex/pkmon/{id}
def _exe(pathParams, queryParams, eventBody, method):
  global PKDEXDATA

  print('PKMON EXECUTING')

  if method == 'GET':
    if pathParams['dexId'] in PKDEXDATA:
      return {
        'statusCode' : '200',
        'headers' : {
          'Access-Control-Allow-Origin' : '*',
          'Content-Type' : 'application/json'
        },
        'body' : json.dumps(PKDEXDATA[pathParams['dexId']])
      }

  return {
    'statusCode' : 404,
    'headers' : {
      'Access-Control-Allow-Origin' : '*',
      'Content-Type' : 'application/json'
    },
    'body' : json.dumps({
      'resason' : 'pokemon not found :D'
    })
  }



