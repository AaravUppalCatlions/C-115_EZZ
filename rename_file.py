import os

source = 'D:/Desktop/downloaded photos'
dest = 'D:\Desktop\downloaded photos\Image_Files'

os.rename(source,dest)
print("Source path renamed to destination path successfully.")
