import json
import os
import urllib
import zipfile

resourcesUrl = 'https://dl.dropboxusercontent.com/s/jt8pv9elgp52og4/Archive.zip?dl=0'
resourceFolder = 'resources'
resourceFile = 'resources.zip'
resourceFilePath = resourceFolder + '/' + resourceFile

dependenciesFile = 'dependencies.json'

def create_download_folder(folderPath):
  print 'Creating folder: ' + folderPath
  if not os.path.exists(folderPath):
    os.makedirs(folderPath)

def download_resources(filePath):
  print 'Downloading: ' + resourcesUrl
  resourceStream = urllib.URLopener()
  resourceStream.retrieve(resourcesUrl, filePath)
  return;

def unzip_resources(filePath, outputPath):
  print 'Unzipping ' + filePath + ' to ' + outputPath
  openFile = open(filePath, 'rb')
  openZipFile = zipfile.ZipFile(openFile)
  for name in openZipFile.namelist():
  	openZipFile.extract(name, outputPath)

def install_dependencies(dependenciesFile):
  print 'Installing dependencies from: ' + dependenciesFile
  with open(dependenciesFile) as data_file:
    data = json.load(data_file)

  dependencies = data['dependencies']

  for i, dependency in enumerate(dependencies):

    command = 'mvn install:install-file -Dfile=' + resourceFolder + '/' + dependency['file']

    if 'version' in dependency:
      command += ' -DgroupId=' + dependency['groupId']
      command += ' -DartifactId=' + dependency['artifactId']
      command += ' -Dversion=' + dependency['version']
      command += ' -Dpackaging=' + dependency['packaging']

    print 'Running: ' + command

create_download_folder(resourceFolder)
download_resources(resourceFilePath)
unzip_resources(resourceFilePath, resourceFolder)
install_dependencies(dependenciesFile)

