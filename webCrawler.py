import os

def createProjectDirectory(directory):
    if not os.path.exists(directory):
        print('Creating project directory ' + directory)
        os.makedirs(directory)
