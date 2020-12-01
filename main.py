import cv2
import os

if __name__ == "__main__":
    directory = r'D:\ОПИСИ\описи Ф\Ф 114 оп 1'
    list_of_files = os.listdir(directory)
    print(list_of_files)
    length_of_list = len(list_of_files)
    print(length_of_list)
    if list_of_files[0] == 'Thumbs.db':
        list_of_files.pop(0)
        print(list_of_files)
    elif list_of_files[length_of_list - 1] == 'Thumbs.db':
        list_of_files.pop()
        print(list_of_files)