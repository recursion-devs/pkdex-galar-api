


class RestResponse:

  BAD_REQUEST = 0
  SUCCESS = 1

  def __init__(self, customHeaders=None):
    self.headers = {}
    if customHeaders:
      self.headers = customHeaders


  @classmethod
  def _bad_request(cls, headers):
    return {
      'statusCode' : 400,
      'headers' : headers,
      'body' : {
        'msg' : 'Bad Request'
      }
    }

  @classmethod
  def _success(cls, headers):
    return {
      'statusCode' : 200,
      'headers' : headers,
      'body' : {
        'msg' : 'success'
      }
    }

  def Resp(self, responseCode):
    if responseCode == RestResponse.BAD_REQUEST:
      return RestResponse._bad_request(self.headers)

    if responseCode == RestResponse.SUCCESS:
      return RestResponse._success(self.headers)

