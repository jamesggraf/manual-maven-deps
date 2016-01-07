import json
import os

resourceFolder = "resources"

with open('dependencies.json') as data_file:
  data = json.load(data_file)

dependencies = data['dependencies']

for i, dependency in enumerate(dependencies):

  command = 'mvn install:install-file -Dfile=' + resourceFolder + '/' + dependency['file']

  if 'version' in dependency:
    command += ' -DgroupId=' + dependency['groupId']
    command += ' -DartifactId=' + dependency['artifactId']
    command += ' -Dversion=' + dependency['version']
    command += ' -Dpackaging=' + dependency['packaging']

  os.system('echo ' + command)