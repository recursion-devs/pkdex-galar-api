
import os


def _get_modules():
  """
  Get available API Modules
  :returns: List of project modules (url endpoint)
  :rtype: list
  """

  moduleList = []
  for root, dirs, files in os.walk('service'):
    for folder in dirs:
      moduleList.append(folder)

  return moduleList


def _get_service_list(module):
  """
  Get Available Service Module
  :param module: module name
  :type module: string
  :returns: List of services
  :rtype: list
  """

  service_list = []
  for root, dirs, files in os.walk('service/' + module):
    for filen in files:
      service_list.append(filen.replace('.py',''))
  return service_list


def _validate_params(module, service, queryParams, eventBody, method):
  """
  Validate param list
  :param module: api module list
  :type module: string
  :param service: service used
  :type service: string
  :param params: list of used request parameters
  :type params: list of string
  :returns: if param list complete
  :rtype: boolean
  """

  service = __import__('service.' + module + '.' + service, fromlist=[service])
  for sparam in service.PARAMS['qparams']:
    if sparam not in queryParams:
      return False

  if method == 'POST':
    for sparam in service.PARAMS['rbody']:
      if sparam not in eventBody:
        return False

  return True
