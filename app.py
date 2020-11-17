import config
import os
import pprint
import collections

def getExtension(fileName):
    splitedName = fileName.split(".")
    if len(splitedName) > 1:
        return splitedName[-1]
    return None

def createDirectories(baseDirectory, childDirectoryList):
    childDirectoryList.append("Other")
    for directory in childDirectoryList:
        directoryPath = os.path.join(baseDirectory, directory)
        if not os.path.isdir(directoryPath):
            os.mkdir(directoryPath)

def mapFilesToExtensions(baseDirectory):
    filesMapping = collections.defaultdict(list)
    for fileName in os.listdir(baseDirectory):
        if fileName[0] != "." and getExtension(fileName) is not None:
            extension = getExtension(fileName).lower()
            filesMapping[extension].append(fileName)
    return filesMapping

def findDirectoryToExtension(structure, extension):
    for directory, extensions in structure.items():
        if(extension in extensions):
            return directory

def moveFile(fileName, destinationDirectory):
    fileToMovePath = os.path.join(config.baseDirectory, fileName)
    whereToMovePath = os.path.join(config.baseDirectory, destinationDirectory, fileName)
    os.rename(fileToMovePath, whereToMovePath)

def moveFilesToFolders(structure, filesMapping):
    for extension, files in filesMapping.items():
        destinationDirectory = findDirectoryToExtension(structure, extension)
        if destinationDirectory is None:
            destinationDirectory = 'Other'
        for file in files:
            moveFile(file, destinationDirectory)

if __name__ == "__main__":
    createDirectories(config.baseDirectory, [x for x in config.structure.keys()])
    filesMapping = mapFilesToExtensions(config.baseDirectory)
    moveFilesToFolders(config.structure, filesMapping)
