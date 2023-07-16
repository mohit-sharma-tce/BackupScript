"""
Written By: ms1241721
Last Modified: ms1241721
Script: Backup using ftp
"""

import os
import ftplib
import time

server = ftplib.FTP()
server.connect('192.168.43.1', 2221)
server.login('android', 'android')

# server.retrlines('LIST')


def copyImages(backupDirectory):

    photoDirectory = backupDirectory+"/"+ "DCIM/Camera"                                         #copying DCIM/Camera images to backup
    MX_photoDirectory = backupDirectory+"DCIM/Camera MX"

    existingFiles = set()
    for localFile in  os.listdir(photoDirectory):
        existingFiles.add(localFile)


    for filename in server.nlst('DCIM//Camera'):

        remoteFilepath = photoDirectory + '/' + filename
        localFilePath = backupDirectory + '/' + photoDirectory+ '/' + filename

        if filename not in existingFiles:                              #Check if file doesn't exist in local
            with open(localFilePath,'wb') as file:
                server.retrbinary('RETR '+remoteFilepath,file.write)
            # print(filename, "processed")

def copyData(backDrive,backupFolder):
    backupDirectory = backDrive+":\\"+backupFolder
    copyImages(backupDirectory)

def main():

    copyData("D","backup")


if __name__ == "__main__":
    print("----------BACKUP SCRIPT---------------------")
    print("-                                          -")
    print("-                                          -")
    print("-                                          -")
    print("-                                          -")
    print("-         written by @ms1241721            -")
    print("")
    main()