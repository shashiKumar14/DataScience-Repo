import ftplib
import wget
import os

#To connect with file server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
ftp_server.encoding ='utf-8'

ftp_server.cwd("/path/to/folder")
list_of_files=ftp_server.nlst()#we can loop the list_of_files for our use

#To use we have to download first
for file in list_of_files:
  link = f'ftp://{USERNAME}:{PASSWORD}@{HOSTNAME}/path/to/folder/{file}'
  page=wget.download(link)
  #we can use this "page" now
  #call function or write code
  ftp_server.cwd("/path/to/folder")
  ftp_server.delete(file)
  os.remove(file)

  
#To store in another folder
ftp_server.cwd("/path/to/another_folder")
with open(filename, "rb") as File_Name:
  ftp_server.storbinary(f"STOR {filename}", File_Name)
  
ftp_server.quit()

