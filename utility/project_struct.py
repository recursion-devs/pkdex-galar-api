
import os


# Get Available API Modules
def _get_modules():
  moduleList = []
  for root, dirs, files in os.walk('service'):
    for folder in dirs:
      moduleList.append(folder)

  return moduleList


# Get Available Service Module
def _get_service_list(module):
  service_list = []
  for root, dirs, files in os.walk('service/' + module):
    for filen in files:
      service_list.append(filen.replace('.py',''))
  return service_list



