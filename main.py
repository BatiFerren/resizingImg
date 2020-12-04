import cv2
import os


# TODO: Have to divide name of file and its extension
def rename_files(source_list, source_directory):
    i = 0
    for item in source_list:
        os.rename(source_directory + '/' + item, source_directory + '/' + str(i).zfill(4) + '.jpg')
        i += 1


def resize_image(source_list, source_directory):
    for item in source_list:
        img_path = source_directory + '/' + item
        img = cv2.imread(img_path)
        old_width = int(img.shape[1])
        old_height = int(img.shape[0])
        new_width = 1000
        k_resize = new_width / old_width
        new_height = int(old_height * k_resize)
        dim = (new_width, new_height)
        imgResized = cv2.resize(img, dim)
        cv2.imwrite(img_path, imgResized)


if __name__ == "__main__":
    # TODO: Need to process russian symbols and spaces in the path of files
    directory = r'D:/OPISI/opisiF/F52_2'
    list_of_files = os.listdir(directory)
    length_of_list = len(list_of_files)
    if list_of_files[0] == 'Thumbs.db':
        os.remove(directory + '/' + list_of_files[0])
        list_of_files.pop(0)
    elif list_of_files[length_of_list - 1] == 'Thumbs.db':
        os.remove(directory + '/' + list_of_files[length_of_list - 1])
        list_of_files.pop()
    rename_files(list_of_files, directory)
    list_of_files = os.listdir(directory)
    resize_image(list_of_files, directory)
